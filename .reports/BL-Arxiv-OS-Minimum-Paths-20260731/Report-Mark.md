# Report-Mark — OS Minimum Paths

## Source Metadata

- Work: *Paths and Intersections: Minimum Realization of Okamura-Seymour Instances*.
- Authors: Yu Chen, Pavlo Pylyavskyy, and Zihan Tan.
- Identifier: arXiv:2607.02883v1; DOI: [10.48550/arXiv.2607.02883](https://doi.org/10.48550/arXiv.2607.02883).
- Submitted: 2026-07-03; categories: cs.DS, cs.CG, and math.CO.
- Primary evidence: [arXiv record](https://arxiv.org/abs/2607.02883), [PDF](https://arxiv.org/pdf/2607.02883), and [full-paper HTML](https://arxiv.org/html/2607.02883).
- Source integrity: the initial unit had a valid PDF but lacked full-paper HTML, so review paused. One bounded repair produced a structurally valid full-paper HTML document and metadata page; the PDF and HTML then passed the complete-source gate. Source files and cache outputs were withheld locally and were not uploaded.

## Concise Research Notes

The paper studies an inverse shortest-path problem. Given an Okamura-Seymour metric on terminals in a fixed cyclic order, it asks for disk-embedded realizations that use the fewest edges. The metric determines a unique medial-chord template, and every minimum realization is the primal graph of an arrangement of that template.

The mechanism starts with repelling terminal pairs. A strict metric inequality makes two corresponding shortest paths necessarily vertex-disjoint. Maximum sizes of repelling sets crossing each boundary cut give lower bounds on channels that a realization needs. After an endpoint correction these lower bounds become chord cut counts, which invert to a unique template. The template has minimum crossing number among feasible templates; its arrangements describe all minimum embedded graph structures. A constructive shortest-path-structure argument then supplies nonnegative edge lengths for each arrangement.

This is a theorem and algorithm paper rather than an empirical benchmark paper. “Efficiently” and “polynomial time” are author claims about the constructions. No formal proof certificate, implementation, runtime evaluation, or independent reproduction was located in this review. The Appendix explicitly shows that edge weights need not be unique even though the template controls the minimum graph structures.

## Evidence and Attribution

| Evidence | Inspected basis | What it supports | Qualification |
|---|---|---|---|
| E1 | Canonical arXiv metadata | identity, authors, submission date, categories, DOI, abstract, and license context | metadata is not proof evidence |
| E2 | Complete PDF and full-paper HTML | definitions, Theorems 1, 15, 19, cut-count construction, and non-uniqueness example | theorem reporting only; no formal proof verification |
| E3 | Public-safe extraction summary | source gate, cache miss-to-cached result, and extractor status | extracted text is navigation support, not a new research result |
| E4 | SLFE Redundancy Review DEP | topology-derived state used to remove redundant graph work | empirical distributed-systems setting differs |
| E5 | Moran Spectra DEP | constructive classification from an invariant while retaining non-unique compatible objects | harmonic-analysis setting differs |
| E6 | Integrals and Rigidity DEP | boundary/value constraints producing rigidity conclusions under explicit assumptions | geometric-analysis setting differs |

## Related DEP Entries

1. [SLFE Redundancy Review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260730-SLFE%20Redundancy%20Review/slfe_redundancy_manuscript.md) — it derives a topology-guided signal to avoid redundant graph computation. The overlap is structural information constraining which graph work is necessary; SLFE is systems scheduling, whereas this paper is exact metric realization.
2. [Moran Spectra](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Moran%20Spectra/moran_spectra_manuscript.md) — it constructs and classifies objects from a compact invariant while preserving non-uniqueness in the solution family. The overlap is the distinction between a forced structural scaffold and remaining realization freedom.
3. [Integrals and Rigidity](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Integrals%20and%20Rigidity/integrals_and_rigidity_manuscript.md) — it uses sharp constraints to identify when geometry is forced. The overlap is a rigidity pattern: observable boundary or metric data imposes global structural consequences only under stated hypotheses.

## Synthesis Note

### Concept Bridge

The selected work turns pairwise terminal distances into a minimal embedded graph by separating a canonical combinatorial template from permitted realizations. The related records show the same broader discipline in different settings: make the invariant explicit, preserve assumptions, distinguish forced structure from remaining degrees of freedom, and validate before skipping work or drawing a rigidity conclusion.

### Potential Implementations — Exactly 3

1. A metric-realization service that validates a terminal distance matrix, computes repelling-pair cut counts, and emits a template plus an auditable infeasibility explanation.
2. A visual debugger that displays terminal order, inferred medial chords, crossing count, and alternative arrangements while keeping the template fixed.
3. A verification harness that compares a constructed realization’s terminal distances against the input metric and rejects negative lengths or non-minimal edge counts.

### Deeper Relationship Observations — Exactly 3

1. The repelling inequality is a local numerical witness for a global topological separation, a useful pattern for turning geometric requirements into checkable certificates.
2. Template uniqueness does not imply a unique concrete drawing or unique edge weights; downstream systems must represent those freedoms explicitly.
3. Minimizing edge count through medial crossings gives a dual representation whose objective is easier to certify than direct search over embedded primal graphs.

### Conceptual Similarities — Exactly 3

1. Each related record centers an invariant or state summary that is more durable than one transient execution or construction.
2. Each separates source-supported conditions from stronger implementation or generalization claims that require additional validation.
3. Each gains value from an explicit fallback or uncertainty boundary when a compact structural summary omits operational detail.

### MVP Implementations with Code Mock-ups — Exactly 3

1. `Kalmanson precheck`

```python
def is_kalmanson(distance, order):
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            for k in range(j + 1, len(order)):
                for m in range(k + 1, len(order)):
                    a, b, c, d = order[i], order[j], order[k], order[m]
                    if distance[a, c] + distance[b, d] < distance[a, b] + distance[c, d]:
                        return False
    return True
```

2. `Repelling-pair witness`

```python
def repel(distance, pair_a, pair_b):
    s, t = pair_a
    u, v = pair_b
    return distance[s, t] + distance[u, v] < max(
        distance[s, u] + distance[t, v],
        distance[s, v] + distance[t, u],
    )
```

3. `Template edge-count receipt`

```python
def realization_receipt(input_metric, realized_metric, edge_count, template_crossings):
    return {
        "distances_match": input_metric == realized_metric,
        "minimum_edge_count": edge_count == template_crossings,
        "accepted": input_metric == realized_metric and edge_count == template_crossings,
    }
```

### Developer Challenges — Exactly 3

1. Preserve a precise cyclic terminal order and arithmetic model; floating-point comparisons can invalidate strict repelling inequalities.
2. Enumerate arrangements without silently treating template uniqueness as uniqueness of every primal graph or weight assignment.
3. Build independent distance and edge-count checks so a visually plausible construction cannot mask a broken realization.

### Author Challenges — Exactly 3

1. Publish an implementation or pseudocode with explicit polynomial complexity bounds and sample instances.
2. Provide machine-checkable examples connecting cut counts, template inversion, arrangements, and edge-length recovery end to end.
3. Clarify stability under approximate metrics, ties, noisy distances, and alternative numeric encodings.

## Validation Notes

- The source gate was satisfied only after both a valid PDF and full-paper HTML document passed structural checks.
- Claims are tied to complete primary evidence or explicitly labeled as reviewer interpretation.
- The related-entry list contains exactly three inspected Black Lake records and does not treat them as evidence for the selected theorems.
- Public text uses canonical URLs and repository-relative records only. It contains no local path, source file, cache output, username, machine name, local timezone, or exact execution timestamp.

## Attribution Block

- Source URL: https://arxiv.org/abs/2607.02883
  - Applies to: metadata and paper identity in this Report-Mark.
  - Notes: canonical arXiv record.
- Source URL: https://arxiv.org/pdf/2607.02883
  - Applies to: theorem and construction review.
  - Notes: complete source was reviewed locally and withheld from the repository.
- Source URL: https://arxiv.org/html/2607.02883
  - Applies to: full-paper structure and theorem review.
  - Notes: validated full-paper HTML was reviewed locally and withheld from the repository.
- Source URL: https://doi.org/10.48550/arXiv.2607.02883
  - Applies to: persistent paper identity.
  - Notes: arXiv-issued DOI.
- Related public records: the three DEP entries linked above.
  - Applies to: Synthesis Note.
  - Notes: conceptual context only; no source files were uploaded.
