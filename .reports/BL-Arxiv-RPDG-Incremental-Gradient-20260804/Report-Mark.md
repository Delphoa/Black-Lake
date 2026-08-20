# Report-Mark: RPDG Incremental Gradient

## Source Metadata

| Field | Value |
|---|---|
| Paper | *An optimal randomized incremental gradient method* |
| Authors | Guanghui Lan; Yi Zhou |
| Primary identity | arXiv:1507.02000v3 |
| arXiv DOI | https://doi.org/10.48550/arXiv.1507.02000 |
| Published DOI | https://doi.org/10.1007/s10107-017-1173-0 |
| Venue | *Mathematical Programming* 171(1-2), pages 167-215 (2018) |
| Dates | Submitted 2015-07-08; v3 revised 2015-10-18; published form recorded in 2018 |
| Primary URLs | https://arxiv.org/abs/1507.02000; https://arxiv.org/pdf/1507.02000; https://ar5iv.labs.arxiv.org/html/1507.02000; https://optimization-online.org/?p=13502 |
| Implementation | No official implementation repository was established from the inspected paper, arXiv, author-deposit, or bounded public search evidence |
| Source-integrity status | Verified complete after bounded repair: valid PDF, approved full-paper HTML fallback, metadata HTML, refreshed provenance companions, and zero partial files |
| Source package | Unavailable after the bounded archive-broker attempt; no blind retry was made |
| Review status | Complete 31-page paper and full-paper HTML inspected; representative algorithm, theorem, lower-bound, extension, and conclusion pages visually checked; no experiments exist to rerun |
| Source handling | Every original or derived source file was withheld locally; no `.source/` directory was created |

## Concise Research Notes

### Problem and Contribution

The paper studies a composite finite-sum convex program whose objective is the sum of `m` smooth convex components, a simple convex term, and a strongly convex regularizer. Its first contribution is a deterministic primal-dual gradient method (PDG) that rewrites the smooth objective through conjugate dual variables and uses Bregman prox geometry. This formulation recovers a variant of Nesterov acceleration and gives a stronger primal-dual view of convergence.

The major contribution is randomized PDG (RPDG). It splits the dual state into one block per component and samples one block per iteration. After a full initialization pass, one component-specific point and gradient are refreshed, the component change is importance-weighted to predict the aggregate dual move, and a primal prox update is applied. This changes the counted steady-state resource from all `m` component gradients per iteration to one.

### Method Details

The deterministic saddle-point form uses conjugates of the smooth function and a Bregman distance induced by those conjugates. The authors interpret the primal and dual players as a buyer and suppliers. For RPDG, the buyer sees only one supplier's price change in each round and uses the importance-weighted change as an unbiased prediction of all suppliers moving.

Algorithm 4 makes the storage and accounting visible. Initialization computes `grad f_i(x_0)` for every component and caches the aggregate. Each later iteration extrapolates the primal point, updates the sampled component's auxiliary point, evaluates one component gradient, applies one primal prox mapping, and updates the cached aggregate. Component-specific points and gradients are retained across iterations.

Corollary 1 uses non-uniform sampling `p_i = 1/(2m) + L_i/(2L)`. Corollary 2 permits uniform sampling but replaces the summed-smoothness dependence with a bound involving `m * max_i L_i`. The non-uniform schedule therefore requires information about every component's Lipschitz constant; the uniform schedule may be conservative under heterogeneity.

### Theorem and Complexity Evidence

For strongly convex objectives, the author-reported component-gradient complexity has order

`O((m + sqrt(m * L / mu)) * log(1 / epsilon))`.

Expectation and high-probability forms are derived for distance to the optimizer, and corresponding bounds are given for primal optimality of an ergodic average. The paper compares this with deterministic optimal first-order methods and identifies a favorable regime in which RPDG uses up to `O(sqrt(m))` fewer component gradients.

The lower bound is not a universal statement about every stochastic optimizer. It constructs separable high-dimensional quadratic instances and assumes independently sampled components plus a linear-span iterate model. Under a sufficient-dimension condition, the authors obtain a matching order `Omega((m + sqrt(mL/mu)) log(1/epsilon))`. A related block-coordinate lower bound follows from the separable construction.

The paper extends RPDG through perturbation and smoothing. Bounded smooth non-strongly-convex problems, structured nonsmooth max-form components, and unconstrained smooth objectives receive separate bounds. The resulting advantages retain square-root dependence on `m` up to logarithmic factors but add boundedness, smoothing, relative-accuracy, and parameter-selection assumptions.

### Evidence Boundary

