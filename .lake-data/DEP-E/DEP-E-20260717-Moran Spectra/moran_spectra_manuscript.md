---
title: "Moran Spectra - DEP-E"
generated_at: "2026-07-17"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of intermediate Beurling dimensions for spectra of a bounded consecutive-digit Moran-measure class."
source_status: "verified complete local PDF and full-paper HTML; metadata and TeX source inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-17"
temporal_cutoff: "arXiv v1 and publisher records available through 2026-07-17"
primary_url: "https://arxiv.org/abs/2302.05868v1"
stable_identifier: "arXiv:2302.05868v1; DOI:10.1016/j.acha.2023.101606"
confidence_summary: "High for identity, theorem statements, formulas, and reported constructions; medium for detailed proof correctness; no formal verification."
safety_scope: "non-sensitive mathematical research and educational tooling"
distribution_notes: "Date-only public provenance; all source files, paths, cache outputs, hashes, and machine details withheld."
---

# Moran Spectra - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2302.05868v1 | https://arxiv.org/abs/2302.05868v1 | Public metadata; the abstract is not treated as the paper body. | 2026-07-17 | Inspected |
| S2 | *On the intermediate value property of spectra for a class of Moran spectral measures* | Primary paper | PDF | arXiv:2302.05868v1 | https://arxiv.org/pdf/2302.05868 | Complete local copy verified and inspected; source file withheld. | 2026-07-17 | Complete paper inspected |
| S3 | Official arXiv full-paper endpoint | Availability check | HTML | arXiv:2302.05868 | https://arxiv.org/html/2302.05868 | Returned HTTP 404 and was not accepted as paper evidence. | 2026-07-17 | Unavailable |
| S4 | ar5iv full-paper rendering | Primary paper cross-check | HTML | arXiv:2302.05868v1 | https://ar5iv.labs.arxiv.org/html/2302.05868 | Approved fallback; complete local copy passed the full-paper structure gate; file withheld. | 2026-07-17 | Integrity-verified and inspected |
| S5 | arXiv e-print | Primary manuscript source | gzip-compressed single TeX | arXiv:2302.05868v1 | https://arxiv.org/e-print/2302.05868 | Decompressed locally and validated as TeX; not redistributed. | 2026-07-17 | Inspected for formulas and structure |
| S6 | ScienceDirect article record | Version-of-record metadata | Publisher HTML | DOI:10.1016/j.acha.2023.101606 | https://www.sciencedirect.com/science/article/abs/pii/S1063520323000933 | Official publisher terms apply. | 2026-07-17 | Metadata, abstract, section snippets, and citation context inspected |
| S7 | Flag Hardy Operators - DEP-E | Related DEP entry 1 of 3 | Markdown | DEP-E-20260716-Flag Hardy Operators | `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md` | Generated Black-Lake synthesis; contextual only. | 2026-07-17 | Inspected |
| S8 | Acoustic Phase Retrieval - DEP-E | Related DEP entry 2 of 3 | Markdown | DEP-E-20260716-Acoustic Phase Retrieval | `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` | Generated Black-Lake synthesis; contextual only. | 2026-07-17 | Inspected |
| S9 | FGLE Midpoint Scheme - DEP-E | Related DEP entry 3 of 3 | Markdown | DEP-E-20260716-FGLE Midpoint Scheme | `.lake-data/DEP-E/DEP-E-20260716-FGLE Midpoint Scheme/fgle_midpoint_scheme_manuscript.md` | Generated Black-Lake synthesis; contextual only. | 2026-07-17 | Inspected |
| S10 | Black-Lake repository authorities | Deposition rules | Markdown | live `origin/main` | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Process authority, not research evidence. | 2026-07-17 | Fetched and read |
| S11 | Black-Lake-Data README | Companion-repository rules | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Process and dedup context only. | 2026-07-17 | Fetched and read |

The arXiv record lists Jinjun Li and Zhiyi Wu as authors, a single submission on 2023-02-12, primary category `math.NT`, secondary category `math.CA`, and the arXiv-issued DOI 10.48550/arXiv.2302.05868. The record exposes the non-exclusive arXiv distribution license. The publisher identifies the journal version in *Applied and Computational Harmonic Analysis*, volume 68, January 2024, article 101606, DOI 10.1016/j.acha.2023.101606.

The complete mathematical review is pinned to arXiv v1. The publisher record confirms publication context and exposes final-version snippets, but this run did not obtain and line-compare the entire version of record. No official repository, code release, or data artifact was found by focused public GitHub search. That absence is recorded as negative discovery evidence, not proof that no private implementation exists.

