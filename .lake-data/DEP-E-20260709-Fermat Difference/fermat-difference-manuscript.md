---
title: "Fermat Difference - DEP-E"
generated_at: "2026-07-09 (public-safe date)"
artifact_type: "DEP research artifact"
primary_subject: "A paper classifying finite-order transcendental entire solutions of coupled Fermat-type difference systems in several complex variables."
source_status: "local archive collected; URLs only in DEP"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-09"
temporal_cutoff: "Sources inspected through 2026-07-09."
primary_url: "https://arxiv.org/abs/2606.30683"
stable_identifier: "arXiv:2606.30683"
confidence_summary: "Medium-high for source identity and theorem/proof structure; lower for formal validation because the proof was reviewed but not mechanically checked."
safety_scope: "pure mathematics research review"
distribution_notes: "No source PDF, TeX package, dataset, or local source file is redistributed."
---

# Fermat Difference - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract page | Primary paper metadata | HTML | arXiv:2606.30683v1 | https://arxiv.org/abs/2606.30683 | arXiv nonexclusive-distribution license link visible; no file redistributed. | 2026-07-09 | Inspected |
| S2 | arXiv experimental HTML | Primary paper full text | HTML | arXiv:2606.30683v1 | https://arxiv.org/html/2606.30683v1 | Public arXiv HTML; formulas require careful review. | 2026-07-09 | Inspected |
| S3 | arXiv PDF | Primary paper source | PDF | arXiv:2606.30683v1 | https://arxiv.org/pdf/2606.30683 | PDF collected in local archive but not redistributed in DEP. | 2026-07-09 | Downloaded locally |
| S4 | arXiv TeX source package | Primary paper source | TeX/source package | `Banerjee+Banerjee.tex`; TeX Live 2025; compiler `latex` | https://arxiv.org/e-print/2606.30683 | Source package collected in local archive but not redistributed in DEP. | 2026-07-09 | Downloaded and inspected |
| S5 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2606.30683 | https://doi.org/10.48550/arXiv.2606.30683 | arXiv-issued DOI. | 2026-07-09 | Referenced |
| S6 | Local single-paper archive metadata | Selection provenance | Local archive record | arXiv:2606.30683 | Local path withheld | Archive contains PDF, abstract HTML, source package, README, and summary CSV; no local path published. | 2026-07-09 | Verified |
| S7 | Black-Lake README | Repository standard | Markdown | default branch | https://github.com/Delphoa/Black-Lake | Repository authority for DEP-E, logs, reports, README, and attribution rules. | 2026-07-09 | Inspected |
| S8 | Black-Lake-Data README | Related repository standard | Markdown | default branch | https://github.com/Delphoa-Labs/Black-Lake-Data | Related DEP context and raw-source attribution standard. | 2026-07-09 | Inspected |
| S9 | 2D-RC OTFS DEP | Related DEP entry | Markdown | DEP-E-20260709-2D-RC OTFS | `.lake-data/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` | Repository-relative related artifact. | 2026-07-09 | Inspected |
| S10 | SANE Embeddings DEP | Related DEP entry | Markdown | DEP-E-20260709-SANE Embeddings | `.lake-data/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md` | Repository-relative related artifact. | 2026-07-09 | Inspected |
| S11 | Tech Intel 2338 DEP | Related DEP entry | Markdown | DEP-E-20260709-Tech Intel 2338 | `.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md` | Repository-relative related artifact. | 2026-07-09 | Inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary arXiv metadata | Title, authors, arXiv ID, DOI, submitted date, comments, subject, abstract, public source links. | Paper identity, stable identifiers, and abstract-level contribution. | High | Abstract alone is insufficient for proof validation. |
| E2 | S2 | Primary arXiv HTML | Introduction, theorem/proof layout, source references, formula context, proof cues. | Problem setting, theorem structure, source context, and limitations. | Medium-high | HTML formulas can be lossy and require math review. |
| E3 | S4 | Primary TeX source package | `00README.json`, TeX source, one main theorem, six lemmas, 45 bibliography entries, proof section. | Source-first theorem and proof review. | High for structure; low for formal proof checking | TeX extraction does not mechanically verify theorem correctness. |
| E4 | S6 | Local archive metadata | PDF, abstract HTML, source package, README, and summary CSV collected and verified. | Archive pull provenance and source collection status. | High | Local absolute paths withheld from public artifact. |
| E5 | S7-S8 | Repository README standards | DEP-E class, naming, contents, final Attribution Block, `.logs`, `.reports`, and `.lake-data` roles. | Artifact placement and validation. | High | Repository process evidence only. |
| E6 | S9 | Related Black-Lake DEP | Mathematical multi-dimensional system review and source-first arXiv manuscript pattern. | Related-entry bridge for formal system structure. | Medium | Domain differs; not evidence for this paper's theorem. |
| E7 | S10 | Related Black-Lake DEP | Locality/topology/attribute structure and graph representation evidence. | Related-entry bridge for structural constraints and locality. | Medium | Domain differs; conceptual relatedness only. |
| E8 | S11 | Related Black-Lake DEP | Formal scientific-computing and quantum-source evidence boundaries. | Related-entry bridge for regime boundaries and formal claim handling. | Medium | Domain differs; conceptual relatedness only. |

