---
title: "Motivic Zeta Depth - DEP-E"
generated_at: "2026-07-26"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of the depth structure of motivic multiple zeta values and its exact-sequence and conjectural framework."
source_status: "verified complete paper bundle inspected; public URLs only; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-26"
temporal_cutoff: "arXiv v4 and repository context available through the public-safe run date"
primary_url: "https://arxiv.org/abs/1710.06135"
stable_identifier: "arXiv:1710.06135v4; DOI:10.48550/arXiv.1710.06135"
confidence_summary: "High for source identity and reported theorem/conjecture statements; medium for independent proof validity because no formalization or derivation was performed."
safety_scope: "non-sensitive mathematical research, exact-arithmetic toy validation, and educational review"
distribution_notes: "Generated Markdown and public URLs only; original sources, extracted text, caches, verification records, local paths, machine information, and exact execution times withheld."
---

# Motivic Zeta Depth - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:1710.06135v4 | https://arxiv.org/abs/1710.06135 | Metadata only; not counted as the paper. | 2026-07-26 | Inspected |
| S2 | Primary paper | Complete research paper | PDF and HTML | arXiv:1710.06135v4 | https://arxiv.org/pdf/1710.06135; https://arxiv.org/html/1710.06135 | Verified copies inspected; files withheld. | 2026-07-26 | Complete |
| S3 | arXiv source package | Provenance companion | Source archive | arXiv:1710.06135v4 | https://arxiv.org/e-print/1710.06135 | Retained for provenance; not deposited. | 2026-07-26 | Withheld |
| S4 | Persistent identifier | Canonical identity | DOI | 10.48550/arXiv.1710.06135 | https://doi.org/10.48550/arXiv.1710.06135 | Identifier metadata. | 2026-07-26 | Verified |
| S5 | MOCS Flexible Lengths | Related processed artifact | Markdown | DEP-E-20260724 | `.lake-data/DEP-E/DEP-E-20260724-MOCS Flexible Lengths/mocs_flexible_lengths_manuscript.md` | Synthesis only. | 2026-07-26 | Inspected |
| S6 | 4 Adic Complexity | Related processed artifact | Markdown | DEP-E-20260721 | `.lake-data/DEP-E/DEP-E-20260721-4 Adic Complexity/4_adic_complexity_manuscript.md` | Synthesis only. | 2026-07-26 | Inspected |
| S7 | Integrals and Rigidity | Related processed artifact | Markdown | DEP-E-20260717 | `.lake-data/DEP-E/DEP-E-20260717-Integrals and Rigidity/integrals_and_rigidity_manuscript.md` | Synthesis only. | 2026-07-26 | Inspected |
| S8 | Black Lake authorities | DEP filing policy | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Process authority, not research evidence. | 2026-07-26 | Fetched and read |

The arXiv record identifies Jiangtao Li as author, reports v1 submitted 2017-10-17 and v4 revised 2018-08-13, and classifies the work under number theory. The record reports 25 pages. No implementation or data artifact was identified in the inspected primary record.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Official metadata and DOI | Title, author, version history, subject, abstract, and canonical locators | Source identity and chronology | High | Abstract alone is insufficient for theorem review. |
| E2 | S2 | Complete primary paper | Definitions, motivic Galois-action material, Lie-algebra sections, theorem/conjecture statements, depth-two/depth-three sections, and references | Method, stated results, assumptions, and limitations | High for source reporting | No proof was independently derived or machine checked. |
| E3 | S2 | Formula-preserving HTML | Map domains/codomains, short exact sequence displays, and conditional statements | Exactness framework and claim labeling | High for transcription | Rendering inspection does not establish validity. |
| E4 | S5-S7 | Related DEP manuscripts | Formal construction, sequence invariant, and rigidity/equality patterns | Cross-DEP synthesis | Medium | Related artifacts do not validate Li's theorems. |
| E5 | S8 and private process evidence | Repository authority and process record | Uniform selection, dedup scan, source-integrity repair, and no-source-upload gate | Eligibility and deposit compliance | High | Private records and source locations are withheld. |

