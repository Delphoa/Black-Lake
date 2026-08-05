---
title: "mLSTM NLI - DEP-E"
generated_at: "2026-08-06"
artifact_type: "DEP-E research manuscript"
primary_subject: "Source-grounded review of a match-LSTM for natural language inference."
source_status: "Verified complete local PDF and full-paper HTML; source files withheld locally"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-06"
temporal_cutoff: "Evidence inspected through 2026-08-06"
primary_url: "https://arxiv.org/abs/1512.08849"
stable_identifier: "arXiv:1512.08849v2; DOI:10.48550/arXiv.1512.08849"
confidence_summary: "High for identity, method, and reported SNLI setup; moderate for reported performance and implementation transfer because no rerun was performed."
safety_scope: "Research synthesis only; synthetic or authorized evaluation examples."
distribution_notes: "Public-safe derived Markdown only; PDF, HTML, metadata, source package, extracted text, and caches are withheld locally."
---

# mLSTM NLI - DEP-E

## Source Metadata

| ID | Field | Value |
|---|---|---|
| S1 | Work | *Learning Natural Language Inference with LSTM* |
| S2 | Authors | Shuohang Wang; Jing Jiang |
| S3 | Platform and dates | arXiv; submitted 2015-12-30; revised 2016-11-10 |
| S4 | Stable identifier | arXiv:1512.08849v2; DOI:10.48550/arXiv.1512.08849 |
| S5 | Primary record | https://arxiv.org/abs/1512.08849 |
| S6 | Full-paper representation | https://ar5iv.labs.arxiv.org/html/1512.08849 |
| S7 | Official implementation | https://github.com/shuohangwang/SeqMatchSeq |
| S8 | Benchmark | https://nlp.stanford.edu/projects/snli/ |
| S9 | Source state | Complete PDF and full-paper HTML verified privately; source files withheld; TeX/source package unavailable |
| S10 | Access date | 2026-08-06 |

The official arXiv full-paper HTML route returned 404 during the bounded source repair. The approved ar5iv representation passed the local full-paper HTML gate and was used for searchable cross-checking. The arXiv metadata/abstract page remains provenance only and is not treated as the paper document.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | https://arxiv.org/abs/1512.08849 | arXiv metadata | Title, authors, version history, abstract, identifier | Source identity and dates | High | Metadata is not full-paper evidence |
| E2 | https://arxiv.org/pdf/1512.08849 | Primary paper PDF | Method, equations, data splits, tables, figures, gate analysis, limitations | Technical and quantitative claims | High | Results were not independently rerun |
| E3 | https://ar5iv.labs.arxiv.org/html/1512.08849 | Full-paper HTML fallback | Searchable section-level corroboration of E2 | Method and results cross-check | High | Fallback rendering can contain conversion artifacts |
| E4 | https://github.com/shuohangwang/SeqMatchSeq | Official author repository | README, dependencies, preprocessing, commands, historical runtime requirements | Implementation availability and reproducibility boundary | High | Code was not executed; repository is historical |
| E5 | https://nlp.stanford.edu/projects/snli/ | Official benchmark page | NLI definition, SNLI scale, labels, distribution and license | Dataset context | High | Benchmark page does not validate the paper’s training run |
| E6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-CFE2%20Search%20Explain/cfe2_search_explanation_manuscript.md | Related DEP manuscript | Counterfactual ranking probe and token-importance synthesis | Cross-source implementation bridge | Medium | Related DEP is derived synthesis, not independent rerun |
| E7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260715-Token%20Cooccurrence%20RAG/2606.30093-whitepaper-review.md | Related DEP review | Proposal-corrector retrieval, token graph routing, provenance | Cross-source retrieval bridge | Medium | Related DEP reports no verified official implementation |
| E8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260714-CompressKV%20Semantic%20Heads/2606.24467-whitepaper-review.md | Related DEP review | Attention-signal selection, evidence retention, memory allocation | Cross-source memory bridge | Medium | Related DEP’s results were not independently rerun |

## Executive Summary

The paper introduces match-LSTM, an LSTM architecture for natural language inference that aligns each hypothesis word with an attention-weighted representation of the premise and carries the resulting match signals through a gated recurrent state. Its central claim is that the model can retain decisive mismatches while forgetting routine matches, improving classification of entailment, contradiction, and neutral relationships.

