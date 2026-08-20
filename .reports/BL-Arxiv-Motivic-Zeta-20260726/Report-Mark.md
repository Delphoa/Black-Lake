# Report-Mark: Motivic Zeta Depth Structure

Run date: 2026-07-26

## Source Metadata

| Field | Evidence |
|---|---|
| Paper | *The depth structure of motivic multiple zeta values* |
| Author | Jiangtao Li |
| Identifier | [arXiv:1710.06135v4](https://arxiv.org/abs/1710.06135v4); [DOI](https://doi.org/10.48550/arXiv.1710.06135) |
| Dates | Submitted 2017-10-17; arXiv record reports v4 on 2018-08-13 |
| Primary evidence | [PDF](https://arxiv.org/pdf/1710.06135), [full-paper HTML](https://arxiv.org/html/1710.06135), and [source package locator](https://arxiv.org/e-print/1710.06135) |
| Source state | Complete locally verified paper bundle; source documents, extracted text, caches, and verification records were withheld locally and not uploaded. |

## Concise Research Notes

**Problem.** The paper studies the depth filtration of motivic multiple zeta values (MZVs), seeking structural explanations for motivic Broadhurst–Kreimer dimension conjectures. Weight is the sum of indices and depth is their count.

**Method.** The author constructs maps related to the motivic Galois action and relates depth-graded spaces to restricted even period polynomials. The full text gives a depth-two short exact sequence and builds analogous maps for higher depth through the depth-graded motivic Lie algebra.

**Evidence and results.** The source states an exact sequence in depth two; it also states depth-three injectivity/surjectivity results for the constructed maps and gives conditional higher-depth exact-sequence consequences under three Lie-algebra conjectures. Its final section links a depth-three totally-odd claim to a linear-algebra isomorphism conjecture. These are source theorem and conjecture statements, not independently verified proofs.

**Limitations.** Higher-depth conclusions are conditional or conjectural, and this review did not reproduce symbolic calculations, independently derive the maps, or machine-check any proof. The paper is mathematical theory rather than an empirical benchmark.

**Implementation relevance.** The paper suggests a safe research-tool pattern: encode finite-weight vector spaces, maps, kernels, and exactness checks with exact arithmetic, then maintain a boundary between instance-level checks and general theorems.

**Reviewer interpretation.** Its reusable lesson is not that finite computation resolves the conjectures; it is that a layered representation can turn a global dimension question into auditable map, kernel, cokernel, and assumption checks.

## Evidence and Attribution

- The official [arXiv record](https://arxiv.org/abs/1710.06135) supports title, author, dates, version, abstract, subject classification, and canonical links.
- The inspected [PDF](https://arxiv.org/pdf/1710.06135) and [full-paper HTML](https://arxiv.org/html/1710.06135) support the definitions, theorem/conjecture labels, motivic Galois action, Lie algebra, short exact sequences, and depth-two/depth-three discussion.
- The [arXiv DOI](https://doi.org/10.48550/arXiv.1710.06135) is the persistent identifier. The public [source-package locator](https://arxiv.org/e-print/1710.06135) is retained for provenance only; no source package is deposited here.

## Related DEP Entries

1. [MOCS Flexible Lengths](../../.lake-data/DEP-E/Series%20001/DEP-E-20260724-MOCS%20Flexible%20Lengths/mocs_flexible_lengths_manuscript.md) — formal generalized-Boolean-function construction, exact correlation identities, and instance-certificate boundaries.
2. [4 Adic Complexity](../../.lake-data/DEP-E/Series%20001/DEP-E-20260721-4%20Adic%20Complexity/4_adic_complexity_manuscript.md) — finite-alphabet sequences, an algebraic complexity invariant, and a provenance-first boundary around unreplicated claims.
3. [Integrals and Rigidity](../../.lake-data/DEP-E/Series%20001/DEP-E-20260717-Integrals%20and%20Rigidity/integrals_and_rigidity_manuscript.md) — theorem-driven monotonicity, equality conditions, and explicit limits on independent proof assurance.

## Synthesis Note

### Concept Bridge

All four artifacts use structured objects to constrain what a valid conclusion can be. Li's paper organizes MZVs by depth and studies maps between graded spaces; MOCS turns parameterized Boolean-function constructions into cancellation identities; 4-adic complexity supplies a sequence invariant; Integrals and Rigidity uses monotonic quantities and equality cases to trigger geometric conclusions. The common bridge is a checkable intermediate object—map, residual, invariant, or defect term—rather than an unbounded narrative claim.

### Potential Implementations

1. **Finite-weight exactness notebook:** represent small graded bases and maps over exact rational arithmetic; report rank, kernel, and cokernel while refusing to generalize beyond enumerated weights.
2. **Certificate-aware sequence lab:** generate small MOCS or quaternary examples and attach exact residual tables, linking construction claims to explicit test vectors.
3. **Assumption-to-obligation registry:** record each theorem's hypotheses, derived invariant, expected equality condition, and unresolved proof dependency for review.

### Deeper Relationship Observations

1. Depth filtrations, correlation constraints, and geometric defect integrals all compress a large problem into graded or scale-indexed layers where failure can be localized.
2. Exactness and rigidity have a similar review role: both demand that no unaccounted defect remains between assumptions and conclusion.
3. Finite computation can validate a representation or expose a counterexample, but it cannot replace a general proof without an explicit completeness argument.

### Conceptual Similarities

1. Each artifact relies on a mathematically defined invariant rather than a subjective score.
2. Each separates a source theorem or reported construction from reviewer-level implementation interpretation.
3. Each benefits from proof-carrying outputs: parameters, maps, residuals, assumptions, and traceable source identity.

### MVP Implementations with Code Mock-Ups

1. **Exactness ledger**

```python
from fractions import Fraction

def rank_2x2(a, b, c, d):
    return 2 if a * d - b * c != 0 else int(any(x != 0 for x in (a, b, c, d)))

assert rank_2x2(Fraction(1), 0, 0, Fraction(1)) == 2
```

2. **Cancellation certificate**

```python
def zero_sum_certificate(values):
    total = sum(values)
    return {"sum": total, "valid": total == 0, "count": len(values)}

assert zero_sum_certificate([1, -1, 1, -1])["valid"]
```

3. **Assumption gate**

```python
def review_gate(assumptions, checks):
    missing = [name for name in assumptions if not checks.get(name, False)]
    return {"status": "ready" if not missing else "blocked", "missing": missing}

assert review_gate(["basis", "map"], {"basis": True, "map": False})["status"] == "blocked"
```

### Developer Challenges

1. Build exact-arithmetic prototypes that show dimensions and residuals without implying a proof of an unbounded family.
2. Version every basis convention, grading, index order, and map definition so a certificate remains reproducible.
3. Design reviewers that surface conditional dependencies instead of silently upgrading conjectures into facts.

### Author Challenges

1. Provide small, independently executable finite-weight examples of the maps and exact sequences to ease audit and pedagogy.
2. Clarify which higher-depth implications depend on each individual Lie-algebra conjecture and which do not.
3. Explore a formalization path for the depth-two construction that can preserve notation while exposing all proof obligations.

## Validation Notes

- Uniform selection used 75,781 PDF candidates and zero-based index 55,420; the chosen unit had no dedup collision and required no reselection.
- The selected unit began partial due to missing full-paper HTML. Review began only after a bounded local repair passed PDF header/EOF and full-paper HTML body, document-marker, heading, and paper-structure checks.
- Public artifacts cite only public URLs and repository-relative paths. No PDF, HTML, source archive, cache, extracted source text, local path, user identifier, machine detail, timezone, or exact execution time is included.

## Attribution Block

- Source URL: https://arxiv.org/abs/1710.06135
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Canonical metadata, title, author, dates, abstract, and public locators.
- Source URL: https://arxiv.org/pdf/1710.06135
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Complete primary paper inspected locally; file withheld.
- Source URL: https://arxiv.org/html/1710.06135
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Full-paper HTML inspected locally; file withheld.
- Source URL: https://arxiv.org/e-print/1710.06135
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Public source-package locator; archive withheld.
- Source URL: https://doi.org/10.48550/arXiv.1710.06135
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Persistent arXiv identifier.
- Repository file: `.lake-data/DEP-E/DEP-E-20260724-MOCS Flexible Lengths/mocs_flexible_lengths_manuscript.md`
  - Applies to: Synthesis Note.
  - Notes: Formal construction and certificate-context bridge.
- Repository file: `.lake-data/DEP-E/DEP-E-20260721-4 Adic Complexity/4_adic_complexity_manuscript.md`
  - Applies to: Synthesis Note.
  - Notes: Sequence-invariant and review-boundary bridge.
- Repository file: `.lake-data/DEP-E/DEP-E-20260717-Integrals and Rigidity/integrals_and_rigidity_manuscript.md`
  - Applies to: Synthesis Note.
  - Notes: Theorem, equality, and rigidity-review bridge.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: all generated artifacts.
  - Notes: Live repository deposition and attribution authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E filing and publication-index update.
  - Notes: Live DEP-E path and index authority.
