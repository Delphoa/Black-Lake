---
title: "MOCS Flexible Lengths - DEP-E"
generated_at: "2026-07-24"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of generalized-Boolean-function constructions for mutually orthogonal complementary sets with flexible non-power-of-two lengths."
source_status: "verified complete local PDF and full-paper HTML inspected; public URLs only; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-24"
temporal_cutoff: "Paper v1 and repository context inspected through the public-safe run date."
primary_url: "https://arxiv.org/abs/2003.06991"
stable_identifier: "arXiv:2003.06991v1; DOI:10.1109/TIT.2020.2980818"
confidence_summary: "High for source identity and reported formal construction; medium for proof transcription and practical implications because no generator, proof assistant, or system experiment was reproduced."
safety_scope: "research review, synthetic sequence generation, simulation-only communications and radar evaluation"
distribution_notes: "No source document, rendering, extracted text, private verification record, local path, or machine context is redistributed."
---

# MOCS Flexible Lengths - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2003.06991v1 | https://arxiv.org/abs/2003.06991 | Metadata and abstract only; not counted as the paper. | 2026-07-24 | Inspected |
| S2 | arXiv PDF | Primary paper | PDF | arXiv:2003.06991v1 | https://arxiv.org/pdf/2003.06991 | Publisher/author terms apply; verified local copy withheld. | 2026-07-24 | Fully inspected and visually reviewed |
| S3 | Full-paper HTML | Primary paper rendering | HTML | arXiv:2003.06991v1 rendering | https://ar5iv.labs.arxiv.org/html/2003.06991 | Approved full-paper fallback; verified local copy withheld. | 2026-07-24 | Fully inspected |
| S4 | Persistent identifiers | Published identity | DOI | 10.48550/arXiv.2003.06991; 10.1109/TIT.2020.2980818 | https://doi.org/10.48550/arXiv.2003.06991; https://doi.org/10.1109/TIT.2020.2980818 | Identifier metadata; no source document redistributed. | 2026-07-24 | Verified |
| S5 | Institutional publication records | Venue metadata | HTML | IEEE TIT 67(6), 3464-3472 | https://repository.essex.ac.uk/30464/; https://researchoutput.ncku.edu.tw/en/publications/how-to-construct-mutually-orthogonal-complementary-sets-with-non--2/ | Institutional records for venue and publication metadata. | 2026-07-24 | Inspected |
| S6 | Black Lake authorities | Deposition rules | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Repository rules for DEP filing, attribution, source withholding, and publication indexing. | 2026-07-24 | Fetched and read |
| S7 | 4 Adic Complexity DEP-E | Related processed artifact | Markdown | DEP-E-20260721-4 Adic Complexity | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-4%20Adic%20Complexity/4_adic_complexity_manuscript.md | Conceptual synthesis only. | 2026-07-24 | Inspected |
| S8 | 2D-RC OTFS DEP-E | Related processed artifact | Markdown | DEP-E-20260709-2D-RC OTFS | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md | Conceptual synthesis only. | 2026-07-24 | Inspected |
| S9 | Multi-Point ISAC DEP-E | Related processed artifact | Markdown | DEP-E-20260716-Multi-Point ISAC | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Multi-Point%20ISAC/multi_point_isac_manuscript.md | Conceptual synthesis only. | 2026-07-24 | Inspected |
| S10 | Private integrity and process evidence | Selection and source verification | Private records | One uniform draw; complete-paper gate passed | Public paths intentionally withheld | Local-only evidence; never uploaded. | 2026-07-24 | Verified |

