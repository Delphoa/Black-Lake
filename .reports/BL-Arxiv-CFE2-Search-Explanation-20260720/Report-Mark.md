# Report-Mark: CFE2 Search Explanations

## Source Metadata

- **Paper:** *CFE2: Counterfactual Editing for Search Result Explanation* (the arXiv record uses the shorter title *Counterfactual Editing for Search Result Explanation*).
- **Authors:** Zhichao Xu, Hemank Lamba, Qingyao Ai, Joel Tetreault, and Alex Jaimes.
- **Identifiers:** arXiv `2301.10389v3`; arXiv DOI https://doi.org/10.48550/arXiv.2301.10389; published DOI https://doi.org/10.1145/3664190.3672508.
- **Dates and venue:** first submitted 2023-01-25; arXiv v3 submitted 2024-06-28; published at ICTIR 2024, pages 145-155.
- **Primary records:** https://arxiv.org/abs/2301.10389, https://arxiv.org/pdf/2301.10389, https://arxiv.org/html/2301.10389, and https://openreview.net/forum?id=G3a15oOyJQ&noteId=86yHStWtLa.
- **Review basis:** verified full PDF and full-paper HTML, arXiv metadata, the official source package, the DOI record, the OpenReview record, the ICTIR accepted-paper listing, and three inspected DEP manuscripts. Original source files were retained in the private archive and are not part of this deposit.
- **Access date:** 2026-07-20; exact execution timestamp withheld.

## Concise Research Notes

The paper treats search-result explanation as a pairwise counterfactual-editing problem. Given a query, a higher-ranked document, and a lower-ranked document, CFE2 edits the query until the lower-ranked document outranks the higher-ranked one. The edit is intended to answer a bounded question: what minimal-looking query change would reverse this local ranking relationship?

CFE2 combines three parts: a dense search model, a ColBERT-inspired masker that identifies influential query tokens, and a masked-language-model editor. The editor conditions on the counterfactual document, searches candidate replacements with beam search, tests each candidate against the rank-flip condition, and selects a flipping candidate with low perplexity. CFE2+ adds task-adaptive pretraining on the target corpus.

Across MS MARCO, Natural Questions, FiQA, FEVER, and SciFact, the reported CFE2 FlipRate ranges from `0.998` to `1.000`. The reported semantic-closeness and fluency measures generally improve over generation-oriented baselines, while runtime is lower than the Summary and GenEx generation baselines but higher than simple masking or maximum-flip baselines. Because several baselines already approach the FlipRate ceiling, the more informative comparison is whether the edit remains close, clear, fluent, and operationally useful.

The human study covers 50 SciFact triplets with at least three qualified Mechanical Turk responses per triplet. CFE2+ is reported above GenEx on fluency, clarity, semantic closeness, and syntactic closeness, but inter-annotator agreement is only slight to fair (`kappa 0.08-0.22`). This limits how strongly the preference results can be generalized.