No local source path appears in this public artifact. Source files are represented only by canonical URLs and public-safe verification summaries.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, subjects, arXiv ID, submission date, version history, abstract, source locators, arXiv DOI | Identity and high-level claims | High | Metadata cannot establish proof details |
| E2 | S2, pp. 1-4 | Primary paper | Definition of the Moran measure, divisibility and boundedness assumptions, Fourier/entropy/Beurling dimension bounds, Theorems 1.1 and 1.2 | Research object and central results | High for source reporting | Mathematical correctness was not independently certified |
| E3 | S2, Proposition 2.1 | Primary paper | Non-decay argument for the Fourier transform on the support | Fourier dimension equals zero | Medium-high | Relies on a classical criterion cited by the paper |
| E4 | S2, Proposition 2.2 | Primary paper | Formula `limsup log(q_1...q_n)/log(b_1...b_n)` for upper entropy dimension | Upper endpoint and distinction from support Hausdorff dimension | High for source reporting | Uses prior pointwise-dimension and entropy results |
| E5 | S2, Proposition 2.4 | Primary paper | Beurling-dimension formula for a separated integer Moran set | Density calculation used by the construction | Medium | Long interval-counting estimate was reviewed but not formalized |
| E6 | S2, Theorem 3.1 and proof of Theorem 1.1 | Primary paper | Maximal tree-mapping criterion; canonical, lacunary, digit-thinned, regular, and irregular components | Realization of every target dimension | Medium-high | Spectrality criterion is imported from Dai and Sun; several construction checks are terse |
| E7 | S2, Lemma 3.3 and proof of Theorem 1.2 | Primary paper | Binary delay choices below the endpoint and sign sequences at the endpoint | Continuum cardinality of every level set | Medium-high | Distinctness and spectrality use construction facts and prior criteria rather than computation |
| E8 | S4-S5 | Full-paper HTML and TeX | Formula, heading, notation, and proof-structure cross-checks | Extraction correction and source triangulation | High for source structure | ar5iv may alter notation; the generic cache source extractor did not parse the single-file gzip |
| E9 | S6 | Publisher metadata | Journal, volume, article number, date context, DOI, abstract, final section headings, citation context | Publication status | High | Publisher metadata does not validate each proof step or expose the full comparison against v1 |
| E10 | S7-S9 | Related DEP artifacts | Multiscale harmonic analysis, Fourier reconstruction, and nonlocal scale-dependent theorem review | Cross-DEP synthesis and implementation translation | Medium | Contextual only; no support for the selected theorem |
| E11 | Public-safe integrity and cache summaries | Verification evidence | PDF header/EOF and size; HTML body/structure metrics; zero partials; extraction statuses | Complete-source and cache gates | High | Raw local paths, hashes, and records are intentionally withheld |
| E12 | S10-S11 | Repository authority | DEP class, filing, publication index, source withholding, README, attribution, and dedup context | Artifact layout and submission policy | High | Process evidence only |

## Executive Summary

Jinjun Li and Zhiyi Wu study how dense the exponential orthonormal bases of a class of singular Moran measures can be. A spectrum is a countable frequency set `Lambda` for which the exponentials `exp(2 pi i lambda x)` form an orthonormal basis of `L^2(mu)`. The Beurling dimension of `Lambda` measures its asymptotic local counting growth. The paper asks whether the possible dimensions of spectra leave gaps between the sparsest and densest constructions.

For consecutive-digit Moran measures generated by integers `2 <= q_n < b_n`, with `q_n` dividing `b_n`, ratios `r_n = b_n/q_n >= 2`, and uniformly bounded `b_n`, the answer is no. Theorem 1.1 states that for every target

`0 <= t <= upper_entropy_dimension(mu)`,

there is a spectrum whose Beurling dimension is exactly `t`. Theorem 1.2 strengthens this: for each fixed `t` in that interval, continuum-many distinct spectra realize the same dimension.

The proof is constructive. The authors first identify the upper entropy dimension as the limsup ratio of cumulative digit growth to cumulative scale growth. The canonical digit spectrum reaches this upper endpoint. A deliberately delayed tree labeling makes the frequency set lacunary and reaches zero. For an intermediate target, selected digit counts are thinned so their cumulative logarithmic growth approaches `t`; this produces a regular integer Moran subset of dimension `t`. A sparse irregular component is then added through a maximal tree mapping. Because that correction has dimension zero and Beurling dimension is finitely stable, the union remains dimension `t` while satisfying the imported spectrality criterion.

The cardinality argument shows that density is a coarse invariant. Below the upper endpoint, independent binary choices in the sparse delays generate continuum-many zero-dimensional corrections. At the endpoint, independent sign choices at every digit level generate continuum-many spectra without changing the dimension. Many structurally different bases therefore share the same asymptotic density.

Confidence is high that this artifact accurately reports the source identity, assumptions, dimension formula, theorem statements, and broad constructions because the complete PDF, verified full-paper HTML, and TeX were inspected. Confidence is medium for detailed proof correctness because the argument imports several nontrivial theorems, includes long asymptotic estimates, and was not checked in a proof assistant or by an independent mathematical referee.

## Detailed Summary

### Problem Context

Let `mu` be a compactly supported Borel probability measure on the real line. It is spectral when there is a countable set `Lambda` such that

`{x -> exp(2 pi i lambda x) : lambda in Lambda}`

is an orthonormal basis for `L^2(mu)`. A single singular measure can have many spectra. Complete classification is usually unavailable, so the paper studies a more tractable invariant: the Beurling dimension of each spectrum.

For a countable `Lambda`, its upper `r`-Beurling density compares the maximum number of frequencies in large intervals with `h^r`. The critical exponent at which that density changes from infinite to zero is the Beurling dimension. Equivalently, the dimension is the limsup of

`log #(Lambda intersect I) / log |I|`

over intervals whose lengths tend to infinity. This makes the invariant sensitive to the largest asymptotic local clusters, not to an average spacing alone.

Earlier work bounds the dimension of a frame spectrum between the measure's Fourier dimension and upper entropy dimension. Hausdorff dimension of the support had been proposed as an upper bound in a broader setting, but counterexamples showed that it is not universal. The selected paper identifies a variable-scale Moran class for which the upper entropy bound is not only valid but completely filled.

### Moran Measure and Assumptions

Choose integer sequences `B = {b_n}` and `D = {q_n}` with digit sets

`D_n = {0, 1, ..., q_n - 1}`.

The measure is the infinite convolution of uniform digit measures placed at successively finer scales:

`mu = delta_(D_1/b_1) * delta_(D_2/(b_1 b_2)) * ...`.

Its support consists of digit expansions

`sum_{k>=1} d_k/(b_1 ... b_k)`, with `d_k in D_k`.

The paper assumes

- `r_n = b_n/q_n` is an integer at least two for every `n`; and
- `sup_n b_n < infinity`.