## Executive Summary

The paper classifies finite-order transcendental entire solutions of a coupled Fermat-type difference system in several complex variables. The system couples powers of two entire functions evaluated at `z` and shifted point `z+c`. The authors extend earlier Fermat-type difference-equation work in one and two complex variables to a several-variable coupled system and argue that the admissible solution structure is determined by the relative sizes of the exponents.

The main theorem has three high-level regimes. In the equal case, the theorem forces all four exponents to be 2 and gives cosine-type solution families built from affine/polynomial terms with `2c`-periodicity constraints. In the `n1 > m1` case, admissibility forces `n2 = m1 = 1` and `n1 = m2 >= 2`, with exponential-times-periodic entire function forms. In the `n1 < m1` case, the symmetric condition forces `n1 = m2 = 1` and `m1 = n2 >= 2`, again yielding exponential-periodic forms.

Reviewer confidence is medium-high for source identity, theorem structure, and proof strategy because the arXiv metadata, HTML, PDF availability, and downloaded TeX source package were inspected. Confidence is lower for mathematical correctness because this run did not perform formal proof verification or independent theorem checking.

## Detailed Summary

### Problem

The classical algebraic equation `x^n + y^m = 1` motivates analytic Fermat-type functional equations. In complex analysis, entire and meromorphic solutions of these equations connect value distribution theory, Nevanlinna theory, differential equations, and difference equations. This paper studies a coupled shifted system in `C^n`, where each equation mixes one function at `z` and the other function at `z+c`.

### Prior Work Context

The introduction cites earlier classifications by Gross-Yang for entire and meromorphic Fermat-type equations, Liu and Liu-Cao-Cao for nonlinear difference equations, and Xu et al. for coupled two-variable Fermat-type systems. The paper includes an example showing that a previous two-variable theorem form is too narrow when a term treated as constant may actually depend on variables.

### Main Result

The downloaded TeX source defines one main theorem. It states that finite-order nonconstant transcendental entire solutions of the coupled system are characterized by exponent relations:

- If `n1 = m1`, the theorem forces `m1 = n1 = m2 = n2 = 2` and gives cosine-type solution forms with polynomial or affine components subject to `2c`-periodicity and exponential shift constraints.
- If `n1 > m1`, the theorem forces `n2 = m1 = 1` and `n1 = m2 >= 2`, with both functions expressed using exponentials multiplied by `2c`-periodic entire functions.
- If `n1 < m1`, the theorem forces `n1 = m2 = 1` and `m1 = n2 >= 2`, with a symmetric exponential-periodic family.

### Proof Strategy

The proof starts from a finite-order nonconstant entire solution pair and applies Nevanlinna-theoretic growth lemmas to derive relations among the characteristics of `f1`, `f2`, and their shifts. For finite-order functions, shift estimates allow `T(r, f(z+c))` to be compared with `T(r, f)`. Those estimates force exponent-balance constraints and eliminate several regimes by contradiction.

For the admissible cases, the proof uses zero-free entire-function representations and algebraic alternatives involving shifted polynomial expressions. Some alternatives produce contradictions, while others yield valid cosine-type or exponential-periodic solution families. The TeX source includes a boxed logic tree summarizing four algebraic exponential alternatives and their outcomes.

### Source Package Notes

