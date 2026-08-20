---
title: "SAILFISH Review - DEP-E"
generated_at: "2026-07-13 (public date-only marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "A source-first review of SAILFISH, a staged static and symbolic analyzer for smart-contract state-inconsistency bugs."
source_status: "Local primary PDF inspected; public URLs preserved; no source files deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-13"
temporal_cutoff: "2026-07-13"
primary_url: "https://arxiv.org/abs/2104.08638"
stable_identifier: "arXiv:2104.08638v2; DOI:10.1109/SP46214.2022.9833721"
confidence_summary: "High for paper content and metadata; medium for reproducibility and present-day compatibility because released artifacts were not executed."
safety_scope: "Defensive security review with bounded, non-exploitative implementation examples"
distribution_notes: "Generated analysis only; source-file redistribution rights were not assumed."
---

# SAILFISH Review - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Note | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | SAILFISH paper | Primary artifact | Local PDF plus author-hosted PDF | arXiv:2104.08638v2 | https://fredfeng.github.io/papers/sailfish.pdf; local path omitted from public artifact | Paper used for review; no file redistributed | 2026-07-13 | Full text inspected |
| S2 | arXiv record | Primary metadata | HTML | 2104.08638v2 | https://arxiv.org/abs/2104.08638 | arXiv record exposes its license link; no source downloaded for deposition | 2026-07-13 | Inspected |
| S3 | IEEE conference record | Version-of-record metadata | DOI / proceedings page | 10.1109/SP46214.2022.9833721 | https://doi.org/10.1109/SP46214.2022.9833721 | Publisher terms apply | 2026-07-13 | Metadata inspected |
| S4 | UCSB SecLab publication page | Institutional metadata | HTML | IEEE S&P 2022 publication | https://seclab.cs.ucsb.edu/publications/priyanka_sailfish_22/ | Public institutional page | 2026-07-13 | Inspected |
| S5 | `ucsb-seclab/sailfish` | Official implementation and data | Git repository / README | `master`, public state on access date | https://github.com/ucsb-seclab/sailfish | README documents code/data and Docker use; repository license visibility was not established in this review | 2026-07-13 | README and tree inspected; code not executed |
| S6 | Antaeus DEP entry | Related Black-Lake-Data artifact | Markdown plus primary arXiv abstract | DEP-20260702-Tech Intel 1102; arXiv:2607.01138v1 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260702-Tech%20Intel%201102/daily_research_findings_2026-07-02_1102.md | Related context only | 2026-07-13 | DEP and primary abstract inspected |
| S7 | Chai DEP entry | Related Black-Lake-Data artifact | Markdown plus primary arXiv abstract | DEP-20260626-Tech Intel 1103; arXiv:2606.26933v1 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260626-Tech%20Intel%201103/daily_research_findings_2026-06-26_1103.md | Related context only | 2026-07-13 | DEP and primary abstract inspected |
| S8 | VeriChat DEP entry | Related Black-Lake-Data artifact | Markdown plus primary arXiv abstract | DEP-20260706-Tech Intel 0104; arXiv:2607.01668v1 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260706-Tech%20Intel%200104/daily_research_findings_2026-07-06_0104.md | Related context only | 2026-07-13 | DEP and primary abstract inspected |

**Paper identity.** *SAILFISH: Vetting Smart Contract State-Inconsistency Bugs in Seconds* is authored by Priyanka Bose, Dipanjan Das, Yanju Chen, Yu Feng, Christopher Kruegel, and Giovanni Vigna. arXiv records initial submission on 2021-04-17 and revision v2 on 2021-12-13. The conference version appeared in the 2022 IEEE Symposium on Security and Privacy, pages 161-178.

**Source collection note.** One local archive PDF and adjacent metadata README were inspected. Public-safety rules prohibit publishing the local path, and no original file was copied into this DEP. The official implementation repository advertises code and experimental data; its artifacts were not executed or repackaged.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary paper | Abstract, definitions, algorithms, implementation, evaluation tables, ablation, limitations, appendices | C1-C6; system mechanism; metrics; boundaries | High | PDF extraction contains typography/symbol noise; experiments not rerun |
| E2 | S2 | Primary metadata | Authors, dates, version, subjects, journal reference, arXiv DOI | Identity and version claims | High | Abstract alone is not treated as proof of empirical claims |
| E3 | S3 and S4 | Publisher/institutional metadata | Venue, pages, DOI, author and publication confirmation | Publication identity | High | Does not validate experimental results |
| E4 | S5 | Official repository | Repository purpose, code/data tree, Docker installation, example command, test cases | Public release and documented workflow | High for availability; medium for usability | No release execution, environment build, data audit, or license audit |
| E5 | S6 plus https://arxiv.org/abs/2607.01138 | Related DEP and primary abstract | Function prioritization, repository context, comparative validation, evidence-linked findings | Conceptual comparison to staged security triage | Medium | New preprint; used only as related context |
| E6 | S7 plus https://arxiv.org/abs/2606.26933 | Related DEP and primary abstract | Differential signals and dependency-graph propagation for cryptographic misuse | Conceptual comparison to graph-guided discovery | Medium | New preprint; used only as related context |
| E7 | S8 plus https://arxiv.org/abs/2607.01668 | Related DEP and primary abstract | Agent workflow integrated with simulation and formal-verification tools | Conceptual comparison to hybrid assurance | Medium | New preprint; used only as related context |
| E8 | Public cache summary derived from local extraction | Processing record | `pypdf`, 117,020 PDF-text bytes, partial status, missing HTML/source text | Review reproducibility and extraction limits | High | Cache itself is local infrastructure and is not deposited |