The authors are Shing-Wei Wu, Chao-Yu Chen, and Zilong Liu. The arXiv record reports one version submitted on 2020-03-16. The paper states receipt on 2019-10-15 and acceptance on 2020-02-14. Institutional records list publication in *IEEE Transactions on Information Theory*, volume 67, issue 6, pages 3464-3472, June 2021. No paper-specific official implementation was located in the inspected primary records or targeted public search.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Official arXiv metadata | Title, authors, identifier, submission date, subject, abstract, DOI links, and publisher comment | Source identity and chronology | High | Abstract does not support theorem-level review |
| E2 | S2, S3 | Primary full paper | Definitions, Theorems 3-4, Corollary 5, Examples 1-4, Tables I-II, conclusion, appendices, and references | Construction mechanism, reported existence results, proof strategy, and limitations | High for source reporting | Proofs were not machine-checked or independently reconstructed |
| E3 | S2 | Visual primary evidence | All nine pages, equation layout, tables, footnotes, chronology, and editorial inconsistencies | Layout-sensitive interpretation and cross-checking | High for transcription | Visual review does not prove formal correctness |
| E4 | S4, S5 | DOI and institutional metadata | IEEE venue, volume, issue, pages, article identity, and publication month | Published-record attribution | High | Does not validate technical claims |
| E5 | S7-S9 | Related DEP manuscripts | Quaternary sequence complexity, OTFS receiver geometry, and ISAC allocation/fusion | Cross-DEP synthesis and implementation context | Medium-high | Related artifacts do not validate the selected paper |
| E6 | S6 | Repository authority | Filing, README, attribution, source-withholding, and publication-index rules | Deposit compliance | High | Process evidence only |
| E7 | S10 | Private integrity/process evidence | Candidate enumeration, uniform draw, dedup scan, PDF/HTML checks, bounded repair, and no-source gate | Selection eligibility and source completeness | High | Private records and paths are intentionally withheld |

## Executive Summary

*How to Construct Mutually Orthogonal Complementary Sets with Non-Power-of-Two Lengths?* presents a generalized-Boolean-function route to flexible-length Golay complementary sets and mutually orthogonal complementary sets. An `(M,N,L)` MOCS contains `M` sequence sets, each with `N` sequences of length `L`; the correlation sums cancel off-peak within a set and across distinct sets. The universal bound is `M <= N`, with equality defining a complete complementary code.

Theorem 3 constructs GCSs at lengths `L = 2^(m-1) + 2^t` by partitioning binary variables into ordered chains, forming quadratic GBFs, truncating the associated length-`2^m` sequence, and adding structured linear terms. Theorem 4 organizes these GCSs into MOCSs. Corollary 5 modifies the construction to reach `M = 2^k` and `N = 2^(k+1)`, hence `M/N = 1/2`.

The evidence is formal rather than empirical: worked constructions, existence tables, and appendix proofs use term pairing and Hamming-weight cancellation. The main practical promise is a compact, direct generator for non-power-of-two resource lengths without serial paraunitary-matrix operations. The paper does not supply code, independent proof certificates, hardware measurements, or system metrics.

Reviewer confidence is high that the inspected paper states and supports its construction family. Confidence is medium for proof correctness beyond source inspection and for practical benefit. The half-flock result is an achieved ratio for Corollary 5; the inspected text does not prove that no other non-power-of-two construction can exceed it.

## Detailed Summary

### Problem Context and Vocabulary

For a q-ary sequence, the paper uses aperiodic correlation. A Golay complementary set contains `N` sequences whose summed autocorrelation is zero at every nonzero shift. An MOCS contains `M` such GCSs and additionally requires the summed cross-correlation between any two distinct GCSs to be zero at every shift. The set size is `M`, the flock size is `N`, and the sequence length is `L`.

Existing GBF constructions largely produce power-of-two lengths because a Boolean function on `m` variables naturally enumerates `2^m` binary inputs. Practical multicarrier systems may use other subcarrier counts. The paper asks whether algebraic GBF structure can be retained while moving to flexible lengths and keeping `M` large.

### Generalized Boolean Function Construction

A generalized Boolean function maps binary vectors to `Z_q`, with even `q`. The quadratic core connects variables along `k` partition blocks through block-specific bijections. Linear terms and a constant may be added without changing the construction class.

The associated sequence evaluates the GBF on binary representations of integer indices. To obtain a flexible length, the paper truncates the length-`2^m` sequence to:

`L = 2^(m-1) + 2^t`, with `0 <= t <= m-1`.

The non-power-of-two cases of primary interest use `1 <= t < m-1`; `t = m-1` gives `L = 2^m`, while the conclusion identifies `t = 0` as a further research boundary for the MOCS family.

