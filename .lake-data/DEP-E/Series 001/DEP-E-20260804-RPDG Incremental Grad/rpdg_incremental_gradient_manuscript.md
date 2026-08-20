---
title: "RPDG Incremental Gradient - DEP-E"
generated_at: "2026-08-04 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of optimal randomized primal-dual incremental gradients for finite-sum composite convex optimization."
source_status: "verified complete local PDF and full-paper HTML; public URLs cited; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-04"
temporal_cutoff: "Paper version v3 and public records inspected through 2026-08-04"
primary_url: "https://arxiv.org/abs/1507.02000"
stable_identifier: "arXiv:1507.02000v3; DOI:10.1007/s10107-017-1173-0"
confidence_summary: "High for source identity, method transcription, and theorem scope; medium for interpretation; no experimental reproduction exists in the paper or this review."
safety_scope: "non-sensitive optimization research and bounded offline evaluation"
distribution_notes: "Generated Markdown only; all PDF, HTML, metadata, receipts, provenance, renderings, caches, and other source material remain local."
---

# RPDG Incremental Gradient - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Primary metadata | HTML | arXiv:1507.02000v3 | https://arxiv.org/abs/1507.02000 | Metadata and source locators; abstract alone was not used for detailed claims. | 2026-08-04 | Inspected |
| S2 | Paper PDF | Primary artifact | PDF | arXiv:1507.02000v3 | https://arxiv.org/pdf/1507.02000 | Complete 31-page paper inspected and sampled visually; file withheld. | 2026-08-04 | Verified complete |
| S3 | Full-paper rendering | Primary artifact fallback | HTML | arXiv:1507.02000v3 | https://ar5iv.labs.arxiv.org/html/1507.02000 | Approved full-paper fallback after official arXiv HTML routes were unavailable; file withheld. | 2026-08-04 | Verified complete |
| S4 | Source-package endpoint | Primary-source locator | TeX/source archive | arXiv:1507.02000 | https://arxiv.org/e-print/1507.02000 | Bounded broker attempt did not produce a source package; no retry loop was used. | 2026-08-04 | Unavailable |
| S5 | arXiv DOI | Persistent identity | DOI | 10.48550/arXiv.1507.02000 | https://doi.org/10.48550/arXiv.1507.02000 | Persistent identifier, not a separate publication. | 2026-08-04 | Resolved |
| S6 | Mathematical Programming article | Version-of-record identity | DOI | 10.1007/s10107-017-1173-0 | https://doi.org/10.1007/s10107-017-1173-0 | Publisher terms apply; no publisher file was redistributed. | 2026-08-04 | Identity verified |
| S7 | Optimization Online record | Author-deposited context | HTML | Technical report updated 2015-10-18 | https://optimization-online.org/?p=13502 | Author-deposited record and paper locator. | 2026-08-04 | Inspected |
| S8 | DBLP record | Bibliographic cross-check | HTML | Math. Program. 171(1-2), 167-215 | https://dblp.org/rec/journals/mp/LanZ18 | Venue, year, volume, pages, and DOI cross-check. | 2026-08-04 | Inspected |
| S9 | Epsilon Prox Affine DEP | Related research | Markdown | DEP-E-20260730 | `.lake-data/DEP-E/DEP-E-20260730-Epsilon Prox Affine/epsilon_prox_affine_manuscript.md` | Processed synthesis; not primary evidence for RPDG. | 2026-08-04 | Inspected |
| S10 | Local Stochastic Bilevel DEP | Related research | Markdown | DEP-E-20260728 | `.lake-data/DEP-E/DEP-E-20260728-Local Stochastic Bilevel/local_stochastic_bilevel_manuscript.md` | Processed synthesis; not primary evidence for RPDG. | 2026-08-04 | Inspected |
| S11 | GPMD Regularized RL DEP | Related research | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` | Processed synthesis; not primary evidence for RPDG. | 2026-08-04 | Inspected |
| S12 | Selection, dedup, repair, and validation records | Process evidence | Private records | Black Lake Arxiv DEP 0900 | Withheld local context | Supports selection, integrity, and source-locality claims only. | 2026-08-04 | Verified |

- **Paper title:** *An optimal randomized incremental gradient method*
- **Authors:** Guanghui Lan and Yi Zhou
- **arXiv history:** submitted 2015-07-08; v3 revised 2015-10-18
- **Subjects:** Optimization and Control (`math.OC`), Computational Complexity (`cs.CC`), and Machine Learning (`stat.ML`)
- **Published form:** *Mathematical Programming* 171(1-2), pages 167-215 (2018)
- **Local source paths:** Withheld by public-output policy
- **Source redistribution:** Not authorized for this automation; all original and derived source material remains local

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5 | Official metadata and DOI | Canonical title, authors, dates, version, subjects, abstract, and identifiers | Source identity and temporal scope | High | Abstract is not method or result evidence |
| E2 | S2, S3 | Complete primary paper | Problem assumptions, conjugate saddle-point reformulation, Bregman prox definitions, Algorithms 1-4, Theorems 1-3, Corollaries 1-4, and Propositions 1-4 | Method, upper bounds, lower bound, extensions, and limitations | High for source characterization | Proofs were read but not independently rederived |
| E3 | S2 | Visual paper evidence | Title/version page, RPDG update, non-uniform complexity, lower-bound construction, perturbation extension, and conclusion | Layout-sensitive confirmation of equations and scope | High | Visual inspection is not independent validation |
| E4 | S6-S8 | Publisher, author-deposit, and bibliographic records | Published DOI, volume, pages, year, and technical-report history | Publication context | High | These records do not validate the mathematics |
| E5 | S2, S3 | Negative evidence in the primary paper | No numerical experiment section, datasets, runtime tables, implementation link, or empirical reproduction package | Empirical and implementation boundary | High | Absence in inspected sources does not prove no private implementation exists |
| E6 | S9 | Related DEP | Prox-affine compiler/runtime, structured proximal and linear operators, and wall-time/residual concerns | Proximal-system relationship | Medium-high | Different solver architecture and evidence base |
| E7 | S10 | Related DEP | Stochastic-gradient complexity and momentum-based variance reduction in a later bilevel setting | Randomized-gradient relationship | Medium | Nonconvex/bilevel assumptions do not transfer directly |
| E8 | S11 | Related DEP | Regularizer-generated generalized Bregman divergence, linear convergence, and bounded-error floor | Geometry and convergence relationship | Medium-high | Tabular regularized RL is a different objective class |
| E9 | S12 | Private process records | Uniform random index, dedup keys, source repair, integrity metrics, and staged-source prohibition | Selection provenance and source-locality assurance | High | Does not imply scientific representativeness |

## Executive Summary

Lan and Zhou study a finite-sum composite convex objective

`Psi(x) = sum_i f_i(x) + h(x) + mu * omega(x)`

over a closed convex set. Each component `f_i` is smooth and convex, `h` is a relatively simple convex term, and `omega` is strongly convex with respect to an arbitrary norm. The paper first recasts the problem as a saddle-point system and builds a deterministic primal-dual gradient method. The key construction uses the conjugate of the smooth objective to define a dual Bregman prox; with a particular parameterization, the method exposes a primal-dual interpretation of Nesterov-style acceleration.

The main contribution is the randomized primal-dual gradient method (RPDG). After an initial full component-gradient pass, each iteration samples one component, refreshes only that component's stored gradient through a dual prox step, forms an unbiased prediction of the aggregate dual change, and performs one primal prox update. For strongly convex problems, the authors derive an order bound of

`O((m + sqrt(m * L / mu)) * log(1 / epsilon))`

component-gradient evaluations, with expectation and high-probability forms. Under favorable smoothness relations, the paper interprets this as up to an `O(sqrt(m))` saving over deterministic optimal first-order methods. It also constructs separable quadratic hard instances and obtains a matching-order lower bound for a specified randomized incremental linear-span model when the dimension is sufficiently large.

The contribution is theorem-driven. The paper contains no numerical experiments, runtime measurements, memory accounting, implementation repository, or empirical comparison. Its optimality claim is therefore precise but conditional: it applies to the stated oracle model, sampling structure, dimensional requirement, and problem assumptions. The most useful implementation lesson is to measure separate cost channels. Component-gradient calls may fall while initialization, stored per-component state, prox mappings, aggregation, parameter estimation, and certificate computation remain material.

## Detailed Summary

### Problem and assumptions

The objective contains `m` smooth convex components plus simple convex and strongly convex terms. The authors write `L = sum_i L_i` for the sum of component Lipschitz-gradient constants and distinguish it from the actual Lipschitz constant `L_f` of the full smooth sum, which can be smaller. They assume the proximal subproblem formed by a linear term plus `h + mu * omega` is easy to solve. For RPDG, every component gradient must be defined beyond the feasible set because auxiliary component-specific points need not remain in `X`, even though the primal iterates do.

This is an oracle-complexity model. A component-gradient evaluation is the main counted resource. The paper does not claim that component functions have equal wall-time cost, that a prox mapping is free, or that memory and communication are negligible.

### Deterministic primal-dual gradient method

The deterministic method replaces the smooth sum with a conjugate saddle-point representation. A Bregman distance generated by the conjugate becomes the dual prox geometry. Algorithm 1 combines primal extrapolation, a dual prox update, and a primal prox update. Algorithm 2 shows that the dual operation can be implemented through a gradient evaluation.

For `mu > 0`, Theorem 1 gives linear convergence for the iterate distance and for primal or primal-dual gaps of ergodic averages under a constant parameter policy. For `mu = 0`, a time-varying policy yields an `O(1/k^2)` primal-gap rate for the ergodic average. The computable gap statement additionally depends on a bounded feasible set.

The authors interpret the method as a buyer-supplier game: the primal player chooses quantities and the dual player chooses prices. That metaphor is explanatory, not evidence of game-theoretic application performance.

### Randomized primal-dual gradient method

RPDG expands the dual variable into `m` component blocks. Algorithm 3 samples `i_t` with probability `p_i`, updates one dual block, inflates that block's change by `1/p_i` to form an unbiased aggregate prediction, and then performs the primal prox mapping. Algorithm 4 gives the efficient recursion:

- extrapolate the current primal iterate;
- update the selected component-specific point;
- evaluate only `grad f_i` for that component;
- update the primal point from the cached aggregate plus the importance-weighted component change; and
- update the aggregate cache.

The initialization computes all `m` component gradients and stores component-specific gradients and points. This makes the steady-state one-gradient description accurate only after an initial full pass. It also introduces `O(m)` component-state storage before accounting for vector dimension.

### Strongly convex upper bounds

Theorem 2 supplies general parameter inequalities. Corollary 1 chooses

`p_i = 1/(2m) + L_i/(2L)`

and derives expectation and high-probability iteration bounds for distance to the optimum and for primal optimality of an ergodic average. The order simplifies to

`O((m + sqrt(m * L / mu)) * log(1 / epsilon))`.

Corollary 2 allows uniform sampling when component smoothness information is unavailable, but its condition number depends on `m * max_i L_i / mu`. The paper notes that non-uniform sampling needs estimates of every `L_i`, while uniform sampling may pay for component heterogeneity.

The headline `O(sqrt(m))` gradient saving is conditional. It is clearest when the square-root term dominates and the full-gradient and summed component smoothness constants are of the same order. If cancellations make `L_f` much smaller than `L`, deterministic comparisons change.

### Lower complexity bound

The paper constructs a separable strongly convex quadratic instance with a tridiagonal block structure. The randomized algorithm class samples components independently with fixed probabilities and produces iterates in a linear span of previously observed component gradients. Theorem 3 lower-bounds the expected squared distance to the optimizer. Corollary 3 turns it into the matching-order requirement

`Omega((m + sqrt(m * L / mu)) * log(||x_0 - x_*||^2 / epsilon))`

when the dimension exceeds a bound that depends on `m` and the iteration budget. Corollary 4 gives a related randomized block-coordinate lower bound.

This is meaningful oracle evidence, but it should not be expanded beyond its assumptions. The result does not automatically cover adaptive sampling with history-dependent distributions, nonlinear information use beyond the span condition, finite-dimensional regimes below the theorem threshold, approximate gradients, asynchronous systems, or hardware-specific cost.

### Non-strongly-convex and nonsmooth extensions

Section 4 uses perturbation and smoothing rather than a single universal parameter-free algorithm:

- For smooth problems on a bounded feasible set with `mu = 0`, a strongly convex perturbation yields an expectation/high-probability bound with a dominant `sqrt(m * L * Omega_X^2 / epsilon)` term and logarithmic factors.
- For structured nonsmooth components represented by max-form functions, Nesterov-style smoothing plus RPDG yields bounds that preserve an `O(sqrt(m))` component-oracle advantage up to logarithmic factors.
- For unconstrained smooth problems, a quadratic perturbation gives a relative-accuracy bound of order `O(sqrt(m / epsilon) * log(m / epsilon))`.

These extensions introduce boundedness radii, smoothing radii, target-accuracy choices, and additional prox assumptions. They are not evidence that one unchanged implementation is parameter-free across every regime.

### Evidence boundary and conclusion

The conclusion explicitly characterizes the work as theoretical. The parameters are conservative and depend on problem quantities such as `L` and `mu`; adaptive versions are left for future study. No numerical section tests the constants, stability, memory, initialization cost, or crossover point where fewer gradients offset additional prox and state-management work.

The public record establishes a later Mathematical Programming article, but this review is pinned to arXiv v3. A published-version difference audit was not performed because the publisher full text was not collected.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | PDG attains optimal deterministic first-order rates for the stated composite convex problem and uses a stronger primal-dual termination view. | Author theorem claim | E2 | Supported by Theorem 1 and the saddle-point analysis; proofs not independently rederived. | High for source report |
| C2 | RPDG uses one sampled component gradient per steady-state iteration. | Author algorithm claim | E2, E3 | Directly visible in Algorithms 3-4; initialization still computes all component gradients. | High |
| C3 | RPDG has order `O((m + sqrt(mL/mu)) log(1/epsilon))` component-gradient complexity in the strongly convex setting. | Author theorem claim | E2 | Supported by Corollaries 1-2 under their parameter and smoothness assumptions. | High for source report |
| C4 | RPDG can save up to `O(sqrt(m))` component-gradient evaluations versus deterministic optimal first-order methods. | Qualified author comparison | E2 | Valid only in the favorable regime described by the paper; not a universal wall-time speedup. | Medium-high |
| C5 | The upper bound is unimprovable for every randomized finite-sum optimizer. | Overbroad implication | E2 | Rejected. The lower bound is for a sufficiently high-dimensional randomized incremental linear-span model with specified sampling assumptions. | High rejection confidence |
| C6 | The non-strongly-convex and structured nonsmooth extensions preserve a square-root-in-`m` oracle advantage up to logarithmic factors. | Author theorem claim | E2 | Supported by Propositions 1-4; each extension adds perturbation/smoothing and boundedness conditions. | High for source report |
| C7 | The paper establishes practical runtime superiority. | Unsupported empirical implication | E5 | Rejected because the paper has no experiments, code, runtime, memory, or systems evidence. | High |
| C8 | A modern evaluation should count gradient, prox, initialization, memory, aggregation, and certificate costs separately. | Reviewer interpretation | E2, E6-E8 | Strong engineering implication grounded in the paper's cost model and related DEPs; not source-tested. | Medium-high |
| C9 | The selected paper passed global dedup and complete-source gates before synthesis. | Process claim | E9 | Exact identifiers/title/slug were clear; the partial archive unit was repaired and verified before review. | High |

## Methodology

- `Research objective`: Preserve the paper's problem, algorithms, theorem scope, limitations, and implementable evaluation implications as a public-safe DEP-E artifact.
- `Sources inspected`: Canonical arXiv metadata; verified complete arXiv v3 PDF; verified full-paper ar5iv HTML fallback; author-deposited Optimization Online record; published DOI and DBLP record; private repair/verification evidence; and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerate local PDFs with `rg --files -g "*.pdf"`; collapse parent directories into paper units; derive arXiv IDs from names; exclude used identifiers; draw a uniform PowerShell `Get-Random` index; then verify exact ID, DOI, title, normalized title, slug, and recent markers.
- `Inclusion criteria`: Primary or near-primary evidence establishing identity, method, theorem statements, proof assumptions, limitations, publication context, source integrity, or concrete cross-DEP overlap.
- `Exclusion criteria`: Abstract-only synthesis, duplicate papers, identifier-incomplete units, unverified full-paper payloads, secondary summaries where the full paper was available, source-file redistribution, and unsupported practical-speed claims.
- `Analytical approach`: Conceptual, comparative, implementation, replication, and theorem-scope analysis. The paper contains no empirical study to reproduce.
- `Evidence handling`: Theorem statements, algorithm definitions, negative evidence, reviewer interpretation, related-DEP synthesis, and process evidence use distinct ledger rows and claim labels.
- `Uncertainty handling`: Proofs were not independently formalized; no code was identified; no experiment exists to rerun; published-version differences and modern empirical competitiveness remain unknown.
- `Extraction process`: Searchable text was extracted from the complete PDF and HTML; algorithms, complexity statements, lower-bound assumptions, extensions, and conclusion were cross-checked; representative pages were visually rendered.
- `Random selection`: 75,960 PDFs collapsed to 75,957 parent-paper units; 565 used-ID units were excluded; 185 identifier-incomplete units were withheld; uniform zero-based eligible index 75,124 was selected from 75,207 eligible units.
- `Dedup and reselection validation`: The live Black Lake and Black-Lake-Data artifact trees, public dedup index, automation memory, exact identifiers, canonical/normalized title, slug, and public-safe 24-hour cutoff date were checked. Duplicate and recent rejections: 0; reselections: 0.
- `Source integrity`: The unit began `partial` because full-paper HTML was missing. The valid PDF was preserved; the approved ar5iv full-paper fallback and metadata were collected through a bounded broker repair; final status was `complete` with zero partial files.
- `Safety handling`: No local absolute path, username, machine identifier, local timezone, precise execution timestamp, source byte payload, or source file is published.
- `Reviewer stance`: Critical research preservation, theorem-scope audit, and bounded implementation translation.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:1507.02000v3; the finite-sum composite objective; PDG and RPDG; strongly and non-strongly convex rates; structured nonsmooth extension; lower-bound model; and exactly three related DEP bridges.
- `Temporal boundary`: The paper is pinned to v3 revised 2015-10-18; public metadata and repository context were inspected through 2026-08-04.
- `Evidence limits`: No independent proof derivation, theorem prover, code, experiment, runtime benchmark, memory profile, or publisher-text comparison.
- `Assumptions`: Smooth convex components with globally Lipschitz gradients; simple prox-compatible `h`; strongly convex prox generator `omega`; known or estimable smoothness/strong-convexity parameters for stated schedules; and oracle access matching each result.
- `Constraints`: Source locality, public-safe provenance, no source redistribution, and no claim that oracle complexity equals wall-clock performance.
- `Out of scope`: Nonconvex objectives, privacy guarantees, asynchronous/distributed execution, adaptive history-dependent sampling beyond the analyzed policy, automatic parameter estimation, and production deployment.
- `Intended use`: Research review, replication planning, optimization-solver design, and DEP preservation.
- `Audience`: Optimization researchers, ML-systems engineers, and reviewers evaluating finite-sum solver claims.
- `Reproducibility boundary`: Algorithms and proofs are inspectable; numerical reproducibility cannot be assessed because the paper provides no experiment or official code.
- `Operational boundary`: Implementation examples are synthetic and offline; they do not certify a production solver.
- `Data sensitivity`: Public scholarly sources and synthetic examples only.

## Observations

- `Observed pattern`: The method moves computational work from repeated full-gradient evaluation into cached component state, importance-weighted dual prediction, and primal prox updates.
- `Technical implication`: A fair benchmark must count the initial `m` gradients and report time-to-accuracy, not only steady-state calls.
- `Contradiction or tension`: The paper's oracle-optimality result is rigorous, while its practical advantage is unmeasured because prox cost, memory, cache locality, and parameter estimation are outside the counted oracle.
- `Observed pattern`: Non-uniform sampling improves the bound when `L_i` are known, but learning or maintaining those constants is itself an operational task.
- `Technical implication`: The lower-bound result should be represented as a model-specific certificate with its dimension and span assumptions attached, not as a universal impossibility statement.
- `Open question`: Whether adaptive sampling, modern variance reduction, or structure-aware solvers dominate RPDG under matched wall-time, memory, and residual criteria remains unanswered by this source.
- `Reviewer hypothesis`: An instrumented prox-aware implementation may preserve the gradient advantage only when component gradients are expensive relative to primal prox and state-management costs.

## Considerations

- **Cost accounting:** Track initialization gradients, per-component gradients, primal prox calls, dual/cache updates, memory, communication, and certificate computation separately.
- **Parameter knowledge:** The stated schedules depend on `L_i`, `L`, `L_f`, and `mu`; inaccurate estimates can invalidate both convergence expectations and comparisons.
- **Numerical stability:** Importance weighting by `1/p_i` can magnify component changes when probabilities are small; floating-point and heterogeneity stress tests are necessary.
- **Stopping rules:** RPDG's analysis gives expected primal error and ergodic primal gaps, but the paper does not provide a generally computable expected primal-dual gap for the randomized method. A real solver needs observable residual and validation criteria.
- **State and privacy:** Per-component caches may be large or sensitive when components map to records or users. An implementation should minimize retained state and avoid exposing record-level gradients.
- **Comparability:** Equal component-gradient counts do not imply equal work when component functions differ in cost or sparsity.
- **Maintenance:** A solver should version parameter estimates, sampling distributions, prox implementations, stopping criteria, and benchmark manifests.

## Strengths

- The paper gives an explicit algorithm rather than only an existence result.
- The saddle-point and Bregman construction explains a concrete relationship between accelerated gradients and primal-dual updates.
- Upper bounds cover distance and ergodic primal optimality, with expectation and high-probability forms.
- The lower-bound construction makes the word "optimal" auditable by exposing the oracle model and dimensional requirement.
- Non-strongly-convex, structured nonsmooth, and unconstrained cases are treated rather than ignored.
- The conclusion clearly states parameter dependence and the lack of adaptive schedules as future work.

## Weaknesses

- No experiment measures convergence constants, runtime, memory, prox cost, or numerical stability.
- No official implementation or reproduction manifest was established.
- Initialization requires a full component-gradient pass and `O(m)` component state, which the one-gradient-per-iteration slogan can obscure.
- The headline saving depends on the relation between `L_f` and `sum_i L_i` and on which term dominates the complexity.
- The lower bound covers a restricted randomized incremental linear-span model in sufficiently high dimension, not all possible adaptive methods.
- Practical stopping and parameter-estimation strategies are underdeveloped.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add prox-aware benchmark accounting | Evaluation | Gradient calls omit material work | Honest crossover and wall-time evidence | Instrumentation overhead | Report calls, time, memory, residuals, and energy under one manifest |
| Develop guarded adaptive smoothness estimates | Parameter selection | Exact `L_i` and `mu` may be unavailable | Broader usability | Backtracking or estimation can erase gains | Compare fixed-oracle and adaptive policies with failure tests |
| Add observable stopping certificates | Solver control | Expected bounds are not live termination tests | Safer and more auditable stopping | Extra full passes or dual work | Calibrate residual/certificate thresholds against objective error |
| Evaluate history-dependent sampling | Algorithm design | Fixed probabilities may waste information | Better performance on heterogeneous components | May fall outside the lower-bound model | Pre-register adaptive rules and compare under equal total work |
| Bound cache and privacy exposure | Systems design | Per-component state can be large or record-linked | Safer deployments | Compression may change convergence | Measure memory, leakage risk, and convergence under aggregation/compression |
| Publish a deterministic reference implementation | Reproducibility | No code accompanies the theory | Enables verification and teaching | Engineering and maintenance burden | Unit tests on synthetic quadratics plus theorem-regime smoke tests |

## Potential Implementations

1. **Gradient Budget Laboratory:** a local benchmark that compares PDG, RPDG, and a simple full-gradient baseline on synthetic finite-sum quadratics while recording initialization, component gradients, prox calls, wall time, memory, and achieved objective gap.
2. **Sampling Policy Auditor:** a tool that derives proposed `p_i` values from supplied smoothness estimates, checks probability floors and importance-weight magnitudes, and refuses policies whose numerical or privacy risk exceeds a declared budget.
3. **Certificate-Gated Solver Wrapper:** a wrapper that separates training iterations from periodic validation passes, records ergodic averages, residuals, and objective estimates, and stops only when an observable acceptance rule and work budget both pass.

## Three Ways to Exercise This Research

1. **Synthetic theorem-regime check:** Objective: verify qualitative linear convergence and call-count accounting on strongly convex diagonal quadratics. Inputs: public synthetic component Hessians with known `L_i` and `mu`. Steps: implement the smallest PDG/RPDG loop, include the full initialization pass, and compare objective error versus component-gradient calls. Output: versioned curves and a work ledger. Success criterion: the implementation follows the stated update and reduces error without violating the work counter. Stop condition: residuals diverge, probabilities are invalid, or parameter assumptions fail.
2. **Heterogeneity stress test:** Objective: test the difference between uniform and non-uniform sampling. Inputs: synthetic components spanning controlled `L_i` ratios. Steps: freeze a seed, run both policies under equal gradient/prox budgets, and record importance weights, variance, wall time, and memory. Output: a crossover table. Success criterion: conclusions remain stable across repeated seeds and include uncertainty. Stop condition: numerical overflow, small-probability instability, or mismatched stopping criteria.
3. **Oracle-to-systems audit:** Objective: determine when fewer component gradients produce lower real cost. Inputs: two safe toy workloads, one gradient-dominated and one prox-dominated. Steps: profile initialization, gradient, prox, aggregation, and validation separately; compare time-to-residual. Output: a resource decomposition and go/no-go rule. Success criterion: every claimed saving is traceable to measured work. Stop condition: an uninstrumented cost channel or incomparable accuracy invalidates the result.

## Example MVP Product

- `Product name`: Gradient Budget Lab.
- `Target user`: Optimization researcher or ML-systems engineer evaluating a finite-sum solver.
- `Problem`: Oracle-complexity claims are often translated into speed claims without measuring initialization, prox work, memory, or certificate quality.
- `Core workflow`: Load a synthetic finite-sum manifest; compute `L_i` and a declared `mu`; run fixed baseline and RPDG policies; record every work channel; evaluate objective/residual checkpoints; export a provenance-rich comparison.
- `Data requirements`: Synthetic convex components, known optimum or high-accuracy reference, parameter manifest, seed list, work budget, and acceptance thresholds.
- `Architecture`: Local problem generator, solver adapters, gradient/prox counters, profiler, certificate evaluator, immutable run ledger, and report renderer.
- `Success metrics`: Correct update traces, deterministic reruns, matched residual thresholds, total component-gradient reduction, wall-time improvement, peak memory, and zero missing cost categories.
- `Risk controls`: Synthetic inputs by default, no record-level gradient logging, probability floors, finite iteration budgets, divergence detection, and no automatic production deployment.
- `Limitations`: The MVP cannot validate the paper's general theorem, prove numerical stability across applications, or establish superiority over modern finite-sum methods.
- `MVP boundary`: Offline research evaluation only; no distributed, privacy-sensitive, or consequential workload.
- `Evaluation plan`: Unit tests for counters and sampling; exact solutions for small quadratics; repeated-seed convergence plots; uniform/non-uniform ablation; and a gradient-dominated versus prox-dominated crossover study.
- `Failure modes`: Incorrect initialization accounting, stale component caches, invalid importance weights, unmatched stopping rules, misleading objective-only comparisons, and profiling overhead that distorts small problems.
- `Maintenance plan`: Pin solver versions, problem manifests, parameter estimates, seeds, and acceptance rules; rerun regression cases after any update.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| *Convex programming with fast proximal and linear operators* | Related Black Lake research | Shows how proximal and affine structure controls real solver cost beyond gradient-oracle counts. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260730-Epsilon%20Prox%20Affine/epsilon_prox_affine_manuscript.md |
| *Local Stochastic Bilevel Optimization with Momentum-Based Variance Reduction* | Related Black Lake research | Later stochastic-gradient setting that makes variance reduction and complexity-to-systems transfer explicit. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-Local%20Stochastic%20Bilevel/local_stochastic_bilevel_manuscript.md |
| *Policy Mirror Descent for Regularized Reinforcement Learning* | Related Black Lake research | Uses regularizer-generated Bregman geometry and distinguishes exact linear convergence from bounded-error floors. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md |
| RPDG technical-report record | Primary author deposit | Preserves the source-era description and update date. | https://optimization-online.org/?p=13502 |
| Mathematical Programming record | Published identity | Establishes the published DOI and bibliographic form. | https://doi.org/10.1007/s10107-017-1173-0 |

Exactly three related DEP entries were used for repository synthesis. Other items in this table are primary records for the selected paper, not additional DEP relationships.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1507.02000 | Title, authors, dates, version, abstract, subjects, and public locators | 2026-08-04 | Canonical metadata; abstract not used as full-paper evidence |
| R2 | https://arxiv.org/pdf/1507.02000 | Complete method, algorithms, theorems, proofs, extensions, and conclusion | 2026-08-04 | Verified local PDF withheld |
| R3 | https://ar5iv.labs.arxiv.org/html/1507.02000 | Searchable full-paper cross-check | 2026-08-04 | Approved fallback; verified local HTML withheld |
| R4 | https://arxiv.org/e-print/1507.02000 | Source-package acquisition attempt | 2026-08-04 | Unavailable after bounded broker attempt |
| R5 | https://doi.org/10.48550/arXiv.1507.02000 | Persistent arXiv identity | 2026-08-04 | DOI locator |
| R6 | https://doi.org/10.1007/s10107-017-1173-0 | Published article identity | 2026-08-04 | Publisher DOI; full text not collected |
| R7 | https://optimization-online.org/?p=13502 | Author-deposited technical-report context | 2026-08-04 | Primary author deposit |
| R8 | https://dblp.org/rec/journals/mp/LanZ18 | Venue, volume, pages, year, and DOI cross-check | 2026-08-04 | Bibliographic record |
| R9 | `.lake-data/DEP-E/DEP-E-20260730-Epsilon Prox Affine/epsilon_prox_affine_manuscript.md` | Related prox/system synthesis | 2026-08-04 | Repository-relative processed artifact |
| R10 | `.lake-data/DEP-E/DEP-E-20260728-Local Stochastic Bilevel/local_stochastic_bilevel_manuscript.md` | Related stochastic-gradient synthesis | 2026-08-04 | Repository-relative processed artifact |
| R11 | `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` | Related Bregman/convergence synthesis | 2026-08-04 | Repository-relative processed artifact |

## Appendix

### Selection and dedup record

| Field | Result |
|---|---|
| Random method | `rg` PDF enumeration, unique parent units, all-time used-ID exclusion, then uniform PowerShell `Get-Random` index |
| PDF candidates | 75,960 |
| Parent-paper units | 75,957 |
| Used base IDs | 2,030 |
| Used-ID units excluded | 565 |
| Identifier-incomplete units withheld | 185 |
| Eligible units | 75,207 |
| Selected zero-based eligible index | 75,124 |
| Duplicate/recent rejections | 0 |
| Reselections | 0 |
| Public-safe 24-hour cutoff date | 2026-08-03 |

### Source-integrity record

| Check | Result |
|---|---|
| Initial state | `partial`: valid PDF, missing verified full-paper HTML |
| Repair | Existing PDF preserved; metadata and approved ar5iv full-paper fallback collected through one bounded broker workflow |
| PDF | 478,223 bytes; `%PDF-` header; trailing `%%EOF`; 31 pages; unencrypted |
| Full-paper HTML | 5,577,971 bytes; 219,658 stripped body characters; document marker; 89 headings; six independently observed structure terms |
| Metadata HTML | 42,216 bytes |
| Source package | Unavailable after bounded attempt |
| Partial files | 0 |
| Final state | `complete` |
| Source upload | None; all original and derived source material withheld locally |

### Replication checklist

- Implement Algorithms 3-4 with explicit initialization accounting.
- Verify component sampling and importance-weighted aggregate updates against hand-computed toy cases.
- Use strongly convex quadratics with known optimum, `L_i`, `L_f`, and `mu`.
- Record component gradients, full-gradient equivalents, prox calls, wall time, peak memory, and residuals.
- Compare uniform and non-uniform sampling under matched total-work and accuracy budgets.
- Stress small sampling probabilities, component heterogeneity, and inaccurate smoothness estimates.
- Do not claim theorem reproduction from a few numerical examples; treat them as implementation checks.
