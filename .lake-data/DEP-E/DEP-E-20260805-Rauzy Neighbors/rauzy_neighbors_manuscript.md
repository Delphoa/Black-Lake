---
title: "Rauzy Neighbors - DEP-E"
generated_at: "2026-08-05"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of contact-to-neighbor graph algorithms for self-affine tiles and Rauzy fractals."
source_status: "verified complete local PDF and full-paper HTML; metadata inspected; source package unavailable; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-05"
temporal_cutoff: "arXiv:2511.16442v1 and related DEP artifacts available through 2026-08-05"
primary_url: "https://arxiv.org/abs/2511.16442"
stable_identifier: "arXiv:2511.16442v1; DOI:10.48550/arXiv.2511.16442"
confidence_summary: "High for source identity, algorithm statements, theorem statements, and example transcription; medium for detailed proof correctness and complexity implications; no formal verification."
safety_scope: "non-sensitive mathematical research and educational tooling"
distribution_notes: "Public URLs and date-only provenance; source files, local paths, caches, hashes, and machine details withheld."
---

# Rauzy Neighbors - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2511.16442v1 | https://arxiv.org/abs/2511.16442 | Public metadata; abstract is not treated as the paper body. | 2026-08-05 | Inspected |
| S2 | Neighbors of self-affine tiles and Rauzy Fractals | Primary paper | PDF | arXiv:2511.16442v1 | https://arxiv.org/pdf/2511.16442 | Complete local copy verified and inspected; source file withheld. | 2026-08-05 | Complete paper inspected |
| S3 | Official arXiv full-paper rendering | Primary paper | HTML | arXiv:2511.16442v1 | https://arxiv.org/html/2511.16442 | Complete local copy verified and inspected; source file withheld. | 2026-08-05 | Complete paper inspected |
| S4 | arXiv-issued DOI | Persistent identifier | DOI | 10.48550/arXiv.2511.16442 | https://doi.org/10.48550/arXiv.2511.16442 | Public identifier; no source file collected for deposition. | 2026-08-05 | Inspected |
| S5 | Moran Spectra - DEP-E | Related research artifact | Markdown | DEP-E-20260717-Moran Spectra | .lake-data/DEP-E/DEP-E-20260717-Moran Spectra/moran_spectra_manuscript.md | Generated Black Lake synthesis; contextual only. | 2026-08-05 | Live file inspected |
| S6 | Flag Hardy Operators - DEP-E | Related research artifact | Markdown | DEP-E-20260716-Flag Hardy Operators | .lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md | Generated Black Lake synthesis; contextual only. | 2026-08-05 | Live file inspected |
| S7 | Acoustic Phase Retrieval - DEP-E | Related research artifact | Markdown | DEP-E-20260716-Acoustic Phase Retrieval | .lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md | Generated Black Lake synthesis; contextual only. | 2026-08-05 | Live file inspected |
| S8 | Black Lake repository README | Deposition authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Process authority, not research evidence. | 2026-08-05 | Fetched and read |
| S9 | Black Lake .lake-data README | Filing authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Process authority, not research evidence. | 2026-08-05 | Fetched and read |
| S10 | Black-Lake-Data README | Companion-repository authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Process authority, not research evidence. | 2026-08-05 | Fetched and read |