On the SNLI split used by the authors, mLSTM with hidden dimension 300 reports 86.1% test accuracy, above the authors’ 82.6% implementation of word-by-word attention at dimension 150 and above the earlier reported 83.5% attention result. The evidence is direct for what the paper reports and weaker for modern transfer: the work uses one benchmark, fixed historical embeddings, and an implementation stack that was not rerun here.

Reviewer interpretation: the lasting contribution is a selective state-retention pattern for evidence matching, not the claim that LSTM gates are inherently faithful explanations. This pattern can inform modern retrieval, ranking, and memory systems when paired with explicit provenance, intervention tests, and fallback behavior.

## Detailed Summary

### Problem

Natural language inference determines whether a hypothesis follows from a premise, contradicts it, or remains neutral. Earlier neural approaches compressed each sentence to one vector before matching. The paper argues that this makes it difficult to give more weight to content words, decisive subject or event mismatches, or hypothesis words that have no plausible premise alignment.

### Background and mechanism

Each sentence is first processed by an LSTM. For each hypothesis position, an attention mechanism computes a weighted combination of premise hidden states. The attention score depends on the premise state, the current hypothesis state, and the previous match state. The concatenated attention vector and hypothesis state form the input to a second LSTM, the mLSTM. Its input, forget, and output gates regulate which match evidence enters, persists, and reaches the final classifier.

The paper adds a fixed NULL vector to the premise so a hypothesis word can align with no premise word. It uses GloVe embeddings and approximates unseen-word embeddings by averaging nearby known-word vectors within a window of nine tokens. Embeddings are not updated during learning, reducing trainable parameters at the cost of a crude unknown-word approximation.

### Data and experiments

The source describes SNLI as 570,152 sentence pairs with entailment, contradiction, neutral, and disagreement labels. After removing disagreement-labeled pairs, the authors use 549,367 training pairs, 9,842 development pairs, and 9,824 test pairs. They train three-class classifiers with Adam, initial learning rate 0.001, decay ratio 0.95 per iteration, batch size 30, and hidden dimensions 150 and 300.

The comparison includes the authors’ implementation of word-by-word attention, mLSTM, mLSTM with bi-LSTM sentence encoders, and mLSTM using raw word embeddings instead of sentence-encoder hidden states. The paper reports training, development, and test accuracy plus a confusion matrix for the 300-dimensional model.

### Results

| Model | Hidden dimension | Train | Dev | Test |
|---|---:|---:|---:|---:|
| Word-by-word attention, authors’ implementation | 150 | 85.5 | 83.3 | 82.6 |
| mLSTM | 150 | 91.0 | 86.2 | 85.7 |
| mLSTM with bi-LSTM sentence modeling | 150 | 91.3 | 86.6 | 86.0 |
| mLSTM | 300 | 92.0 | 86.9 | 86.1 |
| mLSTM with word embeddings | 300 | 88.6 | 85.4 | 85.3 |

The paper reports a statistically significant improvement at the 0.001 level for the comparable 150-dimensional mLSTM versus the authors’ word-by-word-attention implementation. It also reports more confusion involving neutral than between entailment and contradiction, identifying neutral as a difficult class.

### Gate analysis

The authors inspect alignment weights and gate vectors on three examples and report corpus-level summaries. Input gates average 0.287 for stop words and 0.347 for other content words; the paper gives a higher value for the negation word “not.” Forget-gate averages are reported as 0.446 for entailment, 0.507 for neutral, and 0.536 for contradiction. The interpretation is that ordinary matches need not persist, while mismatches that signal contradiction or neutral relations may be carried to the final state.

These measurements are evidence of learned internal correlations. They do not prove that the gates cause the intended classifications or that the same semantics transfer outside SNLI.

### Conclusion and limitations