The source package contains `00README.json` and `Banerjee+Banerjee.tex`. The source metadata records `latex` as the compiler and TeX Live 2025 as the TeX Live version. The TeX source contains one main theorem, six lemmas, one proof environment for the main theorem, and 45 bibliography entries.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The paper studies finite-order transcendental entire solutions of a coupled Fermat-type difference system in several complex variables. | Source metadata and author claim | E1, E2, E3 | Directly supported by the abstract, introduction, and TeX source. | High |
| C2 | The main theorem classifies admissible solution families by relative exponent regimes. | Author theorem claim | E2, E3 | Directly supported by the main theorem statement in the source. | High for reporting; not formally verified |
| C3 | Equal-exponent admissibility forces the all-exponents-two case and cosine-type periodic structures. | Author theorem claim | E3 | Supported by the theorem statement and proof branch. | Medium-high |
| C4 | Asymmetric exponent cases force one side's shifted exponent to be 1 and the opposite exponent pair to match. | Author theorem claim | E3 | Supported by the theorem statement and proof branch. | Medium-high |
| C5 | The proof relies on Nevanlinna growth estimates, finite-order shift estimates, and contradiction arguments. | Reviewer interpretation grounded in proof source | E2, E3 | Supported by lemmas and proof text; detailed proof correctness not mechanically checked. | Medium |
| C6 | The local archive pull succeeded for PDF, abstract HTML, and source package. | Process claim | E4 | Supported by archive summary and verification. | High |
| C7 | No same-paper Black-Lake DEP artifact was found before this targeted run. | Process claim | E5 | Supported by marker checks across repository artifact folders and related search. | High |

## Methodology

- `Research objective`: Pull the user-specified arXiv paper into the local single-paper archive, then run a targeted Black Lake Arxiv DEP workflow that creates a public-safe log, Report-Mark, and DEP-E manuscript.
- `Sources inspected`: arXiv abstract page, arXiv HTML full text, arXiv PDF URL and local PDF collection status, arXiv TeX/source package, local archive summary metadata, live Black-Lake README, live Black-Lake-Data README, and three related Black-Lake DEP manuscripts.
- `Discovery strategy`: The paper was selected by user-specified URL rather than random archive selection. Duplicate checks searched repository artifact folders and related repository search for arXiv ID, title, DOI, and slug markers.
- `Inclusion criteria`: Sources were included when they identified the selected paper, supported theorem/proof/source-package claims, defined repository deposition rules, or supplied the closest available conceptual related-entry context.
- `Exclusion criteria`: Source PDF and TeX package were not copied into the DEP `.source/` folder because this repository deposit uses public URLs and generated analysis only. No formal proof assistant, symbolic algebra verification, or external mathematical review was performed.
- `Analytical approach`: Conceptual, comparative, implementation, product research, replication/proof-review planning, and DEP-ready provenance review.
- `Evidence handling`: Author theorem claims are reported as theorem claims unless formally verified. Reviewer interpretations are separated from source statements. Related DEP entries are conceptual bridges, not proof evidence for this paper.
- `Uncertainty handling`: Formal correctness, TeX parsing loss, formula extraction limits, and broad related-entry overlap are stated explicitly.
- `Extraction process`: Local archive files were created and verified; TeX source was inspected from the downloaded source package; public arXiv HTML was inspected; public artifacts withhold local absolute paths.
- `Version control`: arXiv version v1 was inspected; source package metadata records TeX Live 2025 and compiler `latex`.
- `Targeted selection note`: The recurring random-selection step was intentionally bypassed because the user requested this exact paper.
- `Deduplication validation`: No prior same-paper `.logs`, `.reports`, `.lake-data`, or related repository markers were found; reselection was not applicable.

## Scope, Constraints, and Assumptions

- `Scope`: Review arXiv:2606.30683 as a pure mathematics paper and preserve a schema-complete DEP-E manuscript plus related log and Report-Mark.
- `Temporal boundary`: Public source access date is 2026-07-09.
- `Evidence limits`: The proof was read structurally but not formally verified. Formula extraction from HTML and TeX can lose semantic detail. No proof assistant, computer algebra system, or independent mathematical referee was used.
- `Assumptions`: The downloaded source package corresponds to arXiv:2606.30683v1. The local archive summary correctly records the pulled PDF, abstract HTML, and source package.
- `Constraints`: Public artifacts avoid local absolute paths, home directories, usernames, machine names, local timezone labels, and exact local execution timestamps. Source files are not redistributed.
- `Out of scope`: Formal theorem proving, checking every bibliography claim, producing a complete expository rewrite of the proof, or publishing local archive source files.
- `Intended use`: Black-Lake DEP-E deposition, future math-proof review, source provenance preservation, and structured theorem extraction planning.
- `Audience`: Black-Lake reviewers, mathematics researchers, proof-formalization engineers, and research automation maintainers.
- `Reproducibility boundary`: Another reviewer can inspect the public arXiv sources and repository-relative artifacts, but mathematical correctness requires expert review or formalization.
- `Data sensitivity`: Public paper/repository metadata and local archive selection metadata only; no private data collected.