## Executive Summary

SAILFISH is a static smart-contract analyzer designed to find state-inconsistency bugs without exhaustively symbolically executing an entire contract. The paper's central systems move is to separate broad discovery from precise checking. EXPLORE builds a storage dependency graph and queries it for *hazardous access* pairs: public-reachable operations on the same storage state where at least one operation writes. REFINE then symbolically evaluates only the relevant program slice, using a domain-specific value-summary analysis to constrain storage values and eliminate infeasible candidates.

The authors evaluate 89,853 deduplicated Solidity contracts collected from Etherscan through 2020. They report an average 30.79-second analysis time, fewer warnings than five comparator analyzers, all 136 manually labeled vulnerabilities found in a 750-contract subset, and 47 previously unknown exploitable contracts among a tractability-filtered manual review of SAILFISH-only findings. The VSA ablation is strong internal evidence: warning counts fall beyond a havoc-based symbolic-refinement baseline, while path-by-path summaries time out on 21.50% of a 2,000-contract comparison subset.

The reviewer's confidence is high that the paper describes a coherent and useful staged-analysis design and reports the stated historical results. Confidence is only medium that the released system reproduces those results today or transfers directly to modern Solidity, proxy-heavy architectures, and newer Slither versions. The code/data repository is public and documents Docker-based use, but this run did not build the environment, execute benchmarks, or audit corpus labels. The paper also explicitly disclaims soundness and identifies semantic and dependency-level sources of missed detections and false positives.

Practical relevance lies in the architecture, not in treating one historical tool as a current certification engine. Candidate compression, traceable intermediate representations, and precise second-stage validation recur in Antaeus, Chai, and VeriChat, suggesting a general pattern for security systems that must balance recall, triage cost, and evidence quality.

## Detailed Summary

### Problem and Background

Ethereum smart contracts expose multiple public entry points and maintain persistent state. An adversary can influence execution through callbacks inside a transaction or by manipulating transaction order across the mempool/mining process. A correct static analyzer must therefore reason not only about local syntax but about how multiple public methods and transactions interact through shared storage.

The paper frames two common state-inconsistency mechanisms. A *stale read* occurs when an attacker causes a storage value to be read before the victim flow performs its intended update. A *destructive write* occurs when the attacker changes storage before the victim flow reads it. Reentrancy and TOD can both instantiate these mechanisms. The destructive-write reentrancy pattern is presented as an underexplored case that common single-function or write-after-call signatures miss.

Existing static tools in the paper's comparison face a precision/scalability tradeoff. Syntax- or pattern-based tools over-approximate and emit many false positives; whole-program symbolic exploration encounters path explosion; dynamic tools see only executed attacks and are unsuitable as comprehensive pre-deployment screens. Cross-function calls, attacker-controlled external destinations, and arbitrary public-method order make naive modeling especially costly.

### Formal Object

SAILFISH defines a contract state as storage variables plus contract balance and models external public-function invocations as events. Two schedules begin from the same initial state. If an adversarial schedule transformation—reentrant invocation or transaction reordering—produces a different final state, the contract has a state-inconsistency bug under the paper's definition. Reentrancy and generalized TOD are distinguished by the schedule transformation used.

This definition is useful because it moves beyond an isolated opcode pattern. It asks whether attacker-influenced control or ordering changes the persistent outcome. The implementation does not decide full semantic equivalence directly; it operationalizes the definition through hazardous-access queries and symbolic refinement.

### EXPLORE: Storage Dependency Graph

EXPLORE uses Slither to lift Solidity into an intermediate representation and obtain interprocedural control-flow, data-flow, and taint facts. It builds an SDG whose nodes are storage variables or statements operating on them. Edges represent data dependence from storage to statements, writes from statements to storage, and ordering relations among statements. Datalog rules derive the graph and connect external calls to public entry points so cross-function reentrancy can be considered.

A hazardous-access pair contains two public-reachable operations over the same storage location with at least one write. Additional queries determine whether the pair can participate in reentrancy or one of three TOD forms involving transfer conditions, amounts, or receivers. Taint analysis restricts external calls to destinations that may be attacker-controlled, and owner-only modeling avoids treating some administratively guarded paths as public attack surfaces.

If no query match exists, EXPLORE reports no candidate under its model. If matches exist, the system produces a minimal relevant control-flow slice for refinement. The graph intentionally over-approximates and does not retain all path conditions, so a returned candidate is not yet a confirmed feasible execution.

### REFINE: VSA-Guided Symbolic Evaluation