The paper concludes that mLSTM improves SNLI classification by retaining important word-level matching results. Its stated limitation is data hunger: preliminary experiments on the smaller SICK dataset were not good, which the authors attribute to learning most parameters from scratch apart from pre-trained embeddings. Reviewer-identified limits include one benchmark, one language, historical preprocessing, fixed embeddings, limited ablations by modern standards, no reported uncertainty intervals, and no independent rerun in this review.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | mLSTM performs sequential, word-by-word premise/hypothesis matching with a gated match state. | Author claim | E2, E3 | Directly supported by the model definition and equations. | High |
| C2 | mLSTM reaches 86.1% test accuracy on the reported SNLI split at hidden dimension 300. | Author-reported quantitative result | E2, E3 | The table supports the transcription; no independent rerun was performed. | High for transcription; medium for reproducibility |
| C3 | The mLSTM improves over the authors’ comparable word-by-word-attention implementation. | Author-reported comparative result | E2, E3 | Reported test difference is 85.7% versus 82.6%; implementation parity is asserted by the paper, not rechecked here. | Medium-high |
| C4 | Gate statistics show that match importance is selectively retained. | Author interpretation | E2, E3 | Gate patterns are consistent with the interpretation but are correlational inspection, not a causal intervention. | Medium |
| C5 | The official author repository makes the historical implementation inspectable. | Source metadata and implementation observation | E4 | README confirms code, preprocessing, dependencies, commands, and Docker guidance; code was not run. | High |
| C6 | Selective match-state retention is a reusable design pattern for retrieval and memory systems. | Reviewer interpretation | E6, E7, E8 plus E2 | The bridge is conceptually supported; any modern performance benefit remains a hypothesis. | Medium |

## Methodology

- Research objective: Preserve a source-grounded review of mLSTM and derive bounded implementation and synthesis insights without redistributing local source files.
- Sources inspected: Verified private PDF and full-paper HTML, arXiv metadata, official author repository README, official SNLI page, and exactly three related Black Lake DEP manuscripts.
- Discovery strategy: Enumerated local PDF candidates with rg --files -g "*.pdf", treated each PDF parent directory as one paper unit, derived the identifier from the filename and metadata README, and selected uniformly with PowerShell Get-Random.
- Random selection record: 75,960 PDF candidates; 75,957 unique paper units; zero-based selected unit index 55,698; first draw accepted; no manual convenience selection.
- Inclusion criteria: Candidate had a canonical arXiv identifier, a valid PDF after inspection, a full-paper HTML document after the required repair gate, and no prior Black Lake Arxiv DEP artifact or recent marker.
- Exclusion criteria: Duplicate IDs, titles, DOIs, or slugs; same-paper artifacts; 24-hour markers through 2026-08-05; invalid or abstract-only source units; and source units that could not be repaired to complete PDF plus full-paper HTML.
- Deduplication and reselection validation: Scanned .logs, .reports, .lake-data, .staging, automation memory, live Black Lake exact-ID search, and live Black-Lake-Data exact-ID search. No matching arXiv ID, DOI, normalized title, or slug was found. Excluded count and reselection count were both zero.
- Source-integrity repair: The PDF was preserved because it passed the size, header, and EOF checks. The official arXiv full-paper HTML route returned 404; the approved ar5iv fallback was fetched through the archive collector and passed the size, body, marker, heading, and structure checks. The source package was unavailable.
- Analytical approach: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication planning.
- Evidence handling: Claims are mapped to ledger IDs and separated into author claims, reported measurements, source metadata, reviewer interpretation, and proposed implementation hypotheses.
- Uncertainty handling: No independent reproduction or code execution is implied. Conversion fallback, historical dependencies, small-sample interpretability inspection, and cross-domain transfer gaps are stated explicitly.
- Cross-source synthesis: CFE2, Token Cooccurrence RAG, and CompressKV Semantic Heads were selected for concrete overlap in token salience, evidence routing, attention/state retention, and bounded verification.

## Scope, Constraints, and Assumptions

- Scope: The mLSTM method, SNLI experiment, gate analysis, official implementation status, limitations, and synthesis with three related DEP entries.
- Temporal boundary: Public evidence accessed through 2026-08-06; paper revision v2 dated 2016-11-10.
- Evidence limits: No experiment, source code, Docker image, or dataset download was executed in this review. The source package was unavailable locally after bounded repair.
- Assumptions: The arXiv v2 paper and the cited official repository correspond to the same implementation lineage; the reported table values are transcribed accurately from the inspected PDF and HTML.
- Constraints: Source files are private local archive materials and cannot be redistributed in this public DEP. The historical code stack has dependency and licensing constraints.
- Out of scope: Claims of production readiness, modern state-of-the-art ranking, clinical/legal decision support, or causal faithfulness of attention/gates.
- Intended use: DEP research deposit, follow-on replication planning, and safe architecture ideation.
- Audience: NLP researchers, retrieval engineers, evidence-system reviewers, and agents maintaining source-grounded research records.
- Reproducibility boundary: The public URLs identify the primary work and code, but a full rerun requires the historical toolchain, dataset, embeddings, preprocessing, and model settings.
- Operational boundary: Examples are toy-scale and defensive; they do not make autonomous high-stakes inferences.
- Data sensitivity: Public research metadata and benchmark context; no private query, user, or raw dataset content is deposited.

