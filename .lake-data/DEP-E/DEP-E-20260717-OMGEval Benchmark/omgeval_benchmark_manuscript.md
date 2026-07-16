---
title: "OMGEval Benchmark - DEP-E"
generated_at: "2026-07-17"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of culturally localized multilingual generative evaluation and LLM-as-a-judge evidence."
source_status: "complete local PDF, HTML, metadata, and source package inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-17"
temporal_cutoff: "arXiv:2402.13524v2 revised 2026-01-30; official release repository commit f4dfb6d188e711e72ba7453757209df808122e8e"
primary_url: "https://arxiv.org/abs/2402.13524"
stable_identifier: "arXiv:2402.13524v2; DOI 10.48550/arXiv.2402.13524"
confidence_summary: "High for source identity, construction workflow, and reported tables; medium for benchmark interpretation; low for independent reproducibility because model runs and judge outputs were not rerun."
safety_scope: "offline benchmark evaluation, calibration audit, dataset governance, and bounded product planning"
distribution_notes: "No PDF, HTML, TeX/source archive, extracted text, cache, model output bundle, local path, or private execution detail is redistributed."
---

# OMGEval Benchmark - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | OMGEval arXiv record | Primary metadata | HTML | arXiv:2402.13524v2; DOI 10.48550/arXiv.2402.13524 | https://arxiv.org/abs/2402.13524 | Public metadata and arXiv license locator | 2026-07-17 | Inspected |
| S2 | OMGEval complete paper | Primary artifact | PDF and full-paper HTML | v2, revised 2026-01-30, 12 pages | https://arxiv.org/pdf/2402.13524 and https://arxiv.org/html/2402.13524 | Verified local copies withheld | 2026-07-17 | Inspected in full |
| S3 | OMGEval source package | Primary artifact | TeX/source archive | arXiv:2402.13524v2 | https://arxiv.org/e-print/2402.13524 | Local source package withheld | 2026-07-17 | Inspected through extraction |
| S4 | blcuicall/OMGEval | Official release | GitHub repository | commit `f4dfb6d188e711e72ba7453757209df808122e8e` | https://github.com/blcuicall/OMGEval | MIT repository license; third-party dataset/content rights require separate review | 2026-07-17 | README, top-level inventory, and license inspected |
| S5 | AlpacaFarm | Methodological predecessor | arXiv record | arXiv:2305.14387v4 | https://arxiv.org/abs/2305.14387 | Primary metadata/abstract inspected | 2026-07-17 | Inspected for context |
| S6 | MT-Bench and Chatbot Arena | Methodological neighbor | arXiv record | arXiv:2306.05685v4 | https://arxiv.org/abs/2306.05685 | Primary metadata/abstract inspected | 2026-07-17 | Inspected for judge-bias context |
| S7 | Belebele | Multilingual benchmark | arXiv record | arXiv:2308.16884v2 | https://arxiv.org/abs/2308.16884 | Primary metadata/abstract inspected | 2026-07-17 | Inspected for parallel-language context |
| S8 | M3Exam | Multilingual benchmark | arXiv record | arXiv:2306.05179 | https://arxiv.org/abs/2306.05179 | Primary metadata/abstract inspected | 2026-07-17 | Inspected for benchmark context |
| S9 | Judge Conformal - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` | Repository synthesis context only | 2026-07-17 | Inspected |
| S10 | PAC Confidence - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Repository synthesis context only | 2026-07-17 | Inspected |
| S11 | OViP Preference - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` | Repository synthesis context only | 2026-07-17 | Inspected |
| S12 | Black Lake repository rules | Deposition authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md and https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Public repository governance | 2026-07-17 | Inspected live |
| S13 | Black-Lake-Data repository rules | Companion context authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public repository governance | 2026-07-17 | Inspected live |

Paper/work metadata:

- `Full title`: OMGEval: An Open Multilingual Generative Evaluation Benchmark for Large Language Models.
- `Authors`: Yang Liu, Meng Xu, Shuo Wang, Liner Yang, Haoyu Wang, Zhenghao Liu, Cunliang Kong, Yun Chen, Yang Liu, Maosong Sun, and Erhong Yang.
- `Affiliations shown`: Beijing Language and Culture University, Tsinghua University, Beijing University of Posts and Telecommunications, Northeastern University, and Shanghai University of Finance and Economics.
- `Initial submission`: 2024-02-21.
- `Inspected revision`: arXiv v2, revised 2026-01-30.
- `Subject`: Computation and Language (`cs.CL`).
- `Dataset languages`: Chinese, Russian, French, Spanish, and Arabic; English is retained as the AlpacaEval source/reference condition in the model table.
- `Source files deposited`: none; no `.source/` directory exists.
- `Private source note`: complete local PDF, full-paper HTML, metadata HTML, TeX/source package, and extraction cache were used for source-first review, but their locations and contents are not redistributed.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S3 | Primary paper and metadata | Title, authors, version, abstract, full text, tables, ethics, limitations, and source structure | Identity and complete-paper review | High | Preprint; experiments not independently reproduced |
| E2 | S2-S3, Sections 3.1-3.3 | Primary method evidence | GPT-4 preliminary translation, human localization, two-annotator/one-reviewer verification | Dataset construction and localization mechanism | High for source reporting | No inter-annotator statistics, adjudication logs, or full annotation protocol audit |
| E3 | S2-S3, Section 3.5, Figures 5-6, Tables 2-3 | Primary dataset evidence | Capability taxonomy, distribution, 804-item language sets, localization counts, root-verb analysis | Dataset composition | High for transcription | Uneven categories; exact item-level audit not performed |
| E4 | S2-S3, Sections 3.4 and 4.1-4.3, Table 4 | Primary evaluation evidence | GPT-4 pairwise adjudication, GPT-3.5-Turbo baseline, ten models, full/localized win rates | Main model comparison | High for reported values | Judge outputs, randomization, API versions, and standard errors not recomputed |
| E5 | S2-S3, Section 4.4, Table 5 | Primary human-comparison evidence | 100 Chinese and 100 Spanish cases; full/local split; precision, recall, F1 | Judge-human alignment claim | High for transcription | Only two languages, one model pair, and a limited annotation setting |
| E6 | S2-S3, Sections 7-8 | Primary ethics/limitation evidence | Annotator compensation, research-only recommendation, five-language limitation | Governance and scope boundary | High | Limited detail on consent, demographics, labor process, or content-risk review |
| E7 | S4 | Official release evidence | Repository data, evaluator-prompt, figure, model-output, README, and MIT license inventory | Public artifact availability | High for observed inventory | No end-to-end executable harness, environment lock, or reproduction run established |
| E8 | S5-S8 | Primary contextual records | Pairwise feedback, judge bias, broad multilingual coverage, multilevel benchmark design | Comparative positioning | High for metadata/abstract | These works were not reviewed in full here |
| E9 | S9-S11 | Related DEP artifacts | Judge intervals, finite-sample confidence, shift boundaries, judge-mediated on-policy data | Cross-DEP synthesis | Medium | Conceptual relation; no joint experiment |
| E10 | S12-S13 and process records | Governance/process evidence | Live README rules, uniform random draw, dedup scans, integrity repair, cache verification | Deposition compliance and provenance | High | Operational evidence, not paper evidence |

## Executive Summary

OMGEval responds to a real evaluation gap: open-ended LLM benchmarks were largely English, while multilingual benchmarks often used discriminative or translated tasks that could miss culturally situated usage. The work creates five aligned 804-question sets for Chinese, Russian, French, Spanish, and Arabic. GPT-4 supplies preliminary translation, but culture-bearing elements are manually localized. Each language team uses two annotators and one reviewer, and the benchmark labels nine capability categories.

The central empirical design follows AlpacaEval. A candidate model's response is compared against GPT-3.5-Turbo, and GPT-4 chooses the preferred answer. The paper evaluates ten proprietary and open multilingual models on full language sets and localization subsets. GPT-4 is the only listed model above the 50 baseline on average, with 55.5 for full sets and 54.6 for localized subsets. Guanaco-13B is the strongest listed open model at 14.8 and 13.7. The weakest listed BLOOMZ result is 0.4 and 0.7. These are pairwise win rates under the paper's baseline, judge, prompt, and model snapshots, not timeless measures of multilingual ability.

The human-comparison evidence is useful but narrower than the paper's broad judge-reliability language. For Chinese and Spanish, the authors sample 100 examples per language, split evenly between localized and other items, and compare GPT-3.5-Turbo with PolyLM-Chat-13B. Reported F1 is 0.88/0.79 for Chinese full/localized and 0.91/0.89 for Spanish full/localized. No equivalent check is reported for Russian, French, or Arabic, other model pairs, multiple judge families, or order-randomized repeated judgments.

The most durable contribution is the localization workflow, not the particular 2024-era ranking. Cultural localization makes the questions more relevant to target-language users, but it can also change difficulty and construct meaning. A strong successor should therefore report cultural relevance and cross-language measurement comparability separately. The three related DEP entries suggest a concrete governance stack: interval-valued judge outputs, support- and shift-aware score gates, and an isolated on-policy development loop that cannot ingest immutable benchmark test items.

Reviewer confidence is high for source identity, construction details, and table transcription. Confidence is medium that OMGEval is a reusable benchmark design pattern. Confidence is low that the reported ranking generalizes to current models or establishes unbiased cross-cultural measurement without rerunning a pinned multi-judge, human-calibrated evaluation.

## Detailed Summary

### Problem Context

Multilingual model evaluation can fail in two different ways. A benchmark may be linguistically narrow, evaluating mostly English. Or it may translate English-centered questions into other languages while preserving English cultural assumptions. OMGEval argues that open-ended generation needs evaluation in the language and cultural situations in which users actually communicate.

The paper contrasts discriminative benchmarks with generative preference evaluation. Exact-match and multiple-choice tasks are easier to score but constrain what a model may express. Open-ended questions can probe generation, explanation, creativity, dialogue, coding, reasoning, and knowledge, yet they require a judge. OMGEval adopts an LLM judge to make that evaluation tractable.

### Dataset Construction

The paper begins from 805 AlpacaEval entries, while the final per-language tables and official repository describe 804 questions. The one-item difference is not explained in the inspected text and should be preserved as a minor provenance ambiguity rather than silently normalized.