The paper is by Benoît Loridant, Jörg M. Thuswaldner, and Shu-Qin Zhang. The arXiv record places it in Metric Geometry (math.MG), lists one submission on 2025-11-20, and exposes the PDF, experimental HTML, source locator, and arXiv-issued DOI. The complete source pair was inspected locally after a bounded repair; the optional source package was unavailable. No local path appears in this public artifact.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, subject, arXiv ID, submission date, version, abstract, and source locators | Stable source identity and high-level contribution | High | Metadata cannot establish proof details |
| E2 | S2-S3, abstract and Introduction | Primary paper | Contact graphs are easier to construct; neighbor graphs contain fuller overlap information; the paper proposes efficient constructions | Problem framing and motivation | High | Efficiency is asserted comparatively; no runtime table is supplied |
| E3 | S2, Sections 1.2-1.4 | Primary paper | Self-affine neighbor/contact definitions, corona reduction, Algorithm 1, and Theorem 1.5 | Self-affine algorithm context | High for source reporting | Detailed proof was not independently formalized |
| E4 | S2-S3, Sections 2-3 | Primary paper and full HTML | Pisot substitutions, prefix-suffix graphs, Rauzy subtiles, self-replicating translation sets, and boundary/contact graph variants | Rauzy-fractal construction context | High | Specialized notation is extraction-sensitive |
| E5 | S2-S3, Algorithm 2 | Primary paper and full HTML | Start with contact graph; apply C-corona and reduction repeatedly; stop at a fixed point | Core algorithm | High | Practical graph encoding and tolerance policy are unspecified |
| E6 | S2-S3, Lemmas 4.1-4.4 and Proposition 4.5 | Primary paper and full HTML | Finite ±C connectivity, bounded contact degree, dual-substitution monotonicity, and decomposition of higher-degree walks | Termination proof architecture | Medium-high | Imported geometry and classical separation theorem are not re-proved here |
| E7 | S2-S3, Theorem 4.6 | Primary paper and full HTML | Finite termination and output equality with the self-replicating neighbor graph | Main theorem | High for source transcription; medium for correctness review | No independent proof verification |
| E8 | S2, Section 5 and Figures 10-11 | Primary paper | Two explicit substitutions and reported vertex counts/graph outcomes | Worked examples | High for transcription | Figures were not independently regenerated |
| E9 | S5-S7 | Related Black Lake artifacts | Fractal spectral construction, multiscale harmonic analysis, observability and Fourier reconstruction | Cross-DEP synthesis | Medium | Related artifacts are conceptual context only |
| E10 | Public-safe integrity summaries | Verification evidence | PDF size/header/EOF, HTML size/body/marker/heading/structure checks, metadata presence, no partials | Complete-source gate | High | Raw local records are withheld |
| E11 | S8-S10 | Repository authority | DEP-E class filing, publication index, source withholding, attribution, and dedup rules | Artifact layout and policy | High | Process evidence only |

## Executive Summary

Loridant, Thuswaldner, and Zhang study how to recover a neighbor graph from a smaller contact graph for self-affine tiles and Rauzy fractals. The motivation is structural: contact graphs are often easier to compute, while neighbor graphs retain the overlap information needed to reason about tiling and boundaries.

For Rauzy fractals associated with Pisot substitutions, the paper defines contact and self-replicating boundary graph variants over prefix-suffix and translation structures. Algorithm 2 initializes a graph with the simple contact graph, expands it through a C-corona, reduces it to the largest subgraph whose nodes lie on walks ending in loops, and repeats until consecutive graph states agree.

Theorem 4.6 states that this process terminates after finitely many steps and returns the self-replicating neighbor graph. The proof bounds the contact degree of relevant walks, shows that higher-degree walks decompose into a lower-degree walk and a degree-one contact connection, and uses induction to show that the fixed-point sequence captures all allowable infinite walks. The examples provide explicit substitutions and graph-size observations, but no runtime or memory benchmark.

Reviewer assessment: the source strongly supports the algorithm and proof architecture. The practical value lies in its auditable fixed-point pattern, not in a demonstrated software implementation. A safe downstream system should expose the graph state history, reduction predicate, contact-degree bound, cycle-reachability evidence, and stopping reason. The cross-DEP synthesis is an inference bridge, not an extension of the theorem.

## Detailed Summary

### Problem Context

Self-affine tiles are compact sets generated by expanding integer matrices and digit sets. Rauzy fractals arise from substitutions, especially Pisot substitutions, through a prefix-suffix graph and a graph-directed iterated-function-system construction. Both settings can generate multi-tilings. To decide whether overlaps are only boundary phenomena, one needs a representation of neighboring tile or subtile pairs.

The paper distinguishes a contact graph, which records a smaller local relation, from a neighbor graph, which records the fuller set of overlap relations. The central question is whether the latter can be generated from the former without enumerating the full space naively.

### Self-affine Precursor