### Theorem 3: Flexible-Length GCSs

Theorem 3 constructs a GCS with `N = 2^(k+1)` constituent sequences. Each constituent adds `q/2` times a binary selection of the first variable in every chain plus the final variable `x_m`. A prefix condition aligns the ordered chain positions with the truncated binary interval. The proof pairs sequence/index terms so their complex phases differ by `q/2`, causing cancellation at every nonzero shift.

Example 1 uses `q=4`, `m=6`, and `k=2`. It gives an `(8,36)` GCS for `t=2` and an `(8,40)` GCS for `t=3`; the paper states that one earlier Boolean-function construction cannot produce the latter. At `t=0`, the compared constructions coincide on an `(8,33)` GCS.

### Theorem 4: Flexible-Length MOCSs

Theorem 4 adds a family index `p` through offsets at the last variable of selected chains. If `k'` complete partition blocks lie within the truncation prefix, the construction yields:

- set size `M = 2^k'`;
- flock size `N = 2^(k+1)`; and
- length `L = 2^(m-1) + 2^t`.

Example 2 gives a `(2,8,40)` MOCS and, at `t=4`, a `(2,8,48)` MOCS. Theorem 4 expands length availability but may leave `M` far below `N`.

### Corollary 5: Half-Flock Set Size

Corollary 5 introduces a branch term that selects different chain endpoints based on the last binary variable. This raises the family size to `M = 2^k` while keeping `N = 2^(k+1)`, so:

`M/N = 1/2`.

Example 3 constructs a `(4,8,48)` MOCS. Example 4 constructs an `(8,16,48)` MOCS. The proof uses both shift-wise cancellation and a Hamming-weight result: distinct family labels produce a difference sequence with half of its phases contributing `+1` and half `-1`, so the zero-shift cross-correlation also cancels.

### Tables and Scope

Table I compares MOCS existence for set sizes 4, 8, and 16 at selected lengths, showing new non-power-of-two availability relative to a CCC construction. Table II lists even-length `(M,N)` availability for lengths 4 through 40 and separates the ratios attained by Theorem 4 and Corollary 5.

The tables are existence summaries, not benchmarks. They do not measure PAPR, BER, radar ambiguity, code-generation cost, or robustness. The prose below Table I mentions length 18 even though Table I's visible columns omit 18; length 18 appears in Table II.

### Conclusion and Open Boundary

The paper concludes that GBFs can directly generate flexible-length GCSs and MOCSs without serial sequence operations or paraunitary-matrix blocks. It identifies two open directions: extending the available lengths, including the `t=0` boundary for the MOCS result, and determining whether non-power-of-two GBF constructions can achieve a CCC with `M/N = 1`.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Theorem 3 constructs `2^(k+1)`-sequence GCSs of length `2^(m-1) + 2^t` under the stated partition and prefix conditions. | Formal author claim | E2, E3 | Directly stated and supported by Appendix A's cancellation proof; not machine-checked. | High for reporting; medium for independent validity |
| C2 | Theorem 4 organizes flexible-length GCSs into `(2^k', 2^(k+1), 2^(m-1)+2^t)` MOCSs. | Formal author claim | E2, E3 | Directly stated and supported by Appendix B; transcription checked against the rendered equations. | High for reporting; medium for independent validity |
| C3 | Corollary 5 constructs MOCSs with `M/N = 1/2`. | Formal author claim | E2, E3 | The displayed parameters give `M=2^k` and `N=2^(k+1)`; Appendix C addresses mutual orthogonality. | High |
| C4 | Examples 1-4 and Tables I-II demonstrate flexible non-power-of-two existence beyond selected prior GBF/CCC constructions. | Source-supported existence evidence | E2, E3 | Constructive examples support existence; they are not an exhaustive independent comparison of all known methods. | Medium-high |
| C5 | GBF generation is attractive for storage and fast synthesis compared with serial sequence or paraunitary operations. | Author motivation | E2 | Plausible from algebraic form, but no implementation, storage table, latency, or hardware benchmark is supplied. | Medium-low |
| C6 | One-half is the universal maximal set-to-flock ratio for non-power-of-two MOCSs. | Overbroad implication | E2 | Not established by the inspected result. The paper constructs one-half and explicitly leaves `M/N=1` open. | High rejection confidence |
| C7 | Proof-carrying sequence generation can connect formal correlation identities to reproducible system evaluation. | Reviewer interpretation | E2, E5 | A reasonable implementation synthesis requiring independent generator, verifier, and simulator work. | Medium |

