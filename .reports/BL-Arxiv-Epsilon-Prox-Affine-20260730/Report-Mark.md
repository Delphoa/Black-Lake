# Report-Mark: Epsilon Prox-Affine

- Public-safe review date: `2026-07-30`
- Review type: Randomized source-first arXiv DEP-E review
- Primary subject: *Convex programming with fast proximal and linear operators*
- Source-file policy: Complete source evidence was inspected locally and withheld; no source file is included in this report or DEP.

## Source Metadata

| Field | Value |
|---|---|
| Title | *Convex programming with fast proximal and linear operators* |
| Authors | Matt Wytock; Po-Wei Wang; J. Zico Kolter |
| arXiv | `1511.04815v1` |
| arXiv record | https://arxiv.org/abs/1511.04815 |
| arXiv DOI | https://doi.org/10.48550/arXiv.1511.04815 |
| Submitted | 2015-11-16 |
| Subject | Mathematics - Optimization and Control (`math.OC`) |
| Status | Preprint in the inspected author publication record |
| Complete evidence | Verified PDF, full-paper HTML fallback, TeX/source package, rendered figures/table |
| Implementation | Paper-linked Epsilon repository/project locators were inaccessible; code was not inspected or run |
| Redistribution | All source, cache, render, and verification files withheld locally |

### Selection Record

- Enumeration: required `rg --files -g "*.pdf"` over the local archive.
- PDF candidates: `75,959`.
- Unique PDF-parent units: `75,956`.
- Used arXiv base IDs observed: `1,581`.
- Units excluded by used ID: `460`.
- Identifier-incomplete units withheld: `185`.
- Eligible units: `75,311`.
- Uniform method: PowerShell `Get-Random` over the eligible array.
- Selected zero-based eligible index: `47,711`.
- Accepted identity: arXiv `1511.04815v1`.
- Duplicate rejections/reselections: `0`.

### Dedup Record

- Scopes: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; fetched Black-Lake-Data `.lake-data`, `.logs`, `.reports`, and `.staging`.
- Keys: arXiv ID, arXiv DOI, canonical and normalized title, archive token, and planned slugs.
- Exact ID/title/slug searches: no prior deposit or marker.
- Public-safe 24-hour cutoff date: `2026-07-29`.
- Same-paper recent markers: none.

### Source Integrity Record

- Initial state: `partial`; valid PDF present, full-paper HTML absent.
- Repair: review paused; preserved the valid PDF; one bounded strategy attempted official HTML, used the approved ar5iv full-paper fallback, and fetched metadata HTML plus the source package.
- PDF: `534,013` bytes; `%PDF-` header; trailing `%%EOF`; preserved and repair copies SHA-256-identical.
- Full-paper HTML: `1,077,004` bytes; `88,927` body characters; LaTeXML document marker; `62` heading markers; four structure terms.
- Metadata HTML: `40,353` bytes.
- Source archive: `231,386` bytes.
- Unexpected partial files: `0`.
- Final state: `complete`.
- Local companion records: README, attribution record, machine-readable summary, and verification report updated.

## Concise Research Notes

### Research Question

Can a general disciplined-convex-programming interface retain enough semantic structure to execute with specialized proximal and linear operators, avoiding the cost of always lowering to generic cone form?

### Core Method

Epsilon compiles a DCP expression tree into **prox-affine form**, a sum of prox-friendly functions composed with affine maps. Compiler passes:

1. recognize structured linear maps;
2. match nonlinear subtrees to available proximal rules, with conic fallback;
3. introduce variable copies and equality constraints to expose separability; and
4. emit a typed operator graph for an ADMM-based solver.

The runtime treats dense/sparse matrices and structured maps such as scalar, diagonal, and Kronecker operators as distinct implementations. Proximal atoms include losses, norms, indicators, cones, and total variation. The design retains information that may be erased by a generic sparse-matrix cone representation.

### Mechanism

The source's durable mechanism is a three-stage chain:

`DCP semantics -> structure-preserving prox-affine IR -> specialized operator dispatch`.

