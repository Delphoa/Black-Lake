# Report-Mark: Willmore Loop Groups

## Source Metadata

- **Paper:** *Willmore surfaces in spheres via loop groups I: generic cases and some examples*.
- **Authors:** Josef F. Dorfmeister; Peng Wang.
- **Canonical record:** https://arxiv.org/abs/1301.2756.
- **Full paper:** https://arxiv.org/pdf/1301.2756 and https://ar5iv.labs.arxiv.org/html/1301.2756.
- **Stable identifier:** arXiv:1301.2756v4; https://doi.org/10.48550/arXiv.1301.2756.
- **Chronology:** submitted 2013-01-13; inspected PDF version dated 2016-04-10.
- **Source integrity:** initially partial; bounded local-only repair completed; final state complete.
- **Distribution:** generated Markdown and public URLs only; all source files withheld.

## Concise Research Notes

The paper develops a loop-group treatment of Willmore surfaces in spheres through harmonic conformal Gauss maps. It characterizes the constrained harmonic maps that can arise from a surface, uses the DPW procedure to construct harmonic maps from normalized potentials, and gives a compact-dual correspondence for the non-compact symmetric-space setting.

Theorem 4.5 gives the operational core: a harmonic map produces a meromorphic normalized potential and an admissible potential reconstructs a harmonic map on the open domain where Iwasawa factorization exists. The non-compact Iwasawa decomposition is not global, so poles and big-cell boundaries are mathematical limits, not merely numerical inconveniences.

Theorem 1.1 associates a harmonic map into a simply connected non-compact inner symmetric space with a compact-dual harmonic map sharing its normalized potential; the reverse construction is local. The paper also reports a full, totally isotropic, non-S-Willmore two-sphere in S6, stated as a negative answer to Ejiri's dual-surface question. These are source-reported theorems and examples, not proofs independently certified here.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Assessment |
|---|---|---|---|
| E1 | Official arXiv metadata | identity, authors, dates, abstract, public locators | high-confidence metadata; abstract not used as proof evidence |
| E2 | Verified PDF and full-paper HTML | Sections 1-6, Appendices A-B, Theorems 1.1, 3.4, 3.11, 3.18, 4.5, and 6.6 | high-confidence source reporting; no formal proof check |
| E3 | PDF contents and title page | arXiv v4, 47-page structure, source version | cross-check for scope and chronology |
| E4 | Hyperbolic Catenaries DEP-E | symmetry-compatible surface constructions | contextual bridge only |
| E5 | Integrals and Rigidity DEP-E | analytic-to-geometric theorem chains and rigidity | contextual bridge only |
| E6 | Flag Hardy Operators DEP-E | geometry-aware decomposition and validity domains | contextual bridge only |
| E7 | Public-safe workflow records | random draw, dedup, repair, integrity, source gate | process evidence only |

## Related DEP Entries

1. [Hyperbolic Catenaries - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Hyperbolic%20Catenaries/hyperbolic_catenaries_manuscript.md)
   - **Source basis:** inspected manuscript and evidence ledger for arXiv:2211.15297v2.
   - **Relevance:** both analyse surface geometry through symmetry-compatible constructions; that deposit connects a variational curve law to minimal surfaces, while this one reconstructs Willmore geometry from constrained harmonic maps.
2. [Integrals and Rigidity - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Integrals%20and%20Rigidity/integrals_and_rigidity_manuscript.md)
   - **Source basis:** inspected manuscript and evidence ledger for arXiv:2602.10393.
   - **Relevance:** both are theorem-led differential-geometry reviews that make hypotheses, equality cases, and unverified proof dependencies explicit.
3. [Flag Hardy Operators - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md)
   - **Source basis:** inspected manuscript and evidence ledger for arXiv:1702.07201.
   - **Relevance:** both use a decomposition adapted to the native geometry and identify a domain where the machinery is valid rather than assuming global applicability.

## Synthesis Note

### Concept Bridge

The common pattern is geometry-aware representation followed by guarded reconstruction. Hyperbolic Catenaries chooses a weighted functional aligned to ambient symmetry; Integrals and Rigidity uses analytic quantities whose vanishing defects activate geometric conclusions; Flag Hardy Operators preserves the scale relationship required by its target space. This paper similarly encodes a surface through a constrained conformal Gauss map and reconstructs only where loop-group factorization remains valid.