The divisibility condition supplies compatible digit/frequency systems and ensures singularity in this setting. Bounded `b_n` is used to obtain the stated upper local and entropy-dimension formula and to control the intermediate digit-selection construction. These are material hypotheses, not cosmetic regularity conditions.

### Dimension Bounds

Proposition 2.1 shows the Fourier dimension of `mu` is zero. The proof takes scales `n_k = b_1...b_k` and observes that scaled copies of the support avoid part of the unit interval because `b_n >= 4` and `r_n >= 2`. A classical non-decay criterion then prevents the Fourier transform from tending to zero along a suitable sequence.

Proposition 2.2 identifies the upper entropy dimension:

`upper_entropy_dimension(mu) = limsup_n log(q_1...q_n) / log(b_1...b_n)`.

The upper bound comes through the upper packing/pointwise dimension formula imported from prior work. The lower bound uses entropy at the natural cylinder scale `1/(b_1...b_n)` and compares balls with a bounded enlargement of partition intervals.

For constant `q_n=q` and `b_n=b`, this upper entropy dimension equals the Hausdorff dimension of the support. For variable sequences, the paper records that Hausdorff dimension uses a liminf while the upper entropy dimension uses a limsup; the two can differ. A spectrum achieving the upper entropy endpoint can therefore have Beurling dimension strictly larger than the support's Hausdorff dimension.

### Integer Moran Sets

The proof needs a class of discrete sets whose Beurling dimension is computable. Given scale multipliers `n_k`, digit counts `m_k`, and spacings `t_k` satisfying a separation inequality, the integer Moran set is the union of finite sums

`sum_{i=1}^k x_i t_i (n_1...n_{i-1})`, with `0 <= x_i < m_i`.

Proposition 2.4 states that its Beurling dimension is

`limsup_k log(m_1...m_k) / log(m_k t_k n_1...n_{k-1})`.

The lower bound counts all level-`k` points inside their natural containing interval. The upper bound analyzes arbitrary large intervals, separates endpoint digit cases, and uses the imposed gap condition to control how many level blocks can fit. This proposition turns digit-growth design into an asymptotic density calculation.

### Spectrality Through Tree Mappings

The paper uses a `D`-adic tree whose nodes are finite words in the digit alphabets. A maximal tree mapping assigns each node a compatible residue-class label. The corresponding frequencies are sums of labels multiplied by natural scale factors.

Theorem 3.1, attributed to Dai and Sun, is the spectrality engine. It says that a maximal tree mapping generates a spectrum when the number of nonzero labels along every zero-tail continuation is uniformly bounded. The selected paper constructs mappings with at most one such extra nonzero label for each indexed word. This criterion is essential: density calculations alone do not show that a frequency set is a complete orthonormal basis.

Each positive integer has a mixed-radix expansion in the `q_n` alphabets. The authors associate a delay `s_n` with the corresponding word. If `s_n=0`, the frequency stays in a canonical digit system. If `s_n>0`, one large delayed scale term is added. Varying the delay sequence changes density while the tree criterion preserves spectrality.

### Upper and Lower Endpoints

For the upper endpoint, all delays are zero. The resulting canonical spectrum is an integer Moran set with digit counts `q_k`, spacings `r_k`, and scales `b_k`. Proposition 2.4 reduces its dimension to

`limsup_k log(q_1...q_k)/log(b_1...b_k)`,

which is the upper entropy dimension.

For the lower endpoint, choose delay `s_n=n`. The resulting frequencies grow at least geometrically; the paper obtains a ratio at least two between consecutive positive frequencies. A cited lacunary-set lemma then gives Beurling dimension zero.

These endpoint constructions already show that spectral completeness and frequency density are not locked together for this singular measure class.

### Intermediate Targets

Fix `0 < t < upper_entropy_dimension(mu)`. Lemma 3.2 constructs integers `q'_k` with `1 <= q'_k <= q_k` such that

`limsup_k log(q'_1...q'_k)/log(b_1...b_k) = t`.

The idea is to replace selected digit counts by one and retain full counts at carefully chosen crossing indices. Bounded `b_k` makes the overshoot in the logarithmic ratio vanish asymptotically.

The retained digits define a regular integer Moran set `Lambda_t^1` whose dimension is `t`. The paper then chooses zero delay for mixed-radix indices represented by those retained digits and large delay for the complement. The complete spectrum splits as

`Lambda_t = Lambda_t^1 union Lambda_t^2`.

The irregular component `Lambda_t^2` sits inside a lacunary spectrum and therefore has dimension zero. Finite stability gives

`dim(Lambda_t) = max(dim(Lambda_t^1), dim(Lambda_t^2)) = t`.

This is the main mechanism: one component controls the invariant, while another supplies the labels needed by the spectral construction at asymptotically negligible dimension cost.

### Continuum Cardinality

For `t` below the endpoint, both the retained-index set and its complement are countably infinite. On the complement, the delay can independently be chosen as `n^2` or `n^2+1`. Every binary sequence yields a distinct sparse correction, the correction remains dimension zero, and the regular component remains unchanged. Thus the dimension level contains at least continuum-many spectra; it cannot contain more because spectra are countable subsets encoded by countable sequences of real numbers in this construction.

At the upper endpoint, delays are not used. Instead the paper assigns an independent sign `w_i in {-1,1}` to the frequency digit at each level. Compatible-pair arguments yield a spectrum for every sign sequence. Counting inside symmetric intervals gives the lower dimension bound, while comparison with the all-positive and all-negative canonical spectra gives the upper bound. Every sign sequence therefore has the upper entropy dimension, producing continuum-many endpoint spectra.

### Publication and Evidence Boundary