Performance improves when the IR avoids unnecessary variable expansion, matrix materialization, or generic factorization. The multivariate-lasso example keeps a Kronecker map symbolic; the total-variation example keeps a direct dynamic-programming proximal operator.

### Source-Reported Evidence

- Dense lasso: approximately `10x` faster than SCS over the displayed scaling regime.
- Multivariate lasso: approximately `100x` gap; `27` seconds versus `2,192` seconds for SCS at about `13,500` variables.
- Total variation: `5.7` seconds versus `123` seconds for SCS at `10,000` variables.
- Table 1: Epsilon is fastest across all nineteen visible problem rows where comparison values are present.
- `mnist`: `0.91` seconds for Epsilon, `219.63` seconds for SCS, `1,752.97` seconds for ECOS.
- `mv_lasso`: `7.14` seconds for Epsilon versus `824.83` seconds for SCS; ECOS has no result.

### Evidence Limits

- Hardware, seeds, repeated trials, dispersion, and raw timing traces are not disclosed in the inspected paper.
- Epsilon/SCS use moderate-accuracy defaults while ECOS uses a high-accuracy default.
- Some objectives differ materially; `tv_1d` reports `2.29e5` for Epsilon and `2.95e5` for SCS.
- The source-era baselines do not establish current comparative performance.
- The paper-linked implementation was inaccessible during this review.
- Compiler/kernel correctness, algorithm convergence, and numerical stability were not independently tested.
- No code or experiment was run.

### Reviewer Interpretation

The source strongly motivates typed optimization IRs and operator registries. It does not establish that prox-affine lowering alone caused every speedup, that all emitted multi-block ADMM problems share one convergence guarantee, or that Epsilon remains reproducible and competitive. A modern implementation should pair every transformation with a semantic receipt and every solve with matched residual, feasibility, and failure evidence.

## Evidence and Attribution

| ID | Evidence | Source | Supports | Boundary |
|---|---|---|---|---|
| E1 | Canonical identity, authors, date, version, subject, DOI | https://arxiv.org/abs/1511.04815 | Metadata | Abstract is not full-paper evidence. |
| E2 | Complete architecture, equations, algorithms, examples, and conclusion | https://arxiv.org/pdf/1511.04815 | Method and results | Local PDF withheld; no independent proof. |
| E3 | Searchable complete paper | https://ar5iv.labs.arxiv.org/html/1511.04815 | Section-level cross-checks | Approved fallback; local HTML withheld. |
| E4 | Exact TeX equations, captions, Table 1 values, conclusion | https://arxiv.org/e-print/1511.04815 | Transcription and consistency | Local source archive withheld. |
| E5 | Author publication and Epsilon software context | https://zicokolter.com/publications/ | Preprint/software-link status | Does not establish current software availability. |
| E6 | Paper-linked implementation locator | https://github.com/mwytock/epsilon | Availability check | Inaccessible; no code claims derived. |
| E7 | Visual inspection of Figure 1, Figures 4-6, and Table 1 | https://arxiv.org/pdf/1511.04815 | Diagram/curve/table agreement | No plot digitization or rerun. |
| E8 | Private selection, repair, and validation records | Withheld local context | Eligibility and completeness | No local identity disclosed. |

Every quantitative statement in this report is either directly transcribed from the complete paper or labeled as reviewer interpretation. No secondary summary was used as primary technical evidence.

## Related DEP Entries

| Related entry | Concrete overlap | Source basis |
|---|---|---|
| `.lake-data/DEP-E/DEP-E-20260719-Sparse SSN PMM/sparse_ssn_pmm_manuscript.md` | Both expose structured proximal geometry so a generic outer problem can invoke a specialized inner numerical routine. SSN-PMM adds a differentiable dual and semismooth Newton inner solve; Epsilon uses compiler rules and a proximal registry. | Inspected manuscript sections on two-stage PMM, dual SSN, convergence, residuals, and implementation implications. |
| `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` | CAP's convex robust-PCA stage maps under ADMM to singular-value thresholding and elementwise soft thresholding, a direct example of Epsilon's "problem structure to fast atoms" design. | Inspected manuscript sections on the convex decomposition objective, ADMM updates, and separation from the heuristic allocation stage. |
| `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` | GPMD derives its generalized Bregman update from a convex regularizer, paralleling Epsilon's use of function geometry to select a specialized operator rather than a generic representation. | Inspected manuscript sections on convex state-wise regularizers, generalized subgradient/Bregman geometry, exact updates, and error floors. |

