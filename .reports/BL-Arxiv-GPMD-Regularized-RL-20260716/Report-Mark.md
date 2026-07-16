# Report-Mark: GPMD Regularized RL

## Review Status

- Paper: arXiv:2105.11066v4; SIAM Journal on Optimization 33(2), 1061-1091 (2023)
- Source: verified complete PDF plus approved ar5iv full-paper HTML; SIAM publisher metadata
- Review: generalized Bregman update, exact/approximate convergence, synthetic experiments, and stated future work
- Reproduction: none; source files and extracted text withheld

## Source Metadata

| Field | Value |
|---|---|
| Title | Policy Mirror Descent for Regularized Reinforcement Learning: A Generalized Framework with Linear Convergence |
| Authors | Wenhao Zhan; Shicong Cen; Baihe Huang; Yuxin Chen; Jason D. Lee; Yuejie Chi |
| arXiv / DOI | arXiv:2105.11066v4 / 10.1137/21M1456789; arXiv DOI 10.48550/arXiv.2105.11066 |
| Dates | arXiv 2021-05-24 to 2023-01-10; publisher online 2023-06-22 |
| Availability | arXiv non-exclusive license; SIAM copyright; no official code identified |

## Concise Research Notes

GPMD solves discounted, infinite-horizon tabular regularized MDPs by matching the generalized Bregman divergence to the convex regularizer and recursively updating a subgradient surrogate. The method contains entropy-regularized natural policy gradient and, at infinite learning rate, regularized policy iteration as special cases.

Theorem 1 gives global linear convergence of regularized Q and value estimates for any positive learning rate, without requiring the regularizer to be strongly convex or smooth. Policy convergence additionally requires strong convexity. The iteration bound is proportional to `(1 + eta*tau)/(eta*tau*(1-gamma)) * log(C/epsilon)` and depends at most logarithmically on state-action dimension. Theorem 2 preserves the rate until a floor controlled by policy-evaluation and subproblem errors.

Experiments use random 200-state/50-action MDPs, Tsallis-2 entropy or a log barrier, three learning rates, 3,000 iterations, and averages over five runs. GPMD converges faster than PMD for Tsallis and avoids the roughly `1e-2` PMD floor in the constraint example. This is illustrative evidence, not a finite-sample or operational safety result.

## Evidence and Attribution

| ID | Evidence | Boundary |
|---|---|---|
| R1 | Full paper definitions and Algorithm 1 | exact tabular method; no code audit |
| R2 | Theorem 1 and proof | mathematical claim transcribed; proof not independently checked |
| R3 | Algorithm 2 and Theorem 2 | bounded-error oracle model, not a concrete sampling implementation |
| R4 | Figure 1 and experiment text | five-run synthetic illustration; no raw data/code |
| R5 | Discussion/future work | explicit limits: convex/tabular; sample complexity/function approximation open |
| R6 | SIAM publisher record | publication, pages, dates, publisher DOI |
| R7 | Three related DEP entries | conceptual/adjacent evidence only |
| R8 | Selection, repair, cache, and dedup records | operational evidence |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md` - abstract MDP safety monitoring and controller switching.
2. `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` - empirical proxy-reward policy optimization with function approximation.
3. `https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260715-Tech%20Intel%200102/daily_research_findings_2026-07-15_0102.md` - distributional-RL risk-claim auditing against environment ground truth.

## Synthesis Note

### Concept Bridge

GPMD supplies an optimization theorem for a precisely defined regularized tabular objective. Mosaic shows how MDP abstractions and constraint signals enter an operational monitor with fallbacks; ConMax shows how modern function-approximation policy training depends on composite proxy rewards; the distributional-RL audit shows that learned risk representations can look meaningful while failing ground-truth tests. Together they motivate an objective-to-outcome audit: prove the solver where possible, then test whether the regularizer, approximation, and environment actually express the intended constraint.

### Potential Implementations

1. **Regularizer-aware tabular solver** - implement entropy, Tsallis, weighted-cost, and log-barrier GPMD with theorem-aligned diagnostics.
2. **Approximation-floor harness** - inject controlled evaluation/optimization error and compare observed plateaus with Theorem 2 bounds.
3. **Constraint validity auditor** - compare optimized surrogate constraints with environment outcomes, violations, and fallback interventions.

### Deeper Relationship Observations

1. Mosaic operationalizes an MDP safety signal, but its fallback-controller failures demonstrate why convergence to a modeled objective is not a safety guarantee.
2. ConMax's composite confidence rewards extend the regularizer idea into large function approximators, where geometry and bounded-error assumptions are far less controlled.
3. The distributional-RL audit targets semantic validity rather than solver convergence, filling the most important gap between a risk-shaped objective and a real risk claim.

### Conceptual Similarities

1. Each artifact treats policy behavior as an optimization-and-control problem rather than a static prediction task.
2. Each relies on a designed representation of preference, constraint, confidence, or risk that may diverge from the intended outcome.
3. Each needs explicit approximation, calibration, failure, and environment-ground-truth evidence before deployment claims.

### MVP Implementations with Code Mock-ups

1. **Bound calculator**

```python
from math import log

def iterations(eta: float, tau: float, gamma: float, c: float, eps: float) -> float:
    return (1 + eta * tau) / (eta * tau * (1 - gamma)) * log(c / eps)
```

2. **Constraint witness**

```python
def violation_rate(actions: list[bool]) -> float:
    return sum(actions) / max(1, len(actions))
```

3. **Error-floor check**

```python
def floor_exceeded(error: float, predicted_floor: float, tolerance: float) -> bool:
    return error > predicted_floor + tolerance
```

### Developer Challenges

1. Implementing generalized subgradient/Bregman updates robustly at simplex boundaries and infinite-valued constraints.
2. Separating iteration count from policy-evaluation, subproblem, memory, sample, and wall-clock costs.
3. Producing deterministic ground-truth and approximation-error measurements across seeds and regularizers.

### Author Challenges

1. Release reference code, experiment seeds/data, and theorem-to-implementation tests for nonsmooth regularizers.
2. Provide concrete finite-sample guarantees and experiments with rollout-based evaluation rather than only bounded-error oracles.
3. Extend and stress-test function approximation, nonconvex regularizers, continuous actions, multi-agent settings, and real constraint outcomes.

## Validation Notes

- Uniform first draw: index 8,809/75,776; no exclusions, reselections, or duplicate markers.
- PDF 992,721 bytes with valid header/EOF; ar5iv HTML 5,461,972 bytes with 267,300 body chars, 86 headings, and six structure terms; final source state complete.
- Cache miss to cached in about 1.5 seconds; 107,685/267,835 PDF/HTML text bytes; no source package.
- SIAM DOI/volume/pages/history verified; author page and focused GitHub search found publication references but no official implementation.
- Schema, exact-count, public-safety, and seven-file no-source allowlist are validated before submission.

## Attribution Block

- arXiv: https://arxiv.org/abs/2105.11066v4
- HTML/PDF: https://ar5iv.labs.arxiv.org/html/2105.11066 ; https://arxiv.org/pdf/2105.11066
- Publisher: https://epubs.siam.org/doi/10.1137/21M1456789
- DOI: https://doi.org/10.1137/21M1456789 ; https://doi.org/10.48550/arXiv.2105.11066
- Nature: independent review; no proof/result reproduced; no source, cache, or extracted-text file uploaded.