In the self-affine setting, the neighbor set consists of nonzero translations whose tile overlaps are nonempty. A contact graph is obtained from a finite contact set and is a subgraph of a larger ambient graph. The paper revisits a corona-based process that expands the current graph and then reduces it to nodes that can participate in infinite walks ending in loops. Theorem 1.5 states finite termination and correctness for the self-affine neighbor graph.

### Rauzy-Fractal Structure

For a Pisot substitution, the paper introduces the substitution alphabet, incidence matrix, dominant eigendata, prefix-suffix graph, Rauzy fractal, and subtiles. A dual substitution acts on faces or translated subtile pieces. These pieces induce a self-replicating multi-tiling and boundary relations represented by ambient, contact, and self-replicating boundary graph variants.

The simple variants remove redundancies and use signed connections. A connection links two translated faces or subtile indices. A C-corona collects ambient-graph nodes reachable from the current graph through bounded chains of contact connections. Reduction retains the subgraph whose nodes can lie on walks ending in a loop.

### Algorithm

Algorithm 2 can be summarized as:

1. Set A[1] to the simple self-replicating contact graph.
2. For p greater than 1, set A[p] to the reduction of the C-corona of A[p-1].
3. Stop when A[p] equals A[p-1].
4. Return A[p] as the simple self-replicating neighbor graph, which is equivalent to the full graph under the paper's correspondence.

This is a monotone-looking finite graph refinement, but the proof does not rely only on an informal monotonicity claim. It introduces a contact degree for neighbor nodes, proves that the degree is uniformly bounded, and shows that an infinite walk of degree at most p can be decomposed into a walk already represented at degree p-1 and a contact-level walk.

### Termination and Correctness

Lemma 4.1 gives finite connectivity between elements of the translation structure by subsequent signed contact connections. Lemma 4.2 turns finiteness of the neighbor set into a global maximum contact degree. Lemma 4.3 shows that the degree relation behaves monotonically under the dual substitution. Lemma 4.4 translates graph walks into paired face sequences. Proposition 4.5 decomposes a higher-degree walk into a lower-degree walk and a degree-one walk. Theorem 4.6 then uses induction on contact degree and the global degree bound to show that some finite A[p] is already the desired neighbor graph.

### Examples

The paper gives two substitutions over a three-letter alphabet:

- σ1: 1 maps to 1112, 2 maps to 113, and 3 maps to 1.
- σ2: 1 maps to 112, 2 maps to 1113, and 3 maps to 1.

For σ1, the source reports a self-replicating contact graph with 14 vertices and a simple contact neighbor graph with 26 vertices; after applying Algorithm 2, the simple self-replicating neighbor graph is reported to be the same as the simple self-replicating contact graph. For σ2, the displayed self-replicating neighbor graph is obtained from a self-replicating contact graph whose dark-gray contact nodes number 15. These are worked examples, not a complexity study.

### Limitations and Availability

The paper provides mathematical definitions, proofs, figures, and examples but no benchmark suite, runtime analysis, memory analysis, or official implementation identified in the inspected sources. The source package was unavailable in the local repair and was not required for the review because the complete PDF and full-paper HTML passed the integrity gate. No independent proof assistant formalization or graph reproduction was performed.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Contact graphs are easier to construct, while neighbor graphs retain fuller overlap information. | Author claim | E2-E5 | Directly stated and consistent with the construction setup. | High |
| C2 | Algorithm 2 obtains the Rauzy-fractal neighbor graph by repeated reduced C-coronas. | Author algorithm claim | E5 | Algorithm and input/output contract are explicit. | High |
| C3 | The algorithm terminates after finitely many steps and outputs the self-replicating neighbor graph. | Author theorem claim | E6-E7 | The proof architecture supports the stated induction, but it imports prior geometry and was not independently checked. | Medium-high |
| C4 | The two substitutions provide concrete graph constructions with the reported vertex counts. | Author example claim | E8 | Counts and substitution rules were cross-checked against PDF text and full HTML. | High for transcription |
| C5 | The algorithm is an auditable fixed-point reconstruction pattern for compressed geometric representations. | Reviewer interpretation | E5-E7 | Strong conceptual interpretation, not a theorem about software systems. | Medium |
| C6 | A practical implementation should expose invariant margins and stopping certificates. | Derived implementation inference | E6-E10 | Reasonable downstream control derived from the proof's bounded-degree and fixed-point logic. | Medium |