These three entries are conceptual and implementation bridges only. None independently reproduces or validates Epsilon's source-reported benchmarks.

## Synthesis Note

### Concept Bridge

Across Epsilon, Sparse SSN-PMM, CAP, and GPMD, efficiency comes from **exposing mathematical structure before numerical execution**. The object that crosses the architecture boundary is not an undifferentiated objective. It is a typed decomposition with domains, affine maps, regularizer geometry, proximal capabilities, and explicit constraints. The transferable system pattern is:

`semantic model -> typed decomposition -> compatible numerical atom -> residual/certificate receipt`.

Epsilon makes this compiler/runtime separation explicit. Sparse SSN-PMM shows that a carefully chosen proximal term can expose a differentiable dual. CAP shows that a convex decomposition maps naturally to two thresholding atoms plus a dual update. GPMD shows that the regularizer can generate the update geometry itself. A modern synthesis should retain these mechanisms while adding validation receipts that the source-era systems do not fully expose.

### Potential Implementations

1. **Prox-affine compiler with rule receipts.** Lower an allowlisted convex DSL to a typed IR, recording the exact equivalence rule, introduced variables, separability constraints, and conic fallbacks for every node.
2. **Certified operator registry.** Store each atom's domain, supported affine-map classes, adjoint, proximal contract, numerical limits, slow reference, randomized test receipt, and performance envelope.
3. **Matched-accuracy benchmark service.** Run structure-preserving and conic plans against identical residual/feasibility/objective gates, with compile/setup/factorization/iteration time and all failures retained.

### Deeper Relationship Observations

1. **The intermediate representation is an epistemic boundary.** Once semantic structure is erased, downstream solvers cannot recover why an operator was special; the IR determines both attainable performance and explainability.
2. **Specialization and generality are complements.** Epsilon is general because it can dispatch to many specialized atoms and fall back safely, not because one numerical kernel solves everything efficiently.
3. **Certificates must be layered.** DCP validity certifies modeling grammar, operator tests certify kernels, solver residuals certify numerical progress, and application review certifies downstream meaning; no single layer subsumes the others.

### Conceptual Similarities

1. **Epsilon and Sparse SSN-PMM:** both transform a difficult high-level objective into subproblems whose geometry admits specialized fast operators.
2. **Epsilon and CAP:** both use ADMM-style splitting to separate terms that map to distinct proximal updates.
3. **Epsilon and GPMD:** both derive update behavior from convex function structure rather than treating the objective as an opaque callable.

### MVP Implementations with Code Mock-Ups

1. **Typed operator compatibility check.**

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Atom:
    function: str
    linear_map: str


SUPPORTED = {
    ("l1_norm", "identity"),
    ("least_squares", "dense"),
    ("least_squares", "kronecker"),
    ("total_variation", "identity"),
}


def compatible(atom: Atom) -> bool:
    return (atom.function, atom.linear_map) in SUPPORTED


assert compatible(Atom("least_squares", "kronecker"))
assert not compatible(Atom("l1_norm", "dense"))
```

2. **Transformation receipt.**

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class RewriteReceipt:
    rule: str
    source_node: str
    target_nodes: tuple[str, ...]
    fallback: bool = False


def lower_norm1(variable: str) -> RewriteReceipt:
    return RewriteReceipt(
        rule="norm1_to_prox_atom_v1",
        source_node=f"norm1({variable})",
        target_nodes=(f"prox:l1_norm({variable})",),
    )


receipt = lower_norm1("x")
assert receipt.rule.endswith("_v1")
assert not receipt.fallback
```

3. **Matched-quality timing gate.**

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Run:
    solver: str
    seconds: float
    primal_residual: float
    objective_gap: float


def accepted(run: Run, residual_limit: float, gap_limit: float) -> bool:
    return (
        run.primal_residual <= residual_limit
        and run.objective_gap <= gap_limit
    )