## Methodology

- `Research objective`: Select one eligible local arXiv paper uniformly, enforce complete-paper integrity, review it source-first, relate it to exactly three existing DEP entries, and deposit public-safe Black Lake artifacts.
- `Sources inspected`: Verified complete PDF, approved full-paper HTML fallback, arXiv metadata, arXiv and IEEE DOIs, institutional publication records, live Black Lake and Black-Lake-Data READMEs, publication-index rules, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated local PDFs with `rg --files -g "*.pdf"`, collapsed them by parent directory, selected a uniform PowerShell `Get-Random` index, derived `arXiv:2003.06991`, scanned repository artifacts and automation memory for duplicate markers, and searched public primary/institutional sources plus a paper-specific code query.
- `Inclusion criteria`: Sources were included when they identified the work, supplied full-paper definitions/proofs/examples, established publication metadata, defined repository rules, or provided a concrete sequence/wireless/ISAC bridge.
- `Exclusion criteria`: Abstract-only synthesis, source-file redistribution, unverified code, unrelated inventory rows, secondary summaries as technical evidence, and deployment claims without a simulator or hardware evidence were excluded.
- `Analytical approach`: Conceptual, comparative, formal-evidence, implementation, product, safety, and replication analysis.
- `Evidence handling`: Formal author claims are tied to theorem/example/table evidence. Reviewer interpretations and overbroad implications are labeled separately.
- `Uncertainty handling`: Lack of machine-checked proof, absent code, unmeasured system performance, notation conflicts, and source-package unavailability are explicit.
- `Extraction process`: Full-paper HTML was inspected as structured text; the complete PDF was text-extracted for review and all nine pages were rendered and visually inspected.
- `Version control`: arXiv v1, DOI, publication chronology, and date-only source access are preserved.
- `Cross-checking`: Parameter ratios, example tuples, table coverage, introduction notation, and conclusion claims were checked across PDF and HTML.
- `Reviewer stance`: DEP-ready formal paper review, critique, implementation brief, and replication plan.

The uniform draw used 75,780 PDFs and 75,777 unique parent units. Zero-based index 42,505 was accepted on the first draw. Duplicate exclusions, other exclusions, and reselections were zero. The only companion-repository match was a metadata-only inventory row.

The selected unit began `partial`: the 233,143-byte PDF was valid, but full-paper HTML was absent. A bounded publisher-brokered repair preserved the PDF, collected 41,900-byte metadata HTML, and collected a 2,302,873-byte approved full-paper HTML fallback. The final HTML contained 99,316 body characters, three document markers, 51 heading markers, seven paper-structure term classes, no bad marker, and zero partials. The source-package request was rejected when the strict broker refused a changed `/e-print/` to `/src/` redirect; the PDF-plus-HTML completeness gate still passed.

## Scope, Constraints, and Assumptions

- `Scope`: The selected paper's definitions, construction family, formal evidence, examples, tables, limitations, and bounded implementation implications.
- `Temporal boundary`: arXiv v1, the 2021 published record, and repository context inspected on the public-safe run date.
- `Evidence limits`: No code, proof assistant, symbolic derivation, independent sequence generator, or system experiment was reproduced.
- `Assumptions`: The arXiv PDF and approved full-paper HTML represent the same v1 work; institutional records accurately identify the published version.
- `Constraints`: Source locality, no-source-upload, public-safe path/time handling, and simulation-only implementation guidance are mandatory.
- `Out of scope`: Declaring the theorems independently proven, claiming universal optimality, transmitting waveforms, controlling radios, or evaluating classified/proprietary radar systems.
- `Intended use`: DEP preservation, code-generator planning, formal verification backlog, and synthetic communications/radar benchmarking.
- `Audience`: Information-theory researchers, sequence-design engineers, wireless-systems researchers, formal-methods engineers, and Black Lake reviewers.
- `Depth target`: Full manuscript review with implementation and replication paths.
- `Reproducibility boundary`: Source claims are inspectable; independent validity requires a separate generator, exact correlation verifier, and ideally mechanized proof.
- `Operational boundary`: Any waveform use must remain in synthetic or explicitly authorized test environments until regulatory, hardware, and interference review.
- `Data sensitivity`: Public scholarly metadata and synthetic sequence parameters only.