REFINE symbolically evaluates the candidate slice with Rosette and an SMT solver. A naive approach would treat every storage value as unconstrained at the external-call boundary, allowing infeasible reentrant paths and generating false positives. SAILFISH instead computes a contract-wide value summary that maps storage variables to possible symbolic values paired with preconditions.

VSA is deliberately domain-specific and approximate. It preserves branch-conditioned symbolic values through a union-like merge, but havocs attacker-controlled arguments, external-call returns, variables written in loops, and hard-to-model operations. Arrays and mappings receive weak updates that merge values across indices/keys. These choices sacrifice precision in complex cases to keep summary generation and solver application tractable.

The mutex example illustrates the value. EXPLORE sees hazardous access and a possible reentrant route. VSA records that changing the mutex through public flows requires it to be false. At the external call, the actual symbolic state has the mutex set to true, making the candidate path infeasible. REFINE can then reject the alarm without symbolically exploring unrelated whole-contract paths.

### Implementation

The Explorer is built on Slither and uses its intermediate representation and taint analysis. The Refiner is implemented in Rosette and can use SMT solvers such as CVC4. The official repository now exposes Python, Racket, Solidity test cases, Docker configuration, code, and data. Its README recommends a prebuilt Docker image, documents a `contractlint.py` entry point, and shows range- and havoc-mode examples. Those facts establish artifact availability, not contemporary compatibility or reproduced results.

### Evaluation Design

The authors collected 91,921 Etherscan contract sources through 2020-10-31, excluded 2,068 contracts requiring Solidity versions earlier than 0.3.x or using Vyper, and deduplicated to 89,853 Solidity contracts. They stratified the corpus into small (73,433 contracts under 500 lines), medium (11,730 contracts from 500 to under 1,000 lines), and large (4,690 contracts at least 1,000 lines). Experiments ran on six 40-core, 256-GB Ubuntu machines with a 20-minute per-contract timeout.

Comparators were Securify, Vandal, Mythril, Oyente, and Sereum where each supported the relevant class. The paper records safe, unsafe, timeout, and error separately. This is important because apparent warning rate cannot be interpreted without tool coverage, compiler support, and failure counts.

For ground truth, the authors randomly sampled 750 contracts up to 3,000 lines from 6,581 contracts successfully processed by all five static analyzers. Manual inspection labeled 26 reentrancy and 110 TOD cases. For zero-day exploration, the authors selected 88 of 401 SAILFISH-only reentrancy warnings and 107 of 721 SAILFISH-only TOD warnings, restricting attention to contracts of at most 500 lines for manual tractability.

### Reported Results

Across the full corpus, SAILFISH reports 2,076 reentrancy warnings, 1,211 timeouts, and 3,395 errors; for TOD it reports 7,555 warnings with the same timeout/error counts. On successfully analyzed contracts, the paper reports warning rates of 2.40% for reentrancy and 8.74% for TOD, lower than the compared static tools in their supported configurations.

On the 750-contract manually labeled subset, SAILFISH reports all 26 reentrancy and 110 TOD true positives with zero false negatives, plus 11 and 59 false positives respectively. These are author-produced labels, not an independent blinded replication. The paper explains false positives through imprecise taint and insufficient application-semantic reasoning.

The authors report 47 exploitable contracts among the 195 selected SAILFISH-only candidates: 11 allow Ether draining and 36 allow at least persistent application-metadata corruption. This is meaningful evidence that the detector found nontrivial patterns, including cross-function and delegate-based reentrancy, but the selection restriction prevents interpreting 47/195 as an unbiased population estimate.

Mean analysis time is reported as 30.79 seconds over the full corpus, with 9.80, 80.78, and 246.89 seconds for small, medium, and large groups. The reported mean static-analysis component is 21.74 seconds, symbolic evaluation 39.22 seconds for applicable candidates, and VSA generation 0.06 seconds. Different component populations mean these figures should not be naively summed as an overall mean.

### Ablation and Summary Tradeoff

The static-only configuration emits 3,391 reentrancy and 14,485 TOD warnings. Adding symbolic refinement while havocing state reduces counts to 2,436 and 10,560. Adding VSA reduces them again to 2,076 and 7,555, a reported 14.78% and 28.46% improvement relative to havoc refinement. Warning reduction is not identical to proven precision improvement, but the manually inspected examples and ground-truth subset make the direction plausible.

When the authors replace VSA with path-by-path summaries on 2,000 medium/large contracts that VSA can process, the path-summary variant times out on 21.50%. This supports the design premise that a cheaper, deliberately lossy summary can be more useful than a precise but solver-heavy representation.

### Limitations and Conclusion

SAILFISH requires source code through its Slither implementation, although the authors argue that the conceptual analysis could be ported to a decompiler. It does not claim soundness. Unmodeled exception propagation, transaction reversion, out-of-gas behavior, unresolved or indirect calls, inline assembly, external destination resolution, and Slither call-graph/taint gaps can produce missed detections or false positives. VSA's loop havoc and weak collection updates add further approximation.

