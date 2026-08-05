# Learning Natural Language Inference with LSTM

**Public run date:** 2026-08-06
**Artifact:** Report-Mark for Black Lake Arxiv DEP
**Source files:** Verified locally and withheld; only derived Markdown and public source URLs are deposited.

## Source Metadata

- **Title:** *Learning Natural Language Inference with LSTM*
- **Authors:** Shuohang Wang and Jing Jiang
- **Identifier:** arXiv:1512.08849v2; arXiv-issued DOI: https://doi.org/10.48550/arXiv.1512.08849
- **Submission history:** Submitted 2015-12-30; revised 2016-11-10.
- **Primary sources:** https://arxiv.org/abs/1512.08849, https://arxiv.org/pdf/1512.08849, and the verified full-paper representation at https://ar5iv.labs.arxiv.org/html/1512.08849.
- **Implementation source:** Official author repository https://github.com/shuohangwang/SeqMatchSeq.
- **Benchmark source:** Stanford Natural Language Inference Corpus page at https://nlp.stanford.edu/projects/snli/.
- **Local source state:** Initially partial because full-paper HTML was missing. A bounded repair preserved the valid PDF and added verified full-paper HTML and provenance records locally. The official arXiv HTML route returned 404; the approved ar5iv fallback passed verification. The TeX/source package was unavailable.
- **Review boundary:** Complete paper review, public code/README inspection, benchmark provenance check, and synthesis with three Black Lake DEP entries. No experiment or code execution was performed.

## Concise Research Notes

### Problem

Natural language inference asks whether a hypothesis is entailed by, contradicts, or is neutral to a premise. The paper argues that sentence-level embeddings lose the unequal importance of word- and phrase-level matches, especially when one mismatch is decisive for contradiction or neutrality.

### Method

The match-LSTM (mLSTM) separately encodes premise and hypothesis tokens, computes attention-weighted premise representations for each hypothesis position, concatenates that representation with the hypothesis hidden state, and feeds the pair into a recurrent match state. The input, forget, and output gates decide which local match signals enter, persist in, or leave the aggregate state. A NULL premise token allows unmatched hypothesis words to be represented explicitly.

### Evidence and reported results

On SNLI, the paper retains 549,367 training pairs, 9,842 development pairs, and 9,824 test pairs after discarding disagreement-labeled examples. With hidden dimension 300, mLSTM reports 92.0% training, 86.9% development, and 86.1% test accuracy. Under the authors’ comparable 150-dimensional implementation, mLSTM reports 85.7% test accuracy versus 82.6% for their word-by-word-attention implementation. The paper reports that neutral is more confused with entailment and contradiction than those two labels are with each other.

The gate analysis is interpretive evidence rather than an independent causal test. Reported averages show lower input-gate values for stop words than for other words, while the forget-gate averages rise from entailment to neutral to contradiction. The authors use these patterns to argue that good matches are often forgotten while important mismatches are retained.

### Limitations

The paper evaluates one benchmark and one principal task formulation, does not independently reproduce its own numbers here, freezes GloVe embeddings, and reports preliminary poor performance on the smaller SICK dataset. The official implementation is public but depends on Torch7 and Python 2.7, and its README states that the dataset/preprocessing scripts download external resources. The reported attention and gate behavior is useful evidence about learned state dynamics but should not be treated as a complete explanation of a prediction.

### Implementation relevance and reviewer interpretation

The durable design pattern is selective state retention: compute local alignment, assign salience to each match, and preserve only signals likely to affect the final decision. This pattern bridges naturally to modern retrieval and memory systems, but the reviewer interprets the old result as a mechanism hypothesis rather than a deployment-ready recipe. A modern implementation should compare match-state retention with transformer cross-attention, test out-of-domain transfer, expose evidence spans, and report failure cases.

## Evidence and Attribution

| ID | Evidence | Source basis | Review use |
|---|---|---|---|
| E1 | Paper identity and version history | arXiv metadata record | Title, authors, dates, identifier |
| E2 | Full method, equations, experiments, tables, figures, conclusion | Verified arXiv PDF | Primary technical and quantitative evidence |
| E3 | Searchable full-paper corroboration | Verified ar5iv HTML representation | Section-level cross-check of method and results |
| E4 | Public implementation and dependencies | Official SeqMatchSeq repository README | Code availability, requirements, preprocessing, usage limits |
| E5 | Benchmark definition and licensing context | Stanford SNLI page | Dataset scale, labels, distribution, license |
| E6 | Counterfactual ranking and token-importance probe | Black Lake CFE2 Search Explain manuscript | Related retrieval explanation and pairwise verification |
| E7 | Proposal-corrector retrieval architecture | Black Lake Token Cooccurrence RAG review | Related token routing, provenance, and dense reranking |
| E8 | Attention-selected memory retention | Black Lake CompressKV Semantic Heads review | Related controller selection, salience, and memory budget |

