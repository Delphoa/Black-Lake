---
title: "OS Minimum Paths - DEP-E"
generated_at: "2026-07-31"
artifact_type: "DEP-E research manuscript"
primary_subject: "Minimum realization of Okamura-Seymour metrics"
source_status: "Complete paper gate passed; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-31"
primary_url: "https://arxiv.org/abs/2607.02883"
stable_identifier: "arXiv:2607.02883v1; DOI:10.48550/arXiv.2607.02883"
confidence_summary: "High for paper identity and reported theorem structure; medium for proof correctness and implementation implications."
distribution_notes: "Generated public-safe Markdown and URLs only; source files, caches, and local paths are withheld."
---

# OS Minimum Paths - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public URL | Status |
|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2607.02883v1 | https://arxiv.org/abs/2607.02883 | inspected |
| S2 | *Paths and Intersections: Minimum Realization of Okamura-Seymour Instances* | Primary paper | PDF | arXiv:2607.02883v1 | https://arxiv.org/pdf/2607.02883 | complete paper reviewed; withheld |
| S3 | arXiv experimental rendering | Primary paper | HTML | arXiv:2607.02883v1 | https://arxiv.org/html/2607.02883 | complete paper reviewed; withheld |
| S4 | arXiv-issued DOI | Persistent identity | DOI | 10.48550/arXiv.2607.02883 | https://doi.org/10.48550/arXiv.2607.02883 | inspected |
| S5 | SLFE Redundancy Review | Related DEP entry | Markdown | DEP-E-20260730-SLFE Redundancy Review | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260730-SLFE%20Redundancy%20Review/slfe_redundancy_manuscript.md | inspected |
| S6 | Moran Spectra | Related DEP entry | Markdown | DEP-E-20260717-Moran Spectra | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-Moran%20Spectra/moran_spectra_manuscript.md | inspected |
| S7 | Integrals and Rigidity | Related DEP entry | Markdown | DEP-E-20260717-Integrals and Rigidity | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-Integrals%20and%20Rigidity/integrals_and_rigidity_manuscript.md | inspected |
| S8 | Extraction-cache public summary | Processing provenance | Public-safe JSON summary | schema 1.0 | canonical source URLs above | inspected |

The paper was submitted on 2026-07-03 by Yu Chen, Pavlo Pylyavskyy, and Zihan Tan. It studies an undirected Okamura-Seymour distance-realization problem with a fixed cyclic terminal order. The initial archive unit was partial because only the PDF was present; review stopped until bounded repair produced a validated full-paper HTML document and metadata record. The final source state is complete. A source package was not available, and all source artifacts remain local.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Primary metadata | title, authors, date, categories, DOI, abstract, canonical locators | identity and high-level contribution | High | metadata does not establish theorem details |
| E2 | S2, S3 | Complete primary paper | Kalmanson conditions, repelling pairs, cut counts, template inversion, Theorems 1, 15, 19, and Appendix A | method and reported results | High for reporting | proof correctness not formally certified |
| E3 | S8 | Processing provenance | complete-source gate, cache miss-to-cached result, PDF/HTML extractor status | review provenance | High | derived text is not a substitute for source layout |
| E4 | S5 | Related DEP | topology-derived scheduling state avoids redundant graph work | implementation analogy | Medium | distributed graph-processing problem differs |
| E5 | S6 | Related DEP | invariant-guided constructive classification with non-unique compatible objects | structural analogy | Medium | harmonic-analysis problem differs |
| E6 | S7 | Related DEP | sharp constraints and stated assumptions produce rigidity conclusions | proof-boundary analogy | Medium | geometric-analysis problem differs |

## Executive Summary

The paper solves a minimum-realization problem for OS metrics: starting from terminal distances and their cyclic boundary order, recover disk-embedded weighted graphs that realize those distances using the fewest edges. The reported result is not merely existential. The input metric determines a canonical medial template, its crossing number is the minimum edge count, every minimum graph structure is the primal graph of an arrangement of that template, and nonnegative realizing edge lengths can be computed for each such structure.

The construction makes lower-bound evidence explicit. Two terminal pairs that satisfy a strict repelling inequality must use vertex-disjoint shortest paths. For every boundary cut, the maximum cardinality of a mutually repelling set establishes how many channels are required. Endpoint-corrected cut counts determine a unique chord template. The paper proves that this template has the least crossings among feasible templates and translates its arrangements back into minimum OS realizations.

The result is source-supported for the stated OS setting and exact input model. It does not establish a practical implementation’s numeric stability, a tight published runtime expression in this manuscript, robustness to approximate distances, or formal verification of the imported lemmas. The paper’s Appendix demonstrates that realizing edge weights need not be unique.

## Detailed Summary

### Problem and setting