## Observations

- Observed pattern: The mLSTM’s main architectural change is not attention alone but attention followed by a separate recurrent state that can preserve or discard local matches.
- Observed pattern: The 300-dimensional model’s 86.1% test score is accompanied by 86.9% development accuracy, while the smaller comparable model already reaches 85.7%, suggesting both state design and capacity contribute.
- Technical implication: The NULL alignment and mismatch retention ideas provide explicit hooks for logging unmatched and persisted evidence spans.
- Contradiction or tension: The paper presents gates as interpretable evidence filters, but the reported analysis does not intervene on the gates or establish that the visual patterns are necessary for the decision.
- Cross-source observation: The related DEP entries independently emphasize that local salience signals are useful only when paired with verification, provenance, and fallback paths.
- Open question: Whether a match-state controller improves modern transformer reranking after equalizing tokenizer, compute, data, and calibration budgets remains untested here.

## Considerations

- Data and licensing: SNLI is distributed under a Creative Commons Attribution-ShareAlike 4.0 International license according to the official benchmark page. Any reuse must preserve applicable attribution and share-alike terms; the official repository README also states Singapore Management University copyright.
- Reproducibility: Torch7, Python 2.7, external GloVe resources, and historical scripts create environment risk. A modern reproduction should pin versions and record hashes rather than silently porting the method.
- Evaluation: Aggregate accuracy hides class-conditional and domain-shift failures. Neutral, negation, numeric, entity, and contradiction cases deserve stratified reporting.
- Interpretability: Attention and gate values are inspection signals. They should be accompanied by perturbation, counterfactual, or removal tests before being presented as explanations.
- Operational risk: A match-state filter can omit evidence that becomes relevant later. Retrieval and memory systems should retain provenance and provide a larger-budget or full-context fallback.
- Privacy and safety: NLI or evidence-matching services may process sensitive text. Local processing, minimization, redaction, retention limits, and human review are safer defaults.

## Strengths

- The mechanism directly targets a plausible weakness of sentence-vector matching.
- The paper provides equations, baselines, ablations, a confusion matrix, and an analysis of alignment and gate values.
- The reported experiment uses a large labeled benchmark and a clearly stated train/dev/test split.
- The official repository README gives concrete preprocessing, dependency, and usage information.
- The match-state abstraction remains useful for connecting local evidence to a final sequence decision.

## Weaknesses

- The principal evidence is one benchmark and one historical experimental stack.
- The reported 86.1% result was not independently reproduced in this review.
- Gate visualizations and averages do not establish causal faithfulness.
- Fixed GloVe embeddings and nearby-token averaging may limit semantic coverage and transfer.
- The implementation’s Torch7 and Python 2 requirements increase maintenance and reproducibility burden.
- The preliminary SICK result was poor, indicating sensitivity to dataset scale or domain.
- Accuracy and a small set of gate statistics do not fully expose calibration, robustness, or worst-case errors.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Port the model to a maintained framework with pinned data preprocessing | Reproducibility | Removes historical runtime friction without changing the experiment first | Re-run capability | Porting may alter numerics | Compare tokenization, parameter counts, and outputs on fixed examples |
| Add hard neutral, negation, numeric, and entity-swap subsets | Evaluation | Neutral is reported as difficult and mismatch handling is central | Better failure localization | Requires careful labels | Report per-subset accuracy and calibration |
| Intervene on match-state gates and retained spans | Interpretability | Correlation is not necessity | Stronger causal evidence | Interventions can create distribution shift | Compare deletion, masking, and counterfactual replacements |
| Compare against modern cross-encoders and transformer rerankers | Comparative performance | Historical baselines no longer define the field | Current relevance | Compute and dataset leakage risk | Equalize data, tokenizer, and compute budgets |
| Add out-of-domain and low-resource transfer tests | Generalization | SICK warning suggests data/domain sensitivity | Transfer boundary | Requires licensed or public datasets | Report zero-shot and few-shot degradation |
| Add abstention and recoverable evidence fallback | Safety and deployment | A wrong omission can be harder to detect than a low score | Safer system behavior | More memory and latency | Test on adversarial and long-context cases |

## Potential Implementations