GPT-4 performs preliminary translation into Chinese, Russian, French, Spanish, and Arabic. That translation is a working reference, not the final benchmark. Human annotators identify questions containing cultural elements and adapt names, places, foods, festivals, television, film, books, games, historical periods, and writing systems. Questions without culture-specific content, such as many code or mathematics tasks, may remain closer to direct translations.

The localization examples reveal the intended mechanism. A question about American state names becomes a question about Chinese province names; Thanksgiving turkey becomes Dragon Boat Festival zongzi; Lady Gaga in *American Horror Story* becomes Leslie Cheung in *Farewell My Concubine*. The authors try to preserve feature similarity while changing the cultural referent, such as mapping one holiday destination to another rather than replacing it with an unrelated landmark.

Each language's annotation team contains two annotators and one reviewer with relevant linguistic expertise. Verification criteria include grammatical correctness, fluency, and logical coherence. The paper does not report inter-annotator agreement, revision counts, disagreement categories, time per item, or item-level localization rationales.

### Composition and Slices

Each target language has 804 questions. Localized subsets contain 231 Chinese, 181 Russian, 197 French, 197 Spanish, and 212 Arabic items. The variation is interpreted as reflecting cultural distance from the English source, but that interpretation is not independently tested.

The benchmark assigns nine capability types. General knowledge is 27.0%, professional knowledge 26.7%, generation and creation 17.8%, language comprehension 9.0%, code skills 6.1%, logical reasoning 5.5%, mathematics 4.0%, chit chat 2.9%, and harmlessness 1.1%. This breadth is useful, but aggregate language scores are dominated by the largest categories. A model can improve a headline score without improving thin slices such as harmlessness or mathematics.

Root-verb analysis shows that expression patterns differ across languages. Chinese, for example, has multiple verbs corresponding to English “write.” This is useful evidence that lexical distribution changes under natural localization. It does not by itself establish equivalent difficulty or construct coverage.

### Pairwise Evaluation

OMGEval follows AlpacaEval's pairwise design. A baseline model and candidate model answer the same prompt. GPT-4 receives the instruction and both outputs, then ranks them. Win rate and standard error are the principal outputs. The paper initially planned to use `text-davinci-003` but changed to GPT-3.5-Turbo after the earlier model was retired.

Pairwise comparison is easy to interpret only within its declared envelope. Changing the baseline can change win rates. Changing answer order, judge version, system prompt, decoding settings, language competence, or verbosity preference can change decisions. A score of 55.5 therefore means the inspected GPT-4 configuration preferred GPT-4 over the GPT-3.5-Turbo baseline at that rate across the defined sets; it is not an absolute 55.5% competence score.

The official README includes a structured-output prompt whose prose says the result will be executed as Python. Production reuse should never execute judge text. A safe harness should parse a strict schema, reject extra keys/text, randomize answer order, preserve both judge orders, and treat malformed outputs as failures rather than code.

### Reported Model Results

Table 4 includes English plus the five target languages, with full and localized values for target languages. GPT-4 records 58.9 in English; its target-language full scores range from 52.1 in Russian to 58.3 in Chinese, while localized scores range from 47.2 in Spanish to 62.8 in Chinese. The paper reports average full/localized values of 55.5 and 54.6.

GPT-3.5-Turbo is the baseline at 50.0 throughout. Guanaco-13B has the strongest listed open-model average at 14.8 full and 13.7 localized. Chimera-Inst-Chat-13B is 12.9 and 10.9. Phoenix-Inst-Chat-7B is 7.9 and 10.8. PolyLM-Chat-13B is 7.3 and 10.2. The remaining open models are lower. The authors interpret the gap as evidence that open multilingual models struggle with cultural nuances.

That interpretation is plausible but not uniquely identified. The gap can also include baseline strength, judge preference, prompt formatting, output length, model age, tokenization, safety behavior, and uneven category composition. No matched compute, modern model refresh, multiple judge, or per-slice error taxonomy is reported.

### Human Comparison

For each of Chinese and Spanish, the authors sample 50 localized and 50 other examples. GPT-3.5-Turbo and PolyLM-Chat-13B outputs are compared by humans and GPT-4 using grammatical accuracy, relevance, informativeness, and factual correctness. Reported precision/recall/F1 values are 0.81/0.94/0.88 for Chinese full, 0.70/0.91/0.79 for Chinese localized, 0.92/0.92/0.91 for Spanish full, and 0.90/0.90/0.89 for Spanish localized.

This supports a limited alignment claim for one model pair and two languages. It does not validate all OMGEval judgments. The lower Chinese-localized F1 is especially important: the culturally specific slice appears harder for judge-human alignment than the Chinese full slice.

### Official Release and Reproducibility

The official repository at the inspected commit contains language data, evaluator-prompt material, figures, model outputs, a README, and an MIT license. The README documents construction and example rankings, but it also contains older Chinese-only figures and a to-do list that does not fully align with the v2 paper. The repository's latest observed commit is from 2024, whereas the paper was revised in 2026. This version gap should be tracked explicitly.

No end-to-end reproduction was run. The review did not call model APIs, regenerate outputs, rerun GPT-4 judging, audit every item, or recalculate table statistics. Repository availability therefore supports artifact access, not deterministic reproduction of the paper.

### Ethical and Operational Context