## Methodology

- Research objective: preserve a source-grounded review of the paper's contact-to-neighbor algorithms, proof of finite termination, examples, limitations, and safe implementation implications.
- Sources inspected: the official arXiv metadata page, verified local PDF, verified local full-paper HTML, local metadata/provenance/verification summaries, and three live Black Lake related manuscripts. The official arXiv abstract and HTML pages were also checked online.
- Discovery strategy: the local archive was enumerated with rg --files -g "*.pdf"; parent directories were collapsed to paper units; the selected paper was checked against repository artifacts, automation memory, and related repository search context. The primary paper was then reviewed section-by-section in PDF and full HTML.
- Inclusion criteria: complete primary source pair, stable public identifier, concrete method/proof/evidence details, and related DEP entries with explicit conceptual overlap.
- Exclusion criteria: duplicate or recently marked papers, abstract-only evidence, inaccessible or invalid paper documents, generic topical similarity, local paths, and source-file redistribution.
- Analytical approach: conceptual, comparative, implementation, replication-planning, and DEP-ready provenance analysis.
- Evidence handling: evidence IDs map major claims to source roles; author claims, reviewer interpretation, and implementation inference are labeled separately.
- Uncertainty handling: proof correctness, practical complexity, broader generalization, and reproducibility are marked medium or unavailable where not established by inspected evidence.
- Extraction process: PDF text was cross-checked with full-paper HTML headings, algorithm blocks, theorem text, and example paragraphs; source integrity was validated independently of review.
- Random selection and validation: 75,960 PDF candidates became 75,957 unique parent-directory units; uniform zero-based index 68,395 was accepted; duplicate exclusions and reselections were zero; the public 24-hour cutoff was 2026-08-04. A failed path helper occurred before candidate acceptance and was discarded.
- Source repair process: the initially partial unit received one bounded broker-mediated repair; the valid PDF was preserved; full-paper HTML and companion verification records were produced locally; the source package remained unavailable.
- Safety handling: only public URLs and derived Markdown are deposited; source documents, caches, local paths, and machine identifiers are withheld.
- Reviewer stance: paper report, critique, implementation translation, replication planning, and public-safe DEP deposition.

## Scope, Constraints, and Assumptions

- Scope: the selected paper's graph definitions, self-affine precursor, Rauzy-fractal construction, Algorithm 2, termination proof architecture, examples, related DEP synthesis, and bounded implementation ideas.
- Temporal boundary: primary arXiv version 1 and repository evidence available through 2026-08-05.
- Evidence limits: no independent formal proof check, no graph-code reproduction, no runtime/memory benchmark, no source package, and no publisher-version comparison beyond the arXiv record.
- Assumptions: the PDF and full-paper HTML refer to the same arXiv version; the paper's notation is interpreted according to its definitions; related DEP artifacts are treated as contextual research records rather than theorem validation.
- Constraints: source documents remain local; public artifacts must contain no local paths, usernames, machine identifiers, local timezone labels, or exact local execution timestamps; implementations are educational and synthetic.
- Out of scope: certifying a tiling, proving new generalizations, implementing large ambient graphs, making performance claims, or treating a finite graph run as mathematical proof.
- Intended use: research review, DEP deposition, implementation planning, replication planning, and future theorem-audit work.
- Audience: mathematical researchers, graph-algorithm engineers, formalization reviewers, and agents building evidence-grounded research tooling.
- Reproducibility boundary: source equations and pseudocode are available through public URLs, but the source package, reference implementation, complete input corpus, and runtime environment were not deposited.
- Data sensitivity: public mathematical research; no personal, proprietary, or regulated data.

## Observations