1. Evidence-matching audit layer. User: an NLP engineer or reviewer. Goal: compare a claim or hypothesis with retrieved evidence and expose salient matches and mismatches. Mechanism: modern cross-attention plus a compact match state, with explicit NULL or unmatched spans and per-token provenance. Inputs: authorized text pairs, tokenizer/model revision, evidence identifiers, and evaluation labels. Outputs: pairwise score, evidence spans, mismatch list, uncertainty, and audit receipt. Risk controls: local processing, redaction, no raw-text logging by default, human review for sensitive domains, and abstention on low confidence. Evaluation: stratified NLI tests, removal tests, paraphrase stability, and cross-domain holdout.
2. Retrieval proposal-corrector. User: a retrieval engineer. Goal: find a compact, traceable evidence set for a question. Mechanism: cheap token or graph proposal, dense correction, and mLSTM-style state retention for the evidence currently being assembled. Inputs: authorized corpus, token graph or sparse index, dense embeddings, provenance map, and query. Outputs: ranked passages, retained spans, discarded-but-recoverable candidates, and rationale metadata. Risk controls: preserve source identifiers, keep a recoverable lower tier, enforce corpus access controls, and abstain when sources disagree. Evaluation: recall of gold evidence, answer entailment, citation completeness, latency, and retention budget.
3. Budgeted contradiction triage. User: a human quality reviewer. Goal: prioritize cases where a possible contradiction or neutral relation deserves deeper review. Mechanism: match-state mismatch signals trigger additional retrieval, counterfactual tests, or a larger context budget. Inputs: authorized premise/hypothesis pairs, model scores, provenance, and reviewer policy. Outputs: triage queue, evidence diff, recommended next test, and review disposition. Risk controls: no automatic adverse action, clear uncertainty labels, audit logs without raw sensitive text, and mandatory human disposition. Evaluation: reviewer agreement, missed-contradiction rate, calibration, and time-to-resolution.

## Three Ways to Exercise This Research

1. Synthetic pair matching: create toy premise/hypothesis pairs with explicit entailment, contradiction, neutral, negation, and unmatched-token cases; implement the match-state inspector; and verify that reported evidence spans are stable under token order-preserving paraphrases. Success is correct handling of the synthetic labels; stop if labels become ambiguous.
2. Public benchmark replication plan: use the official SNLI distribution and the public repository only in an authorized environment; pin preprocessing, embeddings, model settings, and random seeds; and compare a modern port with the paper’s table. Success is a reproducible report with mismatches explained; stop if licensing or dependency constraints are unresolved.
3. Retrieval-memory ablation: on a synthetic or authorized text corpus, compare full evidence, fixed-size match-state retention, proposal-corrector routing, and recoverable paging. Success is a measured quality/latency/retention trade-off with provenance intact; stop before using sensitive production text.

## Example MVP Product