The publisher record reports the final article in *Applied and Computational Harmonic Analysis* 68 (2024), article 101606. It also exposes acknowledgements of referee input and a longer reference list than the arXiv v1 text inspected locally. This run uses the publisher for bibliographic context and the complete arXiv v1 sources for mathematical detail. It does not assert that every displayed formula is identical across versions.

The paper contains no empirical evaluation, dataset, benchmark, or released code. Its evidence consists of definitions, propositions, constructive proofs, and cited prior theorems. Numerical finite-level examples could aid intuition, but they would not prove limsup statements or infinite-dimensional basis completeness.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The Fourier dimension of the selected Moran measure class is zero. | Author theorem claim | E3 | The support-scaling/non-decay mechanism is clear; the final implication relies on a cited classical criterion. | Medium-high |
| C2 | The upper entropy dimension equals the limsup cumulative digit/scale ratio. | Author theorem claim | E4 | Formula and proof structure were cross-checked; prior pointwise-dimension results remain imported. | High for source reporting |
| C3 | Every `t` in the closed interval from zero to upper entropy dimension is realized as a spectrum's Beurling dimension. | Author main claim | E5-E6 | Canonical, lacunary, digit-thinning, and zero-dimensional correction mechanisms support the construction under the stated assumptions. | Medium-high |
| C4 | Every fixed dimension level contains continuum-many spectra. | Author main claim | E7 | Binary delay and sign-sequence constructions are explicit; no independent set-theoretic/formal proof check was performed. | Medium-high |
| C5 | Upper entropy dimension, not support Hausdorff dimension, can be the attained upper bound for the variable-scale class. | Author implication | E4, E6 | The limsup/liminf contrast supports the implication when sequences are chosen to separate the two values. | Medium-high |
| C6 | The regular/irregular split is a transferable design pattern for separating invariant control from completeness repair. | Reviewer interpretation | E6-E7, E10 | Strong conceptual reading of the construction, but not a theorem stated by the authors outside this setting. | Medium |
| C7 | Finite truncations alone cannot certify the theorem's asymptotic dimension or spectral completeness. | Reviewer interpretation | E5-E7 | Follows from the limsup and infinite-basis nature of the claims; finite tools remain diagnostic only. | High |
| C8 | No official code release was identified. | Negative discovery observation | Focused public GitHub searches | Search results were empty for the arXiv ID; this does not exclude private or differently named code. | Medium |

## Methodology

- `Research objective`: Preserve a source-grounded review of the paper's dimension interval, continuum-cardinality result, assumptions, proof architecture, evidence limits, and implementation relevance as a DEP-E artifact.
- `Sources inspected`: Complete arXiv v1 PDF, verified full-paper ar5iv rendering, arXiv metadata, decompressed TeX source, extraction-cache summaries and text, official ScienceDirect metadata/section snippets, live repository authorities, and exactly three related Black Lake manuscripts.
- `Discovery strategy`: Uniform local PDF-parent sampling; identifier/title/DOI/slug dedup scans; local source classification; bounded archive repair; missing-only cache extraction; full-text theorem and reference review; publisher lookup; focused public GitHub code search; repository-wide related-entry search.
- `Inclusion criteria`: Primary-source definitions, assumptions, theorem statements, proof mechanisms, formulas, explicit limitations, publication metadata, negative availability evidence, and repository entries with concrete conceptual overlap.
- `Exclusion criteria`: Abstract-only inference, uninspected citation claims as proof evidence, metadata-only author inventories as deposits, secondary summaries as technical authority, and source files barred by the no-upload gate.
- `Analytical approach`: Conceptual, comparative, implementation, product research, and replication-oriented proof review. Empirical analysis is not applicable because the source reports no experiment.
- `Evidence handling`: Major claims map to evidence IDs. Author theorem claims, imported results, reviewer interpretations, negative discovery observations, and process evidence are labeled separately.
- `Uncertainty handling`: Formal correctness, imported lemmas, published-version differences, code absence, and finite-approximation limits are explicit rather than inferred away.
- `Extraction process`: `pypdf` and `html-regex` created reusable local text. PDF glyph/spacing noise was cross-checked against full-paper HTML and decompressed TeX. The generic source extractor failed because the e-print is a single-file gzip rather than a tar archive.
- `Version control`: Mathematical detail is pinned to arXiv:2302.05868v1. Journal publication is pinned to DOI 10.1016/j.acha.2023.101606 and the publisher record available on the access date.
- `Claim selection`: Priority was given to Theorems 1.1-1.2, Propositions 2.1-2.4, the imported tree criterion, endpoint/intermediate constructions, and stated scope boundaries.
- `Cross-checking`: Theorem statements and formulas were compared across PDF, HTML, and TeX; publisher metadata was checked independently; related DEP paths and their primary-source bases were inspected.
- `Safety handling`: No sensitive data or dual-use operational content is present. Example tools use synthetic integer sequences and clearly distinguish finite diagnostics from proofs.
- `Reviewer stance`: Independent manuscript review, proof-dependency mapping, DEP preservation, and bounded implementation translation; not peer review or formal certification.

### Random Selection and Dedup Validation

The archive enumeration contained 75,777 PDFs. Collapsing by parent directory yielded 75,776 paper units. PowerShell `Get-Random` selected zero-based index 17,600 uniformly from the sorted unit list. The first draw was accepted.

Dedup validation found no substantive match for arXiv:2302.05868, DOI 10.48550/arXiv.2302.05868, DOI 10.1016/j.acha.2023.101606, the normalized title, or slug `Moran-Spectra-Dimensions` in Black-Lake logs, reports, DEP entries, the public dedup index, automation memory, Black-Lake-Data code search, or same-paper worktree markers from the preceding 24 hours. Exclusions and reselections were both zero.

### Source Integrity and Cache Method