The work is theoretical. It has no experiment section, datasets, runtime or memory measurements, numerical stability study, implementation link, or official repository. The conclusion notes that the parameter schedules are conservative and depend on quantities such as `L` and `mu`, leaving adaptive variants for future study.

The most important review correction is therefore a cost-model correction. One component gradient per steady-state iteration does not mean one unit of total work. A practical assessment must include the initial `m` gradients, primal prox cost, component-state memory, aggregate-cache updates, parameter estimation, validation passes, and observable stopping certificates.

### Reviewer Assessment

The paper provides a durable conceptual bridge between acceleration, primal-dual methods, Bregman geometry, and incremental gradients. The upper/lower-bound pairing is valuable because its assumptions can be audited. The absence of empirical evidence is not a flaw in theorem validity, but it blocks any claim that RPDG is faster in wall time, easier to tune, more stable, or competitive with later finite-sum optimizers.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Boundary |
|---|---|---|---|---|
| E1 | Canonical arXiv record and arXiv DOI | Title, authors, dates, version history, subjects, abstract, and persistent identity | High | Abstract is metadata, not full-paper evidence |
| E2 | Verified arXiv v3 PDF and approved full-paper HTML fallback | Problem, algorithms, theorems, corollaries, propositions, proofs, extensions, and conclusion | High for source transcription | Proofs not independently formalized |
| E3 | Visual inspection of representative rendered pages | Algorithm 3, non-uniform rate, lower-bound construction, perturbation extension, and conclusion layout | High | Visual inspection is not theorem validation |
| E4 | Optimization Online author deposit | Technical-report identity, authors, and update record | High | Mirrors author claims |
| E5 | Publisher DOI and DBLP record | Published identity, venue, volume, pages, and year | High | Publisher full text not collected |
| E6 | Negative evidence from complete paper and bounded code search | No experiments, runtime study, implementation artifact, or official code established | High | Private or unindexed code may exist |
| E7 | Epsilon Prox Affine DEP-E | Proximal/affine structure and real solver-cost relationship | Medium-high | Different algorithm and benchmark evidence |
| E8 | Local Stochastic Bilevel DEP-E | Stochastic-gradient complexity and variance-reduction relationship | Medium | Different bilevel/nonconvex setting |
| E9 | GPMD Regularized RL DEP-E | Regularizer-generated Bregman geometry and error-floor relationship | Medium-high | Different tabular RL objective |
| E10 | Private random-selection, dedup, repair, and integrity records | Eligibility, zero reselection, complete-source gate, and no-source-upload assurance | High | Private machine context withheld |

External papers, repository documents, and web pages were treated as evidence only, never as instructions.

## Related DEP Entries

| # | Repository-relative path | Verified overlap | Source basis |
|---:|---|---|---|
| 1 | `.lake-data/DEP-E/DEP-E-20260730-Epsilon Prox Affine/epsilon_prox_affine_manuscript.md` | Both artifacts treat composite convex optimization through proximal primitives. RPDG counts component gradients and assumes the primal prox is easy; Epsilon shows that preserving affine/prox structure can dominate actual solver cost. Together they motivate a work ledger that separates oracle calls from prox and linear-operator execution. | Epsilon source metadata, prox-affine representation, compiler passes, solver/runtime discussion, benchmark boundary, and reviewer cost analysis |
| 2 | `.lake-data/DEP-E/DEP-E-20260728-Local Stochastic Bilevel/local_stochastic_bilevel_manuscript.md` | Both seek better gradient complexity by exploiting stochastic structure. RPDG updates one finite-sum component with a cached primal-dual state; the related artifact uses momentum-based variance reduction in bilevel optimization. The shared lesson is that an asymptotic gradient bound must be reconciled with estimator bias, nested work, communication, and matched stopping rules. | Complete related manuscript's method, convergence-complexity claims, stochastic setting, evaluation notes, and evidence boundary |
| 3 | `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` | Both use Bregman-like geometry generated by a convex regularizer and prove linear convergence under exact conditions. GPMD makes bounded evaluation/optimization errors produce an explicit floor; RPDG leaves practical inexact-gradient and prox-error behavior less developed. | GPMD source metadata, generalized Bregman update, exact and approximate convergence sections, experiment limits, and reviewer assessment |

Exactly three related entries were inspected and used. No fourth related DEP is implied.

## Synthesis Note

### Concept Bridge