The paper concludes that staged static exploration plus VSA-guided symbolic refinement offers a workable precision/scalability point for state-inconsistency detection. This review accepts that conclusion as well-supported within the reported historical environment, while withholding any claim of present-day production readiness or independent reproduction.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Hazardous access unifies stale-read and destructive-write causes across reentrancy and TOD. | Author conceptual claim | E1 definitions, examples, and SDG queries | Coherent operational abstraction; it is not a complete semantic characterization of all contract bugs. | High |
| C2 | SDG exploration plus candidate slicing reduces the symbolic search surface. | Author mechanism claim | E1 Sections V-VI and architecture | Directly supported by system design; exact reduction magnitude is not separately quantified. | High |
| C3 | VSA improves refinement beyond unconstrained/havoc symbolic checking. | Author empirical claim | E1 ablation: 2,436 to 2,076 reentrancy and 10,560 to 7,555 TOD warnings | Strong internal ablation, though warning reduction should be paired with more independent labels. | Medium-high |
| C4 | SAILFISH averages 30.79 seconds and compares favorably with the selected analyzers. | Author empirical claim | E1 Table IV and performance discussion | Supported in the historical cluster/tool environment; present-day replication not performed. | Medium-high |
| C5 | SAILFISH found all 136 manually labeled vulnerabilities and 47 previously unknown exploitable contracts. | Author empirical claim | E1 Tables II-III, manual-analysis and appendix discussion | Substantial evidence, but labels and zero-day selection were author-produced and partially tractability-filtered. | Medium |
| C6 | The released repository makes code and experimental data available. | Artifact fact | E4 repository tree and README | Availability confirmed; license, build success, corpus completeness, and result reproduction not verified. | High for availability; low-medium for reproducibility |
| C7 | The staged pattern generalizes to other security assurance systems. | Reviewer interpretation | E5-E7 conceptual comparison | Useful design inference, not a claim established by the SAILFISH experiments. | Medium |

## Methodology

- `Research objective`: Preserve an evidence-grounded review of SAILFISH's problem framing, staged mechanism, empirical support, limitations, reproducibility state, and implementation relevance in a DEP-ready artifact.
- `Sources inspected`: Local primary PDF and adjacent metadata; public arXiv record; author-hosted PDF; IEEE DOI and UCSB SecLab publication pages; official code/data repository; three Black-Lake-Data entries; and the three primary arXiv abstracts cited by those entries.
- `Discovery strategy`: Enumerate unique PDF parent directories with `rg --files -g "*.pdf"`; select one uniform random index with `Get-Random`; derive the arXiv ID from filename/metadata; inspect cached full text by section and table; verify publication/code metadata from primary pages; search both repositories for conceptually overlapping DEP entries without a fixed related-entry index.
- `Inclusion criteria`: Primary paper sections bearing on definitions, method, evaluation, limitations, release claims, and reproduction; official metadata/artifacts; related entries with concrete overlap in staged security reasoning, graph propagation, or precise verification.
- `Exclusion criteria`: Secondary summaries as technical evidence; unrelated keyword matches; exploit operationalization; source redistribution without established permission; repository popularity as a quality signal.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety-and-ethics, product-research, and replication review.
- `Evidence handling`: Major claims map to E1-E8; author claims, artifact facts, and reviewer interpretations are labeled separately; quantitative values are attributed and not presented as reproduced.
- `Uncertainty handling`: Missing execution evidence, historical toolchain constraints, extraction noise, unsoundness, and related-preprint maturity are stated explicitly.
- `Extraction process`: Required extractor preflight found `pypdf` available and `pdftotext` unavailable. A `missing-only` extraction converted an initial miss into a partial cache with 117,020 bytes of PDF text; no local HTML or source-package text existed.
- `Version control`: The paper is pinned to arXiv v2 and the IEEE DOI. Repository state is identified by public URL and access date rather than an unverified release tag.
- `Claim selection`: Prioritized architecture, ground-truth design, benchmark population, timeout/error accounting, ablation, zero-day selection, explicit limitations, and release availability.
- `Cross-checking`: Paper identity and dates were checked against arXiv, venue metadata against DOI/institutional records, release claims against the official repository, and related-entry claims against cited primary abstracts.
- `Safety handling`: All examples are defensive, local-only, synthetic, and non-exploitative. No malicious contract, transaction, payload, or live target is produced.
- `Reviewer stance`: Combined paper report, critique, implementation translation, DEP preservation, and replication planning.

### Random Selection Methodology

The archive contained 75,761 unique PDF-backed parent-directory paper units. One complete list was enumerated, a uniform zero-based random index from 0 through 75,760 was generated, and index 8,874 selected this paper. The first draw passed eligibility, so exclusions and reselections were both zero. This design gives every enumerated paper unit equal selection probability regardless of the number of PDFs inside the unit.

### Cache Methodology

Cache lookup preceded synthesis. The selected arXiv ID had no prior central-cache record. `extract-arxiv` ran in `missing-only` mode against the selected paper unit, extracted PDF text through `pypdf`, preserved public-safe summary fields, and did not overwrite an existing output. Because full PDF text was available, network use was limited to primary metadata, author, venue, official-code, and related-paper records rather than paper-body backfill.

### Dedup and Reselection Validation