## Observations

- `Observed pattern`: The theorem's value lies in regime classification: exponent inequalities are not incidental, they determine whether finite-order nonconstant entire solutions can exist and what form they take.
- `Technical implication`: Mathematical DEP artifacts need theorem-case ledgers, not only prose summaries, because assumptions and conclusions are tightly coupled.
- `Evidence-quality implication`: TeX source is better than abstract-only review for pure math, but formula-preserving extraction remains a hard problem.
- `Operational implication`: Future Black-Lake math reviews should separate source pull, theorem parsing, proof dependency mapping, and formal verification status.
- `Open question`: Can the theorem be converted into a verified decision tree for exponent tuples and solution-form templates?

## Considerations

The paper should not be treated as machine-verified. It is a source-reviewed mathematical classification. The theorem cases, proof dependencies, and bibliography links should be preserved for a future human or proof-assistant pass.

Related-entry synthesis is necessarily broader than in an AI or systems paper because the current Black-Lake repository does not contain direct complex-analysis neighbors. The selected related entries are useful as structural review analogies, not as mathematical prior work for this theorem.

If this paper is later used for implementation, the safe path is symbolic/expository tooling: theorem extraction, assumption ledgers, example generation, and proof dependency maps. The artifact should not imply that a short code classifier validates the theorem.

## Strengths

- The paper states a clear classification target and directly ties solution forms to exponent regimes.
- The source package is available and small enough for direct TeX inspection.
- The theorem extends several prior lines of Fermat-type difference-equation work into several complex variables.
- The proof strategy exposes reusable components: growth estimates, shift invariance for finite-order functions, zero-free representation, and contradiction branches.
- The source includes an example highlighting why a previous theorem form needed refinement.

## Weaknesses

- This run did not formally verify the proof.
- The theorem statement is complex enough that automated TeX extraction can corrupt mathematical notation.
- The paper does not provide a machine-readable decision table for exponent regimes.
- The related-entry set in Black-Lake has no direct complex-analysis neighbor, limiting synthesis specificity.
- The public artifact cannot include local source paths or redistribute the downloaded source package.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add theorem decision table | Exposition | The main theorem is case-heavy. | Easier review and formalization. | Risk of oversimplifying assumptions. | Compare every table row against the TeX theorem statement. |
| Build proof dependency map | Proof review | Lemma usage and contradiction branches are central. | Better human review and formalization planning. | Requires careful formula preservation. | Trace each proof branch to lemmas and equation labels. |
| Formalize exponent classifier | Tooling | The admissible regimes are discrete. | Fast sanity checks for theorem-case routing. | A classifier does not prove the theorem. | Unit-test classifier against theorem cases and nonadmissible examples. |
| Generate symbolic examples | Pedagogy | Solution forms are abstract. | Helps future readers understand admissible families. | Could produce invalid examples if constraints are missed. | Substitute generated candidates back into the system under stated assumptions. |
| Link predecessor theorems | Related work | The paper extends several prior results. | Clarifies novelty and special cases. | Requires careful reading of cited papers. | Build a predecessor-result matrix with source citations. |

## Potential Implementations

1. `Theorem Case Ledger`
   - `User`: Mathematical reviewer or proof formalization engineer.
   - `Goal`: Preserve assumptions, exponent regimes, solution forms, and proof dependencies in a structured artifact.
   - `Core mechanism`: Parse theorem cases from TeX, attach source line/label references, and require human confirmation.
   - `Required inputs`: TeX source, arXiv metadata, theorem labels, equation labels, and reviewer notes.
   - `Outputs`: JSON/Markdown case table, dependency map, and review checklist.
   - `Risk controls`: Mark parsed formulas as unverified until reviewed; do not claim proof validation.
   - `Evaluation`: Human compares ledger rows against TeX theorem statement.