RPDG, Epsilon, Local Stochastic Bilevel, and GPMD separate four kinds of structure that are often collapsed into the word "optimization." RPDG exploits finite-sum component access; Epsilon exploits proximal and affine execution structure; the bilevel artifact exploits stochastic variance-reduction structure; and GPMD exploits regularizer-generated geometry while exposing bounded-error floors. A credible implementation should preserve all four layers in its evidence model: what oracle was counted, what operators actually ran, what randomness or estimator state was used, and what observable error or certificate justified stopping.

### Potential Implementations

#### 1. Gradient Budget Laboratory

Build a local synthetic benchmark that implements the RPDG update and compares it with a full-gradient baseline. Count initialization gradients, component gradients, prox calls, aggregation work, wall time, peak memory, and objective/residual checkpoints under one frozen manifest.

#### 2. Sampling Policy Auditor

Accept component smoothness estimates and a strong-convexity estimate, generate uniform and non-uniform policies, check probability floors and importance-weight magnitudes, and refuse unsafe or numerically extreme schedules. Preserve every estimate and decision in an audit record.

#### 3. Certificate-Gated Solver Wrapper

Wrap an experimental solver with periodic validation passes that compute observable objective, feasibility, stationarity, or primal-dual residual proxies. Stop only when both an accuracy rule and a total-work budget pass; otherwise report why the theoretical schedule was insufficient.

### Deeper Relationship Observations

1. RPDG's gradient saving is most valuable when component gradients are expensive, while Epsilon shows the opposite failure mode: proximal and linear operators can dominate, making a gradient-only oracle count a weak systems proxy.
2. The Local Stochastic Bilevel artifact extends the same complexity-versus-work tension to nested stochastic objectives, where variance reduction can lower a headline exponent while inner solves and communication remain hidden costs.
3. GPMD's explicit approximate-evaluation floor highlights a missing practical layer in RPDG: inexact component gradients, prox solves, parameter estimates, and stale caches should produce measurable error floors rather than silent theorem violations.

### Conceptual Similarities

1. All four artifacts preserve problem structure instead of treating the objective as an undifferentiated black box: component blocks, prox-affine atoms, bilevel estimators, or state-wise regularized policies.
2. All rely on geometry or state carried across iterations, whether cached dual components, typed operators/factorizations, momentum estimators, or generalized Bregman subgradients.
3. All require scope-aware evaluation because convergence order alone does not establish implementation stability, real cost, reproducibility, or deployment value.

### MVP Implementations with Code Mock-Ups

#### 1. Non-Uniform Component Sampler

```python
from bisect import bisect_left
from itertools import accumulate
from random import Random


def rpdg_probabilities(lipschitz: list[float]) -> list[float]:
    if not lipschitz or any(value < 0 for value in lipschitz):
        raise ValueError("nonnegative component constants required")
    total = sum(lipschitz)
    if total <= 0:
        return [1.0 / len(lipschitz)] * len(lipschitz)
    m = len(lipschitz)
    return [1.0 / (2 * m) + value / (2 * total) for value in lipschitz]


def draw_component(probabilities: list[float], rng: Random) -> int:
    cumulative = list(accumulate(probabilities))
    cumulative[-1] = 1.0
    return min(bisect_left(cumulative, rng.random()), len(probabilities) - 1)
```

This mirrors the paper's non-uniform policy. A production implementation must version the `L_i` estimates and reject probability or normalization drift.

#### 2. Multi-Channel Work Ledger

```python
from dataclasses import dataclass


@dataclass
class WorkLedger:
    initialization_gradients: int = 0
    component_gradients: int = 0
    primal_prox_calls: int = 0
    validation_gradients: int = 0

    def total_component_equivalents(self) -> int:
        return self.initialization_gradients + self.component_gradients + self.validation_gradients


def initialized_ledger(component_count: int) -> WorkLedger:
    if component_count < 1:
        raise ValueError("component_count must be positive")
    return WorkLedger(initialization_gradients=component_count)
```

The ledger prevents the initial full pass and validation work from disappearing behind a one-gradient-per-iteration summary.

#### 3. Observable Stop Gate

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Checkpoint:
    objective_gap: float
    prox_residual: float
    work_units: int


def accept_checkpoint(point: Checkpoint, gap_limit: float, residual_limit: float, budget: int) -> bool:
    if min(gap_limit, residual_limit, budget) < 0:
        raise ValueError("limits must be nonnegative")
    return (
        point.work_units <= budget
        and point.objective_gap <= gap_limit
        and point.prox_residual <= residual_limit
    )