An OS instance is a graph embedded in a disk with terminals on its boundary in a fixed cyclic order. A metric is realizable in this family when an edge-weighted instance reproduces every terminal-pair shortest-path distance. The Kalmanson four-point condition characterizes this realizability under the specified order. This paper asks the next question: among all valid realizations, which use the fewest edges?

### Structural certificates

The authors define two terminal pairs as repelling when their pairwise distances satisfy a strict inequality that would be contradicted if the selected shortest paths met. A mutually repelling set crossing a boundary cut therefore needs at least as many disjoint channels as its cardinality. The paper’s shortest-path-structure result makes these boundary-chain conditions sufficient as well as necessary for the relevant realization construction.

### Medial-template construction

The medial graph of a plane graph can be represented as chords in the disk; its chord crossings correspond to primal edges. The authors transform each cut’s maximum repelling-set size into a corrected chord count. These counts invert through a circular cut-incidence relation to a unique chord matching. Any feasible template can be uncrossed to this template, and each nontrivial uncrossing lowers the crossing count. This produces a minimum-crossing, hence minimum-edge, certificate.

### From template to realization

For every arrangement of the fixed template, the standard medial-to-primal construction produces a candidate graph. The paper proves that every such graph meets the chain inequalities, admits an appropriate shortest-path structure, and can receive nonnegative edge lengths that realize the input metric. It also proves the converse: every minimum realization arises from an arrangement of the same template. The graph structure is constrained by the template, while edge weights can remain non-unique.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | A Kalmanson OS metric determines a unique minimum-crossing medial template. | Author theorem | E2, Theorem 15 | faithfully reported; dependent lemmas were not formally verified here | High for reporting |
| C2 | All minimum OS graph structures are primal graphs of arrangements of that template. | Author theorem | E2, Lemma 16 and Theorem 19 | source supports the stated exact setting | High for reporting |
| C3 | Nonnegative realizing edge lengths can be computed efficiently for each such graph structure. | Author theorem | E2, Theorems 1 and 19 | no implementation or tight complexity audit in this review | Medium-high |
| C4 | Template uniqueness implies unique edge lengths or a unique drawing. | Unsupported implication | E2, Appendix A | rejected; the paper explicitly permits non-unique weights and multiple arrangements | High |
| C5 | Repelling-pair certificates can guide a practical noisy-data reconstruction system. | Reviewer interpretation | E2, E3 | plausible direction requiring tolerance, validation, and stress testing | Medium |

## Methodology

- `Research objective`: produce a source-grounded DEP-E review of the paper’s problem, proof architecture, limitations, and implementable abstractions.
- `Sources inspected`: canonical metadata, complete PDF, validated full-paper HTML, public-safe cache summary, focused public code discovery, and exactly three related Black Lake DEP entries.
- `Random selection methodology`: PDF candidates were enumerated with `rg --files -g "*.pdf"`, grouped by parent paper unit, and sampled by a uniform PowerShell `Get-Random` index. The selection used 75,957 units; index 349 was accepted.
- `Dedup and reselection validation`: arXiv ID, DOI, normalized title, slug, logs, reports, DEP-E entries, the public pointer index, automation memory, relevant Black-Lake-Data material, and 24-hour markers were searched. No match was found; exclusions and reselections were both zero.
- `Cache methodology`: after the complete-source gate passed, missing-only extraction created a cache record. PDF text used `pypdf` because `pdftotext` was unavailable; HTML text used `html-regex`; no source text was created because the source package was unavailable.
- `Analytical approach`: conceptual, comparative, implementation, and replication-oriented analysis; author theorems, reviewer inferences, and unsupported implications are kept separate.
- `Evidence handling`: numerical and theorem claims are attributed to inspected primary material; no source file, extracted text, or private path is included.

## Scope, Constraints, and Assumptions

- `Scope`: minimum edge-count realization for the paper’s undirected OS metrics with supplied cyclic terminal order.
- `Temporal boundary`: arXiv v1 and cited public sources inspected through 2026-07-31.
- `Evidence limits`: no formal proof checker, implementation, benchmark, or independent runtime measurement was used.
- `Assumptions`: input distances satisfy the paper’s Kalmanson/OS conditions and exact comparison arithmetic is available.
- `Constraints`: source documents, caches, and repair records remain local and are not distributed.
- `Out of scope`: arbitrary graph metrics, directed variants, noisy measurements, dynamic topology, and production deployment.
- `Intended use`: research review, educational tooling, and a bounded prototype validation plan.

## Observations

- The transferable idea is a certificate pipeline: strict metric inequalities imply separation, cut counts imply a chord template, and crossings certify edge minimality.
- The template is canonical as a combinatorial object while its arrangements retain embedding-level freedom.
- The paper distinguishes graph-structure recovery from weight recovery, and the latter retains degrees of freedom even at minimum size.