Before acceptance, scans covered `.staging/arxiv-dep-dedup-index.json`, Black Lake `.logs`, `.reports`, and `.lake-data`, automation memory, Black-Lake-Data, and active worktree markers. The checks used arXiv ID, publisher DOI, normalized title, and slug. No prior Arxiv DEP or same-paper marker within 24 hours was found. The selected paper was therefore accepted without reselection.

## Scope, Constraints, and Assumptions

- `Scope`: Review SAILFISH's definitions, EXPLORE/REFINE architecture, implementation dependencies, reported empirical evidence, explicit limitations, released-artifact availability, and defensive downstream uses.
- `Temporal boundary`: Sources were accessed through 2026-07-13; the evaluated contract corpus ends on 2020-10-31 and the paper is pinned to arXiv v2 / IEEE S&P 2022.
- `Evidence limits`: Code, Docker image, dataset, solver environment, and experiments were not executed. The PDF extraction contains minor encoding noise. No independent ground-truth labels were obtained.
- `Assumptions`: The local PDF corresponds to arXiv:2104.08638v2 based on filename, embedded version text, title/authors, and public metadata. Repository documentation accurately describes its intended run path, but not necessarily present operability.
- `Constraints`: Public artifacts omit local paths, exact timestamps, machine identity, and local timezone. Redistribution rights were not assumed. Security content remains defensive.
- `Out of scope`: Producing exploit contracts or transactions; scanning live contracts; certifying smart contracts; formally proving SAILFISH sound; auditing every repository file; reproducing the entire Etherscan experiment.
- `Intended use`: Research review, DEP preservation, analyzer design, replication planning, and defensive product ideation.
- `Audience`: Security researchers, static-analysis engineers, smart-contract auditors, verification engineers, and agent-system designers interested in staged assurance.
- `Depth target`: Full manuscript report with schema-complete evidence, methodology, critique, and implementation translation.
- `Reproducibility boundary`: Source identity and paper content are reproducible from public records; benchmark results remain author-reported until the released artifacts and corpus are rerun.
- `Operational boundary`: The artifact may describe detection mechanisms and toy defensive checks but does not provide offensive automation.
- `Data sensitivity`: Public research and repository content; no private contract data or credentials.

## Observations

- `Observed pattern`: The SDG is valuable not merely as a graph but as a provenance-bearing compression layer. It tells the refiner and reviewer which storage relation caused a candidate to exist.
- `Technical implication`: Analyzer pipelines should benchmark intermediate candidate quality, not only final precision/recall. A poor first-stage representation can either overwhelm refinement or erase recall before precision tools run.
- `Observed pattern`: VSA's success comes from intentionally not being maximally precise. It keeps branch/value relationships that matter to this domain and abandons expensive precision around loops, calls, and collections.
- `Contradiction or tension`: The paper motivates pre-deployment analysis, yet its evaluation and inter-contract discussion also draw on deployed-contract transactions and source databases to resolve destinations. Deployment mode affects evidence availability and should be reported explicitly.
- `Contradiction or tension`: Zero false negatives on one 750-contract sample coexists with an explicit unsoundness disclaimer and known call-graph/semantic gaps. The sample result should not be generalized to universal recall.
- `Open question`: How much of the reported advantage survives current Solidity semantics, widespread proxies, Yul/assembly, compiler-generated behavior, and modern analyzers?
- `Reviewer hypothesis`: Pairing graph candidates with independently checkable counterexample constraints or differential execution could improve reviewer trust even when complete soundness is impractical.

## Considerations

Adoption requires explicit compiler and dependency compatibility. Slither, Solidity, Rosette, solver, and Docker versions should be pinned, and unsupported constructs must fail visibly rather than silently reducing coverage. Proxy resolution, delegate calls, inheritance, library linking, and constructor/runtime differences need test fixtures.

Evaluation should separate four outcomes: no candidate under the model, infeasible candidate rejected, feasible vulnerability candidate, and analyzer failure/unknown. Treating failures as safe would be dangerous. Dashboards should preserve timeouts, parse errors, unresolved destinations, and summary havoc events as first-class uncertainty indicators.

Operational use should remain a review aid rather than a deployment gate until modern calibration exists. Findings can affect high-value financial contracts; false negatives carry direct loss risk, while false positives consume scarce audit attention. Human reviewers need source slices, graph relations, path constraints, analyzer versions, and clear confidence labels.

The official dataset may contain vulnerable contract source and exploitability annotations. Any reuse should review licensing, disclosure history, and whether identities were intentionally redacted. This DEP does not copy such material.

The related systems also caution against substituting generative reasoning for evidence. Antaeus adds structured reporting and comparative validation; Chai uses naturally occurring differential signals; VeriChat invokes formal tools. A modern SAILFISH-inspired system should similarly make expensive or learned stages subordinate to inspectable program facts and bounded validators.

## Strengths

- The paper gives a behavior-oriented definition of state inconsistency and connects it to implementable graph queries rather than relying only on syntactic signatures.
- The EXPLORE/REFINE separation is technically legible: lightweight over-approximation preserves candidates, while symbolic feasibility checks spend precision selectively.
- VSA is motivated by an explicit systems tradeoff and supported by both an ablation against havoc refinement and a scalability comparison against path-by-path summaries.
- The evaluation is unusually large for its time and reports timeouts/errors rather than hiding analyzer failures.
- The manually labeled subset distinguishes true positives, false positives, and false negatives for both reentrancy and TOD.
- Appendices expose real false-positive mechanisms, zero-day patterns, inter-contract reasoning, and owner-only heuristics, which helps reviewers understand where precision comes from and fails.
- Code and data were released with a Docker-oriented workflow and test cases, providing a plausible starting point for replication.