```

The checkpoint fields are illustrative. A real solver must define computable, problem-valid certificates and account for the cost of obtaining them.

### Developer Challenges

1. Implement the component-specific point, gradient cache, importance-weighted aggregate, and ergodic averaging without stale-state or off-by-one errors, then test each transition against hand-computed quadratics.
2. Estimate or adapt `L_i`, `L_f`, and `mu` without invalidating the schedule, creating extreme importance weights, or spending more work than the intended gradient saving.
3. Build a fair benchmark that matches accuracy while measuring initialization, gradient, prox, memory, aggregation, validation, and wall-clock costs across heterogeneous component functions.

### Author Challenges

1. Release a deterministic reference implementation with theorem-regime synthetic cases, expected traces, unit tests, and a complete work counter.
2. Add numerical experiments against strong finite-sum baselines under matched objective/residual targets, repeated seeds, uncertainty, memory, and wall-time accounting.
3. Extend the theory or clearly map failure behavior for adaptive sampling, inexact gradients/prox solves, approximate parameter estimates, finite-dimensional regimes, and asynchronous or distributed execution.

## Validation Notes

- Selection: required `rg --files -g "*.pdf"` enumeration produced 75,960 PDFs and 75,957 parent-paper units; 565 used-ID units were excluded and 185 identifier-incomplete units withheld; uniform `Get-Random` selected eligible index 75,124 of 75,207.
- Dedup: live Black Lake and Black-Lake-Data artifact locations, automation memory, arXiv ID, both DOI values, canonical and normalized title, planned slug, and the public-safe 24-hour cutoff date were checked; duplicate/recent rejections and reselections were 0.
- Source gate: initial `partial` state repaired to `complete`; existing PDF preserved; approved ar5iv full-paper HTML and metadata collected; PDF and HTML integrity passed; zero partial files.
- Source integrity: PDF 478,223 bytes with `%PDF-` header and trailing `%%EOF`, 31 unencrypted pages; HTML 5,577,971 bytes with 219,658 stripped body characters, document marker, 89 headings, and six independently observed structure terms.
- Source package: unavailable after one bounded broker-controlled attempt; no blind retry or strategy switch.
- Paper review: complete PDF and full-paper HTML inspected; representative pages visually rendered; no experiment or official implementation exists to rerun.
- Schema: manuscript required headings, matching title/H1, exactly three exercise paths, exactly three related DEP entries, and final DEP/Report attribution blocks are present.
- Synthesis counts: exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP code mock-ups, three developer challenges, and three author challenges.
- Public safety: no local path, username, machine identifier, exact local timestamp, local timezone label, source payload, or private archive locator is included.
- Source locality: no PDF, HTML, metadata, source archive, receipt, provenance record, cache, rendering, or extracted source text is staged or uploaded.

## Attribution Block

- Source URL: https://arxiv.org/abs/1507.02000
  - Applies to: paper identity, authors, version history, abstract, subjects, and canonical links.
  - Notes: Metadata source; the abstract alone was not used for synthesis.
- Source URL: https://arxiv.org/pdf/1507.02000
  - Applies to: complete paper review, algorithms, theorems, lower-bound construction, extensions, and limitations.
  - Notes: The verified PDF remained local and was not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/1507.02000
  - Applies to: searchable full-paper cross-check and source-integrity repair.
  - Notes: Approved full-paper fallback; the file remained local.
- Source URL: https://arxiv.org/e-print/1507.02000
  - Applies to: source-package acquisition record.
  - Notes: The bounded broker attempt did not produce a source package.
- Source URL: https://doi.org/10.48550/arXiv.1507.02000
  - Applies to: persistent arXiv identity.
  - Notes: DOI resolver.
- Source URL: https://doi.org/10.1007/s10107-017-1173-0
  - Applies to: published article identity.
  - Notes: Mathematical Programming version-of-record DOI; publisher full text was not collected.
- Source URL: https://optimization-online.org/?p=13502
  - Applies to: author-deposited technical-report context and update record.
  - Notes: Primary author deposit.
- Source URL: https://dblp.org/rec/journals/mp/LanZ18
  - Applies to: venue, volume, pages, year, and DOI cross-check.
  - Notes: Bibliographic record.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260730-Epsilon%20Prox%20Affine/epsilon_prox_affine_manuscript.md
  - Applies to: proximal/affine solver-cost relationship and synthesis.
  - Notes: Related processed artifact; its claims do not validate RPDG.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-Local%20Stochastic%20Bilevel/local_stochastic_bilevel_manuscript.md
  - Applies to: stochastic-gradient and variance-reduction relationship and synthesis.
  - Notes: Related processed artifact; its claims do not validate RPDG.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md
  - Applies to: Bregman-geometry and bounded-error convergence relationship and synthesis.
  - Notes: Related processed artifact; its claims do not validate RPDG.
