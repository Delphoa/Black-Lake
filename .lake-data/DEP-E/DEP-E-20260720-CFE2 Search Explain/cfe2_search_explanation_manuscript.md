---
title: "CFE2 Search Explanations - DEP-E"
generated_at: "2026-07-20 (public-safe date; exact execution timestamp withheld)"
artifact_type: "DEP-E research manuscript"
primary_subject: "Counterfactual query editing for local search-result explanations"
source_status: "Verified complete private PDF and full-paper HTML; source files withheld locally"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-20"
temporal_cutoff: "Evidence inspected through 2026-07-20"
primary_url: "https://arxiv.org/abs/2301.10389"
stable_identifier: "arXiv:2301.10389v3; DOI:10.1145/3664190.3672508"
confidence_summary: "High for paper identity, method, and transcribed results; moderate for implementation implications; low for untested causal-faithfulness or cross-retriever claims"
safety_scope: "Research synthesis only; production search explanations require privacy, faithfulness, stability, and human-evaluation controls"
distribution_notes: "Public-safe derived Markdown only; no PDF, HTML, source archive, extracted text, cache, or private provenance file is included"
---

# CFE2 Search Explanations - DEP-E

## Source Metadata

- **Primary paper:** *CFE2: Counterfactual Editing for Search Result Explanation*. The arXiv metadata uses *Counterfactual Editing for Search Result Explanation*.
- **Authors:** Zhichao Xu, Hemank Lamba, Qingyao Ai, Joel Tetreault, and Alex Jaimes.
- **Identifiers:** arXiv `2301.10389v3`; arXiv DOI https://doi.org/10.48550/arXiv.2301.10389; published DOI https://doi.org/10.1145/3664190.3672508.
- **Publication:** ICTIR 2024, pages 145-155.
- **Version history:** first submitted 2023-01-25; version 3 submitted 2024-06-28.
- **Primary records:** [arXiv metadata](https://arxiv.org/abs/2301.10389), [PDF](https://arxiv.org/pdf/2301.10389), [full-paper HTML](https://arxiv.org/html/2301.10389), [source endpoint](https://arxiv.org/e-print/2301.10389), [ACM DOI](https://doi.org/10.1145/3664190.3672508), and [OpenReview](https://openreview.net/forum?id=G3a15oOyJQ&noteId=86yHStWtLa).
- **Supporting records:** [ICTIR 2024 accepted papers](https://www.ictir2024.org/program/accepted-papers) and [University of Utah NLP publications](https://nlp.cs.utah.edu/publications/).
- **Local source state:** complete after bounded repair. The valid existing PDF was preserved; official full-paper HTML and companion provenance files were added to the private archive. Original source materials were withheld locally.
- **Review boundary:** source-grounded review and implementation analysis. No experiment or codebase was rerun, and a bounded primary-source search did not establish an official CFE2 code repository.

## Evidence Ledger

| ID | Evidence type | Source | Supports | Confidence and boundary |
|---|---|---|---|---|
| S1 | arXiv metadata | [Abstract and version record](https://arxiv.org/abs/2301.10389) | Title, authors, dates, identifier, abstract contribution, publication linkage | High for metadata; abstract is not treated as the full paper |
| S2 | Primary paper | [arXiv PDF](https://arxiv.org/pdf/2301.10389) | Formal problem, method, datasets, metrics, tables, ablations, human study, limitations | High for what the authors report; results not independently reproduced |
| S3 | Primary paper | [arXiv full-paper HTML](https://arxiv.org/html/2301.10389) | Searchable corroboration of S2 and section-level claim tracing | High; official full-paper representation passed the local integrity gate |
| S4 | Primary source endpoint | [arXiv source](https://arxiv.org/e-print/2301.10389) | Private source-package verification and figure/table inspection | High for document integrity; source package is not redistributed |
| S5 | Publisher metadata | [ACM DOI](https://doi.org/10.1145/3664190.3672508) | Final title, venue, publication identity | High for bibliographic identity |
| S6 | Public review record | [OpenReview](https://openreview.net/forum?id=G3a15oOyJQ&noteId=86yHStWtLa) | Public submission provenance | Supporting evidence, not the final publication |
| S7 | Venue record | [ICTIR accepted papers](https://www.ictir2024.org/program/accepted-papers) | Venue corroboration | Supporting evidence |
| S8 | Institutional record | [Utah NLP publications](https://nlp.cs.utah.edu/publications/) | Author-group publication corroboration | Supporting evidence |
| S9 | Related DEP | [Beyond XAI manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Beyond%20XAI/beyond_xai_manuscript.md) | Faithfulness/accessibility distinction and limits of local proxies | High for the inspected DEP synthesis; its own primary source is arXiv `2602.24176` |
| S10 | Related DEP | [OViP Preference manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md) | Targeted counterfactual verification and shortcut-leakage risks | High for the inspected DEP synthesis; its own primary source is arXiv `2505.15963` |
| S11 | Related DEP | [REAL Temporal Graph review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-REAL%20Temporal%20Graph/2606.10694-whitepaper-review.md) | Beam-search provenance and observed/derived/counterfactual separation | High for the inspected DEP synthesis; its own primary source is arXiv `2606.10694` |
| S12 | Private processing evidence | Integrity and repair records, path withheld | File sizes, PDF markers, HTML document structure, bounded repair outcome | High for integrity status; no private artifact is published |

## Executive Summary

CFE2 explains a local search-result ordering by editing the query until a lower-ranked document overtakes a higher-ranked document. It identifies influential query tokens, replaces them with a masked-language model conditioned on the counterfactual document, verifies the rank flip against the search model, and selects a low-perplexity flipping edit. The resulting query is meant to expose a concise contrast: the original wording favors one result, while a nearby alternative favors the other.

The paper reports near-perfect pairwise FlipRate across five datasets and stronger closeness, clarity, and fluency than generation-oriented baselines in many comparisons. Its practical contribution is a bounded diagnostic that can be recomputed against the model rather than a free-form explanation that cannot be checked. Its central limitation is equally important: a decision-boundary flip does not establish why the model produced the original ranking, and it does not establish causal or global faithfulness.

The best implementation framing is therefore **counterfactual search probe**, not **model truth explanation**. A useful system would expose the edited token, both score vectors, the exact document pair, the model/index version, stability under repeated generation, and a plain-language uncertainty notice. It should never log sensitive raw queries by default.

## Detailed Summary

### Problem formulation

For an original query `q`, a higher-ranked document `d`, and a lower-ranked document `d'`, the system seeks an edited query `q'` for which the search relevance ordering reverses: the counterfactual document becomes more relevant than the original higher-ranked document. The evaluation is pairwise and restricted to documents in the observed result set rather than a claim about the entire corpus.

### System components

The reported search model is CL-DRD, a single-vector dense retriever. A ColBERT-inspired masker scores query-token importance using maximum similarity against document-token representations. The most influential query tokens are masked in stages. A DistilBERT masked-language model, conditioned by prepending the counterfactual document to the masked query, proposes replacements with beam search. Each proposal is rescored by the search model; proposals that flip the pairwise order remain candidates, and the system favors a low-perplexity edit. CFE2+ adds task-adaptive pretraining on the target corpus.

The default configuration uses a 66M-parameter DistilBERT editor and beam size 10. An ablation substitutes a 110M-parameter BERT editor. Another ablation varies beam size and reports quality measures largely stabilizing between sizes 5 and 10 while runtime continues to rise.

### Evaluation design

The experiments cover MS MARCO, FEVER, Natural Questions, FiQA, and SciFact. The paper reports about 20.4k, 53.3k, 1.8k, 4.6k, and 1.2k triplets respectively in that order. Candidate document pairs are drawn from the top five results. The baselines are Mask-only, MaxFlip, Summary, and GenEx.

The main metrics are FlipRate; cosine similarity and BERTScore-F1 for closeness; RelFluency, expressed as a perplexity ratio with an ideal near 1; and runtime per edit. The paper also uses human judgments of fluency, clarity, semantic closeness, and syntactic closeness.

### Reported outcomes

Reported CFE2 FlipRate is `0.998` on MS MARCO, `0.999` on Natural Questions, `0.999` on FiQA, `0.999` on FEVER, and `1.000` on SciFact. Reported cosine similarity ranges from `0.909` to `0.963`, and BERTScore-F1 ranges from `0.933` to `0.963`. Runtime ranges from `0.257` to `0.828` seconds per edit in the main table. The source reports many statistically significant closeness improvements, but several baselines already produce FlipRate between roughly `0.986` and `1.000`, making ceiling effects material.

The SciFact human study includes 50 triplets and at least three qualified Mechanical Turk responses per triplet. It reports CFE2+ above GenEx for fluency (`3.83` versus `3.76`), clarity (`3.88` versus `3.59`), semantic closeness (`3.64` versus `3.12`), and syntactic closeness (`3.61` versus `3.35`). Reported p-values are very small, but kappa values of `0.08-0.22` indicate slight-to-fair inter-annotator agreement.

The BERT editor is reported at `0.503` seconds per FiQA edit versus `0.352` for DistilBERT, about 42.8% slower. The rank-position ablation reports FlipRate `1.000`, `1.000`, `1.000`, and `0.999` for FiQA positions two through five; one of 1,148 examples reportedly fails. A qualitative example changes a car-related query toward the near-synonym “automobile,” flips the ordering, yet adds little useful explanatory information because both documents address essentially the same need.

## Key Claims and Evidence

1. **Claim: counterfactual editing can make a local ranking contrast directly testable.** The formal flip condition and rescoring loop in S2-S3 support this. The evidence establishes a pairwise intervention, not a causal account of the entire ranker.
2. **Claim: CFE2 achieves very high rank-flip success across the five tested corpora.** The main result table in S2-S3 reports `0.998-1.000` FlipRate. This is an author-reported result and shares a ceiling region with several baselines.
3. **Claim: CFE2 generally preserves the original query better than generation-based baselines.** CosSim, BERTScore-F1, RelFluency, and human ratings in S2-S3 support this direction across many comparisons. Metric choice and low human agreement limit the strength of the conclusion.
4. **Claim: task-adaptive pretraining can improve the editor.** CFE2+ results and the human comparison in S2-S3 provide support, most visibly in domain-specific generation. The human study is small and limited to SciFact.
5. **Claim: the approach is efficient enough for interactive investigation.** Main-table runtimes below one second per edit support a prototype use case on the reported hardware and workload. End-to-end online latency, concurrency, privacy filtering, and production indexing were not evaluated.
6. **Reviewer inference: rank-flipping edits should be presented as probes rather than faithful causal explanations.** This follows from the pairwise objective, the qualitative synonym failure, and the faithfulness cautions in S9. It is an interpretation, not an author claim.

## Methodology

### Selection and deduplication

The run enumerated PDF candidates with `rg --files -g "*.pdf"`, treated each PDF parent directory as a paper unit, derived identifiers from filenames and nearby metadata, excluded used arXiv IDs, and drew uniformly with PowerShell `Get-Random`. There were 75,778 PDFs, 75,776 unique parent units, 222 units excluded by 999 observed used IDs, 185 identifier-incomplete units withheld, and 75,369 eligible units. The selected zero-based eligible index was `64,032`. No duplicate rejection or reselection occurred.

The initial parent-directory-only identifier pass produced no candidate draw because identifiers were primarily present in PDF filenames. The mapping was corrected to use filenames plus parent directories before randomness was invoked. Dedup then checked the selected arXiv ID, both DOIs, exact and normalized titles, the `CFE2` token, and slug variants across Black Lake logs, reports, lake data, staging, automation memory, and the fetched Black-Lake-Data default-branch state. It found no match and no same-paper marker on or after the public-safe cutoff date 2026-07-19.

### Source-integrity gate

The initial source unit was `partial`: the PDF was present and valid, but full-paper HTML was missing. A bounded one-paper repair retained the valid PDF and fetched official arXiv full-paper HTML, metadata HTML, and a source package into the private archive. Each companion artifact received one bounded request with a 250 MiB total ceiling, a 50 MiB partial ceiling, and a 180-second request timeout. No fallback was required and no partial file remained.

The final PDF is 1,014,492 bytes, begins with `%PDF-`, and ends with `%%EOF`. The full-paper HTML is 551,159 bytes, contains 98,103 body characters after script/style removal, includes a document marker, contains 47 heading markers, and includes the structure terms Introduction, Methods, Methodology, Results, Discussion, Conclusion, and References. These processing details come from private integrity records; the private paths and source files are withheld.

### Review and synthesis

The review traced identity claims to metadata and publisher records; method, experiment, and limitation claims to the full paper; and the implementation synthesis to explicitly labeled reviewer analysis. Figures and tables were inspected from the verified source representations. Three related DEP entries were selected only after their repository contents and primary-source bases were inspected. Source claims, source inconsistencies, and reviewer inferences are kept distinct.

## Scope, Constraints, and Assumptions

- The evaluated explanation target is a pairwise ordering within a current top-five result set, not a listwise explanation of the whole ranking.
- The empirical search model is CL-DRD. The paper describes the framework as model-agnostic, but the inspected experiments do not establish behavior across multiple retriever architectures.
- The BERT ablation changes the editor, not the search model.
- The study does not report an online search deployment, user-session outcomes, click behavior, longitudinal trust effects, or production-scale throughput.
- The human study covers one dataset and reports slight-to-fair agreement. Worker demographics, compensation context, and dependence structure were not sufficiently established in the inspected sources for stronger claims.
- No official implementation repository was established by the bounded primary-source search. This is not a claim that none exists.
- No result in this manuscript was independently reproduced. Numerical values are transcribed source claims unless explicitly labeled as reviewer calculations.
- Production implementation assumes lawful access to queries and documents, aggressive data minimization, redaction, retention limits, and review for domain-specific harms.

## Observations

1. The explicit rescoring condition makes every proposed explanation falsifiable at the pair level: either the edit flips the ordering under the recorded model state or it does not.
2. FlipRate is almost saturated for both CFE2 and several baselines. Closeness, usefulness, stability, and human agreement carry more diagnostic value than flip success alone.
3. Conditioning the editor on the lower-ranked document makes the candidate targeted, but it also creates a route for lexical copying and decision-boundary exploitation.
4. Beam size displays a practical knee: quality largely stabilizes near 5-10 while runtime continues to increase. The reported configuration uses 10.
5. A semantically trivial substitution can satisfy the mathematical objective without improving a person's understanding of the ranking.
6. Table 7 prints BERT-editor `CosSim 9.959` despite a stated zero-to-one metric range. The inconsistency is preserved rather than silently corrected.

## Considerations

- **Faithfulness:** label the output as a verified local counterfactual, not as the reason the model ranked the documents.
- **Stability:** repeat generation across seeds, beam sizes, index snapshots, and nearby document pairs; disclose when valid edits disagree.
- **Privacy:** search queries can contain sensitive personal information. Minimize collection, redact before processing, and avoid raw-query logs.
- **Safety:** filter edits for toxic, discriminatory, medical, financial, legal, and identity-sensitive content before display.
- **Auditability:** preserve model version, index version, tokenizer, original scores, counterfactual scores, edited positions, generation parameters, and review state.
- **Evaluation:** combine automatic metrics with calibrated human assessment and task outcomes. Do not use statistical significance alone as evidence of practical usefulness.
- **Governance:** keep exploratory engineering output separate from customer-facing explanations until domain and policy review is complete.

## Strengths

- Clear, machine-verifiable pairwise objective.
- Modular masking, editing, and rescoring design.
- Broad evaluation over five retrieval datasets.
- Strong reported flip performance with generally close edits.
- Direct comparison with masking and generation baselines.
- Human evaluation and multiple ablations expose some quality/runtime tradeoffs.
- Qualitative failure discussion acknowledges that objective success can be uninformative.

## Weaknesses

- A flip is not a faithful causal explanation of the original ranking.
- Search-model generality is asserted more broadly than the single-retriever experiment demonstrates.
- Pairwise top-five evaluation omits listwise and full-corpus behavior.
- FlipRate has a strong ceiling across methods.
- Human evaluation is small, single-domain, and low-agreement.
- Automatic closeness/fluency metrics can miss meaning shifts and practical usefulness.
- Online user outcomes and production constraints are not tested.
- Reproduction is limited by the lack of an established official code record in the inspected sources.
- The impossible `9.959` CosSim entry weakens table-level auditability.

## Potential Improvements

1. Test multiple sparse, dense, late-interaction, hybrid, and reranking systems while holding the editing pipeline constant.
2. Add listwise and full-corpus validation so a pairwise flip cannot conceal unrelated ranking changes.
3. Measure stability across seeds, beam sizes, nearby result pairs, index updates, and paraphrases.
4. Introduce entailment and intent-preservation checks in addition to cosine and BERTScore similarity.
5. Run larger preregistered human studies across domains with stronger annotation protocols, compensation disclosure, and agreement analysis.
6. Compare edits against attribution methods, feature ablations, and causal interventions to quantify when a local flip tracks model-relevant evidence.
7. Publish an authoritative correction for the CosSim table inconsistency and a reproducible implementation with versioned models and evaluation scripts.
8. Evaluate real search tasks: debugging time, error detection, reformulation quality, trust calibration, and harm discovery.

## Potential Implementations

1. **Relevance-engineering debugger:** inspect an unexpected pairwise ranking and obtain multiple verified edits with score deltas and stability warnings.
2. **Query-reformulation assistant:** offer privacy-filtered alternatives that shift toward a selected result intent, clearly separating suggestions from explanations.
3. **Regression-test generator:** convert stable counterfactual edits into model-version tests that detect changes in known decision boundaries.
4. **Retriever comparison bench:** run the same document pair and candidate edits through sparse, dense, hybrid, and reranking systems.
5. **Explanation audit queue:** route only low-stability, high-sensitivity, or policy-relevant counterfactuals to human reviewers.
6. **Counterfactual provenance service:** store observed inputs, derived importance/scores, generated alternatives, and reviewer decisions as distinct record types.

## Three Ways to Exercise This Research

1. **Reproduce the reported pairwise task.** On a licensed or synthetic corpus, construct query/higher-document/lower-document triplets, implement the exact flip predicate, and compare CFE2-style editing with masking and generation baselines using FlipRate, closeness, fluency, and latency.
2. **Stress-test semantic faithfulness.** Build adversarial cases involving synonyms, named entities, negation, ambiguity, and sensitive attributes; have reviewers label whether a successful flip is informative, intent-preserving, safe, and stable.
3. **Run a shadow debugging pilot.** Integrate the probe into an internal search-evaluation environment, with no customer-facing output, and measure whether engineers find ranking defects faster without over-interpreting the explanation.

## Example MVP Product

### Product name

**RankFlip Lab**

### Target user and problem

The target user is a relevance engineer investigating why two documents appear in an unexpected order. Existing score dashboards show that a difference exists but often do not provide a compact, testable contrast. RankFlip Lab generates and verifies nearby query edits that reverse only the selected pair, helping the engineer formulate hypotheses about model sensitivity.

### Core workflow

1. The engineer selects an approved synthetic or redacted query and two documents from a fixed result snapshot.
2. The service records the retriever, index, tokenizer, and score versions.
3. A masker proposes influential query tokens; an editor produces bounded candidates.
4. A verifier recomputes both document scores and retains only exact pairwise flips.
5. A quality layer measures semantic closeness, fluency, edit size, toxicity, sensitive-attribute changes, and stability.
6. The interface shows the original/edited query diff, before/after scores, competing valid edits, and a “local counterfactual, not causal proof” notice.
7. The engineer accepts, rejects, or escalates the probe; the system stores the decision without retaining unredacted query content.

### Data requirements

- Approved query-document triplets from synthetic, licensed, or properly governed evaluation data.
- Versioned search-model and index access.
- A masked-language model that is permitted for the deployment context.
- Human usefulness and safety labels for calibration.
- A small adversarial suite covering ambiguity, synonyms, negation, named entities, and sensitive attributes.

### Architecture

- **Snapshot adapter:** freezes query, documents, rank positions, model version, and index version.
- **Importance service:** computes query-token importance against the pair.
- **Candidate editor:** performs bounded beam search with length, token, and latency limits.
- **Flip verifier:** rescales and verifies the before/after inequality.
- **Quality and safety layer:** checks intent preservation, semantic distance, fluency, toxicity, privacy, and stability.
- **Provenance store:** separates observed, derived, counterfactual, and reviewer-authored fields.
- **Review UI:** displays diffs, receipts, limitations, and disposition controls.

### Success metrics

- Verified FlipRate on held-out pairwise tasks.
- Human-rated usefulness and intent preservation.
- Stability across repeated generation and model/index snapshots.
- Median and p95 end-to-end latency.
- Unsafe or sensitive edit rate before and after filtering.
- Engineer time-to-diagnosis and confirmed defect yield.
- Calibration: the rate at which displayed uncertainty corresponds to reviewer disagreement.

### Risk controls

- Synthetic/redacted inputs by default; no raw customer query logging.
- Strict beam, token, runtime, and request limits.
- Sensitive-attribute and domain-risk filters before display.
- Explicit local-counterfactual labeling and prohibition on causal wording.
- Versioned receipts and reproducible rescoring.
- Human review for externally visible output.
- Automatic suppression when edits are unstable, semantically distant, or policy-sensitive.

### Limitations

The MVP cannot prove why the model made its original decision. It covers selected pairs rather than the full ranking, depends on the quality of the editor and similarity checks, and may surface lexical shortcuts instead of meaningful intent changes. Domain transfer, multilingual behavior, and user trust require separate evaluation.

### Implementation phases and stop conditions

- **Phase 1:** offline synthetic benchmark. Stop if valid flips routinely fail intent-preservation review.
- **Phase 2:** internal shadow debugger. Stop if engineers interpret outputs causally despite interface safeguards or if privacy controls cannot prevent raw-query retention.
- **Phase 3:** limited governed deployment. Stop if disagreement, instability, or unsafe-edit rates exceed calibrated thresholds.

## Related Research and Reading

1. [Beyond XAI](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Beyond%20XAI/beyond_xai_manuscript.md) - use its faithfulness and accessibility distinctions to constrain how local counterfactuals are described. It cautions against treating a persuasive proxy as a complete account of system behavior.
2. [OViP Preference](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md) - use its targeted counterfactual and verification framing to test whether edits isolate the intended semantic variable or exploit shortcuts.
3. [REAL Temporal Graph](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-REAL%20Temporal%20Graph/2606.10694-whitepaper-review.md) - use its state/provenance separation to represent original observations, model-derived scores, beam candidates, and hypothetical flips without collapsing them.

These three entries have concrete conceptual overlap and were inspected directly. They are the only related DEP entries selected for this deposit.

## Source References

1. Xu, Zhichao; Lamba, Hemank; Ai, Qingyao; Tetreault, Joel; Jaimes, Alex. *CFE2: Counterfactual Editing for Search Result Explanation*. arXiv `2301.10389v3`, ICTIR 2024. https://arxiv.org/abs/2301.10389.
2. Full-paper PDF: https://arxiv.org/pdf/2301.10389.
3. Full-paper HTML: https://arxiv.org/html/2301.10389.
4. arXiv source endpoint: https://arxiv.org/e-print/2301.10389.
5. arXiv DOI: https://doi.org/10.48550/arXiv.2301.10389.
6. Published ACM DOI: https://doi.org/10.1145/3664190.3672508.
7. OpenReview record: https://openreview.net/forum?id=G3a15oOyJQ&noteId=86yHStWtLa.
8. ICTIR 2024 accepted papers: https://www.ictir2024.org/program/accepted-papers.
9. University of Utah NLP publications: https://nlp.cs.utah.edu/publications/.
10. *Beyond XAI* DEP manuscript: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Beyond%20XAI/beyond_xai_manuscript.md.
11. *OViP Preference* DEP manuscript: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md.
12. *REAL Temporal Graph* DEP review: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-REAL%20Temporal%20Graph/2606.10694-whitepaper-review.md.
13. Black Lake repository rules: https://github.com/Delphoa/Black-Lake/blob/main/README.md.
14. Black Lake lake-data rules: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md.
15. Black-Lake-Data repository rules: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md.
16. Private integrity, repair, and provenance records: path withheld; processing evidence only; no original source file was uploaded.

## Appendix

### Integrity receipt

| Artifact | Final verification | Distribution |
|---|---|---|
| PDF | 1,014,492 bytes; `%PDF-` header; trailing `%%EOF` | Private archive only |
| Full-paper HTML | 551,159 bytes; 98,103 body characters; document marker; 47 headings; seven structure terms | Private archive only |
| Metadata HTML | 42,975 bytes | Private archive only |
| Source package | 1,434,369 bytes; 30 inspected entries | Private archive only |
| Partial files | Zero after bounded repair | None distributed |

### Selected quantitative results

| Dataset | FlipRate | CosSim | BERTScore-F1 | RelFluency | Seconds/edit |
|---|---:|---:|---:|---:|---:|
| MS MARCO | 0.998 | 0.909 | 0.933 | 1.774 | 0.258 |
| Natural Questions | 0.999 | 0.934 | 0.962 | 1.159 | 0.257 |
| FiQA | 0.999 | 0.957 | 0.963 | 1.110 | 0.352 |
| FEVER | 0.999 | 0.944 | 0.949 | 0.972 | 0.364 |
| SciFact | 1.000 | 0.963 | 0.962 | 1.478 | 0.828 |

All values above are transcribed source claims, not reproduced measurements. RelFluency is a perplexity ratio whose ideal is near 1, so neither a uniformly larger nor a uniformly smaller value is automatically better without that reference point.

### Source inconsistency and open questions

- The BERT-editor ablation prints `CosSim 9.959`, outside the documented metric range. No guessed correction is substituted.
- Does a counterfactual edit remain valid across index refreshes and retriever families?
- How often does a rank flip expose a real relevance defect versus a lexical shortcut?
- Can human usefulness agreement be improved with clearer task definitions and domain expertise?
- What uncertainty representation best prevents users from treating a verified local probe as a causal explanation?
