---
title: "Semantic Password Risk - DEP-E"
generated_at: "2026-07-28T15:06:11Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of SE#PCFG, its multilingual semantic password model, empirical evidence, limits, and defensive use alongside current password guidance."
source_status: "Existing repository PDF, HTML, TeX archive, and Markdown inspected; public URLs inspected; no new external source files collected"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-29"
temporal_cutoff: "Sources and standards available on 2026-07-29"
primary_url: "https://arxiv.org/abs/2306.06824"
stable_identifier: "arXiv:2306.06824v2; DOI:10.1109/TDSC.2025.3547773"
confidence_summary: "High for the paper's stated model, datasets, evaluation design, and reported results; medium for deployment implications because no implementation or independent reproduction was performed."
safety_scope: "Defensive analysis, password-policy evaluation, synthetic testing, and privacy-preserving user guidance only"
distribution_notes: "Repository-relative provenance and public URLs only; no password corpora, guesses, or newly collected source payloads are redistributed."
---

# Semantic Password Risk - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S0 | `DEP-20260707-SEPCFG Paper` | Primary source bundle | Git repository snapshot | `0f93e1fce87210a3bf8218476ff8001c699f4f01` | [Selected DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper) | Public repository material; attribution preserved | 2026-07-29 | Every deposited file was inventoried |
| S1 | Selected DEP README | Inventory, context, and attribution | Markdown | Source snapshot above | [README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper/README.md) | Public repository material | 2026-07-29 | Inspected in full |
| S2 | Existing SE#PCFG research report | Prior transformed analysis | Markdown | 2026-07-07 source artifact | [Report](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper/sepcfg_research_report_2026-07-07.md) | Secondary synthesis inside the source DEP; local execution context was not carried forward | 2026-07-29 | Inspected in full and checked against primary material |
| P1 | *SE#PCFG: Semantically Enhanced PCFG for Password Analysis and Cracking* — Yangde Wang, Weidong Qiu, Peng Tang, Hao Tian, and Shujun Li | Primary paper | PDF and arXiv record | arXiv:2306.06824v2; IEEE TDSC 2025; DOI:10.1109/TDSC.2025.3547773 | [arXiv](https://arxiv.org/abs/2306.06824), [PDF](https://arxiv.org/pdf/2306.06824), [IEEE DOI](https://doi.org/10.1109/TDSC.2025.3547773) | arXiv record and source bundle inspected; downstream rights remain with their respective holders | 2026-07-29 | All 15 pages rendered; key methods, tables, results, ethics, and references visually inspected |
| P2 | SE#PCFG TeX/source package | Primary manuscript source and supporting figure data | TeX archive | arXiv:2306.06824v2 source | [Repository copy](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper/.source/2306.06824.source.tar), [arXiv source](https://arxiv.org/e-print/2306.06824) | Existing source-repository file; not copied into this DEP-E | 2026-07-29 | Archive inventory, `main.tex`, bibliography, table definitions, and experiment-data layout inspected |
| P3 | SE#PCFG arXiv metadata snapshot | Primary publication metadata | HTML | arXiv:2306.06824v2 | [Repository copy](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper/.source/2306.06824.abs.html) | Existing source-repository file; not copied into this DEP-E | 2026-07-29 | Title, authors, revision date, abstract, and DOI metadata inspected |
| G1 | NIST SP 800-63B-4 | Current defensive guidance | Standard | 2025 final publication | [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html), [DOI](https://doi.org/10.6028/NIST.SP.800-63B-4) | Public U.S. government standard | 2026-07-29 | Password requirements and strength appendix inspected |
| R1 | *On the Semantic Patterns of Passwords and their Security Impact* — Rafael Veras, Christopher Collins, and Julie Thorpe | Methodological predecessor | NDSS paper page | NDSS 2014 | [NDSS record](https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/semantic-patterns-passwords-and-their-security-impact/), [DOI](https://doi.org/10.14722/ndss.2014.23103) | Public conference record | 2026-07-29 | Official abstract and metadata inspected |
| R2 | *zxcvbn: Low-Budget Password Strength Estimation* — Daniel Lowe Wheeler | Defensive comparator | USENIX paper page | USENIX Security 2016 | [USENIX record](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/wheeler) | Open-access conference record | 2026-07-29 | Official abstract, deployment claims, and bibliographic record inspected |
| R3 | *Fast, Lean, and Accurate: Modeling Password Guessability Using Neural Networks* — William Melicher et al. | Empirical benchmark and defensive comparator | USENIX paper page | USENIX Security 2016 | [USENIX record](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/melicher) | Open-access conference record | 2026-07-29 | Official abstract and bibliographic record inspected |

No password databases, credential material, hashes, executable cracking tools, or new external source files were collected during this pass. The source DEP already contains a PDF, metadata HTML, and TeX archive; those files were inspected in place and are not duplicated here.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S0-S2 | Repository snapshot and Markdown | DEP inventory, prior synthesis, attribution, and stated source roles | Research boundary, provenance, and prior interpretation | High for inventory; medium for analysis | The earlier report is not independent validation and included obsolete local context that was excluded from this artifact |
| E2 | P1, P3 | Primary paper and metadata | Abstract, conceptual model, 43 semantic factor types, 17-dataset table, experimental protocol, results, ethics, revision history, and publication metadata | Main source claims and bibliographic identity | High | Results were read, not independently reproduced |
| E3 | P2 | Primary source archive | `main.tex`, tables, figure definitions, bibliography, semantic-analysis data layout, and cracking-comparison data layout | Exact method details, metrics, data sizes, benchmark choices, and reported numerical results | High for what the archive contains | Raw leaked password databases and implementation code are not included in the source archive |
| E4 | P1 visual rendering | Primary PDF | Tables II-III, semantic-correlation heatmaps, benchmark plots, Tables VI-X, runtime table, ethics, and references | Cross-check of extracted claims against rendered tables and figures | High | Rendering produced non-material font-substitution warnings; no content was unreadable on inspected pages |
| E5 | G1 | Current standard | Password length, blocklist, composition-rule, rate-limit, password-manager, normalization, and storage requirements | Defensive implementation boundary | High | NIST requirements apply to their stated scope; they do not validate SE#PCFG |
| E6 | R1-R3 | Primary related-work pages | Official abstracts and bibliographic records | Historical comparison with semantic grammars, neural guessability estimation, and practical password meters | Medium-high | Full related-paper methods and results were not re-reviewed in this pass |

## Executive Summary

SE#PCFG is a multilingual semantic model of human-chosen passwords. It represents a password at four levels: characters, semantic factors, semantic factor types, semantic patterns, and population-level semantic structure. The authors implement 43 semantic factor types, including language-specific words, names, dates, numeric strings, Pinyin, keyboard patterns, repeated strings, locations, Wikipedia entities, Urban Dictionary entries, and leet transformations. They apply the framework to 17 leaked password databases described as containing about 310 million passwords across Chinese-, English-, German-, and French-dominated populations (E2-E3).

The paper then uses this representation to construct SEPCA, a probabilistic cracking architecture with smoothing for semantic factors not observed in a training set. Across 52 train-target combinations, the authors report that SEPCA improved average user-level coverage over PCFG_w, Semantic PCFG, and FLA by 21.53%, 52.55%, and 7.86%, respectively. At the unique-password level, reported average improvements were 43.83%, 94.11%, and 11.16%. These are author-reported results from real-attack enumeration up to the paper's evaluation scale; they were not reproduced during this review (E2-E4).

The principal defensive value is diagnostic rather than generative. The results show why length and character classes alone can miss predictable human meaning: names, dates, cultural entities, language-specific tokens, and short combinations can remain easy to model. A privacy-preserving checker could use semantic categories to explain risk, but it should not emit guesses or rank candidate passwords. Current NIST SP 800-63B-4 also creates an important boundary: a semantic explanation layer can supplement whole-password blocklist checks, minimum-length rules, rate limiting, password-manager support, and secure storage, but it should not become a new set of mandatory composition rules or a substring-based substitute for the required blocklist comparison (E5).

Confidence is high that the inspected source supports the model description, dataset inventory, experimental setup, and reported results. Confidence is medium that a safe semantic feedback layer would improve real user choices, because the paper does not report a user study, a deployed password meter, false-positive analysis, or independent reproduction.

## Detailed Summary

### Problem and prior context

Password models have traditionally emphasized character transitions, probabilistic grammars, dictionaries, or limited semantic categories. The paper argues that these approaches underrepresent multilingual and culturally specific meaning. Its closest semantic predecessor, Veras et al., demonstrated that segmentation and semantic classification can improve a probabilistic grammar, but SE#PCFG aims for broader semantic coverage and a more extensible processing pipeline (E2, E6).

This is a dual-use problem. Better modeling can improve offline password guessing, yet the same evidence can inform policy design, user feedback, and authorized security evaluation. The paper explicitly frames SEPCA as a cracking architecture; this artifact therefore preserves the empirical findings while excluding guess generation, cracking procedures, credential material, or deployable offensive logic.

### Four structural levels

The framework distinguishes:

1. **Characters**, the raw symbols.
2. **Semantic factors (SFs)**, consecutive characters that form meaningful units.
3. **Semantic factor types (SFTs)**, labels such as a name, date, keyboard pattern, or noun.
4. **Semantic patterns (SPs)**, ordered SFT sequences representing a whole password, plus **semantic structure**, the population distribution over SFs, SFTs, and SPs.

This hierarchy separates a specific token from its category and a single password from population-level behavior. That distinction makes it possible to compare language groups, measure cross-database similarity, and smooth unseen factors under a known type.

### Semantic coverage and computational process

The implementation uses 43 SFTs. Fourteen are described as newly added relative to earlier work, including German and French word classes, Chinese-name acronyms, Wikipedia entities, Urban Dictionary entries, two-consonant strings, and several general categories. Table III of the paper is the authoritative inventory (E4).

Processing has three stages:

- **Pre-processing** identifies mixed-character factors before generic letter-digit-symbol splitting. Examples include keyboard patterns, email addresses, domains, repeated strings, prefixes, and suffixes.
- **Segment analysis** uses corpora and natural-language tools for letter segments, while deterministic checks classify numeric and symbol segments. The implementation uses English, German, French, name, location, Pinyin, Wikipedia, and Urban Dictionary resources.
- **Post-processing** revisits unrecognized or over-segmented strings and recognizes a limited set of common leet transformations.

The paper reports that, across the 17 databases, its segmentation success ranged from 85.11% to 97.14% under its `NN`-based measure. This is an author-defined coverage measure, not a human-annotated semantic-accuracy benchmark.

### Data and scope

The dataset table lists 17 breached databases, each with more than one million passwords and frequency information. The reported database sizes sum to approximately 310 million entries. Six are categorized as Chinese-dominated, five as English-dominated, three as German-dominated, and three as French-dominated. The paper warns that these labels describe dominant website populations rather than verified user nationality or language.

The cleaning process removes passwords longer than 30 characters or containing characters outside the 95 printable ASCII set. This improves comparability with older corpora but limits conclusions about Unicode passwords, modern password-manager output, and current passphrase behavior. The source says non-password personal information was removed and the password databases would not be redistributed.

### Semantic analysis

The paper reports several population patterns:

- Many passwords contain only one to three semantic factors, and nearly all contain five or fewer.
- Chinese-dominated databases differ strongly from non-Chinese groups at semantic-factor and semantic-factor-type levels.
- Language alignment is more visible than service category in the presented correlations.
- MyHeritage is an outlier with lower similarity to other groups, later affecting cross-database cracking transfer.
- Weak patterns include numeric strings, dates, names, nouns, Pinyin sequences, and short name-number combinations.

These observations are population-level associations in historical breach corpora. They do not establish causal explanations for user behavior and should not be generalized to all current users.

### SEPCA and smoothing

SEPCA treats semantic patterns as grammar productions. A password probability is the probability of its semantic pattern multiplied by the probabilities of its semantic factors under their SFTs. To handle unseen semantic factors, the model divides factors into observed and unobserved sets. A cross-database similarity weight allocates probability mass between the two sets; observed factors retain weighted empirical probabilities, while unseen factors share the remaining mass equally within a type.

This makes the smoothing rule inspectable but introduces a strong assumption: unseen factors within one type are equally likely. The paper notes that more complex smoothing and unseen semantic patterns remain future work.

### Evaluation design

The authors use CSDN, Gmail, Eyeem, and Fr_Mix1 as four training databases, one for each studied language group. Each is evaluated against the other 13 targets, yielding 52 train-target cases. Benchmarks are PCFG_w, Semantic PCFG, and FLA. The authors use real enumeration rather than Monte Carlo because a preliminary comparison showed a gap as high as 17.79% for SEPCA between estimated and real-attack coverage.

Evaluation is reported at:

- **User level**, where duplicate password frequencies are retained.
- **Unique-password level**, where each distinct password is counted once.

The source reports equal training data across compared methods and default benchmark configurations. Experiments ran on an Intel Xeon E5-2640 CPU and two Nvidia Tesla M40 GPUs. This hardware record aids provenance but does not establish modern cost or deployment performance.

### Reported results

At user level, SEPCA is reported to outperform both PCFG baselines in all 52 cases and FLA in 51 of 52, with the single FLA comparison decreasing by 0.3%. At unique-password level, the paper reports the best result in 50 of 52 cases. MyHeritage accounts for the principal exceptions, consistent with its lower semantic similarity to training populations.

Reported average generation rates are 32,258 passwords per second for SEPCA, 140,880 for PCFG_w, 82,595 for Semantic PCFG, and 5,787 for FLA. These numbers apply to the authors' implementations, settings, and hardware. They should not be used as a current operational benchmark without reproduction.

### Ethical and defensive interpretation

The authors state that they retained only passwords from already-public leaks, removed other personal information, and would not redistribute the databases. That reduces but does not eliminate legal, ethical, representativeness, or privacy concerns. Breach data remain sensitive, may lack consent, and may be unlawful or inappropriate to use in many jurisdictions or organizations.

For defensive use, semantic categories are most valuable as explanations and evaluation features. A checker can say that a candidate appears to contain a date, name, keyboard run, or culturally common entity without storing the password or producing alternative guesses. NIST SP 800-63B-4 nevertheless requires the whole prospective password to be compared against a blocklist and prohibits other composition rules. A semantic meter should therefore provide non-binding guidance and should not reject passwords solely because they contain a word or substring.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | SE#PCFG models 43 semantic factor types and applies them to 17 leaked databases totaling about 310 million passwords across four language-dominated groups. | Author claim supported by source tables | E2-E4 | Directly supported by the paper's SFT and dataset tables; population labels are approximate, not verified demographics. | High |
| C2 | The implementation identifies between 85.11% and 97.14% of passwords under its segmentation-success measure. | Author result | E2-E3 | Supported by the results table, but the metric uses residual `NN` labeling rather than independent human annotation. | Medium-high |
| C3 | SEPCA improves average user-level coverage over PCFG_w, Semantic PCFG, and FLA by 21.53%, 52.55%, and 7.86%; unique-password improvements are 43.83%, 94.11%, and 11.16%. | Author result | E2-E4 | Values match the paper text and rendered result tables. No statistical recomputation or benchmark replay was performed. | High for reporting; medium for generalization |
| C4 | Language-aligned training improves Chinese, German, and French target averages, while English-target results are more mixed. | Author interpretation | E2-E4 | Supported by Table VIII and the paper's correlation discussion; hidden demographic and dataset effects remain plausible. | Medium |
| C5 | Semantic analysis can improve defensive password feedback beyond character-class rules. | Reviewer interpretation | E2, E5-E6 | Mechanistically plausible and consistent with NIST's rejection of composition rules, but user benefit and calibration require direct testing. | Medium |
| C6 | A semantic meter must remain supplemental to whole-password blocklist checks and should not become a mandatory substring composition rule. | Reviewer implementation conclusion | E5 | Directly follows current NIST requirements and the distinction between explanation and blocklist enforcement. | High |
| C7 | SEPCA evidence should not be operationalized into public guessing or cracking functionality. | Safety conclusion | E2-E3 | The source is explicitly dual-use and relies on breach corpora; a defensive-only boundary is warranted. | High |

## Methodology

- `Research objective`: Preserve and critically review the selected source DEP as a schema-complete DEP-E artifact, distinguishing the paper's claims from defensive implementation inference.
- `Sources inspected`: The selected DEP README, its existing research report, arXiv metadata HTML, the 15-page paper PDF, the TeX/source archive, current NIST SP 800-63B-4 password guidance, and official NDSS/USENIX pages for three related works.
- `Discovery strategy`: Repository inspection established the source inventory and provenance. The PDF was rendered to PNG and visually reviewed. The TeX archive was inventoried, and targeted primary sections, tables, bibliography records, and experimental data layout were inspected. Official primary-source pages were used for current standards and related-work context.
- `Inclusion criteria`: Primary paper material, existing source-deposit artifacts, current authoritative defensive guidance, and primary related-work records that clarify the model's novelty or safe application.
- `Exclusion criteria`: Unverified commentary, executable cracking instructions, credential material, leaked password payloads, source redistribution, repository execution, and unsupported implementation claims.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication.
- `Evidence handling`: Major claims are mapped to evidence IDs. Exact numerical results were checked against TeX and rendered tables. Author claims, reviewer interpretation, and implementation conclusions are labeled separately.
- `Uncertainty handling`: Non-reproduced results remain author-reported. Dataset representativeness, legality, demographic labels, calibration, and product effects are kept as explicit limitations.
- `Extraction process`: All PDF pages were rendered; pages containing the SFT tables, semantic-correlation figures, benchmark plots, result tables, runtime table, weak-pattern table, ethics, and references were visually inspected in detail. The source archive supplied machine-readable manuscript text and table values.
- `Version control`: Repository sources are pinned to commit `0f93e1fce87210a3bf8218476ff8001c699f4f01`; the paper is pinned to arXiv v2 and its IEEE DOI; NIST guidance is the 2025 SP 800-63B-4 publication.
- `Cross-checking`: Dataset sizes, SFT count, benchmark design, reported improvements, runtime, and ethical statements were cross-checked across the PDF, TeX, metadata, and prior report.
- `Reviewer stance`: Critical source preservation, defensive implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: SE#PCFG's semantic representation, processing pipeline, dataset analysis, SEPCA smoothing, benchmark evidence, ethical constraints, and safe defensive uses.
- `Temporal boundary`: Sources and standards available on 2026-07-29.
- `Evidence limits`: No leaked corpus, implementation repository, trained model, benchmark environment, or raw experiment was available or executed. Related works were checked through official records but not fully re-reviewed.
- `Assumptions`: The arXiv v2 source archive corresponds materially to the inspected IEEE-formatted PDF; the source DEP's repository files are authentic copies of the cited materials.
- `Constraints`: Dual-use security risk, privacy and consent concerns around breach corpora, legal uncertainty, lack of redistribution authorization, and the prohibition on publishing operational cracking capability.
- `Out of scope`: Guess generation, password cracking, hash testing, credential recovery, breach-corpus acquisition, production password policy, legal advice, and independent empirical reproduction.
- `Intended use`: DEP preservation, security review, defensive product planning, synthetic evaluation, and future reproducibility work.
- `Audience`: Security researchers, authentication engineers, product designers, policy reviewers, and future Black-Lake reviewers.
- `Reproducibility boundary`: The paper's equations, tables, source text, and derived figure data are inspectable; full reproduction is blocked by unavailable raw password corpora and uninspected implementation code.
- `Operational boundary`: Semantic categories may be analyzed with synthetic inputs, but this artifact does not enable enumeration or ranking of candidate passwords.
- `Data sensitivity`: The artifact contains public research metadata and aggregate results only. Underlying breach passwords are highly sensitive and excluded.

## Observations

- `Observed pattern`: The model's strongest contribution is the separation of token, type, pattern, and population structure. This makes semantic drift and cross-population transfer inspectable rather than treating every string as an undifferentiated character sequence.
- `Observed pattern`: Many reported weak patterns are simple single-factor or two-factor compositions, which explains why superficial complexity can coexist with semantic predictability.
- `Technical implication`: A password meter can use semantic features as explanatory evidence without copying SEPCA's generative path.
- `Technical implication`: Localization is not optional. The paper's cross-database results suggest that dictionaries, names, transliterations, dates, and popular entities should be versioned by locale and time.
- `Contradiction or tension`: The paper recommends richer semantic advice, while current NIST guidance prohibits composition rules and requires whole-password blocklist comparison. This is resolved only if semantic detection is advisory, calibrated, and never a substring-based rejection rule.
- `Contradiction or tension`: The framework seeks broad semantics but filters out Unicode and passwords over 30 characters, limiting its relevance to current international and password-manager-generated secrets.
- `Open question`: Can semantic explanations improve user choices beyond an established blocklist and meter without creating predictable workaround behavior?
- `Open question`: How stable are the 43 SFTs under modern multilingual text, Unicode, passphrases, password-manager adoption, and newer breach populations?
- `Reviewer hypothesis`: A small, local semantic explanation layer may add user value when it is evaluated as a supplemental message generator rather than as a strength oracle.

## Considerations

- **Privacy:** Candidate passwords should be analyzed locally and never logged. Telemetry should contain only coarse, differentially private or thresholded aggregate categories.
- **Standards alignment:** Current NIST guidance requires minimum length, whole-password blocklist comparison, rate limiting, password-manager support, and secure hashing. Semantic feedback cannot replace these controls.
- **False positives:** Names, words, and dates can appear coincidentally in long random strings or passphrases. A meter needs calibrated confidence and an explanation that avoids deterministic rejection.
- **Localization:** Corpora can encode cultural bias and may misclassify minority languages, transliterations, or names. Locale packs need documented provenance, update cadence, and opt-out behavior.
- **Security:** A public API returning detailed semantic decompositions could become an oracle for improving guesses. Keep outputs coarse and non-enumerative.
- **Legal and ethical use:** Do not acquire or process leaked password corpora without explicit authorization and counsel. Synthetic or policy-approved datasets should be the default.
- **Maintenance:** Names, slang, brands, games, and cultural entities drift. Static dictionaries create stale risk estimates.
- **Accessibility and usability:** Guidance must be understandable and should not pressure users into predictable substitutions. Password-manager generation should remain the preferred recommendation.
- **Evaluation:** Product testing should measure false rejection, user comprehension, password reuse, workaround behavior, local latency, and privacy—not only correlation with an offline guess rank.

## Strengths

- The four-level semantic model is explicit, inspectable, and extensible.
- The source evaluates 43 SFTs across 17 large datasets and four language-dominated groups.
- The 52 matched train-target comparisons use the same training sets across benchmarks.
- The authors explain why real enumeration was chosen and quantify the observed Monte Carlo discrepancy.
- Rendered tables and the TeX archive provide unusually rich provenance for checking reported values.
- The paper acknowledges ethical constraints and declines to redistribute the password databases.
- The source exposes meaningful negative evidence: MyHeritage transfer is weaker, Unicode is excluded, and semantic dictionaries are incomplete.

## Weaknesses

- Raw datasets and an end-to-end implementation are unavailable in the inspected bundle, preventing independent reproduction.
- Breach corpora are historical, sensitive, non-consensual, and unlikely to represent current password-manager or passkey users.
- Dataset language labels are inferred from dominant website populations rather than verified user attributes.
- ASCII-only cleaning and a 30-character cap exclude important modern password behavior.
- Segmentation success is measured through residual unknown labels, not a gold-standard semantic annotation set.
- Equal probability for unseen factors within an SFT is simple and may misrepresent real distributions.
- The comparison does not provide a full statistical uncertainty analysis or modern hardware-normalized cost study.
- No user study tests whether semantic feedback leads to safer choices or merely predictable transformations.
- The model is intrinsically dual-use and can strengthen offensive guessing if operationalized.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release a synthetic multilingual semantic benchmark | Reproducibility | Raw breach data cannot be redistributed safely | Enables shared segmentation and calibration tests | Synthetic data may not match human behavior | Publish generation rules, hidden labels, and challenge splits |
| Add Unicode and long-passphrase support | Coverage | Current cleaning excludes modern international behavior | Better alignment with current standards and users | Tokenization ambiguity and locale bias | Curated multilingual edge cases and normalization tests |
| Replace `NN` residual coverage with human-labeled accuracy | Measurement | Recognition rate is not semantic correctness | Reveals precision, recall, and confusion by SFT | Annotation cost and sensitive examples | Double annotation with adjudication on synthetic/public-safe strings |
| Calibrate advisory confidence | Product safety | False alarms can frustrate users and create workarounds | More useful explanations with fewer unnecessary warnings | Calibration can drift | Reliability diagrams and locale-stratified false-positive tests |
| Separate blocklist enforcement from semantic explanation | Standards alignment | NIST requires whole-password comparison and rejects composition rules | Avoids accidental policy nonconformance | More complex UX and logic | Conformance review plus controlled usability study |
| Use privacy-preserving local inference | Privacy | Passwords must not leave the client | Reduces data exposure | Bundle size and update complexity | Network-denial tests, log inspection, and privacy review |
| Evaluate against current password managers and passphrases | Generalization | Historical breach corpora underrepresent modern choices | Clarifies where semantic analysis still adds value | Requires authorized, non-sensitive test sets | Synthetic manager output and recruited-user study with no secret retention |
| Publish versioned locale cards | Governance | Dictionaries encode culture, time, and bias | Auditable updates and clearer limitations | Ongoing maintenance | Coverage, bias, and drift reports per release |

## Potential Implementations

### Local semantic explanation layer

- `User`: Authentication product teams and end users.
- `Goal`: Explain why a human-chosen password may be predictable without exposing it.
- `Core mechanism`: Local, coarse classification of patterns such as dates, keyboard runs, names, and common entities.
- `Required inputs`: One candidate password in volatile client memory and a versioned, public-safe locale pack.
- `Outputs`: Non-binding reasons, confidence, and a recommendation to use a password manager.
- `Risk controls`: No logging, no network transmission, no guess generation, no token-by-token decomposition returned to remote callers.
- `Evaluation`: False-positive rate, local latency, user comprehension, and absence of network or storage leakage.

### Standards-aware password control evaluator

- `User`: Security and compliance teams.
- `Goal`: Test whether an authentication flow correctly separates blocklists, length, rate limiting, storage, and advisory feedback.
- `Core mechanism`: A synthetic test harness maps each control to NIST SP 800-63B-4 requirements and checks semantic messages independently.
- `Required inputs`: Synthetic passwords, policy configuration, and test-only authentication endpoints.
- `Outputs`: Conformance findings, message-quality findings, and regression cases.
- `Risk controls`: Synthetic data only, isolated environment, no credential reuse, and no external attack traffic.
- `Evaluation`: Requirement coverage, deterministic test results, and review by authentication specialists.

### Locale-drift audit

- `User`: Maintainers of password meters.
- `Goal`: Detect stale or biased semantic dictionaries before release.
- `Core mechanism`: Compare versioned locale packs against public, non-sensitive language resources and curated synthetic cases.
- `Required inputs`: Locale metadata, dictionary diffs, and synthetic test suites.
- `Outputs`: Coverage gaps, bias flags, collision rates, and recommended retirements.
- `Risk controls`: No breach corpora, personal names only from explicitly licensed public resources, and documented provenance.
- `Evaluation`: Reviewer agreement, regression stability, and locale-stratified error rates.

## Three Ways to Exercise This Research

1. `Synthetic segmentation benchmark`: Objective — test whether a defensive classifier recognizes coarse semantic categories without producing guesses. Inputs — a hand-authored synthetic set of dates, keyboard runs, names, random strings, Unicode passphrases, and ambiguous cases. Method — label the set, run local classification, and calculate per-category precision and recall. Output — a confusion matrix and failure inventory. Success criterion — documented error rates with zero retained plaintext after the run. Stop condition and safety boundary — stop if any component transmits, logs, ranks, or generates candidate passwords.
2. `NIST control-separation review`: Objective — verify that semantic feedback does not become a prohibited composition rule or substring blocklist. Inputs — SP 800-63B-4 requirements, a mock password flow, and synthetic cases. Method — test whole-password blocklist behavior, length, rate limiting, password-manager support, and semantic messaging as separate controls. Output — a control map and regression suite. Success criterion — every rejection is attributable to an authorized control and semantic messages remain advisory. Stop condition and safety boundary — use no real accounts, breach data, or production credential endpoints.
3. `Locale-card pilot`: Objective — measure how a small semantic vocabulary behaves across languages and Unicode. Inputs — licensed public lexicons, synthetic examples, normalization variants, and a locale-card template. Method — document provenance, test normalization, measure false positives, and review cultural assumptions with language experts. Output — one versioned locale card and a bounded test pack. Success criterion — reproducible results, explicit limitations, and no unexplained high-error subgroup. Stop condition and safety boundary — exclude private names, leaked corpora, and any resource without clear usage rights.

## Example MVP Product

- `Product name`: Semantic Cue
- `Target user`: Teams operating password-based authentication while transitioning toward password managers, passkeys, and stronger authenticators.
- `Problem`: Character-class meters can give vague or misleading feedback when a password contains predictable human meaning.
- `Core workflow`: The user enters a password; a local module first leaves authoritative acceptance decisions to length and whole-password blocklist controls, then optionally identifies coarse semantic cues and displays one short explanation plus a password-manager recommendation.
- `Data requirements`: Versioned public-safe patterns, synthetic calibration cases, and no breach corpus in the client or service.
- `Architecture`: Client-only classifier, signed locale-pack updates, a standards-control adapter, an ephemeral result object, and optional aggregate telemetry that is disabled by default and never contains password-derived tokens.
- `Success metrics`: Zero password egress, zero plaintext logging, median local latency below 50 ms on target devices, calibrated false-positive rates by locale, improved user comprehension, and no increase in predictable substitutions.
- `Risk controls`: No guess generation, no ranking API, no server-side decomposition, strict content-security policy, reproducible bundle builds, locale provenance review, and a kill switch for problematic rules.
- `Limitations`: It cannot prove password strength, estimate every offline attacker, replace a blocklist, remove phishing risk, or compensate for weak storage and rate limiting.
- `MVP boundary`: One English locale pack, a small set of high-confidence categories, synthetic-only evaluation, and no production telemetry.
- `Deployment model`: Browser module or native local component integrated into an existing password flow.
- `Evaluation plan`: Static privacy review, network-denial tests, synthetic regression suite, standards conformance review, accessibility study, and a small consented usability study with no password retention.
- `Failure modes`: False semantic matches, locale bias, stale dictionaries, overconfident messages, and accidental coupling between advisory output and acceptance logic.
- `Maintenance plan`: Signed quarterly locale updates, rollback support, public change notes, regression thresholds, and annual standards review.

## Related Research and Reading

**Initial pass:** No prior Black-Lake DEP Class artifact, output log, source report, or Report-Mark existed for the selected DEP. The items below establish the paper's methodological lineage and the current defensive boundary; no item is labeled as a later-pass expansion.

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| *Password Cracking Using Probabilistic Context-Free Grammars* — Weir et al. | Foundational primary paper | Establishes the PCFG baseline and grammar structure extended by SE#PCFG | https://doi.org/10.1109/SP.2009.8 |
| *On the Semantic Patterns of Passwords and their Security Impact* — Veras, Collins, and Thorpe | Primary methodological predecessor | Introduces semantic segmentation, classification, and grammar-based use of semantic patterns | https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/semantic-patterns-passwords-and-their-security-impact/; https://doi.org/10.14722/ndss.2014.23103 |
| *Fast, Lean, and Accurate: Modeling Password Guessability Using Neural Networks* — Melicher et al. | Primary benchmark and defensive system paper | Supplies FLA, the neural benchmark used by SE#PCFG, and a client-side guessability model | https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/melicher |
| *zxcvbn: Low-Budget Password Strength Estimation* — Wheeler | Primary defensive password-meter paper | Demonstrates a deployable alternative to character-class meters and frames low-budget online-attack estimation | https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/wheeler |
| NIST SP 800-63B-4 | Current authoritative guidance | Defines minimum length, whole-password blocklist, no composition rules, rate limiting, password-manager support, and secure storage requirements | https://pages.nist.gov/800-63-4/sp800-63b.html; https://doi.org/10.6028/NIST.SP.800-63B-4 |
| PCFG password guess generator | Official implementation locator cited by the paper | Useful for a future static, authorized comparison of grammar definitions and defaults | https://github.com/lakiw/pcfg_cracker |
| Semantic Password Guesser | Official implementation locator cited by the paper | Useful for a future pinned audit of the Semantic PCFG benchmark | https://github.com/vialab/semantic-guesser |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| SR0 | [Selected source DEP at `0f93e1f`](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper) | Source boundary, inventory, prior artifact, and deposited primary files | 2026-07-29 | Every file was inventoried; source files were inspected in place |
| SR1 | [Selected DEP README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper/README.md) | Package contents, tags, descriptions, and attribution | 2026-07-29 | Inspected in full |
| SR2 | [Existing source research report](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper/sepcfg_research_report_2026-07-07.md) | Prior synthesis, implementation ideas, and reference discovery | 2026-07-29 | Secondary source; claims were checked against primary material; local context was not copied |
| SR3 | Yangde Wang, Weidong Qiu, Peng Tang, Hao Tian, and Shujun Li. [*SE#PCFG: Semantically Enhanced PCFG for Password Analysis and Cracking*](https://arxiv.org/abs/2306.06824), arXiv:2306.06824v2, [PDF](https://arxiv.org/pdf/2306.06824), [IEEE DOI](https://doi.org/10.1109/TDSC.2025.3547773) | Conceptual model, 43 SFTs, 17 datasets, SEPCA, evaluation, results, ethics, and limitations | 2026-07-29 | Primary paper; 15-page PDF rendered and key tables/figures inspected |
| SR4 | [SE#PCFG TeX/source archive](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper/.source/2306.06824.source.tar), [arXiv source endpoint](https://arxiv.org/e-print/2306.06824) | Exact manuscript text, equations, tables, bibliography, figure definitions, and derived experiment-data layout | 2026-07-29 | Primary source archive inspected; not copied into Black-Lake |
| SR5 | [SE#PCFG arXiv metadata HTML](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/0f93e1fce87210a3bf8218476ff8001c699f4f01/.lake-data/DEP-20260707-SEPCFG%20Paper/.source/2306.06824.abs.html) | Title, authors, abstract, revision history, and DOI metadata | 2026-07-29 | Existing source snapshot |
| SR6 | [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html), [DOI](https://doi.org/10.6028/NIST.SP.800-63B-4) | Current requirements for password length, blocklists, composition rules, guidance, rate limiting, password managers, normalization, and storage | 2026-07-29 | Authoritative defensive standard; does not validate SE#PCFG |
| SR7 | Rafael Veras, Christopher Collins, and Julie Thorpe. [*On the Semantic Patterns of Passwords and their Security Impact*](https://www.ndss-symposium.org/ndss2014/ndss-2014-programme/semantic-patterns-passwords-and-their-security-impact/), [DOI](https://doi.org/10.14722/ndss.2014.23103) | Semantic-password methodology and predecessor evidence | 2026-07-29 | Official NDSS record and abstract inspected |
| SR8 | Daniel Lowe Wheeler. [*zxcvbn: Low-Budget Password Strength Estimation*](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/wheeler) | Defensive meter comparison, client-side feasibility, and limits of character-class feedback | 2026-07-29 | Official USENIX record and abstract inspected |
| SR9 | William Melicher et al. [*Fast, Lean, and Accurate: Modeling Password Guessability Using Neural Networks*](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/melicher) | FLA benchmark identity and client-side neural guessability context | 2026-07-29 | Official USENIX record and abstract inspected |
| SR10 | William Weir et al. [*Password Cracking Using Probabilistic Context-Free Grammars*](https://doi.org/10.1109/SP.2009.8) | Foundational PCFG locator cited by the primary paper | 2026-07-29 | DOI and source-paper bibliography used as locator; full paper not re-reviewed |
| SR11 | [PCFG password guess generator](https://github.com/lakiw/pcfg_cracker) | Official PCFG implementation locator cited by the paper | 2026-07-29 | Discovered only; repository not inspected, executed, or collected |
| SR12 | [Semantic Password Guesser](https://github.com/vialab/semantic-guesser) | Official semantic-grammar implementation locator cited by the paper | 2026-07-29 | Discovered only; repository not inspected, executed, or collected |

No password corpus, credential material, hash set, executable cracking tool, implementation repository, or newly downloaded external source file was collected in this pass.

## Appendix

### Source inventory

- `Black-Lake-Data/.lake-data/DEP-20260707-SEPCFG Paper/README.md` — inspected in full.
- `Black-Lake-Data/.lake-data/DEP-20260707-SEPCFG Paper/sepcfg_research_report_2026-07-07.md` — inspected in full as prior synthesis.
- `Black-Lake-Data/.lake-data/DEP-20260707-SEPCFG Paper/.source/2306.06824.abs.html` — inspected for metadata and abstract.
- `Black-Lake-Data/.lake-data/DEP-20260707-SEPCFG Paper/.source/2306.06824.pdf` — 15 pages rendered; key evidence pages visually inspected.
- `Black-Lake-Data/.lake-data/DEP-20260707-SEPCFG Paper/.source/2306.06824.source.tar` — archive inventory, manuscript source, bibliography, figure definitions, and data layout inspected.

### Replication checklist

- [x] Pin the source DEP snapshot.
- [x] Confirm title, authors, arXiv version, and IEEE DOI.
- [x] Cross-check dataset counts, SFT count, evaluation design, reported improvements, runtime, and ethics in primary source material.
- [x] Inspect rendered tables and figures for the major reported results.
- [ ] Obtain lawful, authorized, documented datasets or a synthetic replacement.
- [ ] Obtain and statically audit the exact SE#PCFG/SEPCA implementation.
- [ ] Recreate preprocessing and semantic labels with versioned corpora.
- [ ] Reproduce the 52 matched train-target comparisons.
- [ ] Add confidence intervals, ablations, Unicode/passphrase tests, and modern baselines.
- [ ] Conduct a privacy-reviewed usability study of advisory semantic feedback.

### Sanitization note

This artifact replaces source-local execution context with repository-relative paths, public URLs, date-only access records, and UTC provenance. No required source claim or attribution was removed.