runs = [
    Run("structure_preserving", 0.8, 8e-5, 6e-4),
    Run("conic_reference", 1.4, 7e-5, 5e-4),
]
eligible = [run for run in runs if accepted(run, 1e-4, 1e-3)]
assert len(eligible) == 2
```

Dependencies: Python 3.10+ standard library only. These examples are illustrative and local-only. They do not solve an optimization problem or certify production behavior.

### Developer Challenges

1. **Semantic correctness:** proving that every rewrite preserves objective, domain, shape, and constraints while producing actionable counterexamples when it does not.
2. **Numerical contracts:** validating adjoints, proximal optimality, factorization caching, precision behavior, and failure signaling across heterogeneous operator implementations.
3. **Fair evaluation:** separating compile/setup/factorization/iteration costs and enforcing matched solution-quality gates across solvers without hiding timeouts or unsupported cases.

### Author Challenges

1. **Reproducibility detail:** publishing hardware, package versions, seeds, repetition counts, raw traces, and complete stopping rules sufficient for independent replay.
2. **Causal attribution:** isolating how much gain comes from prox-affine representation versus kernel implementations, tolerances, factorization choices, or framework overhead.
3. **Durable software lineage:** maintaining an accessible version-pinned repository, license, test suite, benchmark manifest, and migration path as CVXPY and solver APIs evolve.

## Validation Notes

- Complete-source gate passed before synthesis.
- PDF and HTML both met the mandatory byte and structure checks.
- The abstract page was used only for metadata.
- Paper figures/table were visually inspected from the complete PDF.
- Title, authors, version, DOI, and preprint status were cross-checked against canonical/author sources.
- Exactly three related DEP entries were inspected and included.
- The Synthesis Note contains one Concept Bridge and exactly three items in each required category.
- The three Python mock-ups are standard-library-only and intended for syntax validation before submission.
- No experiment, source repository, or benchmark was executed.
- No `.source/` directory was created.
- No PDF, HTML, metadata, TeX/source archive, extracted text, cache, render, verification file, or local path is included.
- Public-output leak, heading/count, code-syntax, URL-attribution, index, and staged allowlist checks remain required immediately before commit.

## Attribution Block

- Source URL: https://arxiv.org/abs/1511.04815
  - Applies to: source identity, authors, version, date, subject, abstract context, and source locators.
  - Notes: Canonical metadata page; not treated as complete-paper evidence.
- Source URL: https://arxiv.org/pdf/1511.04815
  - Applies to: complete-paper review, equations, figures, Table 1, and conclusion.
  - Notes: PDF inspected locally and withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/1511.04815
  - Applies to: searchable complete-paper review.
  - Notes: Approved fallback after official full-paper HTML was unavailable; local copy withheld.
- Source URL: https://arxiv.org/e-print/1511.04815
  - Applies to: exact TeX equations, benchmark values, captions, and conclusion.
  - Notes: Source package inspected locally and withheld.
- Source URL: https://doi.org/10.48550/arXiv.1511.04815
  - Applies to: persistent identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html
  - Applies to: license context.
  - Notes: Does not authorize source upload by this automation.
- Source URL: https://zicokolter.com/publications/
  - Applies to: author publication record and software-link context.
  - Notes: Author-maintained record.
- Source URL: https://github.com/mwytock/epsilon
  - Applies to: implementation-availability assessment.
  - Notes: Paper-linked locator was inaccessible; code was not inspected or run.
- Source URL: https://proceedings.mlr.press/v48/wangh16.html
  - Applies to: follow-up research context on epigraph projections.
  - Notes: Primary proceedings record.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-Sparse%20SSN%20PMM/sparse_ssn_pmm_manuscript.md
  - Applies to: related DEP bridge.
  - Notes: Proximal/semismooth structured solver synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-CAP%20Rank%20Sparsity/cap_rank_sparsity_manuscript.md
  - Applies to: related DEP bridge.
  - Notes: ADMM and thresholding-operator synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md
  - Applies to: related DEP bridge.
  - Notes: Convex regularizer and generalized Bregman-geometry synthesis.