## Observations

- `Observed pattern`: The paper's key move is controlled truncation. It does not abandon the length-`2^m` GBF representation; it chooses a binary prefix whose boundary supports cancellation pairings.
- `Technical implication`: Parameter ordering and bit conventions are part of the proof. A generator that reverses bit significance or block permutations may emit plausible-looking but invalid families.
- `Contradiction or tension`: The introduction's printed `r=N/M` cannot be upper-bounded by one under `M<=N`; later sections consistently use `M/N`.
- `Contradiction or tension`: The abstract's "maximal achievable" wording is not a universal nonexistence theorem; the conclusion still asks whether `M/N=1` is possible.
- `Editorial observation`: The Table I prose cites length 18 while the visible Table I columns do not; Table II includes 18.
- `Open question`: Can the proof be mechanized with a reusable library for GBF sequence families and correlation cancellation?
- `Reviewer hypothesis`: The best engineering value may be resource-grid flexibility rather than a standalone correlation improvement, because non-power-of-two lengths can reduce padding or unused subcarriers.

## Considerations

Formal correlation identities should be separated from system performance. Zero summed aperiodic correlation does not automatically imply lower BER, lower PAPR, better radar ambiguity, resistance to synchronization error, or security. Each target system needs matched comparisons with equal bandwidth, energy, code rate, channel estimation, and receiver complexity.

Numerical verification needs care. Complex roots of unity can create small floating residuals, while exact symbolic arithmetic can become expensive. A trustworthy tool should state whether a certificate is exact, algebraic, or tolerance-based and should preserve the bit-order and indexing conventions that generated it.

Wireless and radar implementations can be dual-use. This artifact stays at synthetic sequence generation and authorized simulation. It provides no live-frequency configuration, interference procedure, target-tracking deployment, or autonomous control path.

Source rights are also distinct from technical reproducibility. The paper and its metadata are publicly locatable, but local copies and renderings remain private. A future reference implementation should publish original code and tests under an explicit license rather than bundling source documents.

## Strengths

- The paper states a precise combinatorial target and supplies explicit construction formulas.
- The result covers a useful family of non-power-of-two lengths while preserving a direct GBF representation.
- Theorems, examples, tables, and appendices create a traceable line from parameters to existence claims.
- Theorem 3 subsumes selected earlier flexible-length GCS results as special cases.
- Corollary 5 gives a simple, interpretable `M/N=1/2` ratio and a proof strategy for zero-shift cross-correlation.
- The construction is compatible with deterministic generation and exhaustive toy-scale verification.

## Weaknesses

