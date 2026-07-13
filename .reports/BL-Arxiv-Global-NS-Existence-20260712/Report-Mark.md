# Report-Mark: Global NS Existence

## Source Metadata

- `Paper`: Global Existence of Strong and Weak Solutions to 2D Compressible Navier-Stokes System in Bounded Domains with Large Data and Vacuum.
- `Authors`: Xinyu Fan, Jiaxu Li, Jing Li.
- `Stable identifiers`: arXiv:2102.09229v2; arXiv DOI 10.48550/arXiv.2102.09229; publisher DOI 10.1007/s00205-022-01790-4.
- `Publication`: *Archive for Rational Mechanics and Analysis*, volume 245, pages 239-278 (2022).
- `Primary URLs`: https://arxiv.org/abs/2102.09229; https://arxiv.org/pdf/2102.09229; https://link.springer.com/article/10.1007/s00205-022-01790-4.
- `Source access date`: 2026-07-12.
- `Source-file policy`: No PDF, TeX source, code, or other original source file was deposited.

## Concise Research Notes

The paper treats a two-dimensional barotropic compressible Navier-Stokes system on a bounded simply connected `C^{2,1}` domain with Navier-slip boundary conditions. Pressure is proportional to `rho^gamma`, shear viscosity is a positive constant, and bulk viscosity is proportional to `rho^beta`. For `gamma > 1` and `beta > 4/3`, the authors state global unique strong solutions for `W^{1,q}` initial density and global weak solutions for bounded initial density, allowing vacuum and imposing no smallness condition on the initial data.

The proof bottleneck is a uniform upper bound on density in the presence of a boundary. The effective viscous flux solves a Neumann problem. A conformal map sends the domain to the unit disk; the disk Neumann Green's function is pulled back; and angle preservation plus the slip condition converts dangerous boundary singularities into commutator-like velocity differences. The resulting estimate closes the density bound, after which material-derivative, vorticity, higher-regularity, approximation, compactness, and uniqueness arguments produce the stated solutions.

The most important limitation is explicit: the method requires `beta > 4/3`, while the authors suggest `beta > 1` may be extremal and leave `1 < beta <= 4/3` open. The review is source-grounded but not a formal proof verification. Mathematical glyphs in the extracted PDF text contain encoding noise, and the final compactness steps rely partly on earlier literature.

## Evidence and Attribution

| Evidence | Inspected basis | Use | Limitation |
|---|---|---|---|
| Primary metadata | arXiv record and Springer article page | Identity, authors, versions, dates, abstract, venue, and DOI. | Metadata does not verify the proof. |
| Primary full text | Complete PDF-derived text | Theorems, definitions, estimates, proof architecture, remarks, and references. | Symbol encoding is imperfect; proof not independently checked. |
| Extraction cache | Public-safe cache summary | Fresh cache, extractor fallback, output status, and text size. | Private cache paths and exact local timestamps excluded. |
| Repository policy | Live README files for Black Lake and Black-Lake-Data | DEP class, paths, required contents, and attribution rules. | Process evidence only. |
| Related DEP manuscripts | Three repository-relative Black Lake entries | Conceptual synthesis and implementation framing. | Context only; not validation evidence for the paper. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-Fermat Difference/fermat-difference-manuscript.md`
   - `Relevance`: Both artifacts review global-solution theorems whose conclusions depend on explicit parameter regimes and multi-stage analytic arguments. Fermat Difference also preserves the boundary between structural source review and formal verification.
   - `Source basis`: The related manuscript's source metadata, theorem summary, proof strategy, methodology, limitations, and proof-formalization backlog were inspected.
2. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md`
   - `Relevance`: Physical Data AI treats PDE choice as a representation prior whose value depends on domain fit. The selected paper supplies the complementary mathematical lesson: equation, coefficient, topology, and boundary assumptions determine what can actually be proved.
   - `Source basis`: The related manuscript's executive summary, PDE-shaped method, domain-fit limitations, and implementation sections were inspected.
3. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md`
   - `Relevance`: RRT-CBF uses forward-invariant safe sets and boundary-like constraints in computational dynamics. The selected paper uses analytic invariant estimates and boundary geometry. Both show that constraints must be paired with explicit assumption and failure telemetry.
   - `Source basis`: The related manuscript's barrier-function method, evidence ledger, boundary conditions, operational risks, and simulation-only limitations were inspected.

## Synthesis Note

### Concept Bridge

Across the selected paper and the three related deposits, structure is valuable only when its validity regime is explicit. Fermat Difference organizes global entire solutions by exponent relations. Physical Data AI organizes learned representations by PDE/domain fit. RRT-CBF organizes motion by barrier-defined invariant sets. Global NS Existence organizes a global PDE proof by viscosity exponents, domain topology, slip geometry, and regularity. The shared design principle is an assumption-to-conclusion ledger: every useful guarantee should retain the parameter, geometry, evidence, and verification boundary that makes it meaningful.

### Potential Implementations

1. `PDE Theorem Assumption Ledger`: Extract domain, coefficients, boundary conditions, regularity, exponent thresholds, conclusions, and evidence anchors into reviewed YAML and Markdown.
2. `Proof Bottleneck Mapper`: Build a directed graph from the main theorems through density control, Green-function representation, commutator estimates, higher regularity, compactness, and uniqueness.
3. `Boundary Cancellation Toy Lab`: Use synthetic smooth disk fields to illustrate the difference between a raw singular kernel and a velocity-difference commutator kernel without claiming to prove the PDE theorem.

### Deeper Relationship Observations

1. Each work has a regime boundary that is part of the result, not an implementation detail: exponent cases in Fermat Difference, domain fit in Physical Data AI, barrier-model fidelity in RRT-CBF, and `beta > 4/3` plus simple connectivity in Global NS Existence.
2. Intermediate representations are the audit surface: theorem branches, physical coefficients, barrier margins, and effective viscous flux expose why a conclusion may hold or fail more clearly than a final output alone.
3. Approximation does not remove uncertainty; it relocates it. Smooth positive-density approximants, numerical obstacle models, trainable PDE layers, and symbolic theorem parsers all need explicit convergence, fidelity, or review checks.

### Conceptual Similarities

1. All four artifacts use mathematical structure to narrow an otherwise underdetermined problem.
2. All four require explicit boundary conditions on parameters, geometry, or admissible inputs.
3. All four benefit from separating source claims, reviewed mechanisms, computational demonstrations, and independently verified guarantees.

### MVP Implementations with Code Mock-ups

1. `Theorem-record completeness check`

```python
REQUIRED = {"domain", "boundary", "coefficients", "initial_data", "conclusion"}

def missing_theorem_fields(record):
    """Review aid only; completeness is not proof verification."""
    return sorted(REQUIRED - set(record))
```

2. `Proof-edge provenance check`

```python
def proof_edge(source_id, target_id, citation):
    if not source_id or not target_id or not citation:
        raise ValueError("Every dependency edge needs a source anchor")
    return {"from": source_id, "to": target_id, "citation": citation,
            "status": "reviewed-not-proved"}
```

3. `Threshold-regime labeler`

```python
def beta_regime(beta):
    if beta <= 1:
        return "outside-paper-regime"
    if beta <= 4 / 3:
        return "source-identified-open-regime"
    return "theorem-assumption-satisfied"
```

These examples use synthetic metadata only. Production hardening would require formula-preserving source anchors, versioned schemas, review signatures, and tests against deliberately corrupted or incomplete records.

### Developer Challenges

1. Preserving mathematical notation, theorem numbering, and equation anchors across PDF, HTML, LaTeX, Markdown, and graph representations without silent symbol drift.
2. Designing a dependency schema rich enough for function spaces, trace assumptions, exponent inequalities, and imported results while remaining reviewable.
3. Preventing interfaces and exports from presenting a source-reviewed dependency graph as a formal correctness certificate.

### Author Challenges

1. Isolate and improve the exact estimate that forces `beta > 4/3`, or provide a counterexample clarifying whether the threshold is sharp.
2. Extend or delimit the boundary commutator method for multiply connected domains, other boundary conditions, or weaker boundary regularity.
3. Publish a formula-preserving proof dependency map that makes compactness, approximation, and uniqueness imports auditable without overstating formal verification.

## Validation Notes

- One uniform random index selected the paper from 75,761 PDF-parent units: zero-based index 17,885.
- Dedup scans checked arXiv ID, both DOI markers, normalized title, and slug across the pointer index, Black Lake logs/reports/deposits, automation memory, Black-Lake-Data search, and the preceding 24 hours. Matches: 0. Reselections: 0.
- Extraction preflight found `pypdf` but no `pdftotext`. Fresh local `missing-only` extraction produced 72,259 bytes of PDF text. Final cache status is partial only because local HTML and source-package text are absent.
- Exactly three related DEP entries are listed and used.
- Synthesis Note counts: 3 potential implementations, 3 deeper relationship observations, 3 conceptual similarities, 3 MVP code mock-ups, 3 developer challenges, and 3 author challenges.
- The schema-complete manuscript is `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md`.
- Public-safe validation excludes private absolute paths, usernames, machine names, workspace roots, timezone labels, and exact local execution timestamps.
- Source files collected for deposition: none. No `.source/` directory was created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2102.09229
  - Applies to: paper identity, authors, abstract, version history, subject, and DOI links.
  - Notes: Primary arXiv metadata record.
- Source URL: https://arxiv.org/pdf/2102.09229
  - Applies to: theorem statements, proof mechanisms, limitations, and references.
  - Notes: Primary PDF inspected through a private cache; not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2102.09229
  - Applies to: persistent arXiv identification.
  - Notes: arXiv-issued DOI.
- Source URL: https://link.springer.com/article/10.1007/s00205-022-01790-4
  - Applies to: version-of-record metadata, publication history, abstract, venue, and references.
  - Notes: Publisher page; subscription content not collected.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-Fermat%20Difference/fermat-difference-manuscript.md
  - Applies to: theorem-regime and proof-review bridge.
  - Notes: Processed DEP artifact; contextual evidence only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md
  - Applies to: PDE/domain-fit implementation bridge.
  - Notes: Processed DEP artifact; contextual evidence only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: invariance and boundary-constraint bridge.
  - Notes: Processed DEP artifact; contextual evidence only.
