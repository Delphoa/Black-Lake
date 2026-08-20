# Constraint Propagation in Coupled Fermat Difference Systems

## A detailed review and re-conceptualization of “Finite order transcendental entire solutions of coupled Fermat-type difference equations in several complex variables”

**Source paper:** Jhilik Banerjee and Abhijit Banerjee, arXiv:2606.30683v1, 27 June 2026.[^paper]
**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260709-Fermat Difference`[^source-dep]
**Source commit:** `a1ffd4737ce95c14f3a15251ee4fbba4403108a5`
**Paired task indicator:** `BL-DEPPAIR-20260714-6BFECDD5`
**Direction:** `DEP-E -> DEP-A`
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E review and complete canonical v1 paper inspection, including theorem, six lemmas, proof cases, figures, references, acknowledgments, and source-package context
**Reproduction boundary:** the proof was structurally reviewed but not formally verified by a proof assistant, computer algebra system, or independent referee
**One-way provenance:** source action review-only; source DEP modified: no; files moved: no; files copied: no; new derived data generated: yes

---

## Executive assessment

### The paper in one sentence

The paper classifies finite-order transcendental entire solution pairs for a coupled shifted Fermat-type system in several complex variables and shows that admissible forms depend sharply on the ordering of the principal exponents.

### The deeper idea

The argument is an exercise in analytic constraint propagation. Nevanlinna growth and shift estimates first turn two functional equations into algebraic restrictions on exponents. Once those restrictions leave only a few regimes, zero-free factorization converts relevant entire functions into exponentials of entire functions. Finite order pushes those exponents toward polynomial structure. Coupling and shift identities then force either trigonometric/cosine families with periodic constraints, exponential-periodic families, or contradictions.

### Bottom-line judgment

The complete source contains a coherent classification theorem, supporting lemmas, and a proof organized into three main regimes with four sub-branches in the equal case. The source DEP-E captures that architecture accurately and states its limitations. This intake independently checked the full canonical HTML and source structure but did not validate each analytic step formally. The correct verdict is “well-specified theorem and traceable proof strategy; correctness not independently certified.” Formula loss in HTML also means exact notation should be taken from the TeX/PDF, not from this prose restatement.

### Principal strengths

- The theorem explicitly links exponent inequalities to solution forms.
- The proof exposes reusable dependencies: growth estimates, shift control, zero-free representation, polynomial reduction, and periodicity.
- A counterexample in the introduction motivates correction of an incomplete predecessor form.
- The source is compact, public, and structurally suitable for formalization.

### Principal qualifications

1. This review is not a peer-review verdict or machine proof.
2. HTML conversion omits many formula glyphs, so exact equations are not retyped from lossy text.
3. The main theorem's hypotheses and case constraints are dense; a small transcription error can change the result materially.
4. Novelty relative to every cited predecessor was not independently established by reading all 45 references.

## 1. The problem and research question

Classical Fermat equations ask when powers can sum to one. Complex analysis replaces numbers with entire or meromorphic functions and studies how growth, zeros, and functional dependencies constrain solutions. Difference equations add shifted arguments, so values at a point interact with values at a translated point. In several complex variables, the shift is a nonzero vector and periodicity can occur along its direction.

The reviewed system contains two coupled equations. Each combines a power of one function at the present variable with a power of the other function at the shifted variable. Four positive exponents determine the nonlinear balance. The functions are required to be nonconstant transcendental entire and of finite order.

The paper asks: for each relation among the main exponents, which exponent tuples admit such solutions, and what analytic forms must those solutions take? The finite-order condition is essential because it makes shifts manageable in Nevanlinna characteristic estimates and constrains zero-free factorizations.

The introduction places the question after classical entire-function Fermat equations, differential-difference variants, and a prior coupled system. Example 1.1 shows a solution outside the predecessor theorem's claimed form because an object treated as a constant can depend on variables. This provides a concrete reason to revisit and generalize the classification.[^context]

## 2. Formal and technical reconstruction

### 2.1 Objects and assumptions

Let the unknowns be two transcendental entire functions on a complex vector space, and let the system relate their powered values at the current point and at a fixed nonzero shift. Four exponents appear. The theorem assumes finite order and nonconstancy. “Entire” removes poles; “transcendental” excludes polynomials; “finite order” bounds growth; and coupling means neither equation can be classified independently.

Because extracted HTML drops symbols, this review does not invent a character-level restatement. The canonical theorem and Equation 1.3 remain authoritative.[^theorem]

### 2.2 The three exponent regimes

Theorem 1.1 divides on the relative size of the first exponent pair.

In the equal regime, admissibility forces all four relevant exponents to equal two. The solution families have cosine-like structure built from exponential combinations of polynomial or affine terms. Shift conditions create a period of twice the shift and phase/sign constraints. The proof admits two algebraic sub-branches and rejects two others by contradiction.

In the first asymmetric regime, where the first function's present exponent dominates its coupled counterpart, the theorem forces two exponents to one and the remaining two to a common value at least two. Solutions take exponential forms multiplied by entire functions periodic under twice the shift.

The opposite asymmetric regime is symmetric: the roles of the exponent pairs exchange, again forcing two unit exponents, equality of the larger pair, and exponential-periodic solution forms.

The theorem is a necessity-and-form classification under its hypotheses. It should not be read as a claim about infinite-order entire solutions, meromorphic functions with poles, other coupling graphs, or arbitrary shifts.

### 2.3 Lemma stack

The source states six lemmas before the proof. Their roles can be reconstructed without duplicating lossy formulas. One supplies a several-variable Nevanlinna estimate for nonconstant meromorphic functions. Another controls algebraic relations of meromorphic functions. A further lemma forces degeneracy when a sum of meromorphic terms under growth restrictions vanishes. Another identifies when entire functions under composition or growth constraints reduce to polynomials. A difference analogue controls the characteristic of finite-order functions under shifts. The zero-free factorization lemma represents a zero-free entire function as an exponential of an entire function under appropriate conditions.[^lemmas]

The remark after Lemma 2.6 clarifies that a zero-free entire function automatically meets the relevant zero-set compactness condition, enabling exponential representation. These are not peripheral citations; they are the proof's dependency graph.

### 2.4 Growth reduction

The proof begins with a finite-order nonconstant entire solution pair and applies the Nevanlinna lemmas to both equations. Shift estimates allow characteristics at the translated argument to be compared to those at the original argument outside controlled exceptional sets. Combining inequalities yields restrictions summarized in the source as equations 3.5 and 3.9.

Those restrictions reduce the continuous analytic problem to three discrete parameter regimes. This reduction is the proof's conceptual hinge. Once exponent balance is fixed, the remaining equations have zero-free combinations suitable for exponential factorization.

### 2.5 Equal-exponent branch

In Case 1, equal exponents and the growth constraints force the quadratic configuration. Several combinations have no zeros. Lemma 2.6 and its remark permit exponential representations. Finite order and another lemma make the exponent functions polynomial. Solving paired exponential identities produces four algebraic alternatives, summarized in Figure 3.

Two alternatives imply the required polynomial pieces are constant, contradicting nonconstancy. The other two generate admissible cosine-type expressions. Shift relations constrain signs, phases, and periodic pieces. The proof's trigonometric appearance is therefore not assumed; it emerges from paired exponentials under the quadratic Fermat identity.

### 2.6 Asymmetric branches

Cases 2 and 3 use exponent restrictions to reduce the coupled system to a difference equation with exponential solutions. Comparing any two solutions shows that their ratio or difference has periodic behavior along twice the shift. The general solution is an exponential factor times an entire periodic factor. Symmetry between the two original functions maps one asymmetric case to the other.

The proof ends after Case 3, followed by a conflict-of-interest statement and references. There is no experimental section, code, or numerical appendix.

## 3. Architecture of the proof and information flow

The proof pipeline is: state the coupled system and finite-order assumptions; obtain growth inequalities; compare shifted and unshifted characteristics; derive exponent-balance constraints; route into equal, greater, or lesser regimes; establish zero-free combinations; factor them exponentially; reduce exponent functions to polynomials where required; solve algebraic exponential alternatives; reject contradictory branches; and read periodicity from shift relations.

This architecture separates global and local constraints. Nevanlinna theory supplies global growth control. Algebraic manipulation supplies local identities. Zero-free factorization translates multiplicative structure into additive exponents. Periodicity arises from comparing shifted solutions.

The guarantee boundary is the theorem under its hypotheses. The paper does not provide executable validation, exhaustive symbolic examples, or a formal proof object. A reader must verify each lemma's hypotheses, exceptional-set handling, nonconstancy step, and branch algebra.

## 4. Evidence reconstructed and review methodology

This is pure mathematics, so “experimental design” is not materially applicable. The evidence is deductive. The primary object is a v1 arXiv paper with an abstract, acknowledgments, introduction, one main theorem, six key lemmas, one main proof, three classification figures, a conflict statement, and 45 references. The source package contains a JSON manifest and one principal TeX file, as recorded by the DEP-E.

The review checked that the abstract's classification claim corresponds to Theorem 1.1; that the three regimes in the theorem reappear in the proof; that the six lemmas precede and are invoked within the proof; that the predecessor counterexample motivates the stated generalization; and that the source ends cleanly. No empirical dataset, baseline, randomness, runtime, or statistical significance exists to audit.

The equivalent quantitative audit is a proof-dependency audit. For every branch, the relevant questions are: are lemma hypotheses satisfied; are exceptional sets combined correctly; does finite order justify polynomial reduction; does zero-free status hold; are all algebraic alternatives exhaustive; and do periodicity conditions match the original shift system?

## 5. Results: theorem statement and meaning

The principal result is a regime-complete classification for the specified system. Equal principal exponents allow finite-order nonconstant transcendental entire solutions only in the quadratic case, with cosine-type families. Unequal regimes force unit exponents on one coupled side and equality of the remaining higher exponents, with exponential-periodic families. Outside those regimes, the proof's growth constraints rule out the targeted solution class.[^theorem]

The result means the exponent tuple is not a tunable cosmetic parameter. It controls analytic existence and form. Finite-order growth plus translation symmetry is strong enough to collapse a broad nonlinear system into a small family.

This review does not assert that the proof is correct beyond reporting and structural consistency. A complete mathematical assessment would check each formula against TeX, verify cited lemma versions, and attempt counterexamples or formalization.

## 6. Ablations and counterfactual proof checks

There are no experimental ablations. The appropriate analogues are hypothesis-removal and branch checks.

Remove finite order, and the shift characteristic estimates may fail to give the same exponent balance; the classification need not survive. Allow meromorphic rather than entire functions, and poles introduce divisor terms and invalidate zero-free reasoning. Set the shift to zero, and periodicity logic degenerates into an algebraic functional equation. Permit polynomial rather than transcendental solutions, and nonconstancy contradictions must be reconsidered. Change the coupling pattern, and symmetry between Cases 2 and 3 can disappear.

These counterfactuals identify which assumptions carry causal proof weight. They are proposed proof tests, not claims that alternate theorems are false.

## 7. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper studies a coupled Fermat difference system in several variables. | Title, abstract, Equation 1.3, and introduction. | Strongly supported. | Exact notation belongs to canonical TeX/PDF. |
| The theorem classifies finite-order transcendental entire solutions by exponent regime. | Theorem 1.1 and proof cases. | Strongly supported as a source report. | Correctness not formally verified. |
| Equal exponents force the quadratic cosine family. | Case 1 and sub-branches. | Structurally supported. | Requires validation of growth reduction and exhaustive alternatives. |
| Unequal regimes force unit/common exponents and exponential-periodic forms. | Cases 2 and 3. | Structurally supported. | Periodicity and solution completeness need formula-level checking. |
| The result corrects or extends a predecessor theorem. | Example 1.1 and related-work discussion. | Supported as motivation. | Full novelty requires direct predecessor review. |
| The proof is rigorous and complete. | Formal paper structure. | Unresolved independently. | No referee report, proof assistant, or line-by-line verification here. |
| The classification can be implemented as a simple exponent router. | Discrete theorem cases. | Useful reviewer proposal. | A router does not validate analytic hypotheses or prove the theorem. |

## 8. External primary-source context

The canonical arXiv record identifies v1, math.CV, the two authors, 27 June 2026, and the DOI.[^paper] The complete HTML contains 473 extracted lines and flags the article's section structure. The public source-package locator permits formula-preserving review from TeX.[^source]

The introduction cites classical and modern work on meromorphic mappings, Fermat-type differential and difference equations, and several-variable Nevanlinna theory. The main novelty claim should be scoped to the particular coupled several-variable classification. Because this intake did not read all predecessor papers fully, it cannot certify “first” or exhaustiveness of the related-work account.

There is no code artifact and none is needed for the theorem. A future formalization repository would be a new derivative, not evidence that the published proof was already machine-checked.

## 9. Independent re-conceptualization: an analytic type checker

The theorem can be interpreted as a type checker for functional systems. The input type consists of exponent tuple, shift, function class, and growth class. Nevanlinna constraints reject incompatible types before solving explicit functions. Admissible types route to constructors: cosine-periodic or exponential-periodic families. Proof branches act like exhaustiveness checks.

This interpretation makes the theorem easier to audit. A structured ledger can record preconditions, forced equalities, constructor, periodicity, and contradiction reason. It also makes a falsifiable prediction: any proposed finite-order entire solution outside the accepted routes must violate a hypothesis or reveal a gap in the proof.

**Boundary of the analogy:** mathematical existence is not software type checking. Lemmas rely on analytic estimates and exceptional sets, not finite syntactic rules. A program can encode the theorem statement but cannot establish its truth.

The transferable design principle is to separate parameter-regime elimination from explicit solution construction. This reduces review complexity and suggests an order for formalization.

## 10. Research notes and critical considerations

Formula extraction is the dominant archival risk. Missing superscripts, subscripts, vectors, and quantifiers can invert conditions. Public reviews should point readers to theorem labels rather than reproducing uncertain notation.

The phrase “all solutions” depends on exact hypotheses. Finite order, entire, transcendental, nonconstant, and nonzero shift must accompany every durable restatement.

The predecessor counterexample is valuable because it shows how a hidden dependence can be misclassified as constant. A formalization should model which variables each auxiliary function may depend on.

The proof uses cited lemmas in versions tailored to several complex variables. A verification pass must confirm domains, exceptional sets, and characteristic notation match the current use.

The source has figures summarizing intellectual history and proof routing. They improve exposition but do not add logical evidence beyond equations and proof text.

Another review risk is silent symmetry. Cases 2 and 3 look like mirror images, but a proof auditor should not accept one merely by visual analogy. The original equations couple present and shifted arguments in a specific order, so exchanging the functions may also require exchanging exponent labels and periodic factors. A durable proof ledger should record the exact renaming that maps one case to the other and verify the transformed hypotheses line by line. This check is inexpensive compared with redoing the Nevanlinna estimates and would catch a common class of transcription error: a correct result copied into the wrong coordinate or exponent slot. The same discipline applies to the two admissible cosine sub-branches. Their phase and sign conditions should remain attached to the precise algebraic alternative that produced them.

## 11. Implications

Scientifically, the result adds a structured classification to analytic difference equations and suggests that coupling plus finite growth can be more restrictive than either alone. For research tooling, it is a good candidate for theorem-case extraction, citation dependency maps, and formula-preserving archives.

Deployment and governance are not materially applicable in the usual operational sense. The relevant safeguard is epistemic: label the theorem as source-reviewed, not independently verified; preserve version and exact source; require expert review before using it as a foundation; and never treat a code example as proof.

## 12. New hypotheses derived from the paper

These are reviewer hypotheses, not established findings.

### Hypothesis 1: dependency-guided formalization is tractable

**Proposition:** the proof can be formalized modularly by first encoding shift-growth lemmas, then exponent routing, then explicit constructors.
**Predicted observation:** most proof effort concentrates in the lemma interface and exceptional sets rather than branch algebra.
**Falsifier:** branch-specific analytic arguments cannot share a common library.
**Minimum test:** formalize the exponent-reduction stage in a suitable proof assistant.

### Hypothesis 2: solution examples expose transcription defects quickly

**Proposition:** symbolic substitution of simple periodic and affine choices will detect most errors in a theorem-case ledger.
**Predicted observation:** intentionally altered signs or periods fail the original system.
**Falsifier:** substitutions remain inconclusive because conditions cannot be represented symbolically.
**Minimum test:** construct one example per admissible family and verify identities under explicit shift assumptions.

### Hypothesis 3: finite order is the decisive exclusion mechanism

**Proposition:** relaxing finite order permits qualitatively broader solution behavior not captured by the three regimes.
**Predicted observation:** known infinite-order constructions evade the characteristic inequalities.
**Falsifier:** the same classification follows without finite-order assumptions.
**Minimum test:** survey or construct infinite-order candidates while tracking exactly which lemma fails.

## 13. Replication and falsification agenda

First, produce a formula-preserving theorem ledger from the TeX source. Each row should include exact hypotheses, exponent relation, forced equalities, solution form, periodicity, and equation label. A second mathematician should compare it against the PDF.

Second, build a proof dependency graph. For every use of Lemmas 2.1–2.6, record instantiated functions, satisfied assumptions, exceptional set, and conclusion. Verify that cited predecessor statements match the versions used.

Third, trace Equation 3.1 through the constraints summarized by 3.5 and 3.9. This is the highest-priority step because all regime routing depends on it. Any missing inequality or reversed ratio could invalidate the classification.

Fourth, check the four equal-case algebraic alternatives for exhaustiveness and contradiction. Then substitute simple admissible cosine and exponential-periodic examples into the original system.

Fifth, formalize a bounded portion. Success is not a full theorem immediately; it is a machine-checked statement of the exponent router plus one valid constructor under explicit assumptions. Archive failures and ambiguities.

The theorem would be falsified by a finite-order nonconstant transcendental entire solution outside all stated families or by a failure of one stated family to satisfy the system under its recorded conditions.

## 14. Durable restatement

> Under finite-order, entire, transcendental, nonconstant, and nonzero-shift hypotheses, the paper reports that a coupled Fermat-type difference system admits only sharply constrained exponent regimes: a quadratic cosine-periodic family when the leading exponents match, and paired exponential-periodic families in the two asymmetric cases.

The enduring insight is the proof architecture: global growth bounds determine discrete admissible types before explicit analytic forms are constructed.

## Appendix A. Complete table and figure coverage ledger

### Tables

The paper contains no conventional numerical tables. The theorem and branch statements function as the principal case ledger.

### Figures

1. **Figure 1, evolution of Fermat-type equations:** positions the present coupled several-variable system in the literature; contextual, not proof evidence.
2. **Figure 2, classification structure:** routes the system into trigonometric and two exponential-periodic branches; mirrors Theorem 1.1.
3. **Figure 3, equal-case logic tree:** records four algebraic exponential alternatives, two contradictions, and two admissible cosine branches.

### Theorems, lemmas, and equations

- Theorem 1.1 was covered in all three regimes.
- The predecessor Theorems A–E and Example 1.1 were accounted for as motivation and context.
- Lemmas 2.1–2.6 and Remark 2.1 were mapped to their proof roles.
- Equations 3.1–3.9 carry growth reduction; 3.10 onward carry zero-free factorization and branch algebra; 3.27–3.28 carry asymmetric periodic solutions.
- Exact symbols were not reconstructed from lossy HTML; canonical TeX remains authoritative.

## Appendix B. Source and evidence notes

### Primary reviewed artifact

Both DEP-E files were read completely. The canonical v1 HTML article contains abstract, acknowledgments, introduction, notation, key lemmas, proof, figures, conflict statement, and references. The source DEP-E records one main TeX file and a JSON source manifest. The document ends cleanly.

### External primary sources

- https://arxiv.org/abs/2606.30683
- https://arxiv.org/html/2606.30683v1
- https://arxiv.org/pdf/2606.30683
- https://arxiv.org/e-print/2606.30683
- https://doi.org/10.48550/arXiv.2606.30683

### Evidence boundary

The paper reports the theorem and proof. This review inspected the complete paper and source structure but did not perform formal verification, independently referee every inference, or review all cited predecessors in full. Reviewer inference is confined to the type-checker re-conceptualization, caveats, and hypotheses.

## Footnotes

[^paper]: Canonical metadata and complete article: https://arxiv.org/abs/2606.30683 and https://arxiv.org/html/2606.30683v1
[^source-dep]: Immutable DEP-E source: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-Fermat%20Difference
[^context]: Introduction and predecessor counterexample: https://arxiv.org/html/2606.30683v1
[^theorem]: Theorem 1.1 in the complete article: https://arxiv.org/html/2606.30683v1
[^lemmas]: Key lemmas and proof: https://arxiv.org/html/2606.30683v1
[^source]: Public TeX source locator: https://arxiv.org/e-print/2606.30683