The selected unit began `partial`: its PDF passed the size/header/EOF checks, but full-paper HTML was missing. Repair preserved the PDF, collected metadata and e-print companions, and used approved ar5iv full-paper HTML after the official endpoint returned 404. The final HTML passed minimum bytes, body characters, document marker, heading count, and structure-term gates. Zero partial files remained.

The central cache began as a miss. `extract-arxiv` ran in `missing-only` mode with no network, produced PDF and HTML text, and ended `cached`. `pdftotext` was unavailable, so `pypdf` was the successful PDF fallback. The valid single-file gzip TeX source was not readable by the generic tar extractor, leaving source-text output absent. That is a cache shortfall, not a source-integrity failure.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's one-dimensional consecutive-digit Moran measures; Fourier, entropy, Hausdorff, and Beurling dimension relations; spectrum constructions; continuum multiplicity; and bounded educational/verification tooling.
- `Temporal boundary`: arXiv v1 and public publisher/repository records available through 2026-07-17.
- `Evidence limits`: No formal proof assistant, independent referee review, full version-of-record comparison, official code, executable notebook, or reproduction. Several prior theorems were not recursively re-proved.
- `Assumptions`: The paper's notation is interpreted as upper entropy and upper Beurling dimension where stated; public ar5iv and TeX representations are used only to cross-check the complete PDF.
- `Constraints`: Public output cannot include local paths, machine identifiers, exact timestamps, source documents, extracted text, cache internals, or hashes. ArXiv/publisher licenses remain controlling.
- `Out of scope`: Characterizing all spectra; removing divisibility or boundedness hypotheses; proving higher-dimensional analogues; validating journal revisions line by line; or claiming numerical finite truncations prove the theorems.
- `Intended use`: DEP preservation, mathematical review, proof-planning, educational exploration, and follow-on research prioritization.
- `Audience`: Harmonic analysts, fractal-measure researchers, formalization engineers, and developers building bounded mathematical exploration tools.
- `Depth target`: Manuscript report with proof architecture and replication/formalization planning.
- `Reproducibility boundary`: Source identity, formulas, and finite illustrative calculations are reproducible from public sources; infinite-dimensional correctness is not independently reproduced.
- `Operational boundary`: Tools may explore finite sequences and counting profiles but must label all outputs as diagnostics rather than proof certificates.
- `Data sensitivity`: Public mathematical sources only; source files remain locally withheld by repository policy.

## Observations

- `Observed pattern`: The attainable dimension set is a closed interval even though each spectrum is discrete and the family of all spectra is not classified.
- `Observed pattern`: Every point in that interval has continuum multiplicity, so Beurling dimension discards most combinatorial information about a spectrum.
- `Technical implication`: The regular/irregular decomposition decouples density control from completeness repair. This is the proof's most transferable mechanism.
- `Technical implication`: Upper entropy dimension is operationally natural because the construction tracks cumulative digit growth through a limsup. Hausdorff dimension, governed by a liminf here, can miss high-density subsequences.
- `Contradiction or tension`: The paper gives explicit existence constructions but not a practical algorithm with finite error bounds for selecting a spectrum at a requested dimension.
- `Contradiction or tension`: The generic extraction cache labels source extraction failed even though format-aware decompression validates readable TeX. Cache status and source integrity must therefore remain separate fields.
- `Open question`: Can the boundedness of `b_n` be replaced by a weaker regularity condition controlling overshoot in the digit-thinning lemma?
- `Open question`: Which non-consecutive or higher-dimensional digit systems preserve a full dimension interval?
- `Reviewer hypothesis`: A formal proof effort should isolate Proposition 2.4 and Lemma 3.2 first; they contain the reusable combinatorial core and can be tested independently of harmonic-analysis definitions.

## Considerations

- The word "spectrum" here means an exponential orthonormal basis of a measure, not a matrix eigenvalue spectrum. Product translations should preserve that distinction.
- Beurling dimension is an upper local-growth exponent. A finite sample or average spacing can misrepresent it, especially when the construction uses long sparse blocks and selected dense subsequences.
- The theorem's spectrum property depends on an imported maximal tree-mapping criterion. A tool that only implements digit thinning produces a candidate density profile, not a certified spectrum.
- The upper entropy/Hausdorff separation depends on variable-scale sequences. Constant-scale examples collapse the distinction and cannot demonstrate that implication.
- Continuum multiplicity is mathematical non-uniqueness, not an instruction to enumerate the family. Software should use reproducible finite encodings and never imply exhaustive coverage.
- A published-version comparison may alter exposition, citations, or proof details. Journal metadata confirms publication but does not authorize assuming identity with the preprint.
- Educational code should use arbitrary-precision integers or logarithms of products; direct products grow exponentially and will overflow fixed-width types.
- Formalization should pin each imported theorem with exact hypotheses, especially the tree spectrality criterion, pointwise-dimension formula, entropy equivalence, compatible-pair result, and lacunary dimension lemma.

## Strengths

- The result answers a natural structural question with a full interval theorem rather than isolated examples.
- The continuum-cardinality theorem materially strengthens existence and exposes the coarseness of the dimension invariant.
- Endpoint and intermediate constructions are explicit enough to reveal the mechanism: canonical density, lacunary sparsity, controlled digit thinning, and sparse completeness repair.
- The paper links Fourier, entropy, Hausdorff, and Beurling dimensions in one measure class and explains why their roles differ.
- Proposition 2.4 gives a reusable dimension formula for separated integer Moran sets.
- The proof records exact hypotheses and does not claim a complete classification of spectra.
- The journal publication record and subsequent citations indicate that the result entered the peer-reviewed literature, although this review does not treat publication as proof certification.

## Weaknesses