The paper states that annotators and reviewers received approximately USD 2,500 in total and recommends research-only use aimed at improving LLMs across cultural backgrounds. The benchmark includes harmlessness and culturally sensitive material, but the paper provides limited documentation on annotator demographics, consent, exposure to harmful content, dispute resolution, dataset takedown, or representativeness within each language community.

Deployment-grade use would need a dataset card, contributor and labor process, content-risk review, locale-specific governance, correction path, and evidence that benchmark scores do not become high-stakes proxies for people or cultures.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Culturally localized questions improve the relevance of multilingual generative evaluation beyond direct translation. | Author conceptual claim | E2-E3 | Strong design rationale and concrete examples; user relevance and measurement equivalence were not directly compared. | Medium-high |
| C2 | OMGEval provides 804 open-ended questions for each of five target languages with human verification. | Author dataset claim | E2-E3, S4 | Paper and repository agree on 804 final questions; item-level verification logs were not audited. | High for reporting |
| C3 | GPT-4 substantially outperforms the listed open multilingual models under the OMGEval pairwise protocol. | Author empirical claim | E4 | Table 4 directly supports the ranking within the tested baseline/judge/model envelope. | High for transcription; low for current generality |
| C4 | GPT-4 judgment aligns with human evaluation on the tested multilingual samples. | Author empirical claim | E5 | Supported for Chinese and Spanish, one model pair, and 100 examples per language; broader wording should be narrowed. | Medium-high |
| C5 | Localized subsets expose cultural-performance gaps not visible in generic translated prompts. | Author interpretation | E3-E5 | Some models decline and others improve; the design is informative but not a clean causal estimate of culture understanding. | Medium |
| C6 | A benchmark score should include judge uncertainty and finite support. | Reviewer interpretation | E4-E5, E9 | Directly motivated by single-judge compression and related interval-confidence work. | High as governance recommendation |
| C7 | Benchmark test items must be isolated from on-policy feedback. | Reviewer implementation observation | E7, E9 | Necessary to preserve evaluation meaning when judge-mediated development loops are used. | High |
| C8 | Official repository availability does not establish end-to-end reproducibility. | Reviewer evidence assessment | E7 | Release artifacts are useful, but model/API versions and a complete executable table-reproduction path were not validated. | High |

## Methodology

- `Research objective`: Preserve a schema-complete review of OMGEval and translate its evidence into bounded multilingual-evaluation, calibration, and dataset-governance choices.
- `Sources inspected`: Complete arXiv v2 PDF, official full-paper HTML, metadata HTML, TeX/source archive, official repository README/tree/license at a pinned commit, four primary related-paper records, live Black Lake and Black-Lake-Data rules, and exactly three related Black Lake manuscripts.
- `Discovery strategy`: Enumerate archive PDFs with `rg --files -g "*.pdf"`, collapse parent directories into paper units, draw a uniform zero-based PowerShell `Get-Random` index, inspect adjacent metadata, run multi-layer dedup checks, repair missing full-paper HTML, build a local extraction cache, inspect paper sections/tables, verify public primary records, and search related DEP entries by concrete conceptual overlap.
- `Inclusion criteria`: Sources establishing paper identity, dataset construction, quantitative results, human comparison, ethics, limitations, official artifact availability, repository rules, duplicate status, or direct calibration/feedback-loop overlap.
- `Exclusion criteria`: Abstract-only technical evidence, secondary summaries where primary records were available, unrelated keyword hits, unverified model/code behavior, and local source files from the public deposit.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, replication, and provenance analysis.
- `Evidence handling`: Evidence IDs distinguish author claims, reported results, official release observations, reviewer interpretations, related-DEP synthesis, and process evidence. Quantitative values were cross-checked in extracted PDF/source text and official full-paper HTML.
- `Uncertainty handling`: Model results remain author reported; judge-human agreement is not generalized beyond the sampled languages/model pair; the 805-to-804 transition, version gap, and missing reproduction evidence remain visible.
- `Extraction process`: Local missing-only extraction used `pypdf`, HTML text extraction, and source-package extraction. All three text representations completed. No network fallback was used by the cache stage.
- `Source-integrity methodology`: The selected unit was initially partial because full-paper HTML was missing. A valid 2,528,158-byte PDF with `%PDF-` header and trailing `%%EOF` was preserved. Official full-paper HTML, metadata HTML, and source package were fetched locally. The 117,918-byte HTML produced 31,670 body characters, 72 heading/section markers, seven paper-structure terms, and a valid article/main/LaTeXML marker. No `.part` files remain.
- `Random selection`: 75,777 PDF candidates collapsed to 75,776 unique paper units; uniform zero-based selected index 39,883.
- `Dedup validation`: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data were searched for arXiv ID, DOI, exact title, and slug; exclusions 0 and reselections 0; public-safe 24-hour cutoff marker 2026-07-16.
- `Version control`: Paper pinned to v2; official repository pinned to `f4dfb6d188e711e72ba7453757209df808122e8e`; related DEP paths pinned by repository-relative location.
- `Cross-checking`: Metadata checked between local and public arXiv records; tables checked across PDF/source text and official HTML; repository inventory and license checked at the pinned commit; related-entry concepts checked in their manuscripts.
- `Safety handling`: Examples are offline, schema-validating, human-reviewed, and benchmark-leakage aware. No model text is executed as code, no test item enters training, and no automated production approval is proposed.
- `Reviewer stance`: Critical paper report, DEP-ready preservation, benchmark-governance analysis, implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: OMGEval's motivation, data construction, cultural localization, capability slices, pairwise judge protocol, reported model/human results, official release, limitations, and bounded implementation implications.
- `Temporal boundary`: Sources inspected through 2026-07-17; paper pinned to v2 revised 2026-01-30; official repository pinned to a 2024 commit.
- `Evidence limits`: No model inference, API judging, human annotation, full item audit, dataset execution, statistical recomputation, end-to-end reproduction, or current-model benchmark run. A separate page-image render was unavailable; figures were assessed through full text, captions, tables, and official HTML.
- `Assumptions`: The canonical PDF, HTML, and source package describe the same v2 paper; extracted table values preserve the source; the paper-linked GitHub repository is official.
- `Constraints`: Public artifacts cannot expose local paths, usernames, machine identifiers, local timezone labels, precise local execution timestamps, source files, caches, raw model outputs, or licensed third-party data.
- `Out of scope`: Declaring a state-of-the-art current leaderboard, certifying fairness across cultures, reproducing model/API costs, redistributing the benchmark source bundle, or using scores for high-stakes decisions about people.
- `Intended use`: Research review, benchmark design, evaluation engineering, dataset governance, calibration planning, DEP deposition, and follow-on replication.
- `Audience`: Multilingual NLP researchers, evaluation engineers, dataset maintainers, model-governance reviewers, localization specialists, and Black Lake maintainers.
- `Reproducibility boundary`: Source transcription and repository inventory are reproducible from public locators; paper results require pinned historical model/API access, prompts, outputs, judge configuration, and statistics not validated here.
- `Data sensitivity`: Public research data with potential cultural, religious, discriminatory, and harmful-content exposure; governance must account for annotator and community impact.