- No official reference implementation or executable example suite was located.
- Proofs were not machine-checked, and the paper provides no independent verification artifact.
- The abstract's maximality wording is broader than the clearly demonstrated construction result.
- The introduction contains an `N/M` versus `M/N` inconsistency.
- The Table I prose and visible columns disagree about length 18.
- The paper gives no generator complexity, storage, hardware, PAPR, BER/BLER, radar ambiguity, or synchronization results.
- The length family and prefix/partition conditions do not cover arbitrary non-power-of-two lengths.
- Comparisons with paraunitary and sequence-operation constructions remain qualitative rather than experimentally matched.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release a reference generator | Reproducibility | Parameter-heavy formulas are easy to mistranscribe | Reproducible examples and adoption | Maintenance and licensing | Reproduce every example and table row |
| Add exact correlation certificates | Formal evidence | Floating checks alone can hide convention errors | Auditable construction validity | Symbolic cost at larger sizes | Compare exact and numerical residuals |
| Mechanize Theorems 3-4 and Corollary 5 | Proof assurance | Appendix case splits are intricate | Independent formal confidence | High proof-engineering cost | Proof assistant checks all obligations |
| Clarify ratio and maximality language | Exposition | `N/M` conflicts with `M<=N`; global scope is ambiguous | More precise downstream use | Editorial revision | State construction-specific and universal claims separately |
| Reconcile Tables I-II from code | Evidence quality | Manual tables can drift from formulas | Machine-generated existence catalog | Generator bugs may propagate | Cross-check against independent implementation |
| Benchmark system metrics | Practical transfer | Correlation identities do not establish system gain | Evidence for OFDM/OTFS/ISAC use | Large simulation matrix | Matched energy, bandwidth, channel, and receiver tests |
| Compare broader length families | Research coverage | The current form excludes many lengths | More flexible resource allocation | New mathematics required | Publish coverage and nonexistence results |

## Potential Implementations

### Flexible-Length MOCS Compiler

- `User`: Sequence-design researcher or wireless engineer.
- `Goal`: Generate theorem-conformant q-ary GCS/MOCS families for chosen resource lengths.
- `Core mechanism`: Parse `q,m,k,t`, partitions, permutations, and coefficients; construct GBFs; evaluate truncated sequences; add family offsets.
- `Required inputs`: Public theorem parameters and synthetic configurations.
- `Outputs`: Sequence arrays, `(M,N,L)` metadata, convention manifest, and source locators.
- `Risk controls`: Bounded parameter sizes, no radio output, explicit bit order, and failed generation on unmet prefix conditions.
- `Evaluation`: Match Examples 1-4 and verify every correlation identity.

### Correlation Certificate Engine

- `User`: Formal reviewer or benchmark maintainer.
- `Goal`: Determine whether a generated family satisfies GCS and MOCS identities.
- `Core mechanism`: Compute all required aperiodic auto- and cross-correlation sums with exact cyclotomic arithmetic when feasible and labeled numerical fallback otherwise.
- `Required inputs`: q-ary sequences and their generation manifest.
- `Outputs`: Maximum residual, failed shifts/set pairs, arithmetic mode, and replayable certificate.
- `Risk controls`: Resource caps, tolerance disclosure, deterministic replay, and no certification when source parameters are incomplete.
- `Evaluation`: Mutation tests must detect bit reversal, truncation, coefficient, and permutation errors.

### Multicarrier and ISAC Evaluation Harness

- `User`: OFDM, OTFS, or integrated sensing/communications researcher.
- `Goal`: Test whether flexible-length formal properties improve end-to-end outcomes.
- `Core mechanism`: Insert certified sequences into synthetic matched system models and compare against CCC, prior GBF, and paraunitary baselines.
- `Required inputs`: Public synthetic channels, equalized power/bandwidth settings, receivers, and benchmark configurations.
- `Outputs`: PAPR, BER/BLER, ambiguity, rate, sensing, latency, storage, and failure reports.
- `Risk controls`: Simulation-only default, no live transmitter interface, authorization gate for testbed use, and complete configuration provenance.
- `Evaluation`: Repeated matched trials with uncertainty and explicit infeasibility.

## Three Ways to Exercise This Research

1. `Toy theorem reproduction`: Objective - reproduce one `(M,N,L)` example; inputs - small public parameters from the paper; method - implement GBF evaluation, truncation, and offsets, then enumerate all correlation sums; output - sequence family and residual table; success criterion - the reported tuple and zero identities match; stop condition - any indexing ambiguity or nonzero exact residual.
2. `Independent table audit`: Objective - regenerate the existence rows behind Tables I-II; inputs - bounded ranges of `m,k,t` and partitions; method - enumerate admissible parameter sets with two independently written generators; output - reconciled coverage table and discrepancies; success criterion - both implementations agree and explain the length-18 statement; stop condition - shared code paths or undocumented pruning invalidate independence.
3. `Synthetic system transfer`: Objective - test practical value without live transmission; inputs - certified families, matched CCC/paraunitary baselines, and a public OFDM/OTFS/ISAC simulator; method - equalize bandwidth, power, rate, and receiver assumptions; output - PAPR, BER/BLER, ambiguity, rate, sensing, and cost comparisons; success criterion - confidence intervals and complete configs are published; stop condition - unmatched resources or missing provenance.