- The measure class is narrow: one-dimensional, consecutive digits, exact divisibility, ratios at least two, and uniformly bounded scale bases.
- Several central inputs are imported. Readers must consult prior work for the tree spectrality criterion, pointwise-dimension formula, entropy equivalence, and compatible-pair theorem.
- Some construction steps are stated tersely, including countable infinitude in Lemma 3.3 and distinctness details in the continuum argument.
- No finite-construction error analysis tells a numerical user how many levels are needed to approximate a target dimension.
- No official code or reproducible notebook was identified.
- The arXiv source inspected is v1; this artifact does not line-compare it against the complete published version.
- PDF extraction contains typography noise, and the generic source cache does not support this e-print's valid single-file gzip format.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| State a constructive finite-prefix algorithm with overshoot bounds | Lemma 3.2 | The proof is constructive but does not expose finite convergence rates | Makes target-dimension exploration reproducible and falsifiable | Bounds may require stronger regularity than bounded `b_n` | Prove prefix-error inequalities and test adversarial bounded sequences |
| Expand the continuum-cardinality proof | Theorem 1.2 | Several injectivity and countability facts are terse | Easier formal review and fewer hidden assumptions | More notation | Explicitly map binary/sign sequences to distinct frequency sets and prove injectivity |
| Package imported hypotheses as a dependency table | Whole proof | Spectrality and dimension results come from several sources | Supports peer review and proof-assistant planning | Requires careful version pinning | For each theorem, list exact statement, source, and hypothesis match |
| Compare arXiv v1 and version of record | Publication evidence | Publisher snippets indicate editorial changes | Separates substantive revision from bibliographic change | Full publisher access may be constrained | Equation/theorem/reference diff under lawful access |
| Add finite synthetic examples | Exposition | Variable digit sequences are abstract | Improves intuition without changing theorem status | Finite examples can mislead about limsup behavior | Show multiple truncation lengths and explicit non-certification labels |
| Extend the cache extractor to gzip-compressed single TeX | Research infrastructure | Current tar-only source extraction loses valid text | More complete local evidence and fewer false failure signals | Format detection must avoid unsafe decompression | Magic-byte check, bounded decompression, TeX-marker validation, fixture tests |

## Potential Implementations

### Target-Dimension Construction Sandbox

- `User`: Harmonic-analysis researcher or graduate student.
- `Goal`: Explore how finite digit-thinning choices approach a requested dimension.
- `Core mechanism`: Accept bounded integer sequences `q_n`, `b_n`, verify divisibility assumptions, and display cumulative logarithmic ratios for candidate `q'_n` choices.
- `Required inputs`: Synthetic or researcher-provided finite integer sequences and target `t`.
- `Outputs`: Assumption ledger, prefix ratios, retained/removed digit positions, overshoot plot, and explicit finite-only disclaimer.
- `Risk controls`: No proof claim; arbitrary-precision/log-domain arithmetic; reject invalid divisibility; surface truncation sensitivity.
- `Evaluation`: Unit tests on constant-scale cases, adversarial alternating sequences, and known target endpoints.

### Beurling Density Diagnostic

- `User`: Researcher inspecting a finite frequency construction.
- `Goal`: Estimate local counting slopes across interval scales without confusing them with the asymptotic theorem.
- `Core mechanism`: For finite sorted frequencies, compute the maximum count in intervals of multiple widths and regress `log count` against `log width` over user-selected ranges.
- `Required inputs`: Finite frequency list, interval widths, and comparison construction.
- `Outputs`: Scale-wise upper-count profile, estimated slopes, stability bands, and locations of densest intervals.
- `Risk controls`: Label estimates as diagnostics; show endpoint and range sensitivity; avoid extrapolation beyond observed scales.
- `Evaluation`: Lacunary sets, regular lattices, mixed block constructions, and perturbation tests.

### Proof Dependency and Hypothesis Auditor

- `User`: Mathematical reviewer or formalization engineer.
- `Goal`: Track every imported theorem and verify that its hypotheses match the selected Moran construction.
- `Core mechanism`: Represent propositions, definitions, imports, and dependency edges in a structured graph with source/page locators.
- `Required inputs`: Paper theorem inventory and verified bibliographic references.
- `Outputs`: Missing-hypothesis warnings, circularity checks, formalization order, and review checklist.
- `Risk controls`: Human confirmation for every mathematical match; no automated correctness certificate; immutable source/version pins.
- `Evaluation`: Reconstruct the dependency chain for Theorems 1.1 and 1.2 and compare it with an independent reviewer map.

## Three Ways to Exercise This Research

1. `Constant-scale endpoint check`: Objective—recover the canonical dimension for `q_n=q`, `b_n=b`. Inputs—small valid integers with `q|b` and `b/q>=2`. Method—compute prefix ratios `log(q^n)/log(b^n)` and generate finite canonical frequencies. Output—constant ratio and counting profile. Success criterion—ratios equal `log q/log b` at every prefix. Stop condition—do not infer infinite-basis completeness from the finite set.
2. `Alternating-scale limsup lab`: Objective—see why upper entropy and Hausdorff-style liminf behavior can separate. Inputs—two valid `(q,b)` pairs arranged in increasingly long alternating blocks. Method—plot cumulative digit/scale ratios and their running upper/lower envelopes. Output—visible limsup/liminf separation. Success criterion—multiple truncation lengths reproduce the designed envelopes. Stop condition—if blocks are too short for stable envelopes, report the example as inconclusive.
3. `Sparse-correction stress test`: Objective—test whether adding a toy lacunary component changes finite density estimates. Inputs—one regular finite Moran frequency set and one geometrically growing correction. Method—compare maximum interval counts before and after union over expanding windows. Output—scale-wise slope difference and correction contribution. Success criterion—the correction remains negligible over widening tested scales. Stop condition—treat any result as diagnostic only; no finite test proves zero asymptotic dimension.