2. `Symbolic Fermat Difference Sandbox`
   - `User`: Research educator or mathematician exploring examples.
   - `Goal`: Generate simple candidate solution families for admissible exponent regimes.
   - `Core mechanism`: Encode exponent-regime conditions and solution templates, then run symbolic substitution checks on simple cases.
   - `Required inputs`: Exponent tuple, shift vector, template parameters, periodicity assumptions, and symbolic algebra backend.
   - `Outputs`: Candidate examples, substitution traces, and failure reasons.
   - `Risk controls`: State that substitution checks are examples only, not proof of classification.
   - `Evaluation`: Validate against examples from the paper and intentionally invalid regimes.

3. `Pure Math DEP Parser`
   - `User`: Black-Lake maintainer processing arXiv mathematics papers.
   - `Goal`: Convert TeX-heavy papers into DEP-ready theorem, lemma, proof, and reference ledgers.
   - `Core mechanism`: Extract environments, labels, citations, theorem statements, proof sections, and source metadata.
   - `Required inputs`: arXiv source package, metadata HTML, public URLs, and repository policy.
   - `Outputs`: Manuscript, Report-Mark, theorem ledger, and validation warnings.
   - `Risk controls`: Formula-loss warnings, no local paths in public artifacts, no formal-verification claims without proof assistant output.
   - `Evaluation`: Required-section checks, source-reference completeness, and sample human theorem audit.

## Three Ways to Exercise This Research

1. `Make a theorem table`: Objective: convert the main theorem into a table of exponent assumptions, forced equalities, solution form, and source label. Inputs: TeX theorem statement and this manuscript. Method: manually transcribe cases and compare against source. Output: theorem-case ledger. Success criterion: every source case is represented exactly once. Safety boundary: no claim of proof verification.
2. `Trace one proof branch`: Objective: follow the `n1 = m1` branch from growth estimates to the all-exponents-two conclusion. Inputs: TeX proof, lemma list, and equation labels. Method: build a dependency chain with assumptions, lemma use, and conclusion. Output: proof-branch map. Success criterion: every inference cites a source equation or lemma. Safety boundary: expert math review still required.
3. `Generate toy examples`: Objective: produce simple symbolic examples for the admissible all-exponents-two family. Inputs: simple affine functions, shift vector, and periodic component choices. Method: substitute into the coupled system and record whether identities hold. Output: example notebook or Markdown trace. Success criterion: examples either satisfy the equations or show a clear failed condition. Safety boundary: examples do not validate classification.

## Example MVP Product

- `Product name`: MathDEP Theorem Ledger
- `Target user`: Black-Lake reviewers processing pure mathematics arXiv papers.
- `Problem`: Pure math papers contain theorem/proof structures that are hard to preserve in DEP artifacts without losing assumptions, labels, and formula context.
- `Core workflow`: Pull arXiv source, extract metadata, parse theorem/lemma/proof environments, create case/dependency ledgers, generate a manuscript, and flag formula-loss risks for human review.
- `Data requirements`: arXiv ID, abstract HTML, TeX source package, PDF URL, theorem labels, equation labels, citations, and reviewer notes.
- `Architecture`: Local arXiv puller, TeX environment parser, formula-preserving text extractor, theorem-case ledger, proof dependency map, sanitization gate, and Markdown exporter.
- `Success metrics`: Percentage of theorem environments extracted, number of cases with source labels, formula-loss warning count, reviewer correction rate, and zero local-path leaks.
- `Risk controls`: Human review required for parsed formulas, no formal-proof claims without proof assistant output, no local absolute paths in public artifacts, and no redistribution without license review.
- `Limitations`: MVP cannot prove the theorem, fully parse all TeX macros, or replace expert mathematical review.
- `MVP boundary`: Source-structured review aid, not a theorem prover.
- `Deployment model`: Local CLI or repository automation step.
- `Evaluation plan`: Test on this paper, SANE, and one simpler theorem paper; compare extracted theorem ledgers with manual source review.
- `Failure modes`: Corrupted formulas, missed custom theorem environments, false confidence from code examples, and overbroad related-entry synthesis.
- `Maintenance plan`: Add macro dictionaries, theorem-environment patterns, and human correction workflow as new math papers are processed.

Minimal illustrative sketch:

```python
def admissible_regime(n1, m1, n2, m2):
    if n1 == m1 == n2 == m2 == 2:
        return "cosine-periodic-family"
    if n1 > m1 and n2 == m1 == 1 and n1 == m2:
        return "n1-dominant-exponential-periodic"
    if n1 < m1 and n1 == m2 == 1 and m1 == n2:
        return "m1-dominant-exponential-periodic"
    return "outside-main-admissible-forms"
```

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Fermat Difference paper | Primary arXiv paper | Reviewed work on coupled Fermat-type difference systems in several complex variables. | https://arxiv.org/abs/2606.30683 |
| Fermat Difference source package | Primary TeX source | Source for theorem/proof structure and source package metadata. | https://arxiv.org/e-print/2606.30683 |
| 2D-RC OTFS DEP | Related Black-Lake DEP | Formal multi-dimensional system review and source-first mathematical structure. | `.lake-data/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` |
| SANE Embeddings DEP | Related Black-Lake DEP | Locality, topology, and structural constraints in source-reviewed graph methods. | `.lake-data/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md` |
| Tech Intel 2338 DEP | Related Black-Lake DEP | Formal scientific-computing and evidence-boundary context. | `.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md` |
| Gross-Yang and related Fermat-type work | Cited prior work | Predecessor family for analytic Fermat-type equations. | Cited by the reviewed paper |
| Liu, Liu-Cao-Cao, Xu et al. | Cited prior work | Difference-equation and coupled-system predecessors extended by this paper. | Cited by the reviewed paper |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2606.30683 | Metadata, abstract, authors, submitted date, subject, DOI, license link, and source links. | 2026-07-09 | Primary arXiv metadata page inspected. |
| R2 | https://arxiv.org/html/2606.30683v1 | Full-text theorem/proof structure and source context. | 2026-07-09 | Public arXiv HTML inspected. |
| R3 | https://arxiv.org/pdf/2606.30683 | PDF source availability and local archive pull. | 2026-07-09 | PDF archived locally but not redistributed. |
| R4 | https://arxiv.org/e-print/2606.30683 | TeX source package for theorem/proof extraction. | 2026-07-09 | Source package archived locally and inspected; not redistributed. |
| R5 | https://doi.org/10.48550/arXiv.2606.30683 | Persistent DOI reference. | 2026-07-09 | DOI referenced. |
| R6 | Local single-paper arXiv archive metadata, path withheld | Archive pull provenance and local PDF/HTML/source presence. | 2026-07-09 | Local path withheld under public-safety policy. |
| R7 | https://github.com/Delphoa/Black-Lake | Output repository DEP-E, log, report, README, and attribution requirements. | 2026-07-09 | Live README inspected. |
| R8 | https://github.com/Delphoa-Labs/Black-Lake-Data | Related repository DEP and attribution expectations. | 2026-07-09 | Live README inspected. |
| R9 | `.lake-data/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` | Related formal system/source-review context. | 2026-07-09 | Repository-relative related artifact inspected. |
| R10 | `.lake-data/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md` | Related locality/topology/source-review context. | 2026-07-09 | Repository-relative related artifact inspected. |
| R11 | `.lake-data/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md` | Related formal scientific-computing/evidence-boundary context. | 2026-07-09 | Repository-relative related artifact inspected. |

## Appendix

### Targeted Selection and Deduplication Record

- Selection type: user-specified arXiv URL, not random.
- Selected identifier: arXiv:2606.30683.
- Paper archive status: PDF, abstract HTML, source package, README, and summary CSV collected.
- Source package contents: `00README.json`; `Banerjee+Banerjee.tex`.
- Source metadata: compiler `latex`; TeX Live 2025.
- Duplicate markers found before acceptance: 0.
- Reselections required: 0.
- Same-paper search keys included arXiv ID, DOI, title phrase, `Fermat Difference`, `Coupled Fermat`, and author names.
- Same-paper locations checked: `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, and related Black-Lake-Data search.

### Source Collection Notes

No `.source/` directory was created in this DEP. The local arXiv archive contains collected source artifacts, but the repository deposit references public URLs and generated analysis only.

### Validation Checklist

- Required manuscript headings are present.
- YAML `title` and H1 are identical and under 40 characters.
- `## Evidence Ledger` exists.
- `## Key Claims and Evidence` separates source theorem claims from reviewer interpretation.
- `## Three Ways to Exercise This Research` contains exactly three entries.
- `## Example MVP Product` includes product name, target user, problem, workflow, data requirements, architecture, success metrics, risk controls, and limitations.
- Claims are tied to evidence ledger IDs or source references.
- Related research includes exactly three Black-Lake related entries in the core synthesis.
- Public artifact text uses repository-relative paths and public URLs, not local absolute paths.