## Considerations

- A real implementation should represent equality and strict inequality carefully; naive floating-point arithmetic can change the repelling relation.
- A user-facing tool should show both template and arrangement choices so “canonical” is not misconstrued as a single visual graph.
- Any use with learned or measured distances needs a separate feasibility and tolerance policy before applying exact theorems.

## Strengths

- The paper links a metric-only input to an explicit structural recovery object rather than leaving the result at existence.
- Its dual medial formulation yields a clean minimality certificate through crossing count.
- It makes the boundary between unique template, multiple arrangements, and non-unique weights explicit.

## Weaknesses

- The manuscript review could not independently certify imported lemmas or the full proof chain.
- No public implementation, complexity benchmark, or numerical stress test was identified in focused discovery.
- The method’s exact assumptions leave approximate-metric and noisy-input behavior unresolved.

## Potential Improvements

- Add worked machine-readable instances with distances, cut counts, template chords, arrangements, and recovered lengths.
- Publish a reference implementation with exact-arithmetic and tolerance-aware modes plus property tests.
- State explicit input-size complexity bounds and analyze degeneracies, ties, and numerical conditioning.

## Potential Implementations

1. A metric-feasibility checker that reports violated Kalmanson inequalities and repelling-pair witnesses.
2. A medial-template explorer that produces a minimal crossing certificate and lists arrangement alternatives.
3. A realization verifier that recomputes terminal distances, checks nonnegative lengths, and confirms edge count against the template.

## Three Ways to Exercise This Research

1. Generate small exact OS metrics, reconstruct their template, and compare every recovered terminal distance with the input matrix.
2. Perturb a valid distance matrix by controlled noise to measure when Kalmanson and repelling certificates change.
3. Enumerate arrangements of one template and demonstrate which graph features vary while the edge-minimality certificate remains fixed.

## Example MVP Product

- `Product name`: OS Metric Template Lab.
- `Target user`: graph-algorithm researcher or advanced student studying planar metric realization.
- `Problem`: manual reasoning about whether terminal distances imply a compact disk-embedded graph is error-prone.
- `Core workflow`: enter an ordered distance matrix, run feasibility checks, inspect cut and template certificates, choose an arrangement, and verify realized distances.
- `Data requirements`: a small, exact or rational terminal-distance matrix and explicit cyclic terminal order.
- `Architecture`: validation module, repelling-pair engine, cut-count/template builder, arrangement viewer, and independent shortest-path verifier.
- `Success metrics`: valid fixtures reconstruct correctly; invalid fixtures receive a specific failed constraint; all emitted graphs match input terminal distances.
- `Risk controls`: default to exact/rational arithmetic; label theorem preconditions; require verification before export; do not present approximate output as a certified minimum realization.
- `Limitations`: it would not establish performance on large inputs, handle arbitrary graph-metric families, or replace formal proof review.

## Related Research and Reading

- Chen and Tan, [*Paths and Intersections: Characterization of Quasi-metrics in Directed Okamura-Seymour Instances*](https://arxiv.org/abs/2410.19246), for the directed realization counterpart.
- Chen and Tan, [*Paths and Intersections: Recognizing Outerplanar Metrics*](https://arxiv.org/abs/2606.25827), for a related path-and-intersections recognition setting.
- Okamura and Seymour, [*Multicommodity flows in planar graphs*](https://doi.org/10.1016/0095-8956(81)90043-4), for the OS-instance context.
- Feder et al., [*Representing graph metrics with fewest edges*](https://doi.org/10.1007/3-540-36494-3_29), for broader minimum-realization context.
- The three related DEP entries S5-S7, for graph-work avoidance, invariant-based construction, and rigidity framing.

## Source References

1. https://arxiv.org/abs/2607.02883
2. https://arxiv.org/pdf/2607.02883
3. https://arxiv.org/html/2607.02883
4. https://doi.org/10.48550/arXiv.2607.02883
5. https://arxiv.org/abs/2410.19246
6. https://arxiv.org/abs/2606.25827
7. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260730-SLFE%20Redundancy%20Review/slfe_redundancy_manuscript.md
8. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-Moran%20Spectra/moran_spectra_manuscript.md
9. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-Integrals%20and%20Rigidity/integrals_and_rigidity_manuscript.md

## Appendix

### Public-Safe Validation Record

- Source gate: complete PDF and complete full-paper HTML passed; metadata-only material was not used as paper evidence.
- Cache: cached after missing-only extraction; PDF and HTML text are available in the local cache, while source text is unavailable because no source package was available.
- Source policy: all original source files and derived source material remain local; this DEP contains generated Markdown and public URLs only.
- Review boundary: proof statements and algorithmic claims were checked against complete primary sources but were not independently formalized, implemented, or benchmarked.