## Example MVP Product

- `Product name`: Moran Spectrum Lab
- `Target user`: Graduate students, harmonic analysts, and proof engineers studying constructive spectra.
- `Problem`: The paper's nested digit and tree constructions are hard to audit from formulas alone, while naive finite plots can overstate asymptotic conclusions.
- `Core workflow`: Enter finite `q_n`, `b_n`, and target `t`; validate assumptions; compute entropy-ratio prefixes; propose finite digit thinning; generate canonical and toy sparse-correction frequencies; inspect upper-count profiles; export a hypothesis/evidence report.
- `Data requirements`: Synthetic integer sequences only. Optional user frequency lists remain local.
- `Architecture`: Local Python library for exact/log-domain arithmetic, a small browser or notebook interface, a deterministic report generator, and an optional graph module for proof dependencies.
- `Success metrics`: 100% rejection of invalid divisibility cases; exact endpoint ratios on constant-scale fixtures; deterministic outputs; no overflow on long prefixes; explicit finite-only labels on every density estimate; dependency graph covers every imported result used by the paper's main theorems.
- `Risk controls`: Local-only processing; no proof or spectrum certification; immutable source citations; truncation sensitivity displayed by default; arbitrary-precision arithmetic; input size limits.
- `Limitations`: Cannot prove infinite orthonormal completeness, limsup equality, continuum cardinality, or extensions beyond the paper's hypotheses.
- `MVP boundary`: No symbolic theorem proving, no arbitrary measure input, no automated literature assertions, and no attempt to enumerate continuum-many spectra.
- `Deployment model`: Local notebook or static browser application with no required backend.
- `Evaluation plan`: Unit tests for constant, alternating, lacunary, and invalid sequences; property tests for monotonic counts; reviewer comparison of dependency maps; usability test with one analyst and one student.
- `Failure modes`: Misleading slope fits from short prefixes, integer overflow in unguarded code, invalid scale assumptions, and users interpreting candidate density as spectrality.
- `Maintenance plan`: Version source citations, retain fixture outputs, test decompression/parser changes, and re-review the paper dependency map after any algorithm change.

## Related Research and Reading

### Exactly Three Related DEP Entries

| Item | Type | Concrete Relevance | Public Locator |
|---|---|---|---|
| Flag Hardy Operators - DEP-E | Black-Lake manuscript | Both works are theorem-driven harmonic analysis organized by multiscale frequency structure. The flag review highlights how geometry and decay thresholds control basis-like decompositions; the Moran paper controls frequency density by digit scales. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md |
| Acoustic Phase Retrieval - DEP-E | Black-Lake manuscript | The closest repository bridge to exponential/Fourier data. It reconstructs a source through Fourier coefficients after a conditioning step, while the Moran paper constructs exponential orthonormal bases and studies their density. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Acoustic%20Phase%20Retrieval/acoustic_phase_retrieval_manuscript.md |
| FGLE Midpoint Scheme - DEP-E | Black-Lake manuscript | Provides a complementary pure-analysis case where nonlocal structure, scale-dependent constructions, convergence limits, and imported proof conditions must be audited separately from finite computation. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-FGLE%20Midpoint%20Scheme/fgle_midpoint_scheme_manuscript.md |

### Primary and Near-Primary Reading Identified by the Paper

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| An and He, *A class of spectral Moran measures* | Prior theorem paper | Establishes spectrality for a related Moran class and supplies foundational context. | *Journal of Functional Analysis* 266 (2014), 343-354 |
| Dai and Sun, *Spectral measures with arbitrary Hausdorff dimensions* | Prior theorem paper | Source of the tree-mapping spectrality criterion used by the selected proof. | *Journal of Functional Analysis* 268 (2015), 2464-2477 |
| Fu, He, and Wen, *Spectra of Bernoulli convolutions and random convolutions* | Prior theorem paper | Contains the Bernoulli-convolution conjecture the selected theorem reports settling. | *Journal de Mathématiques Pures et Appliquées* 116 (2018), 105-131 |
| Czaja, Kutyniok, and Speegle, *Beurling dimension of Gabor pseudoframes for affine subspaces* | Definition/method paper | Introduces the Beurling-dimension framework and formulas cited by the selected paper. | *Journal of Fourier Analysis and Applications* 14 (2008), 514-537 |
| An and Lai, *Arbitrarily sparse spectra for self-affine spectral measures* | Related preprint | Provides zero-dimensional sparse-spectrum context. | https://arxiv.org/abs/2006.13497 |
| Li and Wu, *On the quasi-Beurling dimensions of the spectra for planar Moran-type Sierpinski spectral measures* | Author-related paper | Extends an intermediate-value theme to a planar quasi-Beurling setting. | *Applied and Computational Harmonic Analysis* 62 (2023), 475-497 |