- Observed pattern: the paper compresses a global overlap question into a finite graph fixed point whose state transitions are locally generated.
- Technical implication: a production implementation should store every graph state and reduction decision because the proof's value is tied to the path to the fixed point, not just the terminal graph.
- Observed pattern: the termination proof depends on a structural contact-degree bound rather than a numerical tolerance.
- Contradiction or tension: the source claims greater efficiency than naïve construction but does not provide asymptotic or measured cost evidence.
- Open question: the extra Rauzy structure may be essential, so transfer to arbitrary graph-directed iterated-function systems should be treated as a research hypothesis.
- Reviewer hypothesis: combining fixed-point certificates with Fourier or spectral diagnostics could produce useful educational tests for finite approximations, provided the output is explicitly labeled non-proof.

## Considerations

The algorithm is mathematically specialized. Its implementation needs exact or carefully canonicalized representations of substitutions, faces, translations, graph edges, signs, and reductions. Floating-point geometry should not silently replace the paper's discrete structure. If numerical approximations are used for visualization, they should be separate from the exact graph state.

Complexity is the main adoption risk. The ambient graph may be much larger than the contact graph, and each corona expansion can add nodes before reduction. A useful implementation should report peak node counts, edge counts, expansion ratios, reduction ratios, and contact-degree bounds. These are not supplied by the source and must be measured independently.

The related DEP bridges suggest a cross-domain governance rule: never treat a compact representation as sufficient evidence by itself. Moran Spectra requires an explicit spectrality criterion beyond density; Flag Hardy Operators requires scale and cancellation assumptions beyond a generic norm; Acoustic Phase Retrieval requires a condition margin beyond a recovered-looking field. A shared evidence ledger can make these prerequisites visible.

## Strengths

1. The paper gives a clear conceptual reason to prefer contact graphs as an intermediate representation.
2. Algorithm 2 is short, deterministic in its stated graph abstractions, and paired with a correctness theorem.
3. The proof identifies concrete intermediate lemmas rather than presenting termination as an empirical observation.
4. The two substitutions make the abstract construction inspectable through finite examples.
5. The source provides enough full text to cross-check definitions, algorithms, theorem statements, and examples in both PDF and HTML.

## Weaknesses

1. No executable reference implementation, runtime table, or memory profile is supplied.
2. The graph-encoding details needed for an independent implementation are distributed across specialized definitions and prior references.
3. Several proof ingredients rely on prior results and a classical separation theorem; this review did not formally verify them.
4. The examples are narrow and do not establish behavior across substitution families or higher dimensions.
5. The source's efficiency comparison remains qualitative in the absence of measured baselines.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish exact graph encodings and example fixtures | Reproducibility | Vertex/edge conventions are specialized | Independent reproduction | Author maintenance | Compare generated graph states and final counts |
| Add complexity instrumentation | Evaluation | Efficiency is currently qualitative | Measured scaling and bottleneck visibility | Implementation effort | Sweep substitutions and record peak states |
| Formalize imported assumptions | Proof audit | The termination proof depends on prior geometric facts | Clearer scope and mechanized checking | Substantial mathematical work | Proof assistant or line-by-line dependency ledger |
| Test broader graph-directed systems | Generalization | Rauzy-specific structure may be essential | Boundary of applicability | Risk of false generalization | Counterexample search with explicit failure logs |

## Potential Implementations

1. Contact-to-neighbor graph inspector: User—mathematical researcher or formalization engineer. Goal—reproduce finite graph states for small substitutions. Inputs—exact substitution rules, contact graph, signed connection rules, and reduction predicate. Outputs—state history, final graph, vertex/edge counts, cycle-reachability certificate, and contact-degree report. Risk controls—small synthetic fixtures, exact encodings, deterministic ordering, and explicit refusal on unsupported graph classes. Evaluation—reproduce the two source examples and test malformed inputs.
2. Proof-dependency ledger: User—reviewer or theorem-audit team. Goal—make imported lemmas, assumptions, and induction steps machine-checkable as a dependency map. Inputs—paper sections, lemma identifiers, graph invariants, and proof obligations. Outputs—claim-to-evidence matrix, missing-assumption warnings, and a review report. Risk controls—label inference separately and never output proof-certified status from static parsing alone. Evaluation—coverage of every theorem dependency and manual agreement on sampled edges.
3. Fractal-spectrum teaching sandbox: User—student or researcher learning self-similar geometry. Goal—connect substitution graphs, Moran-like digit systems, and Fourier diagnostics on small finite approximations. Inputs—synthetic substitutions, digit rules, and bounded graph sizes. Outputs—visual graph refinements, finite spectra, density summaries, and warnings when asymptotic conclusions are unsupported. Risk controls—educational-only labels, finite-size caveats, no deployment claims. Evaluation—known toy cases, invariant checks, and deliberate failure fixtures.