## Observations

- `Observed pattern`: Localization is the benchmark's distinctive mechanism. It treats multilinguality as language plus cultural context, not translation alone.
- `Measurement tension`: Replacing cultural referents can improve naturalness while changing item difficulty, expected background knowledge, or answer scope. Relevance and invariance are separate objectives.
- `Judge tension`: GPT-4 enables scale but compresses multidimensional quality into one pairwise preference and may share preferences with the evaluated GPT family.
- `Support pattern`: The capability distribution is dominated by knowledge and generation. Thin categories need separate intervals and should not inherit confidence from aggregate language totals.
- `Human-evidence pattern`: Chinese-localized F1 is lower than Chinese full-set F1, which is direct evidence that cultural slices can alter judge reliability.
- `Version pattern`: The paper's 2026 revision postdates the latest observed official repository commit, so paper, data, prompt, and output versions need an explicit compatibility matrix.
- `Safety observation`: The documented evaluator prompt's language about executing returned Python is unsuitable for a secure harness; judge output must be treated as untrusted data.
- `Open question`: Can native-speaker human panels and multiple independent judges produce stable per-slice intervals without making evaluation cost prohibitive?

## Considerations

Evaluation governance should begin with construct definitions. “Multilingual capability” can mean linguistic fluency, factual knowledge, cultural familiarity, instruction following, safety, or preference alignment. OMGEval mixes these within one aggregate. A release card should preserve language, capability, localization status, judge, baseline, prompt, and support count as separate dimensions.

Judge governance should include answer-order randomization, repeated sampling, multiple judge families, blinded human calibration, disagreement preservation, verbosity controls, self-enhancement audits, and strict output-schema parsing. A judge interval can expose instability but cannot certify absence of shared cultural or model-family bias.

Dataset governance should record who localized each item, why a cultural substitution was considered analogous, which variants were rejected, how disputes were resolved, and how communities can request corrections. Localization should not imply that one annotator group represents every speaker of a language.

Benchmark contamination is a major operational risk. If OMGEval failures are used to generate training data, the immutable test split must remain inaccessible to training and feedback services. A development set can support OViP-style on-policy improvement, but it needs distinct IDs, access controls, and lineage.

Cost and availability matter. Historical GPT model versions and API behavior may be unavailable. Reproduction should therefore archive allowed aggregate outputs, prompts, model identifiers, judge identifiers, order seeds, parser versions, and cost records without storing secrets or disallowed raw data.

## Strengths

- Directly targets open-ended multilingual generation rather than only discriminative or exact-match tasks.
- Makes cultural localization an explicit step with concrete categories and examples.
- Uses human verification after machine translation rather than presenting raw translation as final data.
- Preserves full and localized subsets, enabling at least one culturally focused comparison.
- Reports a capability taxonomy and distribution rather than treating the item set as undifferentiated.
- Compares proprietary and open multilingual models under one declared pairwise protocol.
- Includes a direct human comparison for Chinese and Spanish and reports precision, recall, and F1.
- Releases data, prompts, figures, model outputs, documentation, and an MIT-licensed repository snapshot.
- States annotation compensation, research-use intent, and the five-language limitation.

## Weaknesses

