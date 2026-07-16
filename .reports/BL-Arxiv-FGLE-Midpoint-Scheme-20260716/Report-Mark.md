# Report-Mark: FGLE Midpoint Scheme

## Review Status

- Paper: arXiv:1601.02301v1, *An implicit midpoint difference scheme for the fractional Ginzburg-Landau equation*
- Source: verified complete PDF plus approved ar5iv full-paper HTML
- Review: discretization, norm analysis, boundedness, existence, convergence, uniqueness, iteration, and numerical evidence
- Reproduction: none; source files and extracted text withheld

## Source Metadata

| Field | Value |
|---|---|
| Title | An implicit midpoint difference scheme for the fractional Ginzburg-Landau equation |
| Authors | Pengde Wang; Chengming Huang |
| ID / DOI | arXiv:1601.02301v1 / 10.1016/j.jcp.2016.02.018 |
| Date | Submitted 2016-01-11; journal issue 2016-05-01 |
| Publication | *Journal of Computational Physics* 312, 31-49 |
| License | CC BY-NC-SA 4.0 on arXiv |

## Concise Research Notes

The method combines implicit midpoint time stepping with a second-order weighted and shifted Grünwald approximation of the Riesz fractional derivative. The paper builds discrete fractional Sobolev/norm inequalities, then proves an `l2_h` bound, existence, `O(tau^2+h^2)` convergence, and uniqueness under distinct assumptions.

The convergence theorem requires a smooth solution and sufficiently small time step but no relation between `tau` and `h`; this is the paper's “unconditional” claim. The uniqueness theorem later assumes `tau <= C h`. The whole-line equation is also truncated to a finite interval with zero exterior data while truncation error is assumed negligible.

The exact `alpha=2` table approaches second-order refinement. Fractional-order tables also report about second order, but use the same scheme at a finer grid as numerical truth. The linearized inner iteration reuses a time-invariant matrix, yet has no iteration-convergence, runtime, memory, or scaling evidence. No official implementation was found.

## Evidence and Attribution

| ID | Evidence | Boundary |
|---|---|---|
| R1 | Sections 2-3 and operator lemmas | method and norm machinery; no formal proof check |
| R2 | Theorems 4.1-4.4 | author theorem statements; assumptions differ |
| R3 | Section 5.1 iteration | implementable outline; no convergence/cost study |
| R4 | Tables 1-2 and Figures 1-6 | synthetic author results; fractional self-reference |
| R5 | arXiv/Elsevier/code search | metadata verified; no official code identified |
| R6 | Three related DEP manuscripts | conceptual context only |
| R7 | Selection, repair, cache, and dedup records | operational evidence |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md` - nonlinear PDE estimates, theorem dependencies, existence/uniqueness separation, and proof-review limits.
2. `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md` - nonlocal operator bounds, discrete reconstruction, imported lemmas, and finite-grid versus theorem evidence.
3. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - synthetic PDE validation, mesh separation, independent solver checks, mismatch testing, and cost evidence.

## Synthesis Note

### Concept Bridge

The FGLE paper contributes a complete numerical-analysis chain from nonlocal operator approximation to theorem and synthetic experiment. Global NS Existence shows how nonlinear PDE claims depend on explicit regularity, boundary, compactness, and uniqueness machinery; Flag Hardy Operators shows that nonlocal-operator bounds and discretized demonstrations must preserve geometry and imported assumptions; Acoustic Phase Retrieval supplies an empirical protocol for separating discretization, solver, model, noise, and field mismatch. Together they define a theorem-to-runtime evidence ledger.

### Potential Implementations

1. **Fractional convergence harness** - run independent `tau`, `h`, domain, and solver-tolerance sweeps against exact/manufactured and independent-solver references.
2. **Theorem-assumption ledger** - map each boundedness, existence, convergence, and uniqueness claim to its own hypotheses and imported lemmas.
3. **Structured-operator benchmark** - compare dense, Toeplitz/FFT, and preconditioned realizations at matched error and residual.

### Deeper Relationship Observations

1. FGLE and Global NS both rely on a priori estimates to control nonlinear evolution, but a numerical bound does not automatically imply iteration convergence or unique solvability.
2. FGLE's WSGD/Sobolev bridge and Flag Hardy's scale-sensitive operator bounds share a principle: nonlocal geometry must survive discretization before norm estimates are meaningful.
3. Acoustic Phase Retrieval's independent forward-solver requirement exposes the weakness of using the same FGLE scheme on a finer grid as fractional ground truth.

### Conceptual Similarities

1. All four artifacts separate theorem conditions from broader informal claims.
2. All depend on nonlocal or PDE operators whose boundary and discretization choices materially affect evidence.
3. All require explicit uncertainty about imported proofs, numerical references, and implementation realization.

### MVP Implementations with Code Mock-ups

1. **Observed-order calculator**

```python
from math import log

def observed_order(coarse: float, fine: float, ratio: float = 2.0) -> float:
    return log(coarse / fine) / log(ratio)
```

2. **Theorem-condition gate**

```python
def uniqueness_gate(tau: float, h: float, constant: float) -> bool:
    return tau <= constant * h
```

3. **Residual stop rule**

```python
def converged(previous: list[complex], current: list[complex], tol: float) -> bool:
    return max(abs(a - b) for a, b in zip(previous, current)) <= tol
```

### Developer Challenges

1. Implementing the dense nonlocal operator without losing accuracy, memory, or scalability.
2. Separating nonlinear iteration error from spatial, temporal, and domain-truncation error.
3. Building independent reference solvers and deterministic fixtures for fractional orders.

### Author Challenges

1. Release code, parameter files, solver tolerances, residual traces, and exact table/figure reproduction scripts.
2. Clarify theorem-specific uses of “unconditional” and reconcile convergence with the uniqueness step relation.
3. Add manufactured fractional solutions, independent solvers, domain sweeps, baseline timing, memory, and complexity evidence.

## Validation Notes

- Uniform first draw: index 47,945/75,776; no exclusions, reselections, or duplicate markers.
- PDF 1,743,106 bytes with valid header/EOF; ar5iv HTML 2,651,436 bytes with 123,389 body characters, two document markers, 51 headings, and six structure terms; final source state complete.
- Official HTML was unavailable after bounded retries. Metadata HTML was 42,428 bytes and remained metadata only; zero partials; no source package.
- Cache miss became cached in about 6.3 seconds; 53,161/123,257 PDF/HTML text bytes.
- No proof, solver, or experiment was reproduced. Focused search found no official implementation.
- Schema, exact-count, public-safety, and seven-file no-source allowlist are validated before submission.

## Attribution Block

- Paper: https://arxiv.org/abs/1601.02301v1
- HTML/PDF: https://ar5iv.labs.arxiv.org/html/1601.02301 ; https://arxiv.org/pdf/1601.02301
- Journal DOI: https://doi.org/10.1016/j.jcp.2016.02.018
- arXiv DOI: https://doi.org/10.48550/arXiv.1601.02301
- Nature: independent review; no result reproduced; no source, cache, or extracted-text file uploaded.