## Three Ways to Exercise This Research

1. Fixed-point graph exercise: Objective—reproduce Algorithm 2 on a toy substitution. Inputs—one of the two source substitutions, a hand-authored contact graph, and a deterministic reduction rule. Method—generate successive C-coronas, reduce each state, and compare consecutive states. Output—state history and termination certificate. Success criterion—stable output with no missing loop-reachability annotations. Stop condition—ambient nodes exceed the bounded toy limit or exact graph invariants fail.
2. Proof-obligation exercise: Objective—map the termination theorem to explicit obligations. Inputs—Lemmas 4.1-4.4, Proposition 4.5, and Theorem 4.6. Method—create a dependency graph from connectivity to bounded degree to decomposition to induction. Output—reviewable proof ledger. Success criterion—every theorem step has a source or an explicit unresolved dependency. Stop condition—an imported result cannot be identified or its assumptions conflict.
3. Cross-DEP diagnostic exercise: Objective—compare invariant preservation across graph refinement, Moran spectra, and Fourier reconstruction. Inputs—synthetic finite graph states, a small digit system, and a conditioned inverse problem. Method—record the compact representation, invariant margin, expansion/reconstruction step, and stop condition for each. Output—a side-by-side evidence table. Success criterion—each path exposes its correctness or stability margin. Stop condition—an analogy would require treating finite output as proof.

## Example MVP Product

- Product name: Graph Fixed-Point Audit Lab
- Target user: Researchers and engineers prototyping exact graph constructions from structured geometric or symbolic inputs.
- Problem: A final graph is difficult to trust when intermediate expansion, reduction, and proof assumptions are invisible.
- Core workflow: Load a small substitution and contact graph; validate graph schema; run deterministic corona/reduction iterations; compute cycle reachability and contact-degree diagnostics; export a source-linked evidence ledger.
- Data requirements: Public paper metadata, user-supplied exact substitution rules, synthetic contact graphs, graph transition rules, and versioned test fixtures.
- Architecture: Local-only parser; exact graph model; corona operator; reduction engine; invariant checker; iteration recorder; Markdown/JSON evidence exporter; review dashboard.
- Success metrics: Reproduction of both source example fixtures; deterministic state histories; zero silent reduction changes; clear stop reasons; complete source-to-claim mapping.
- Risk controls: Exact arithmetic where required; bounded graph size; no unsupported graph-class auto-admission; immutable fixture versions; human review for theorem interpretation.
- Limitations: No theorem proving, no automatic generalization, no large-scale complexity guarantee, and no replacement for mathematical review.
- MVP boundary: Two substitutions, finite graphs, exact discrete encodings, and offline reports only.
- Deployment model: Local CLI plus a static review report.
- Evaluation plan: Unit tests for graph invariants, property tests for fixed points, fixture regression tests, and manual theorem-ledger review.
- Failure modes: State explosion, ambiguous graph conventions, false stability from an incomplete reduction predicate, and overinterpretation of finite examples.
- Maintenance plan: Version graph schemas, paper references, fixtures, and reduction rules separately; rerun validation when any changes.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Moran Spectra - DEP-E | Related Black Lake research artifact | Self-similar measures, spectral sets, Beurling dimension, tree mappings, and invariant-versus-correction construction. | .lake-data/DEP-E/DEP-E-20260717-Moran Spectra/moran_spectra_manuscript.md; https://arxiv.org/abs/2302.05868v1 |
| Flag Hardy Operators - DEP-E | Related Black Lake research artifact | Geometry-aware multiscale decomposition, almost-orthogonality, and proof thresholds. | .lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md; https://arxiv.org/abs/1702.07201 |
| Acoustic Phase Retrieval - DEP-E | Related Black Lake research artifact | Observability intervention, condition margins, and Fourier reconstruction from partial measurements. | .lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md; https://arxiv.org/abs/1803.11323 |