## Weaknesses

- Ground truth and zero-day validation were produced by the authors; no independent blinded annotation or inter-rater agreement is reported in the inspected text.
- The 47 zero-day result comes from a size-restricted manual selection of SAILFISH-only warnings, so it does not estimate prevalence or overall precision without selection-bias caveats.
- The corpus and tool versions are historical. Many comparison tools had compiler-support failures or severe timeouts, complicating a clean capability comparison.
- The paper does not claim soundness, and important Solidity/EVM behaviors are abstracted or delegated to Slither. Zero false negatives on the sample therefore cannot establish recall guarantees.
- Weak updates for collections and havoc for loops/external returns can hide useful invariants or create false positives; the empirical effect of each approximation is not isolated.
- The repository documentation exposes a runnable route but does not, from the inspected README alone, provide a table-to-command reproduction manifest, current compatibility statement, or clearly visible license.
- Reported component times apply to different candidate populations and are easy to misinterpret without a precise accounting diagram.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Rebuild a current stratified corpus with independent dual annotation | Evaluation | Historical contracts and author labels limit transfer | Modern precision/recall estimates with disagreement data | High annotation cost; disclosure sensitivity | Pre-register sampling, adjudication, and confidence labels |
| Add compiler/proxy/assembly compatibility fixtures | Front end | Modern contracts use constructs outside the original environment | Visible coverage boundaries and fewer silent misses | Large version matrix | CI across pinned Solidity/Slither versions and synthetic fixtures |
| Emit proof-carrying candidate bundles | Refinement / UX | Reviewers need more than a vulnerability label | Auditable storage pair, call boundary, slice, constraints, and unknowns | Serialization and solver-trace complexity | Human audit study and deterministic bundle replay |
| Measure each abstraction independently | VSA / soundness | Loop havoc, weak collections, and external calls have different effects | Actionable precision/recall engineering | Requires curated microbenchmarks | Ablations per construct plus mutation tests |
| Add differential execution for bounded witnesses | Validation | Symbolic feasibility does not by itself show persistent impact | Stronger confirmation on authorized toy/private test environments | Execution-environment modeling risk | Compare symbolic candidates to deterministic local traces |
| Publish an artifact manifest tied to every table | Reproducibility | Repository presence is weaker than result traceability | One-command or staged reproduction with expected hashes | Maintenance burden | Fresh-machine reproduction and artifact-evaluation checklist |

## Potential Implementations

1. **Pull-request storage-risk review.** `User`: smart-contract developer or auditor. `Goal`: identify newly introduced hazardous-access relations before merge. `Core mechanism`: build a diff-scoped SDG, compare it with the base revision, and refine only new cross-function candidates. `Required inputs`: authorized source, compiler metadata, dependency lockfiles. `Outputs`: source slices, storage relations, feasibility status, and explicit unknowns. `Risk controls`: local execution, no live-chain interaction, fail-closed on unsupported syntax, human approval. `Evaluation`: labeled regression fixtures across compiler/proxy patterns.
2. **Analyzer calibration laboratory.** `User`: security research team. `Goal`: compare SAILFISH-style staged analysis with current analyzers on a controlled corpus. `Core mechanism`: normalize outputs, record errors/timeouts, and route disagreements into human adjudication or bounded validators. `Required inputs`: public/synthetic contracts, pinned containers, label protocol. `Outputs`: per-tool precision/recall, failure taxonomy, cost curves, and evidence bundles. `Risk controls`: no deployment claims, independent labels, license review. `Evaluation`: pre-registered sampling and repeated runs.
3. **State-invariant teaching sandbox.** `User`: security educator or new auditor. `Goal`: teach stale read, destructive write, reentrancy, TOD, and summary-guided refinement without real targets. `Core mechanism`: synthetic contracts and graph visualizations that let users change ordering, locks, and storage relations. `Required inputs`: bundled toy examples. `Outputs`: state diffs, hazardous pairs, and explanation traces. `Risk controls`: no mainnet addresses, no exploit broadcasting, bounded simulations. `Evaluation`: learner ability to explain false-positive pruning and boundary conditions.

## Three Ways to Exercise This Research