## Example MVP Product

- `Product name`: MOCS ProofBench.
- `Target user`: Information-theory researcher, sequence-design engineer, or reproducibility reviewer.
- `Problem`: Paper-derived complementary-code generators are difficult to audit because small indexing mistakes can silently invalidate correlation guarantees.
- `Core workflow`: Select a theorem profile, enter bounded parameters, validate prefix/partition conditions, generate sequences, compute certificates, compare with a known example, and export a public-safe evidence bundle.
- `Data requirements`: Synthetic integer parameters, public theorem metadata, optional user-authored sequence arrays, and no personal or restricted data.
- `Architecture`: Parameter schema and validator; GBF evaluator; truncation and family generator; exact/numerical correlation engine; example registry; certificate renderer; local artifact store.
- `Success metrics`: Reproduction of all four paper examples; zero expected residuals; mutation-test detection; deterministic output; bounded runtime; reviewer comprehension.
- `Risk controls`: No radio-control or waveform-transmission interface; strict size caps; explicit arithmetic mode and tolerance; source-document withholding; authorization gate for any external testbed.
- `Limitations`: It would verify generated instances, not prove the general theorems; large exact checks may be expensive; system benefit requires a separate simulator.
- `MVP boundary`: Local CLI or notebook for toy and moderate sequence families only.
- `Deployment model`: Local-only Python package with JSON and Markdown output.
- `Evaluation plan`: Golden examples, property tests, injected indexing faults, cross-implementation comparison, and human review of certificates.
- `Failure modes`: Incorrect bit significance, invalid partition order, floating cancellation, unbounded parameter growth, and mistaken use of an instance certificate as a universal proof.
- `Maintenance plan`: Version theorem profiles, retain test vectors, pin arithmetic dependencies, and require review for new construction families.

## Related Research and Reading

### Exactly Three Related DEP Entries

1. [4 Adic Complexity](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-4%20Adic%20Complexity/4_adic_complexity_manuscript.md) - reviews interleaved quaternary sequences with optimal autocorrelation and 4-adic complexity, adding a sequence-unpredictability lens to the selected paper's correlation-focused construction.
2. [2D-RC OTFS](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md) - reviews geometry-aware OTFS symbol detection, connecting flexible algebraic signaling to delay-Doppler receiver behavior and BER/BLER evaluation.
3. [Multi-Point ISAC](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Multi-Point%20ISAC/multi_point_isac_manuscript.md) - reviews cooperative sensing/communications allocation, connecting sequence orthogonality to end-to-end power, interference, sensing, and rate tradeoffs.

### Primary and Near-Primary Reading