## Executive Summary

Li studies the depth-graded structure of motivic multiple zeta values. The paper uses maps related to the motivic Galois action to describe short exact sequences in small depths and to formulate an analogous higher-depth program. Its central explanatory role is to connect dimensions of depth-graded spaces, period-polynomial relations, and structural conjectures about the motivic Lie algebra.

The source establishes a depth-two short exact sequence involving the totally odd component and the dual of a restricted even period-polynomial space. It also states depth-three map properties and derives higher-depth exact-sequence consequences only under three specified conjectures. In the final depth-three discussion, a further conclusion is reduced to a linear-algebra isomorphism conjecture. These distinctions are essential: the source has established and conditional claims, not one uniform proof across all depths.

The practical research value is an auditable decomposition strategy. A prototype can model finite-weight spaces and maps, then separately examine dimensions, kernels, cokernels, and assumptions. That supports small-instance validation and counterexample search without misrepresenting them as a proof of general conjectures.

## Detailed Summary

### Problem and Vocabulary

Multiple zeta values are nested convergent series indexed by positive integers. The paper uses **weight** for the sum of those indices and **depth** for their number. Motivic MZVs provide an algebraic setting with a motivic Galois action; the depth filtration produces graded pieces whose dimensions are the target of the Broadhurst–Kreimer-style structural questions.

The paper also considers the quotient modulo the motivic zeta value of two and the **totally odd** subspace. Restricted even period polynomials enter as a structured target for maps that reveal relations among depth-graded objects.

### Method and Architecture

The full text builds maps associated with the motivic Galois action, passes through a depth-graded motivic Lie algebra, and relates map kernels/cokernels to period-polynomial spaces. This turns a dimension-generating-function question into a sequence of linear-algebra and exactness questions.

For depth two, the paper gives a short exact sequence from the depth-two totally odd graded component into a tensor product of depth-one components, followed by a map to the dual period-polynomial space. For higher depths it constructs maps from a depth-r component to a tensor product of depth one and depth-r-1, then to a period-polynomial factor tensored with depth-r-2.

### Stated Results and Boundaries

The source presents the depth-two short exact sequence as a theorem. It states that for depth three the first constructed map is injective and the second surjective. For all depth at least three, the displayed exact-sequence conclusion is conditional on three conjectures about the depth-graded motivic Lie algebra: non-degeneration, vanishing, and surjectivity.

Later, the paper gives depth-two and depth-three conclusions for the quotient setting and identifies a conjectural long exact sequence for depth at least four. It then connects the depth-three totally odd question to a matrix/kernel formulation and records a further isomorphism conjecture. The source marks these higher-level statements as conjectures or conditional implications.

### Evidence and Interpretation

The result is theoretical: the inspected evidence is definitions, formal maps, theorem/conjecture statements, and mathematical derivations. No numerical benchmark or independent computational replication is claimed here. A finite-weight implementation could test whether specified matrices have expected ranks or whether a concrete sequence of vector spaces is exact, but such checks would only support bounded instances.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The paper defines depth-graded motivic-MZV spaces and uses motivic-Galois-action-related maps to study their structure. | Source-supported method | E2, E3 | Directly supported by the construction sections. | High |
| C2 | A short exact sequence is stated for the depth-two totally odd setting with a period-polynomial dual target. | Theorem reported by source | E2, E3 | The theorem and maps are displayed; proof not independently checked. | High for reporting; medium for independent validity |
| C3 | Depth-three map properties and a higher-depth exact sequence have different evidentiary status. | Source theorem / conditional implication | E2, E3 | The source states depth-three injectivity/surjectivity and makes the general conclusion conditional on three conjectures. | High |
| C4 | The depth-three totally-odd conclusion is resolved unconditionally in all weights. | Unsupported implication | E2 | Rejected: the source reduces it to a stated linear-algebra isomorphism conjecture. | High rejection confidence |
| C5 | Small exact-arithmetic experiments can help audit representation choices and locate failures. | Reviewer interpretation | E3, E4 | Useful for bounded validation but not a replacement for proof. | Medium-high |