1. **Reproduce a mutex false-positive prune:** Objective: verify the qualitative VSA mechanism on a synthetic contract. Inputs: the repository's non-reentrant test case or an equivalent toy fixture, pinned local container, and no networked chain. Method: run static-only, havoc-refinement, and range/value-summary modes; compare candidate and final outputs. Output: a three-mode evidence bundle. Success criterion: the staged modes differ for the expected documented reason. Stop condition: any dependency mismatch or unexplained result is recorded rather than bypassed.
2. **Build a ten-contract compatibility matrix:** Objective: measure version sensitivity without claiming population performance. Inputs: ten public toy contracts spanning locks, cross-function writes, TOD, proxies, and unsupported assembly across selected compiler versions. Method: compile and analyze each fixture under pinned toolchains, recording parse, graph, refinement, timeout, and unknown status. Output: a version-by-fixture matrix. Success criterion: every outcome is reproducible and unsupported cases are explicit. Stop condition: do not test live financial contracts or deploy findings.
3. **Audit the evidence chain for one reported table:** Objective: determine whether the released artifacts connect a paper metric to exact inputs and commands. Inputs: official repository, one table, Docker instructions, and data manifest. Method: trace README commands, corpus files, configurations, output parsers, and expected aggregates without modifying sources. Output: a replication gap list and proposed manifest. Success criterion: each table cell is either reproducibly derived or marked with a specific missing link. Stop condition: licensing or data-provenance ambiguity prevents further use.

## Example MVP Product

- `Product name`: StateSlice Review Lab.
- `Target user`: Smart-contract security engineers evaluating source changes in authorized repositories.
- `Problem`: Whole-program symbolic analysis is expensive, while signature-only warnings are noisy and difficult to audit.
- `Core workflow`: Import a pinned local project; compile with declared versions; construct storage-access and control/data-flow facts; show hazardous-access pairs introduced by a diff; run bounded refinement on selected candidates; export an evidence bundle with source slices, constraints, tool versions, and unknowns.
- `Data requirements`: User-authorized source, compiler manifests, dependency locks, and bundled synthetic regression fixtures. No private chain keys, transaction signing, or live exploit targets.
- `Architecture`: Local CLI plus browser UI; compiler adapter; Slither-compatible graph extractor; immutable candidate ledger; bounded symbolic/differential validator; static report generator. Every adapter emits coverage and failure metadata.
- `Success metrics`: Reproducible output hashes on fixtures; candidate recall on independently labeled synthetic cases; precision after refinement; median and tail latency; timeout/error visibility; reviewer time-to-triage; percentage of findings with complete evidence bundles.
- `Risk controls`: Local-only default; no transaction broadcast; no secret logging; explicit authorization banner; synthetic demo data; fail-closed unsupported constructs; human review before any security conclusion; clear non-certification language.
- `Limitations`: An MVP cannot establish soundness, resolve every proxy/inter-contract target, model all EVM behavior, or infer exploitability/business impact automatically.
- `MVP boundary`: Diff-scoped Solidity source and synthetic fixtures only; no live-chain scanning, bytecode-only analysis, automated disclosure, or remediation commits.
- `Deployment model`: Local CLI and loopback web interface in a pinned container.
- `Evaluation plan`: Smoke tests for each supported compiler; mutation tests for storage/call relations; blinded review of a small independent fixture set; deterministic replay; security review of file handling.
- `Failure modes`: Unsupported syntax silently omitted, stale compiler metadata, wrong external-call resolution, solver timeout interpreted as safe, collection abstraction masking an invariant, or UI suppressing uncertainty.
- `Maintenance plan`: Versioned compatibility matrix, monthly dependency review, fixture additions for each parser/refiner incident, immutable result schema, and periodic independent label audits.

Illustrative safe interface:

```text
stateslice review --project ./authorized-toy-project --base main --head feature
  -> candidates.json
  -> refinement.json
  -> coverage-and-unknowns.md
```

This is a product interface sketch, not an assertion that the command exists.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| SAILFISH official repository | Official implementation | Code, data, Docker path, and test fixtures for replication | https://github.com/ucsb-seclab/sailfish |
| Antaeus DEP entry | Related Black-Lake-Data entry | Candidate prioritization plus context-grounded validation for repository-level logic bugs | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260702-Tech%20Intel%201102/daily_research_findings_2026-07-02_1102.md |
| Antaeus primary record | Primary preprint | Verifies the related entry's repository-scale staged pipeline and reported evaluation scope | https://arxiv.org/abs/2607.01138 |
| Chai DEP entry | Related Black-Lake-Data entry | Graph propagation and validation of semantic vulnerability signals | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260626-Tech%20Intel%201103/daily_research_findings_2026-06-26_1103.md |
| Chai primary record | Primary preprint | Verifies the dependency-graph and differential-testing basis of the related entry | https://arxiv.org/abs/2606.26933 |
| VeriChat DEP entry | Related Black-Lake-Data entry | Hybrid reasoning integrated with simulation and formal verification | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260706-Tech%20Intel%200104/daily_research_findings_2026-07-06_0104.md |
| VeriChat primary record | Primary preprint | Verifies the tool-integrated verification workflow and reported AES S-Box case study | https://arxiv.org/abs/2607.01668 |