The bibliography above is preserved as reading context identified in the primary paper. Except for the arXiv locator explicitly opened during this run's broader source review, these cited works were not independently re-reviewed and do not serve as direct evidence for the selected theorem in this artifact.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2302.05868v1 | Identity, version, authors, subjects, abstract, license, source locators | 2026-07-17 | Metadata only |
| R2 | https://arxiv.org/pdf/2302.05868 | Complete definitions, propositions, theorems, constructions, acknowledgements, references | 2026-07-17 | Verified local copy inspected; file withheld |
| R3 | https://arxiv.org/html/2302.05868 | Official HTML availability | 2026-07-17 | Returned 404; not evidence for paper content |
| R4 | https://ar5iv.labs.arxiv.org/html/2302.05868 | Full-paper structure and formula cross-check | 2026-07-17 | Approved verified fallback; local copy withheld |
| R5 | https://arxiv.org/e-print/2302.05868 | TeX formula and source-structure cross-check | 2026-07-17 | Valid gzip-compressed single TeX; local file withheld |
| R6 | https://doi.org/10.48550/arXiv.2302.05868 | Persistent arXiv identity | 2026-07-17 | DataCite DOI |
| R7 | https://doi.org/10.1016/j.acha.2023.101606 | Journal publication identity | 2026-07-17 | Publisher DOI |
| R8 | https://www.sciencedirect.com/science/article/abs/pii/S1063520323000933 | Venue, volume, article number, publication context, abstract, snippets | 2026-07-17 | Official publisher record |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md | Related multiscale harmonic-analysis synthesis | 2026-07-17 | Contextual only |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Acoustic%20Phase%20Retrieval/acoustic_phase_retrieval_manuscript.md | Related Fourier reconstruction synthesis | 2026-07-17 | Contextual only |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-FGLE%20Midpoint%20Scheme/fgle_midpoint_scheme_manuscript.md | Related nonlocal analysis and proof-audit synthesis | 2026-07-17 | Contextual only |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, source withholding, attribution, and commit rules | 2026-07-17 | Process authority |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-07-17 | Process authority |
| R14 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion-repository context and cross-repository dedup authority | 2026-07-17 | Process authority |
| R15 | https://arxiv.org/abs/2006.13497 | Sparse-spectrum related reading identified by the paper | 2026-07-17 | Related reading, not direct evidence |

## Appendix

### A. Random Selection and Dedup Trace

- Candidate enumeration command family: `rg --files -g "*.pdf"` against the local archive root.
- PDF count: 75,777.
- Unique PDF-parent paper units: 75,776.
- Random method: PowerShell `Get-Random` over sorted unique units.
- Accepted zero-based index: 17,600.
- Duplicate exclusions: 0.
- Other exclusions: 0.
- Reselections: 0.
- Acceptance: first draw.
- Checks: public dedup index; Black-Lake `.logs`, `.reports`, and `.lake-data`; normalized title; arXiv ID; arXiv and journal DOI; slug; automation memory; Black-Lake-Data code search; recent worktree markers.

### B. Source Integrity and Cache Verification

| Item | Public-Safe Result |
|---|---|
| Initial source state | `partial`: valid PDF, missing full-paper HTML |
| PDF | 243,499 bytes; `%PDF-` header; trailing `%%EOF`; preserved |
| Official HTML | HTTP 404; rejected as unavailable |
| Approved fallback HTML | 2,453,288 bytes; 142,726 body characters; document marker; 45 headings; five structure terms |
| Metadata HTML | 40,030 bytes; metadata only |
| E-print | 17,636-byte gzip; 60,687 decompressed TeX bytes; one TeX source |
| Partials | 0 |
| Final source state | `complete`; gate passed before synthesis |
| Initial/final cache | miss / `cached` |
| Cache mode | `missing-only`; no network |
| PDF extractor | `pypdf` succeeded; `pdftotext` unavailable |
| HTML extractor | `html-regex` succeeded |
| Source extractor | `tarfile` failed on valid non-tar single-file gzip; independent format-aware validation passed |
| Text outputs | PDF 44,524 bytes; HTML 110,876 bytes; source 0 bytes |
| Public upload | none; no `.source/` directory |

### C. Proof Dependency Outline

1. General frame-spectrum bounds place Beurling dimension between Fourier and upper entropy dimensions.
2. Proposition 2.1 establishes the zero Fourier-dimension lower endpoint for this measure class.
3. Proposition 2.2 computes the upper entropy dimension from digit/scale growth.
4. Proposition 2.4 computes Beurling dimension for separated integer Moran sets.
5. The imported maximal tree-mapping criterion converts bounded-tail label constructions into spectra.
6. The canonical construction attains the upper endpoint; the lacunary delay construction attains zero.
7. Lemma 3.2 selects reduced digit counts for an arbitrary intermediate target.
8. The regular/irregular union and finite stability preserve the target dimension while maintaining spectrality.
9. Binary delays give continuum multiplicity below the endpoint; sign sequences give continuum multiplicity at the endpoint.

This outline is a review map, not a replacement proof. Formalization must import or re-prove every external theorem with exact hypotheses.

### D. Validation Checklist

- Required YAML fields are present; `title` and H1 are identical and 21 characters long.
- All required manuscript headings use the schema names and order.
- `## Evidence Ledger` and `## Key Claims and Evidence` distinguish source claims, imports, reviewer inference, negative discovery, and process evidence.
- Every major executive-summary claim maps to evidence and a source reference.
- `## Three Ways to Exercise This Research` contains exactly three numbered paths.
- `## Example MVP Product` contains every required product field and explicit non-certification controls.
- Exactly three related DEP entries are used and each has a concrete overlap explanation and public locator.
- Selection, source-integrity repair, cache method, dedup, extraction fallback, and source-withholding status are explicit.
- No local absolute path, username, drive path, machine name, exact execution timestamp, or local timezone label appears.
- No source file, `.source/` directory, cache, extracted source text, or integrity record is included in the public DEP.

### E. Replication and Formalization Checklist

- [ ] Pin every imported theorem and exact hypothesis.
- [ ] Reproduce Proposition 2.4's interval-count upper bound independently.
- [ ] Formalize the digit-thinning lemma with explicit finite overshoot bounds.
- [ ] Prove the tree mapping satisfies maximality and the bounded-tail criterion for each target.
- [ ] Make injectivity of binary-delay and sign-sequence families explicit.
- [ ] Compare the full journal version against arXiv v1 under lawful access.
- [ ] Add finite examples only as diagnostics with truncation warnings.
- [ ] Extend source extraction to bounded single-file gzip TeX without changing the public no-source policy.