### Potential Implementations

1. **Normalized-potential notebook:** symbolic checks of algebraic conditions before a DPW reconstruction.
2. **Factorization-domain monitor:** a research tool that records Iwasawa-cell membership and flags low-margin points.
3. **Theorem-dependency graph:** a review interface linking claims to hypotheses, factorization results, and surface-versus-nonimmersion alternatives.

### Deeper Relationship Observations

1. Each related deposit succeeds by retaining an invariant matched to the target question rather than applying a generic coordinate transformation.
2. The selected paper and Flag Hardy Operators both make domain-of-validity a substantive result: non-global Iwasawa cells versus a stated endpoint and kernel range.
3. The selected paper and Integrals and Rigidity distinguish source theorem reporting from independent proof certification.

### Conceptual Similarities

1. Like Hyperbolic Catenaries, this paper connects a geometric surface property to a lower-level construction law.
2. Like Integrals and Rigidity, it converts structured analytic information into global geometric knowledge under stated hypotheses.
3. Like Flag Hardy Operators, it requires decompositions that respect the original geometry and cannot be presumed globally valid.

### MVP Implementations With Code Mock-ups

1. **Potential Constraint Check**

```python
def potential_is_admissible(block):
    return block["null_condition"] and block["meromorphic"]
```

This validates declared toy constraints only; it does not claim to reconstruct a surface.

2. **Cell-Boundary Receipt**

```python
def factorization_receipt(point_id, in_big_cell, margin):
    return {"point": point_id, "valid": in_big_cell and margin > 0,
            "margin": margin}
```

The receipt fails closed near a numerical decomposition boundary.

3. **Proof-Dependency Card**

```python
def theorem_card(name, hypotheses, dependencies):
    return {"theorem": name, "hypotheses": list(hypotheses),
            "dependencies": list(dependencies), "certified": False}
```

The status preserves the distinction between a paper claim and a formal proof.

### Developer Challenges

1. Numerical factorizations can become ill-conditioned near big-cell boundaries and need an explicit failure state.
2. Meromorphic poles, gauge choices, and matrix constraints need typed inputs and provenance to avoid presenting arbitrary harmonic maps as surfaces.
3. A useful interface must keep source reporting, computational checks, and formal certification separate.

### Author Challenges

1. Provide a maintained computational companion for the normalized-potential examples with expected intermediate invariants.
2. Clarify which frame singularities are removable in surface reconstruction and give a reusable numerical criterion.
3. Connect the constructions more explicitly to later classification and moduli results.

## Validation Notes

- Random selection: 75,780 PDFs collapsed to 75,777 paper units; 324 prior-identifier units and 185 identifier-incomplete units were excluded; final eligible pool 75,268; uniform index 48,133; zero reselections.
- Dedup: arXiv ID, DOI, normalized title, slug, repository artifacts, automation memory, relevant Black-Lake-Data entries, and preceding-24-hour markers had no owning duplicate.
- Source integrity: initial partial state was repaired to complete. The 47-page PDF passed size/header/EOF; full-paper HTML passed size, body, marker, heading, and structure checks; no partials remain.
- Review coverage: complete HTML structure and representative PDF sections were cross-checked. The available PDF renderer did not produce preview images, so no visual-figure claim is made.
- Public safety: no private path, username, machine name, environment-specific timestamp, credential, source file, or extracted source text is present.
- Source-upload gate: generated Markdown only; no PDF, HTML, archive, cache, render, receipt, extracted source text, or `.source/` directory may be staged.

## Attribution Block

- Source URL: https://arxiv.org/abs/1301.2756
  - Applies to: this report and the DEP-E manuscript.
  - Notes: canonical identity, authors, dates, and public locators.
- Source URL: https://arxiv.org/pdf/1301.2756
  - Applies to: theorem and version cross-checking.
  - Notes: verified private copy inspected; source file withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/1301.2756
  - Applies to: full-paper structure and theorem cross-checking.
  - Notes: validated fallback used after the archive unit lacked full-paper HTML; source file withheld.
- Source URL: https://doi.org/10.48550/arXiv.1301.2756
  - Applies to: persistent identifier.
  - Notes: arXiv identifier resolver.
- Source files: PDF, full-paper HTML, metadata HTML, repair records, and review derivatives.
  - Applies to: all generated artifacts.
  - Notes: withheld locally; zero source-document uploads.