## Related DEP Entries

1. **CFE2 Search Explain** — .lake-data/DEP-E/DEP-E-20260720-CFE2 Search Explain/cfe2_search_explanation_manuscript.md ([public file](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260720-CFE2%20Search%20Explain/cfe2_search_explanation_manuscript.md)). Selected because it turns token-importance signals and ranking changes into a recomputable pairwise probe. Its relevance is grounded in the inspected manuscript and its cited primary arXiv sources.
2. **Token Cooccurrence RAG** — .lake-data/DEP-A/DEP-A-20260715-Token Cooccurrence RAG/2606.30093-whitepaper-review.md ([public file](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-Token%20Cooccurrence%20RAG/2606.30093-whitepaper-review.md)). Selected because it combines cheap token-level structural routing with provenance-preserving candidate recovery and dense correction. Its relevance is grounded in the inspected review and its cited arXiv paper.
3. **CompressKV Semantic Heads** — .lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/2606.24467-whitepaper-review.md ([public file](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-CompressKV%20Semantic%20Heads/2606.24467-whitepaper-review.md)). Selected because it uses functionally selected attention signals to retain evidence under a memory budget and explicitly separates controller signals from storage. Its relevance is grounded in the inspected review and its cited primary sources.

## Synthesis Note

### Concept Bridge

The selected paper supplies a sequential match accumulator: local alignments become state, and gates decide what persists. CFE2 supplies an explicit pairwise verification loop for testing whether a small change alters a ranking. Token Cooccurrence RAG supplies a cheap proposal layer followed by provenance-aware lexical and dense correction. CompressKV supplies a controller-selection and budget-allocation view of evidence retention. Together they suggest an auditable evidence-matching stack: propose candidate alignments cheaply, score them with specialized signals, retain high-impact state under a bounded budget, and verify the downstream decision with an explicit intervention.

### Potential Implementations

1. **Pairwise evidence-verification gate:** Use a modern cross-encoder or mLSTM-style match state to compare a claim with retrieved passages, then apply a CFE2-style controlled edit or passage substitution to test whether the decision is stable. Preserve token/span provenance and abstain when the result changes under harmless paraphrases.
2. **Budgeted multi-hop evidence router:** Use token co-occurrence or sparse lexical diffusion to propose bridge passages, use dense reranking to correct the proposal, and use a match-state controller to retain only the spans that contribute to the current answer. Keep a recoverable lower tier rather than discarding evidence irreversibly.
3. **Salience-aware review queue:** Calibrate which alignment or attention signals predict later human-review decisions, allocate more compute to high-sensitivity cases, and expose retained spans, mismatches, and uncertainty to a reviewer. This is appropriate for research triage, not autonomous high-stakes adjudication.

### Deeper Relationship Observations

1. All four concepts separate candidate generation from final judgment: mLSTM builds a match state, CFE2 generates edits and checks flips, TIGRAG proposes graph neighborhoods before dense reranking, and CompressKV selects controllers before retention.
2. Salience is conditional rather than absolute. A stop word, token, passage, or attention head matters only relative to the current premise, hypothesis, query, answer, or downstream use.
3. The most useful synthesis is recoverable selectivity. The older mLSTM compresses many local matches into state; newer systems compress retrieval or cache state. Provenance and fallback paths are needed to distinguish efficient omission from silent evidence loss.

### Conceptual Similarities

1. **Token-level alignment:** mLSTM attention, CFE2 token masking, TIGRAG token graph routing, and CompressKV token retention all treat local units as actionable evidence rather than relying only on one global embedding.
2. **Stateful importance:** mLSTM gates, CFE2 score-and-flip verification, PPR diffusion, and semantic-head attention all make importance depend on context and downstream behavior.
3. **Evidence-bound evaluation:** Each related artifact warns that a proxy can be mistaken for truth: a gate pattern is not a causal explanation, a flip is not faithful attribution, co-occurrence is not a typed relation, and attention is not a correctness certificate.

### MVP Implementations with Code Mock-Ups

1. **Toy match-state inspector:** A safe, dependency-free prototype records exact token overlap and mismatch positions for synthetic premise/hypothesis pairs. It is an inspection aid, not a trained NLI model.

~~~python
def match_state(premise, hypothesis):
    premise_tokens = set(premise.lower().split())
    pairs = []
    for token in hypothesis.lower().split():
        pairs.append({"token": token, "matched": token in premise_tokens})
    mismatches = [item["token"] for item in pairs if not item["matched"]]
    return {"pairs": pairs, "mismatch_count": len(mismatches), "mismatches": mismatches}