These three entries are contextual bridges only. They do not validate the selected paper's graph theorem.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2511.16442 | Title, authors, subject, version, date, abstract, and public locators | 2026-08-05 | Primary metadata; abstract-only evidence was not used for the review |
| R2 | https://arxiv.org/html/2511.16442 | Definitions, graph constructions, Algorithm 2, proof structure, theorem, and examples | 2026-08-05 | Complete full-paper HTML verified locally; file withheld |
| R3 | https://arxiv.org/pdf/2511.16442 | Page-level cross-check of algorithms, theorem, examples, and references | 2026-08-05 | Complete PDF verified locally; file withheld |
| R4 | https://doi.org/10.48550/arXiv.2511.16442 | Persistent identifier | 2026-08-05 | arXiv-issued DOI |
| R5 | .lake-data/DEP-E/DEP-E-20260717-Moran Spectra/moran_spectra_manuscript.md | Related fractal and spectral construction context | 2026-08-05 | Live repository file; contextual only |
| R6 | .lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md | Related multiscale harmonic-analysis context | 2026-08-05 | Live repository file; contextual only |
| R7 | .lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md | Related observability and Fourier-reconstruction context | 2026-08-05 | Live repository file; contextual only |
| R8 | https://arxiv.org/abs/2302.05868v1 | Primary basis for related Moran Spectra entry | 2026-08-05 | Related source locator |
| R9 | https://arxiv.org/abs/1702.07201 | Primary basis for related Flag Hardy Operators entry | 2026-08-05 | Related source locator |
| R10 | https://arxiv.org/abs/1803.11323 | Primary basis for related Acoustic Phase Retrieval entry | 2026-08-05 | Related source locator |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, source withholding, attribution, and commit rules | 2026-08-05 | Process authority |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index requirements | 2026-08-05 | Process authority |
| R13 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository context and source-deposition rules | 2026-08-05 | Process authority |
| R14 | .logs/20260805-Arxiv-Rauzy-Neighbors-LOG.md | Selection, deduplication, source-integrity, and handoff context | 2026-08-05 | Generated public-safe operational log |
| R15 | .reports/BL-Arxiv-Neighbours-Rauzy-20260805/Report-Mark.md | Detailed notes and cross-DEP synthesis | 2026-08-05 | Generated public-safe Report-Mark |

## Appendix

### Source-Integrity Gate

- Initial state: partial because the local archive unit had a valid PDF but no qualifying full-paper HTML.
- Repair: one bounded broker-mediated single-paper repair; valid PDF preserved; metadata, provenance, and verification companions updated locally.
- Final PDF evidence: 3,910,321 bytes, %PDF- header, trailing %%EOF.
- Final full-paper HTML evidence: 681,818 bytes, 136,019 body characters after removing scripts/styles, article/main/LaTeXML marker, 93 heading markers, and four structure terms.
- Metadata: non-empty official arXiv metadata page; source package unavailable.
- No partial files remained. No source file was copied into this DEP.

### Random Selection and Deduplication

- Selection method: rg PDF enumeration, unique parent-directory paper units, uniform PowerShell Get-Random index.
- Candidate counts: 75,960 PDFs; 75,957 unique paper units.
- Selected index: 68,395 zero-based.
- Dedup scan: repository .logs, .reports, .lake-data, .staging, automation memory, and Black-Lake-Data context.
- Exclusions: 0. Reselections: 0.
- Public 24-hour cutoff: 2026-08-04.

### Public Distribution Boundary

Only this derived Markdown manuscript, its DEP README, the public-safe log, the public-safe Report-Mark, and the required publication-index/dedup pointers are eligible for repository publication. The PDF, full-paper HTML, metadata HTML, source package, extracted text, caches, verification records, local paths, and machine details are withheld locally.