- Five languages do not support broad claims about global multilinguality, especially low-resource languages outside the selected set.
- The transition from 805 source entries to 804 final questions is not explained in the inspected paper.
- Capability distribution is uneven; aggregate results can obscure thin or safety-relevant categories.
- Human verification lacks reported inter-annotator agreement, disagreement taxonomy, item-level rationale, and labor detail.
- GPT-4 is both a compared model and the evaluator family, creating a self-enhancement/conflict-of-interest risk.
- One baseline at 50 makes win rates baseline dependent and not absolute competence estimates.
- Human comparison covers only Chinese and Spanish, one model pair, and 100 items per language.
- Judge order, verbosity, style, repeated-sample variance, and cross-judge disagreement are not comprehensively reported.
- The official repository snapshot predates paper v2 and no complete pinned reproduction path was validated.
- No current-model refresh, leakage audit, measurement-invariance analysis, or community-level cultural validity study is presented.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish item-level localization provenance | Dataset governance | Cultural substitutions change construct meaning | Auditable relevance and correction | More annotation overhead | Native-speaker review, rationale taxonomy, revision history |
| Test measurement invariance | Cross-language validity | Localized items may not be equivalent in difficulty or meaning | Separates cultural relevance from ranking comparability | Requires more human data | Anchor items, differential item analysis, matched human panels |
| Use multi-judge randomized adjudication | Judge validity | One GPT-4 configuration can encode order, style, and family bias | More robust preference estimates | Higher inference cost | Swap order, repeat seeds, judge ensemble, disagreement intervals |
| Add per-slice intervals and support cards | Statistics | Aggregate scores hide sparse categories | Honest uncertainty and release thresholds | Wider intervals for thin slices | Bootstrap or conformal intervals with held-out human labels |
| Expand human calibration to all languages | Evidence breadth | Current validation covers Chinese and Spanish only | Direct evidence for every target language | Recruiting cost and labor governance | Pre-register balanced samples and report per-slice agreement |
| Pin an executable reproduction manifest | Reproducibility | Paper and repository versions diverge | Deterministic table regeneration | Historical APIs may be unavailable | Container, prompts, outputs, parser, seeds, checksums, cost log |
| Replace executable output handling | Security | Judge text is untrusted | Prevents code execution and injection | Strict parsers may reject more outputs | JSON schema validation, no `eval`, malformed-output tests |
| Separate immutable test and adaptive development sets | Contamination control | Feedback loops can overfit the benchmark | Preserves benchmark meaning | Less training data | Access-control tests and lineage audit |
| Balance capability categories | Coverage | Knowledge dominates thin safety/math/chat slices | More decision-useful diagnostics | New-item quality risk | Targeted collection, native review, hidden test refresh |

## Potential Implementations

1. `Multilingual Judge Calibration Card`
   - `User`: Evaluation and model-release teams.
   - `Goal`: Publish OMGEval results with explicit judge uncertainty rather than a single win rate.
   - `Core mechanism`: Randomize answer order, query multiple pinned judges, calibrate against native-speaker labels, and attach interval width and disagreement to every language/capability/localization slice.
   - `Required inputs`: Versioned prompts, candidate/baseline outputs, judge IDs, human calibration labels, slice metadata, and immutable split IDs.
   - `Outputs`: Slice cards, win-rate intervals, judge-human agreement, disagreement matrix, and withhold/review flags.
   - `Risk controls`: No execution of model text, no raw personal data, blinded judging, independent human audit, and fail-closed parsing.
   - `Evaluation`: Seeded order-bias, verbosity, malformed-output, low-support, and judge-disagreement fixtures.

2. `Cultural Localization Ledger`
   - `User`: Benchmark maintainers and localization reviewers.
   - `Goal`: Preserve why and how each culturally specific item changed.
   - `Core mechanism`: Store source prompt, translated draft, localization categories, analogical rationale, reviewer decisions, community notes, and version lineage in a schema separate from the public test answer path.
   - `Required inputs`: Public benchmark items, annotator-approved rationales, locale tags, review outcomes, and correction requests.
   - `Outputs`: Public-safe dataset card, item provenance hashes, unresolved-dispute queue, and revision changelog.
   - `Risk controls`: Consent-aware contributor records, harmful-content controls, no unnecessary identity exposure, and takedown/correction process.
   - `Evaluation`: Sampled native-speaker audit, rationale completeness, inter-reviewer agreement, and measurement-invariance study.

3. `Leakage-Safe Feedback Sandbox`
   - `User`: Teams improving models from multilingual failure slices.
   - `Goal`: Use model-specific errors without contaminating immutable evaluation items.
   - `Core mechanism`: Allow OViP-style failure-guided candidate generation only from development IDs, run native-speaker and independent-judge review, and block any test ID or semantic near-duplicate from training export.
   - `Required inputs`: Development prompts, model outputs, judge disagreement, test-item hashes, similarity index, and reviewer decisions.
   - `Outputs`: Audited development examples, rejection reasons, lineage manifest, and contamination report.
   - `Risk controls`: Immutable test denylist, semantic-duplicate checks, human approval, content safety, rate limits, and append-only provenance.
   - `Evaluation`: Synthetic leakage attacks, paraphrase matching, judge-bias audit, and held-out benchmark stability.

## Three Ways to Exercise This Research