- Product name: Match-State Evidence Audit
- Target user: NLP or retrieval engineers reviewing model evidence behavior.
- Problem: A single global relevance score does not show which local matches or mismatches drive a decision.
- Core workflow: ingest an authorized text pair; compute token/span alignment; retain a bounded match state; display retained and omitted evidence; run optional safe paraphrase or removal checks; export an audit receipt.
- Data requirements: public or authorized text pairs, labels for evaluation, tokenizer/model version, source identifiers, and retention policy.
- Architecture: local tokenizer and encoder; alignment module; gated match-state or transformer reranker; provenance store; intervention runner; reviewer UI; structured receipt writer.
- Success metrics: per-class F1, hard-case recall, calibration error, explanation stability, evidence-span agreement, p95 latency, and percentage of receipts with complete provenance.
- Risk controls: no autonomous high-stakes decisions, local-by-default text handling, redaction, access controls, source citations, uncertainty labels, recoverable context, and human approval.
- Limitations: the MVP cannot prove causal faithfulness, may inherit dataset shortcuts, depends on the quality of labels and tokenization, and does not guarantee transfer beyond its evaluation distribution.
- MVP boundary: synthetic and public evaluation only; no production user text, model retraining, or irreversible evidence deletion.
- Deployment model: local CLI or notebook with optional review UI.
- Evaluation plan: smoke tests, held-out hard subsets, deletion/counterfactual tests, reviewer study, and cross-domain validation.
- Failure modes: misaligned spans, neutral examples forced into binary labels, shortcut-driven mismatch scores, stale model versions, and provenance loss.
- Maintenance plan: pin model/tokenizer versions, refresh evaluation slices, review drift, and rerun the evidence-perturbation suite before upgrades.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| CFE2 Search Explain | Related Black Lake DEP | Counterfactual query edits and explicit pairwise rank-flip verification | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-CFE2%20Search%20Explain/cfe2_search_explanation_manuscript.md |
| Token Cooccurrence RAG | Related Black Lake DEP | Token-level proposal routing, provenance, dense correction, and multi-hop evidence assembly | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260715-Token%20Cooccurrence%20RAG/2606.30093-whitepaper-review.md |
| CompressKV Semantic Heads | Related Black Lake DEP | Attention-signal selection and bounded evidence retention under memory constraints | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260714-CompressKV%20Semantic%20Heads/2606.24467-whitepaper-review.md |
| Reasoning about entailment with neural attention | Methodological neighbor | Preceding attention-based NLI architecture discussed by the paper | https://arxiv.org/abs/1509.06664 |
| A large annotated corpus for learning natural language inference | Benchmark paper | Introduces the SNLI corpus used by the reviewed work | https://aclanthology.org/D15-1075/ |
| Learning Natural Language Inference with LSTM code | Official implementation | Historical preprocessing and mLSTM usage reference | https://github.com/shuohangwang/SeqMatchSeq |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1512.08849 | Identity, authors, dates, abstract, version | 2026-08-06 | Canonical metadata; abstract-only page not used as the paper document |
| R2 | https://arxiv.org/pdf/1512.08849 | Full paper method, tables, figures, limitations | 2026-08-06 | Complete PDF verified privately; not redistributed |
| R3 | https://ar5iv.labs.arxiv.org/html/1512.08849 | Full-paper HTML cross-check | 2026-08-06 | Approved fallback after official HTML 404; not redistributed |
| R4 | https://github.com/shuohangwang/SeqMatchSeq | Code availability and historical requirements | 2026-08-06 | Official author repository; not executed |
| R5 | https://nlp.stanford.edu/projects/snli/ | Dataset definition, scale, labels, license | 2026-08-06 | Official benchmark page |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-CFE2%20Search%20Explain/cfe2_search_explanation_manuscript.md | Counterfactual ranking and token-importance synthesis | 2026-08-06 | Related DEP reviewed in the repository |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260715-Token%20Cooccurrence%20RAG/2606.30093-whitepaper-review.md | Proposal-corrector retrieval and provenance synthesis | 2026-08-06 | Related DEP reviewed in the repository |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260714-CompressKV%20Semantic%20Heads/2606.24467-whitepaper-review.md | Attention-controlled memory retention synthesis | 2026-08-06 | Related DEP reviewed in the repository |
| R9 | https://arxiv.org/abs/1509.06664 | Prior neural-attention NLI method | 2026-08-06 | Background reading cited by the paper |
| R10 | https://aclanthology.org/D15-1075/ | SNLI benchmark paper | 2026-08-06 | Benchmark context |
| R11 | Private local archive unit | Source integrity and complete-paper review | 2026-08-06 | PDF, full-paper HTML, metadata, provenance, and verification records remained local; no source file was uploaded |

## Appendix

### Selection and source-integrity record

The local archive enumeration used rg --files -g "*.pdf" and produced 75,960 PDF candidates, collapsed to 75,957 unique parent-directory units. Uniform PowerShell Get-Random selected zero-based unit index 55,698 on the first draw. The selected unit had arXiv ID 1512.08849 and no duplicate marker in Black Lake artifact areas, automation memory, or the live Black-Lake-Data exact-ID search. The 24-hour cutoff was 2026-08-05; excluded count and reselection count were zero.

The initial source state was partial because the full-paper HTML was missing. The preserved PDF measured 560,057 bytes, began with %PDF-, and ended with %%EOF. The repaired full-paper HTML measured 384,962 bytes, contained 46,865 body characters after script/style removal, a document marker, 35 heading markers, and six paper-structure terms. The official arXiv full-paper endpoint returned 404; the approved ar5iv fallback returned a valid paper representation. The source package was unavailable. These source files and private verification records remain local.

### Evidence boundary

The manuscript distinguishes direct paper claims, reported measurements, source metadata, reviewer interpretation, and hypotheses for future implementation. It does not claim peer-review status beyond the arXiv record, modern state-of-the-art performance, independent reproducibility, causal faithfulness, or deployment readiness.