~~~

2. **Proposal-corrector retrieval stub:** A small synthetic candidate list demonstrates cheap lexical proposal followed by a bounded semantic-style reranking score. Real deployments must add authorization, privacy, provenance, and evaluation controls.

~~~python
def proposal_corrector(query_terms, candidates):
    query = set(query_terms)
    scored = []
    for item in candidates:
        terms = set(item["text"].lower().split())
        overlap = len(query & terms)
        scored.append({**item, "proposal_score": overlap})
    return sorted(scored, key=lambda item: item["proposal_score"], reverse=True)
~~~

3. **Recoverable retention controller:** This toy controller retains the highest-scoring spans while returning the omitted spans as a recoverable lower tier. It does not delete data and uses only synthetic scores.

~~~python
def retain_with_fallback(spans, budget):
    ranked = sorted(spans, key=lambda item: item["salience"], reverse=True)
    return {"hot": ranked[:budget], "cold": ranked[budget:]}
~~~

### Developer Challenges

1. How will you prove that a retained mismatch or span changes the downstream decision rather than merely correlating with it?
2. How will you preserve exact token/span provenance across tokenization, graph expansion, reranking, paraphrase edits, and model revisions?
3. How will you evaluate efficiency and quality at equal compute, equal latency, and equal evidence coverage rather than relying on one aggregate score?

### Author Challenges

1. Re-test the match-LSTM on modern NLI datasets and cross-domain shifts, including hard neutral, negation, numerical, and entity-swapping cases.
2. Replace qualitative gate inspection with controlled interventions that measure whether manipulating remembered mismatches changes predictions for the intended reasons.
3. Compare the match-state idea with current cross-attention and reranking systems under pinned preprocessing, multiple seeds, confidence intervals, and public failure analyses.

## Validation Notes

- Source-integrity gate: complete after bounded repair; valid PDF and full-paper HTML confirmed; official HTML 404 and approved ar5iv fallback used.
- Review evidence: complete paper representation inspected, including method, experiments, table results, gate analysis, conclusion, and references; official code README and SNLI benchmark page were verified online.
- Deduplication: no matching arXiv ID, DOI, normalized title, or slug was found in the required Black Lake areas, automation memory, live Black-Lake-Data exact-ID search, or the 24-hour marker window.
- Public-output policy: source files, extracted text, caches, local archive metadata, and machine details are withheld. The deposit contains derived Markdown only.
- Structural checks required before submission: schema headings and title contract; three exercise paths; three related entries; three synthesis implementations, observations, similarities, mock-ups, developer challenges, and author challenges; final Attribution Block.

## Attribution Block

- Source URL: https://arxiv.org/abs/1512.08849
  - Applies to: Report-Mark.md
  - Notes: Canonical paper identity, authors, version history, abstract, and arXiv-issued DOI.
- Source URL: https://arxiv.org/pdf/1512.08849
  - Applies to: Report-Mark.md
  - Notes: Primary PDF inspected locally and withheld from the repository.
- Source URL: https://ar5iv.labs.arxiv.org/html/1512.08849
  - Applies to: Report-Mark.md
  - Notes: Approved full-paper HTML fallback used after the official arXiv HTML route returned 404; inspected locally and withheld.
- Source URL: https://github.com/shuohangwang/SeqMatchSeq
  - Applies to: Report-Mark.md
  - Notes: Official author repository verified for implementation availability, dependencies, preprocessing, and usage.
- Source URL: https://nlp.stanford.edu/projects/snli/
  - Applies to: Report-Mark.md
  - Notes: Official SNLI benchmark definition, scale, labels, distribution, and license context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-CFE2%20Search%20Explain/cfe2_search_explanation_manuscript.md
  - Applies to: Report-Mark.md
  - Notes: Related DEP inspected for counterfactual ranking probes and token-importance verification.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260715-Token%20Cooccurrence%20RAG/2606.30093-whitepaper-review.md
  - Applies to: Report-Mark.md
  - Notes: Related DEP inspected for proposal-corrector retrieval, token routing, dense correction, and provenance.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260714-CompressKV%20Semantic%20Heads/2606.24467-whitepaper-review.md
  - Applies to: Report-Mark.md
  - Notes: Related DEP inspected for attention-signal selection, evidence retention, and bounded memory allocation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: Report-Mark.md
  - Notes: Live repository authority for public-safe layout, provenance, and submission rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: Report-Mark.md
  - Notes: Live DEP filing and publication-index rules.
- Source files: private local archive unit, PDF/full-paper HTML/metadata/verification records
  - Applies to: Report-Mark.md
  - Notes: Inspected for source integrity and review; withheld locally and not uploaded.