1. `Judge-order audit`: Objective: measure answer-order sensitivity on a bounded public subset. Inputs: public OMGEval prompts, two fixed public model-output sets, two pinned judges, and native-speaker labels for a small calibration sample. Method: judge both answer orders with fixed seeds, compare disagreement and human agreement by language/localization slice, and compute intervals. Output: order-bias and calibration card. Success criterion: every published slice reports support, order effect, judge disagreement, and human agreement. Stop condition: withhold ranking if order effect exceeds the predeclared tolerance. Safety boundary: offline evaluation; never execute judge output.
2. `Localization invariance lab`: Objective: distinguish cultural relevance from changed difficulty. Inputs: a small matched set of source and localized prompts, bilingual/native reviewers, declared constructs, and blinded model outputs. Method: annotate answerability, cultural fit, difficulty, and intended capability; compare source/localized results using predeclared anchors. Output: item-level invariance and relevance report. Success criterion: substitutions are either supported as comparable or explicitly labeled non-equivalent. Stop condition: remove items with unresolved construct drift. Safety boundary: compensated review and content-risk screening.
3. `Leakage-guard challenge`: Objective: verify that an adaptive development loop cannot ingest benchmark test items. Inputs: separate development/test IDs, paraphrased canaries, a similarity checker, and synthetic judge feedback. Method: attempt exact, normalized, translated, and paraphrased leakage; require the export gate to reject all canaries while admitting reviewed development examples. Output: contamination test report. Success criterion: 100% seeded leakage rejection with explainable reasons. Stop condition: disable training export after any test-item leak. Safety boundary: synthetic/public data only and no model deployment.

## Example MVP Product

- `Product name`: CultureBench Evidence Card
- `Target user`: Multilingual evaluation engineers, benchmark maintainers, and model-governance reviewers.
- `Problem`: A single multilingual win rate hides judge uncertainty, cultural-localization choices, sparse slices, baseline dependence, and benchmark contamination risk.
- `Core workflow`: Import a versioned result bundle; validate prompt/output/judge manifests; randomize and compare answer order; compute per-language/capability/localization support and intervals; compare judges with a native-speaker calibration set; check test-item lineage; export a public-safe evidence card for human decision.
- `Data requirements`: Public or approved prompts and outputs, immutable split IDs, language/capability/localization tags, pinned judge metadata, human calibration labels, and no unnecessary personal data.
- `Architecture`: Local batch CLI with a schema validator, non-executing judge parser, order-randomization module, interval/calibration engine, lineage/leakage guard, and Markdown/JSON exporter. Raw outputs remain local; public cards contain aggregate, sanitized evidence.
- `Success metrics`: 100% manifest completeness; deterministic reruns; every slice exposes support and uncertainty; all seeded order/judge/leakage failures detected; zero use of `eval` or code execution; zero private-path or secret findings; reviewer can approve, withhold, or request more evidence from one card.
- `Risk controls`: Offline-only MVP, allowlisted inputs, strict JSON schema, immutable test denylist, blinded human audit, fail-closed missing data, no autonomous deployment, and explicit statement that benchmark preference is not absolute cultural competence.
- `Limitations`: Inherits judge and human-label bias, cannot prove cultural representativeness, may have wide intervals for thin slices, depends on access to historical outputs, and does not establish production safety.
- `MVP boundary`: Evaluation evidence and contamination control only; no model training, no automatic release approval, no high-stakes decisions, and no source-file redistribution.
- `Deployment model`: Local CLI in an authorized evaluation environment.
- `Evaluation plan`: Unit tests for schemas/parsers, synthetic order and malformed-output fixtures, public subset smoke test, bilingual human audit, and seeded leakage challenge.
- `Failure modes`: Correlated judges, stale model versions, incomplete slice tags, hidden prompt changes, human-panel disagreement, semantic near-duplicate leakage, and thresholds chosen after viewing results.
- `Maintenance plan`: Pin judges and parsers, version dataset cards, refresh development items without changing hidden test IDs, retain prior evidence cards, and require governance review for schema/threshold changes.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| OMGEval | Primary reviewed paper | Culturally localized multilingual generative evaluation and reported evidence | https://arxiv.org/abs/2402.13524 |
| blcuicall/OMGEval | Official release | Data, evaluator prompts, figures, model outputs, README, and license | https://github.com/blcuicall/OMGEval |
| AlpacaFarm | Direct methodological predecessor | Pairwise feedback simulation and automatic evaluation lineage | https://arxiv.org/abs/2305.14387 |
| MT-Bench and Chatbot Arena | LLM-judge neighbor | Position, verbosity, self-enhancement, reasoning, and human-agreement context | https://arxiv.org/abs/2306.05685 |
| Belebele | Multilingual benchmark | Broad parallel-language comprehension coverage and comparison baseline | https://arxiv.org/abs/2308.16884 |
| M3Exam | Multilingual benchmark | Multilingual, multimodal, multilevel examination context | https://arxiv.org/abs/2306.05179 |
| Judge Conformal - DEP-E | Related Black Lake DEP 1 of exactly 3 | Adds interval-valued LLM judging and uncertainty routing | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md |
| PAC Confidence - DEP-E | Related Black Lake DEP 2 of exactly 3 | Adds finite-sample support, coverage, and shift-envelope requirements | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md |
| OViP Preference - DEP-E | Related Black Lake DEP 3 of exactly 3 | Adds judge-mediated on-policy feedback-loop and contamination governance | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2402.13524 | Title, authors, version, subject, abstract, DOI, source links, and license locator | 2026-07-17 | Canonical metadata |
| R2 | https://arxiv.org/pdf/2402.13524 | Complete paper, figures, tables, methods, results, ethics, limitations, and references | 2026-07-17 | Verified private copy inspected; not deposited |
| R3 | https://arxiv.org/html/2402.13524 | Public full text, tables, headings, and cross-check | 2026-07-17 | Verified private copy inspected; not deposited |
| R4 | https://arxiv.org/e-print/2402.13524 | Source structure, tables, and extraction cross-check | 2026-07-17 | Private source package inspected; not deposited |
| R5 | https://doi.org/10.48550/arXiv.2402.13524 | Persistent identifier | 2026-07-17 | ArXiv-issued DOI |
| R6 | https://github.com/blcuicall/OMGEval | Official release inventory and documentation | 2026-07-17 | Inspected at commit `f4dfb6d188e711e72ba7453757209df808122e8e` |
| R7 | https://github.com/blcuicall/OMGEval/blob/f4dfb6d188e711e72ba7453757209df808122e8e/LICENSE | Repository license | 2026-07-17 | MIT; third-party content rights still separate |
| R8 | https://arxiv.org/abs/2305.14387 | AlpacaFarm/AlpacaEval context | 2026-07-17 | Primary record inspected |
| R9 | https://arxiv.org/abs/2306.05685 | LLM-as-a-judge bias and human-preference context | 2026-07-17 | Primary record inspected |
| R10 | https://arxiv.org/abs/2308.16884 | Parallel multilingual benchmark context | 2026-07-17 | Primary record inspected |
| R11 | https://arxiv.org/abs/2306.05179 | Multilingual/multilevel benchmark context | 2026-07-17 | Primary record inspected |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, source-withholding, DEP, log, report, and commit rules | 2026-07-17 | Live authority |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-07-17 | Live authority |
| R14 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository and related-context authority | 2026-07-17 | Live authority |
| R15 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md | Interval-valued judge synthesis | 2026-07-17 | Related DEP 1 of exactly 3; source basis https://arxiv.org/abs/2509.18658 |
| R16 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md | Finite-sample confidence and shift synthesis | 2026-07-17 | Related DEP 2 of exactly 3; source basis https://arxiv.org/abs/2011.00716 |
| R17 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md | Preference-loop and judge-governance synthesis | 2026-07-17 | Related DEP 3 of exactly 3; source basis https://arxiv.org/abs/2505.15963 |

