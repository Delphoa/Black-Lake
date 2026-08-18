# Report-Mark: [2203.14680] Transformer Feed-Forward Layers Build Predictions by Promoting Concepts in the Vocabulary Space

Run date: 2026-08-19

## Source Metadata

- Title: [2203.14680] Transformer Feed-Forward Layers Build Predictions by Promoting Concepts in the Vocabulary Space
- Authors: Not available from inspected sources
- Identifier: arXiv:2203.14680
- Public sources: https://arxiv.org/abs/2203.14680; https://arxiv.org/html/2203.14680; https://arxiv.org/pdf/2203.14680
- Source state: complete local PDF and full-paper HTML passed the required integrity gate; source files were withheld from public output.
- Batch position: 170 of 200; selection pool contained 469 unseen valid IDs.

## Concise Research Notes

- Problem: The paper's primary source frames the research problem as: Abstract Transformer-based language models (LMs) are at the core of modern NLP, but their internal prediction construction process is opaque and largely not understood. In this work, we make a substantial step towards unveiling this underlying prediction process, by reverse-engineering the operation of the feed-forward network (FFN) layers, one of the building blocks of transformer models. We view the token representation as a changing distribution over the vocabulary, and the output from each FFN layer as an additive update to that distribution. Then, we analyze the FFN updates in the vocabulary space, showing that each update can be decomposed to sub-updates corresponding to single FFN parameter vectors, each promoting concepts that are often human-interpretable. We then leverage these findings for controlling LM predictions, where we reduce the toxicity of GPT2 by almost 50%, and for improving computation efficiency with a simple early exit rule, saving 20% of computation on average. 1 1 1 Our codebase is available at https://github.com/aviclu/ffn-values .
- Method: Method-related full-paper text: which both WikiLM and GPT2 did not observe during training. We utilize our findings to create a simple, intuitive method for toxic language suppression.
- Evidence/results: Evidence-related full-paper text: Through a series of experiments, we find that (a) sub-update vectors across the entire network often encode a small-set of human-interpretable well-defined concepts, e.g. A transformer LM with L = 10 , d m = 3000 formulae-sequence 𝐿 10 subscript 𝑑 𝑚 3000 L=10,d_{m}=3000 will have 30 , 000 30 000 30,000 value vectors, and every token that passes through the transformer will weight these value vectors differently,...
- Limitations: Limitation-related full-paper text: Model Toxicity Severe Sexually Threat Profanity Identity PPL toxicity explicit attack GPT2 58.5% 49.2% 34.1% 16.4% 52.5% 16.8% 21.7 ↑ ↑ \uparrow 10 Manual Pick 30.8% 24.8% 20.4% 6.0% 27.9% 8.8% 25.3 ↑ ↑ \uparrow 10 API Graded 52.7% 44% 33.2% 13.3% 47.6% 15.3% 23.8 SD 37.2% 26.4% 21.7% 7.8% 32% 8.4% 23.9 WordFilter 46.9% 32.4% 21.9% 16.3% 32.3% 14.7% - Table 5: Evaluation results on the challenging subset of...
- Implementation relevance: The paper can inform a bounded evidence map, evaluation harness, or research-to-prototype workflow, but the batch did not reproduce the experiments.
- Reviewer interpretation: The strongest supported conclusion is that the paper presents a structured research contribution with inspectable full-paper evidence. Transfer to production remains an inference requiring paper-specific validation.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution | Reviewer use |
|---|---|---|---|
| E1 | Full-paper HTML, including title, abstract, headings, and extracted method/evidence text | https://arxiv.org/html/2203.14680 | Primary evidence for notes and claims. |
| E2 | Validated PDF presence and integrity markers | https://arxiv.org/pdf/2203.14680 | Confirms complete source pair; no source file was uploaded. |
| E3 | Canonical arXiv metadata | https://arxiv.org/abs/2203.14680 | Stable identifier and public provenance. |

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260728-Language to Space Intake` — selected because the entry label shares conceptual cues `space, language` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260818-Language Guided Abstracti` — selected because the entry label shares conceptual cues `abstract, language` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-E/DEP-E-20260727-Language-to-Space` — selected because the entry label shares conceptual cues `space, language` with the paper review. Basis: live repository README/artifact path; context only.

## Synthesis Note

### Concept Bridge

The selected paper connects to DEP-A-20260728-Language to Space Intake, DEP-A-20260818-Language Guided Abstracti, DEP-E-20260727-Language-to-Space through the shared problem of turning a technical research mechanism into inspectable evidence, reusable system boundaries, and follow-on evaluation. The relationship is conceptual: the selected paper remains the primary evidence source, while the three DEP entries provide repository-grounded comparison cues.

### Potential Implementations

1. Build an evidence-led implementation brief that maps the paper's mechanism to the related entries' system or evaluation concerns.
2. Build a synthetic benchmark harness that compares the paper's stated mechanism with one baseline and records provenance for every input and output.
3. Build a local research notebook that links paper claims, related DEP notes, and follow-up experiments without redistributing source files.

### Deeper Relationship Observations

1. Each concept becomes more useful when its mechanism is paired with an explicit evidence ledger rather than a headline summary.
2. The paper-to-DEP bridge exposes a recurring boundary between research novelty and implementation readiness.
3. Related artifacts can function as design memory, but only primary-paper evidence can support claims about this paper's own results.

### Conceptual Similarities

1. All four research objects can be represented as a mechanism, an evidence surface, and a set of constraints.
2. All benefit from controlled comparison against baselines or neighboring designs.
3. All require provenance and uncertainty labels for safe downstream reuse.

### MVP Implementations with Code Mock-Ups

1. Evidence ledger mapper:

```python
claims = [{"id": "C1", "source": "E1", "status": "review"}]
assert all(c["source"].startswith("E") for c in claims)
```

2. Bounded comparison record:

```python
record = {"paper_id": "arXiv:2203.14680", "baseline": "toy-baseline", "data": "synthetic"}
print(record)
```

3. Safe implementation checklist:

```python
checks = ["public-data-only", "human-review", "no-source-upload"]
assert len(checks) == 3
```

### Developer Challenges

1. Preserve paper-specific evaluation conditions while composing a reusable implementation surface.
2. Prevent related DEP context from being mistaken for independent validation.
3. Build provenance and failure reporting into the first prototype rather than adding them after deployment.

### Author Challenges

1. Report enough implementation and failure detail for an independent reviewer to reproduce the central claim.
2. Test whether the method transfers across the neighboring contexts surfaced by the related DEP entries.
3. Clarify which assumptions are essential to the result and which can be relaxed.

## Validation Notes

- Candidate enumeration used `rg --files -g "*.pdf"` against the local archive; the paper unit was accepted only after PDF and full-paper HTML validation.
- Dedup scan covered repository `.logs`, `.reports`, `.lake-data`, the public dedup index, and automation memory; duplicate exclusions: 396; reselections: 0.
- Public staging allowlist contained only Markdown logs, Report-Mark, DEP README/manuscript, and the DEP-E publication-index update.
- Local PDFs, HTML, metadata, source packages, extracted text, caches, and local paths were not staged or uploaded.
- No independent reproduction or benchmark rerun was performed.

## Attribution Block

- Source URL: https://arxiv.org/html/2203.14680
  - Applies to: primary research notes, evidence ledger, manuscript, and Report-Mark.
  - Notes: Full-paper HTML inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/pdf/2203.14680
  - Applies to: source integrity verification.
  - Notes: PDF inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/abs/2203.14680
  - Applies to: canonical identifier and metadata.
  - Notes: Abstract page is metadata only.
- Repository file: .lake-data/DEP-A/DEP-A-20260728-Language to Space Intake
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260818-Language Guided Abstracti
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-E/DEP-E-20260727-Language-to-Space
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