The three DEP rows above are the exactly three related repository entries selected for this run. Their paired arXiv rows are source-basis records, not additional DEP entries.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2104.08638 | Title, authors, v1/v2 dates, subjects, journal reference, abstract, arXiv DOI | 2026-07-13 | Primary metadata |
| R2 | https://fredfeng.github.io/papers/sailfish.pdf | Full paper content, figures/tables, implementation, evaluation, limitations, appendices | 2026-07-13 | Author-hosted primary paper; cross-check for local extraction |
| R3 | https://doi.org/10.1109/SP46214.2022.9833721 | Publisher DOI and conference identity | 2026-07-13 | Version-of-record identifier |
| R4 | https://seclab.cs.ucsb.edu/publications/priyanka_sailfish_22/ | Institutional author and venue metadata | 2026-07-13 | UCSB SecLab publication page |
| R5 | https://github.com/ucsb-seclab/sailfish | Code/data availability, Docker guidance, example invocation, repository tree | 2026-07-13 | Official repository; not executed |
| R6 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260702-Tech%20Intel%201102/daily_research_findings_2026-07-02_1102.md | Antaeus related-entry synopsis | 2026-07-13 | Existing DEP evidence |
| R7 | https://arxiv.org/abs/2607.01138 | Antaeus primary abstract and metadata | 2026-07-13 | Primary basis for R6 |
| R8 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260626-Tech%20Intel%201103/daily_research_findings_2026-06-26_1103.md | Chai related-entry synopsis | 2026-07-13 | Existing DEP evidence |
| R9 | https://arxiv.org/abs/2606.26933 | Chai primary abstract and metadata | 2026-07-13 | Primary basis for R8 |
| R10 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260706-Tech%20Intel%200104/daily_research_findings_2026-07-06_0104.md | VeriChat related-entry synopsis | 2026-07-13 | Existing DEP evidence |
| R11 | https://arxiv.org/abs/2607.01668 | VeriChat primary abstract and metadata | 2026-07-13 | Primary basis for R10 |
| R12 | Public extraction-cache summary for arXiv:2104.08638 | Extractor, cache status, byte count, and missing local HTML/source text | 2026-07-13 | Derived local processing record; no local path exposed |

## Appendix

### A. Replication Checklist

- [x] Paper identity pinned to arXiv v2 and publisher DOI.
- [x] Full paper body reviewed beyond the abstract.
- [x] Evaluation population, exclusions, timeout, and error categories recorded.
- [x] Main quantitative claims tied to evidence IDs.
- [x] Official code/data repository availability verified.
- [ ] Repository license and every source-data permission audited.
- [ ] Docker image pulled and hash-pinned.
- [ ] Toolchain built on a fresh machine.
- [ ] Published test cases executed.
- [ ] Full 89,853-contract corpus reconstructed and hashed.
- [ ] Tables II-IV and Figure 11 independently regenerated.
- [ ] Manual labels independently re-annotated with agreement reporting.
- [ ] Modern Solidity/proxy compatibility evaluated.

### B. Selection, Cache, and Dedup Record

| Item | Public-safe value |
|---|---|
| Candidate definition | Unique parent directory containing at least one PDF |
| Enumeration command class | `rg --files -g "*.pdf"` |
| Candidate count | 75,761 |
| Random method | Uniform PowerShell `Get-Random` zero-based index |
| Selected index | 8,874 |
| Exclusions | 0 |
| Reselections | 0 |
| arXiv ID | 2104.08638v2 |
| DOI | 10.1109/SP46214.2022.9833721 |
| Slug | SAILFISH-Vetting |
| Initial cache | Miss |
| Refresh mode | `missing-only` |
| Extractor | `pypdf` fallback because `pdftotext` was unavailable |
| Final cache | Partial: PDF text present; HTML/source text absent |
| PDF text | 117,020 bytes |
| Dedup scans | Public index, Black Lake logs/reports/DEP, automation memory, Black-Lake-Data, and 24-hour worktree markers |
| Dedup result | No prior marker; accepted on first draw |

### C. Quantitative Claim Snapshot

| Measure | Author-reported value | Caveat |
|---|---:|---|
| Deduplicated contract corpus | 89,853 | Collected through 2020; 2,068 sources excluded before final corpus |
| Manual ground-truth subset | 750 | Sampled from contracts all five static tools processed successfully |
| Labeled reentrancy / TOD | 26 / 110 | Author manual labels |
| SAILFISH false positives | 11 / 59 | Reentrancy / TOD on the labeled subset |
| SAILFISH false negatives | 0 / 0 | Sample result, not a soundness guarantee |
| Mean full-corpus time | 30.79 seconds | Historical six-machine environment and toolchain |
| Full-corpus timeouts | 1,211 | Errors separately reported as 3,395 |
| Previously unknown exploitable contracts | 47 | From 195 size-filtered, manually selected SAILFISH-only warnings |
| Ether-draining / metadata-corrupting among 47 | 11 / 36 | Author impact classification |
| Static-only warnings | 3,391 / 14,485 | Reentrancy / TOD |
| Havoc-refinement warnings | 2,436 / 10,560 | Reentrancy / TOD |
| VSA-refinement warnings | 2,076 / 7,555 | Reentrancy / TOD |
| Path-summary timeout rate | 21.50% | On a selected 2,000-contract medium/large subset |

### D. Public-Safety and Source Policy

Local absolute paths, usernames, machine names, exact local timestamps, and local timezone labels are omitted. No source file was copied into the DEP, and no `.source/` directory was created. Public URLs identify every external source used. Security examples are synthetic and defensive; no exploit payload or live target is included.