Reviewer interpretation: a rank-flipping edit is a useful local diagnostic, but a successful flip is not by itself evidence that the edit faithfully explains the model's original ranking mechanism. It may instead expose a decision-boundary shortcut, lexical sensitivity, or retriever-specific artifact.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supported finding | Qualification |
|---|---|---|---|
| E1 | [arXiv abstract and version record](https://arxiv.org/abs/2301.10389) | Identity, authorship, version dates, abstract-level contribution, venue linkage | Metadata record, not a substitute for the full paper |
| E2 | [arXiv PDF](https://arxiv.org/pdf/2301.10389) and [full-paper HTML](https://arxiv.org/html/2301.10389) | Formal objective, system components, datasets, metrics, results, ablations, human study, limitations, and qualitative examples | Primary technical evidence |
| E3 | [ACM DOI record](https://doi.org/10.1145/3664190.3672508) | Published identity and ICTIR bibliographic record | Publisher metadata may require institutional access for some views |
| E4 | [OpenReview record](https://openreview.net/forum?id=G3a15oOyJQ&noteId=86yHStWtLa) | Independent public record for the submission and its metadata | Does not replace the final publication |
| E5 | [ICTIR 2024 accepted papers](https://www.ictir2024.org/program/accepted-papers) and [Utah NLP publications](https://nlp.cs.utah.edu/publications/) | Venue and author-group corroboration | Supporting provenance only |
| E6 | Private integrity verification, path withheld | Existing PDF preserved; official full-paper HTML and companion records repaired and validated | Processing evidence is private; no source artifact was uploaded |

The full paper reports five evaluation corpora: MS MARCO, FEVER, Natural Questions, FiQA, and SciFact. It reports approximately 20.4k, 53.3k, 1.8k, 4.6k, and 1.2k evaluation triplets respectively when ordered as MS MARCO, FEVER, Natural Questions, FiQA, and SciFact. The dense retriever is CL-DRD; the default editor is a 66M-parameter DistilBERT masked-language model; the principal comparison systems are Mask-only, MaxFlip, Summary, and GenEx.

Selected reported CFE2 results are: MS MARCO `0.998` FlipRate, `0.909` CosSim, `0.933` BERTScore-F1, `1.774` RelFluency, and `0.258` seconds per edit; Natural Questions `0.999`, `0.934`, `0.962`, `1.159`, and `0.257`; FiQA `0.999`, `0.957`, `0.963`, `1.110`, and `0.352`; FEVER `0.999`, `0.944`, `0.949`, `0.972`, and `0.364`; and SciFact `1.000`, `0.963`, `0.962`, `1.478`, and `0.828`. These are source claims, not independently reproduced results.

The human-evaluation table reports CFE2+ versus GenEx mean scores of `3.83` versus `3.76` for fluency, `3.88` versus `3.59` for clarity, `3.64` versus `3.12` for semantic closeness, and `3.61` versus `3.35` for syntactic closeness. The paper reports statistically significant differences, but the low agreement values warrant caution. The BERT-editor ablation reports `0.503` seconds per FiQA edit versus `0.352` for DistilBERT, or about 42.8% slower.

One source inconsistency is preserved explicitly: the BERT-editor ablation table prints `CosSim 9.959`, although the metric is defined on a zero-to-one scale. This report treats it as an apparent source typo and does not silently replace it with a guessed value.

## Related DEP Entries

1. [Beyond XAI manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Beyond%20XAI/beyond_xai_manuscript.md) - establishes that an accessible local explanation should not be mistaken for global or causal faithfulness. This sharpens the boundary around what CFE2's rank-flipping edits can support. Source basis: the inspected DEP manuscript and its primary arXiv record, `2602.24176`.
2. [OViP Preference manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md) - connects targeted counterfactual construction with semantic-isolation checks, shortcut-leakage controls, and independent verification. Source basis: the inspected DEP manuscript and its primary arXiv record, `2505.15963`.
3. [REAL Temporal Graph review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-REAL%20Temporal%20Graph/2606.10694-whitepaper-review.md) - links beam-searched retrieval and counterfactual expansion to explicit provenance separation among observed, derived, and hypothetical states. Source basis: the inspected DEP review and its primary arXiv record, `2606.10694`.

## Synthesis Note

### Concept Bridge

CFE2 supplies a compact local intervention: change the query, re-evaluate the same document pair, and observe whether the ordering reverses. Beyond XAI supplies the epistemic boundary, OViP supplies verification discipline for targeted counterfactuals, and REAL supplies a provenance model for separating observed inputs, derived scores, and counterfactual states. Together they suggest a safer product pattern: treat edits as falsifiable probes with receipts, not as definitive narratives about model causality.

### Potential Implementations

1. **Search-debugging console:** let relevance engineers inspect a document pair, generate bounded counterfactual queries, and compare score deltas while preserving the original query and model version.
2. **Explanation-quality gate:** require a candidate edit to satisfy rank flip, semantic-closeness, fluency, stability, and human-agreement thresholds before it can be shown outside an engineering environment.
3. **Counterfactual provenance ledger:** record observed query and ranks separately from model-derived token importance, generated edits, reranked scores, and reviewer judgments.

### Deeper Relationship Observations

1. The edit acts like a local intervention but not a causal identification procedure; Beyond XAI's faithfulness distinction therefore constrains the strongest defensible language.
2. CFE2 and OViP both depend on targeted perturbations, so both inherit a semantic-isolation problem: success is ambiguous if the intervention changes multiple latent intents at once.
3. CFE2's beam candidates naturally form a small counterfactual state graph, making REAL's observed/derived/counterfactual provenance split useful even though the underlying application domain differs.

### Conceptual Similarities

1. All four artifacts use constrained alternatives to reveal model behavior that is difficult to infer from a single output.
2. Each benefits from an independent verification layer that checks whether a generated explanation or candidate actually satisfies the claimed condition.
3. Each separates useful operational evidence from stronger causal or global claims that the available experiment does not establish.

### MVP Implementations with Code Mock-Ups

1. **Pairwise flip verifier:** recompute both orderings and reject candidates that do not establish the exact before-and-after condition.

```python
def valid_flip(score, original_query, edited_query, higher_doc, lower_doc):
    before = score(original_query, higher_doc) > score(original_query, lower_doc)
    after = score(edited_query, lower_doc) > score(edited_query, higher_doc)
    return before and after
```

2. **Evidence receipt:** keep observed, derived, and counterfactual fields distinct so an interface cannot blur a generated edit into a source fact.

```python
def evidence_receipt(query, pair, scores, edit, model_version):
    return {
        "observed": {"query": query, "document_pair": pair},
        "derived": {"scores": scores, "model_version": model_version},
        "counterfactual": {"edited_query": edit},
    }
```

3. **Illustrative release gate:** require multiple quality dimensions, with thresholds calibrated on a real validation set rather than copied from this example.

```python
def release_ok(metrics):
    return (
        metrics["flip_rate"] >= 0.95
        and metrics["semantic_closeness"] >= 0.90
        and metrics["agreement"] >= 0.40
        and metrics["p95_latency_ms"] <= 750
    )
```

### Developer Challenges

1. Pairwise explanations can become stale when the corpus, top-k candidate set, reranker, tokenizer, or model version changes; every receipt needs model and index versioning.
2. Beam search adds latency and may surface unsafe or privacy-sensitive query variants; production systems need bounded search, redaction, and no raw-query logging by default.
3. Automatic closeness and fluency metrics do not guarantee usefulness or faithfulness; evaluation needs adversarial cases, human review, and calibration across domains.

### Author Challenges

1. The empirical claim of model agnosticism is under-tested because the search model is CL-DRD throughout; the BERT ablation varies the editor, not the retriever.
2. The human study is limited to 50 SciFact triplets and reports slight-to-fair agreement, leaving uncertainty about annotation reliability and cross-domain generalization.
3. The paper's automatic evaluation is close to a FlipRate ceiling, and the printed `9.959` CosSim value complicates auditability unless corrected by an authoritative erratum.

## Validation Notes

- Random selection used uniform `Get-Random` over 75,369 eligible units after 75,778 PDFs were grouped into 75,776 parent units; selected zero-based eligible index `64,032`.
- Dedup scanned Black Lake logs, reports, lake data, staging records, automation memory, and the fetched Black-Lake-Data default-branch state. It found no matching arXiv ID, DOI, normalized title, title token, or slug, and no same-paper marker on or after the public-safe cutoff date 2026-07-19. Reselections: zero.
- Initial source state was `partial`: the PDF passed integrity checks, but full-paper HTML was absent. A bounded repair preserved the PDF and added official arXiv full-paper HTML plus provenance companions to the private archive.
- Final private gate: PDF 1,014,492 bytes with `%PDF-` and trailing `%%EOF`; HTML 551,159 bytes with 98,103 body characters, a document marker, 47 heading markers, and seven paper-structure terms. No fallback was needed.
- This review did not execute the paper's experiments. A bounded primary-source search did not establish an official implementation repository, so reproducibility remains unverified rather than assumed absent.
- Public output contains only generated Markdown. PDFs, HTML, source archives, extracted text, caches, and private provenance records were withheld locally.

## Attribution Block

- Xu, Zhichao; Lamba, Hemank; Ai, Qingyao; Tetreault, Joel; Jaimes, Alex. *CFE2: Counterfactual Editing for Search Result Explanation*. arXiv `2301.10389v3`, ICTIR 2024. https://arxiv.org/abs/2301.10389; https://arxiv.org/pdf/2301.10389; https://arxiv.org/html/2301.10389; https://doi.org/10.48550/arXiv.2301.10389; https://doi.org/10.1145/3664190.3672508.
- OpenReview public record: https://openreview.net/forum?id=G3a15oOyJQ&noteId=86yHStWtLa.
- ICTIR 2024 accepted-paper record: https://www.ictir2024.org/program/accepted-papers.
- University of Utah NLP publication record: https://nlp.cs.utah.edu/publications/.
- Related Black Lake DEP: *Beyond XAI*. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Beyond%20XAI/beyond_xai_manuscript.md.
- Related Black Lake DEP: *OViP Preference*. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md.
- Related Black Lake DEP: *REAL Temporal Graph*. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-REAL%20Temporal%20Graph/2606.10694-whitepaper-review.md.
- Repository rules consulted: https://github.com/Delphoa/Black-Lake/blob/main/README.md and https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md.
- Related-repository rules consulted: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md.
- Private source-integrity and repair records: path withheld; processing evidence only; no original source file was uploaded.