## Methodology

- `Research objective`: Review one uniformly selected eligible arXiv paper source-first, preserve theorem/conjecture boundaries, connect it to exactly three related DEP entries, and create public-safe DEP-E artifacts.
- `Sources inspected`: Verified complete PDF, metadata HTML, full-paper HTML, source archive, official arXiv metadata, DOI, live Black Lake authorities, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDF candidates using `rg --files -g "*.pdf"`, treated parent directories as paper units, selected a uniform PowerShell random index, inspected nearby metadata, and checked public paper records.
- `Inclusion criteria`: Primary evidence identifying the work or supporting definitions, maps, theorem/conjecture status, limitations, provenance, or a concrete related-DEP bridge.
- `Exclusion criteria`: Abstract-only analysis, unverified generalization from finite examples, source-file redistribution, and generic topical matches.
- `Analytical approach`: Conceptual, comparative, formal-structure, implementation, replication, and provenance review.
- `Evidence handling`: Theorem and conjecture statements are labelled as source claims; reviewer interpretations and implementation ideas are labelled separately.
- `Uncertainty handling`: Missing formal verification, no independent derivation, no external code artifact, and conditional higher-depth claims remain explicit.
- `Random selection methodology`: 75,781 PDFs were enumerated; a uniform zero-based index of 55,420 selected the final paper unit.
- `Deduplication and reselection validation`: `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and related DEP context were scanned for the identifier, DOI, normalized title, slug, and recent markers. The public 24-hour cutoff was 2026-07-25; exclusions and reselections were both zero.
- `Source integrity`: The unit began partial because full-paper HTML was absent. A bounded repair preserved the valid PDF and verified metadata HTML, full-paper HTML, and a source archive. The PDF header/EOF and HTML size/body/document-marker/heading/structure gates passed with zero partial files.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's depth filtration, stated maps, depth-two and depth-three statements, conditional higher-depth program, and three related DEP bridges.
- `Temporal boundary`: arXiv v4 and repository material inspected through 2026-07-26.
- `Evidence limits`: No formal proof assistant, independent derivation, symbolic computation, source-code implementation, or specialist referee review was performed.
- `Assumptions`: The verified source bundle corresponds to arXiv v4; notation is interpreted as rendered in the inspected primary paper.
- `Constraints`: Public output excludes source documents, extracted text, paths, usernames, machine details, timezones, and exact execution times.
- `Out of scope`: Proving any conjecture, resolving the linear-algebra isomorphism question, or claiming code/data availability not shown in the primary record.
- `Intended use`: Research deposition, mathematical reading support, bounded exact-arithmetic validation design, and follow-on proof-review planning.

## Observations

1. The paper's strongest reusable design is a translation from global dimension questions into maps between explicitly graded spaces.
2. The depth-two theorem, depth-three statements, and higher-depth conjectures should not be collapsed into a single evidence category.
3. Period-polynomial relations act as a structured obstruction or target, making the source suitable for map-level auditing.
4. A matrix-rank check can meaningfully test one finite-weight manifestation while leaving all-weight exactness unresolved.
5. The related DEP entries reinforce the value of keeping parameters, invariants, defect terms, and proof obligations explicit.

## Considerations

Mathematical prototypes should use exact rational or algebraic arithmetic where feasible, retain basis ordering and grading conventions, and report all assumptions. Floating-point rank estimates can hide near-dependencies; any numerical fallback should state tolerance and be marked exploratory. A review artifact should distinguish theorem transcription, instance certificate, conjectural extrapolation, and independent proof evidence.

## Strengths

1. The paper gives a clear structural vocabulary linking depth, weight, motivic Galois action, Lie algebras, and period polynomials.
2. It makes claim status visible through theorem and conjecture labels.
3. The depth-two result provides a concrete anchor for the broader program.
4. The depth-three discussion exposes a finite-linear-algebra interface useful for bounded audit.
5. The reference trail gives direct mathematical context for the construction.

## Weaknesses

1. Higher-depth conclusions depend on stated conjectures rather than an unconditional proof.
2. The review did not independently verify the long derivations or imported results.
3. No implementation, test vectors, or mechanized proof artifact was identified in the inspected primary record.
4. Dense notation makes transcription and convention drift a material risk for any prototype.
5. Finite computations may be mistaken for proof unless their scope is prominently constrained.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish small-weight map examples | Pedagogy and audit | Definitions are abstract and notation-dense | Easier independent checking | Examples can obscure general scope | Match displayed maps and dimensions against the paper |
| Formalize the depth-two sequence | Proof assurance | It is the concrete base case | Machine-checked obligations | High proof-engineering effort | Proof-assistant acceptance and peer review |
| Create exact matrix fixtures | Reproducibility | Depth-three discussion has a linear-algebra interface | Repeatable finite checks | Risk of overclaiming | Fixed-weight rank/kernel fixtures with explicit scope |
| Add a dependency graph | Claim management | Conditional implications span multiple conjectures | Transparent assumptions | Maintenance burden | Each conclusion links to named assumptions |

## Potential Implementations

1. **Graded-map explorer**
   - `User`: Number-theory researcher or student.
   - `Goal`: Inspect bounded vector spaces and map dimensions.
   - `Core mechanism`: Versioned bases and exact matrices indexed by weight/depth.
   - `Required inputs`: Public theorem notation and manually reviewed finite fixtures.
   - `Outputs`: Rank/kernel/cokernel tables and assumption labels.
   - `Risk controls`: No automatic theorem conclusion; every result carries a finite-scope label.
   - `Evaluation`: Hand-check a small paper-derived example.

2. **Proof-obligation tracker**
   - `User`: Formalization team.
   - `Goal`: Separate established lemmas from conjectural dependencies.
   - `Core mechanism`: Directed graph from definitions through map properties to conclusions.
   - `Required inputs`: Source references, hypothesis labels, and proof-assistant links when available.
   - `Outputs`: Missing-obligation and dependency reports.
   - `Risk controls`: Human review for all logical edges.
   - `Evaluation`: Compare graph paths with the paper's theorem/conjecture labels.

3. **Cross-DEP certificate library**
   - `User`: Research-infrastructure maintainer.
   - `Goal`: Reuse representation and certificate patterns across mathematical DEPs.
   - `Core mechanism`: Typed records for parameters, invariants, maps, residuals, and assumptions.
   - `Required inputs`: Public-safe derived metadata only.
   - `Outputs`: Auditable Markdown/JSON evidence cards.
   - `Risk controls`: No source redistribution and no claim promotion without review.
   - `Evaluation`: Validate one MZV fixture, one MOCS residual fixture, and one rigidity-assumption card.

## Three Ways to Exercise This Research

1. **Map transcription check:** Objective—encode one displayed finite map; inputs—public theorem notation and a small hand-reviewed basis; method—use exact arithmetic to calculate rank; output—a scoped ledger; success criterion—reproducible result; stop condition—basis or map convention is ambiguous.
2. **Conditional-claim audit:** Objective—separate unconditional, conditional, and conjectural statements; inputs—the paper's theorem/conjecture labels; method—build a dependency table; output—claim-status graph; success criterion—every general conclusion has stated assumptions; stop condition—an implication cannot be sourced.
3. **Certificate-pattern comparison:** Objective—compare MZV maps with MOCS residuals and rigidity defects; inputs—three related DEP summaries; method—identify invariants and failure signals; output—reusable schema; success criterion—no synthesis claim exceeds cited artifacts; stop condition—overlap is merely topical.

## Example MVP Product

- `Product name`: Graded Proof Ledger.
- `Target user`: Mathematical researcher, formalization contributor, or research reviewer.
- `Problem`: Dense theorem chains make it easy to blur a finite check, a conditional implication, and an established theorem.
- `Core workflow`: Register a source claim, its graded spaces/maps, assumptions, exact finite fixtures, and review status; calculate bounded certificates; export a public-safe review card.
- `Data requirements`: Public source identifiers, manually reviewed symbolic fixtures, and no personal or restricted data.
- `Architecture`: Source registry, typed map schema, exact-arithmetic backend, dependency graph, certificate renderer, and review gate.
- `Success metrics`: Every claim has a source, every finite result has explicit bounds, and assumption gaps block promotion.
- `Risk controls`: Local-only experiments by default, no source-file redistribution, human review of encodings, and visible uncertainty labels.
- `Limitations`: Cannot establish general mathematical truth without a valid general proof or formalization; fixtures may contain transcription errors.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| MOCS Flexible Lengths | Related Black Lake DEP | Algebraic construction, exact cancellation identities, and instance-certificate boundaries. | `.lake-data/DEP-E/DEP-E-20260724-MOCS Flexible Lengths/mocs_flexible_lengths_manuscript.md` |
| 4 Adic Complexity | Related Black Lake DEP | Finite-alphabet sequence invariant and provenance-conscious mathematical review. | `.lake-data/DEP-E/DEP-E-20260721-4 Adic Complexity/4_adic_complexity_manuscript.md` |
| Integrals and Rigidity | Related Black Lake DEP | Theorem, monotonicity/equality, and independent-proof-boundary patterns. | `.lake-data/DEP-E/DEP-E-20260717-Integrals and Rigidity/integrals_and_rigidity_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1710.06135 | Metadata, author, title, chronology, abstract, and locators | 2026-07-26 | Metadata only |
| R2 | https://arxiv.org/pdf/1710.06135 | Primary theorem/conjecture text and references | 2026-07-26 | Verified source withheld |
| R3 | https://arxiv.org/html/1710.06135 | Formula-aware full-paper structure and map displays | 2026-07-26 | Verified source withheld |
| R4 | https://arxiv.org/e-print/1710.06135 | Public source-package locator | 2026-07-26 | Archive withheld |
| R5 | https://doi.org/10.48550/arXiv.1710.06135 | Persistent identifier | 2026-07-26 | Identifier only |
| R6 | `.lake-data/DEP-E/DEP-E-20260724-MOCS Flexible Lengths/mocs_flexible_lengths_manuscript.md` | Formal-construction synthesis | 2026-07-26 | Contextual only |
| R7 | `.lake-data/DEP-E/DEP-E-20260721-4 Adic Complexity/4_adic_complexity_manuscript.md` | Sequence-invariant synthesis | 2026-07-26 | Contextual only |
| R8 | `.lake-data/DEP-E/DEP-E-20260717-Integrals and Rigidity/integrals_and_rigidity_manuscript.md` | Rigidity-proof synthesis | 2026-07-26 | Contextual only |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository deposit policy | 2026-07-26 | Process authority |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E path and index policy | 2026-07-26 | Process authority |

## Appendix

### Selection and Integrity Record

- Candidate enumeration: 75,781 PDFs from the local arXiv archive, using `rg --files -g "*.pdf"`.
- Random selection: uniform zero-based index 55,420; paper identifier 1710.06135.
- Eligibility: no matching paper identifier, DOI, normalized title, slug, or recent marker in scanned public artifact surfaces and automation memory; exclusions 0, reselections 0.
- Repair: the original unit lacked full-paper HTML, so review stopped until a bounded repair produced a complete verified bundle. PDF size/header/EOF and full-paper HTML size/body/document-marker/heading/structure requirements passed.
- Public-output boundary: no PDF, HTML, metadata page, source archive, extracted text, cache, local path, machine information, or exact local timestamp appears in this DEP, the Report-Mark, or the log.