- Wu, Chen, and Liu, [selected arXiv paper](https://arxiv.org/abs/2003.06991) and [IEEE DOI](https://doi.org/10.1109/TIT.2020.2980818).
- Paterson, [Generalized Reed-Muller codes and power control in OFDM modulation](https://doi.org/10.1109/18.817522), a foundational GBF/Reed-Muller connection cited by the selected paper.
- Chen, [Complementary sets of non-power-of-two length for peak-to-average power ratio reduction in OFDM](https://doi.org/10.1109/TIT.2016.2608899), a direct predecessor cited as part of Theorem 3's lineage.
- Xiao and Cao, [New constructions of mutually orthogonal complementary sets and Z-complementary code sets](https://doi.org/10.1007/s12095-023-00673-z), a later extended-Boolean-function neighbor.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2003.06991 | Identity, authors, date, abstract, subject, version, and public locators | 2026-07-24 | Metadata only |
| R2 | https://arxiv.org/pdf/2003.06991 | Complete paper, equations, examples, tables, conclusion, appendices, and visual review | 2026-07-24 | Verified local copy withheld |
| R3 | https://ar5iv.labs.arxiv.org/html/2003.06991 | Full-paper structured text | 2026-07-24 | Verified local copy withheld |
| R4 | https://arxiv.org/e-print/2003.06991 | Public source-package locator | 2026-07-24 | Redirect rejected by strict broker; no package collected |
| R5 | https://doi.org/10.48550/arXiv.2003.06991 | Persistent arXiv identity | 2026-07-24 | Identifier only |
| R6 | https://doi.org/10.1109/TIT.2020.2980818 | IEEE publication identity | 2026-07-24 | Publisher identifier |
| R7 | https://repository.essex.ac.uk/30464/ | Institutional publication and accepted-version metadata | 2026-07-24 | Near-primary institutional record |
| R8 | https://researchoutput.ncku.edu.tw/en/publications/how-to-construct-mutually-orthogonal-complementary-sets-with-non--2/ | Venue, volume, issue, pages, article number, and publication month | 2026-07-24 | Near-primary institutional record |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository deposition and source-withholding rules | 2026-07-24 | Process authority |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP class and publication-index rules | 2026-07-24 | Process authority |
| R11 | `.lake-data/DEP-E/DEP-E-20260721-4 Adic Complexity/4_adic_complexity_manuscript.md` | Sequence-complexity and autocorrelation synthesis | 2026-07-24 | Related DEP; primary basis `https://arxiv.org/abs/2209.10279` |
| R12 | `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` | OTFS receiver and channel-geometry synthesis | 2026-07-24 | Related DEP; primary basis `https://arxiv.org/abs/2311.08543` |
| R13 | `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` | ISAC fusion, power, rate, and interference synthesis | 2026-07-24 | Related DEP; primary basis `https://arxiv.org/abs/2208.07592` |
| R14 | Private integrity and process records | Selection, dedup, repair, and source verification | 2026-07-24 | Withheld locally; no public path |

## Appendix

### Parameter Glossary

- `q`: Even alphabet modulus.
- `m`: Number of binary variables in the GBF.
- `k`: Number of partition blocks/chains.
- `t`: Truncation parameter.
- `M`: Number of GCS members in the MOCS, called set size.
- `N`: Number of constituent sequences in each GCS, called flock size.
- `L`: Sequence length.
- `k'`: Number of complete partition blocks contained within the truncation prefix used by Theorem 4.

### Replication Checklist

- Pin the paper version, equation transcription, bit order, partition order, permutations, `q,m,k,t`, and linear coefficients.
- Reproduce Examples 1-4 before generating new families.
- Check every nonzero-shift summed autocorrelation within each set.
- Check every shift, including zero, for cross-correlation between distinct sets.
- Record exact versus numerical arithmetic and any tolerance.
- Regenerate Tables I-II from code and reconcile editorial discrepancies.
- Compare with independent implementation and mutation tests.
- Add matched OFDM/OTFS/ISAC evaluation only after formal instance verification passes.

### Selection and Dedup Record

The run enumerated 75,780 PDFs and 75,777 unique PDF-parent units. A uniform PowerShell `Get-Random` draw selected zero-based index 42,505. The first draw was accepted. Duplicate exclusions, other exclusions, and reselections were zero. Searches covered arXiv ID, arXiv DOI, IEEE DOI, normalized title, slug, processed artifact paths, automation memory, relevant companion-repository entries, and same-paper markers within 24 hours.

### Source Integrity Record

Initial state was partial: the existing PDF passed size, header, EOF, and hash checks, while full-paper HTML was missing. A bounded v4 publisher-brokered repair collected metadata HTML and an approved full-paper HTML fallback. Final state was complete with valid PDF, 2,302,873-byte HTML, 99,316 body characters, three document markers, 51 heading markers, seven paper-structure term classes, no error/abstract-only marker, and zero partials. A strict redirect-policy rejection prevented source-package collection but did not affect the complete-paper gate.

### Source-Withholding Confirmation

No PDF, HTML, metadata page, source archive, extracted text, cache, rendering, private verification record, local archive path, or `.source/` directory is included. Only generated public-safe Markdown, the public dedup pointer, and public source URLs are deposited.