## Appendix

### Replication Checklist

- [ ] Pin arXiv v2, the official repository commit, and an explicit data/prompt compatibility map.
- [ ] Verify why 805 source entries become 804 final items and record all excluded/modified IDs.
- [ ] Record immutable test and separate development IDs with hashes and access controls.
- [ ] Pin candidate/baseline model snapshots, tokenizers, templates, decoding, language prompts, and output hashes.
- [ ] Replace any executable parsing with strict non-executing JSON-schema validation.
- [ ] Randomize answer order and preserve both order results with declared seeds.
- [ ] Run at least two independently governed judge families and repeated judge samples.
- [ ] Collect blinded native-speaker calibration labels for all five languages and every capability/localization slice.
- [ ] Report support, interval width, judge disagreement, human agreement, and abstention per slice.
- [ ] Test measurement invariance and difficulty drift between source and localized items.
- [ ] Audit verbosity, style, self-enhancement, safety-refusal, and cultural-preference bias.
- [ ] Publish aggregate costs, failures, parser rejects, and seed-level results without secrets or local paths.
- [ ] Prove through canary tests that no immutable test item or paraphrase enters training or feedback generation.
- [ ] Release a public-safe dataset card, annotation protocol, labor/compensation note, correction path, and version changelog.

### Public-Safe Process Record

- Selection used `rg --files -g "*.pdf"`, 75,777 PDF candidates, 75,776 unique parent units, and uniform zero-based index 39,883.
- Dedup checks found no prior OMGEval automation log, Report-Mark, DEP-E manuscript, or live Black-Lake-Data match. Exclusions and reselections were zero.
- The selected unit began partial because full-paper HTML was missing. Official full-paper HTML, metadata HTML, and source package were repaired locally; the valid PDF was preserved.
- PDF, HTML, companion-record, extraction-cache, and no-partial-file gates passed.
- PDF, HTML, TeX/source archive, extracted text, cache, local locations, and raw source files remain private and were not deposited.
- The official repository was inspected but not cloned, executed, or used to rerun results.
- No current leaderboard, full reproducibility, peer-review status, or cultural-fairness certification is implied.

### Metric Interpretation Notes

- `Win rate`: Pairwise preference frequency against a declared baseline under a declared judge configuration; not absolute capability.
- `Localization subset`: Items manually adapted for target-language cultural context; not automatically measurement-equivalent across languages.
- `Judge-human F1`: Agreement for one sampled comparison task; not proof of universal judge reliability.
- `Support`: Number and diversity of items/labels inside a language, capability, localization, model, and judge slice.
- `Interval`: Uncertainty representation for a declared calibration envelope; it does not remove systematic bias.
- `Benchmark contamination`: Use of test items or near-duplicates in training, selection, feedback, or prompt optimization that invalidates held-out interpretation.
