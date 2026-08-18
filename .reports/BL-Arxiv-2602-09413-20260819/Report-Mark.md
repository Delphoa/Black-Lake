# Report-Mark: LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging

Run date: 2026-08-19

## Source Metadata

- Title: LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging
- Authors: Not available from inspected sources
- Identifier: arXiv:2602.09413
- Public sources: https://arxiv.org/abs/2602.09413; https://arxiv.org/html/2602.09413; https://arxiv.org/pdf/2602.09413
- Source state: complete local PDF and full-paper HTML passed the required integrity gate; source files were withheld from public output.
- Batch position: 137 of 200; selection pool contained 469 unseen valid IDs.

## Concise Research Notes

- Problem: The paper's primary source frames the research problem as: Abstract Model merging aims to combine multiple fine-tuned models into a single multi-task model without access to training data. Existing task-vector merging methods such as TIES, TSV-M, and Iso-C/CTS differ in their aggregation rules but treat all layers nearly uniformly. This assumption overlooks the strong layer-wise heterogeneity in large vision transformers, where shallow layers are sensitive to interference while deeper layers encode stable task-specific features. We introduce LARV, a training-free, data-free, merger-agnostic L ayer-wise A daptive R escaling V eneer that plugs into any task-vector merger and assigns a per-layer scale to each task vector before aggregation, and show it consistently boosts diverse merging rules. LARV adaptively suppresses shallow-layer interference and amplifies deeper-layer alignment using a simple deterministic schedule, requiring no retraining or modification to existing mergers. To our knowledge, this is the first work to perform layer-aware scaling for task-vector merging. LARV computes simple data-free layer proxies and turns them into scales through a lightweight rule; we study several instantiations within one framework (e.g., tiered two/three-level scaling with fixed values, or continuous mappings) and show that tiered choices offer the best robustness, while continuous mappings remain an ablation. LARV is orthogonal to the base merger and adds negligible cost. On FusionBench with Vision Transformers, LARV consistently improves all task-vector baselines across 8/14/20-task settings; for example, Iso-C + LARV reaches 85.9% on ViT-B/32, 89.2% on ViT-B/16, and 92.6% on ViT-L/14. Layer-wise analysis and corruption tests further indicate that LARV suppresses shallow-layer interference while modestly amplifying deeper, task-stable features, turning model merging into a robust, layer-aware procedure rather than a uniform one.
- Method: Method-related full-paper text: LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging 1 Introduction 2 Related Work Global and training-free merging. Structured and conflict-aware training-free merging.
- Evidence/results: Evidence-related full-paper text: 4 Results and Analysis 4.1 Experimental Setup 4.2 Main Results Across Backbones (8 tasks) Key Observations. C Experimental Setup and Protocol C.1 FusionBench Configuration and Evaluation Protocol C.2 Hyperparameters and Implementation Details D Ablation on Scaling Strategy: Beyond Simple Depth Priors D.1 Comprehensive Comparison to Depth-Only Heuristics Depth-only heuristics.
- Limitations: Limitation-related full-paper text: This paradigm is both meaningful for revealing surprising linear structure in parameter space and useful for enabling capability sharing with no data, rapid deployment under data-access constraints, and mix-and-match assembly across tasks and architectures [ 35 , 24 , 16 , 1 , 7 ] .
- Implementation relevance: The paper can inform a bounded evidence map, evaluation harness, or research-to-prototype workflow, but the batch did not reproduce the experiments.
- Reviewer interpretation: The strongest supported conclusion is that the paper presents a structured research contribution with inspectable full-paper evidence. Transfer to production remains an inference requiring paper-specific validation.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution | Reviewer use |
|---|---|---|---|
| E1 | Full-paper HTML, including title, abstract, headings, and extracted method/evidence text | https://arxiv.org/html/2602.09413 | Primary evidence for notes and claims. |
| E2 | Validated PDF presence and integrity markers | https://arxiv.org/pdf/2602.09413 | Confirms complete source pair; no source file was uploaded. |
| E3 | Canonical arXiv metadata | https://arxiv.org/abs/2602.09413 | Stable identifier and public provenance. |

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260715-Mapping Text to Multiplex` — selected because the entry label shares conceptual cues `multiple, multi` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260715-ObjectCache Layerwise Obj` — selected because the entry label shares conceptual cues `layer, wise` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260721-ALVTS Layerwise` — selected because the entry label shares conceptual cues `layer, wise` with the paper review. Basis: live repository README/artifact path; context only.

## Synthesis Note

### Concept Bridge

The selected paper connects to DEP-A-20260715-Mapping Text to Multiplex, DEP-A-20260715-ObjectCache Layerwise Obj, DEP-A-20260721-ALVTS Layerwise through the shared problem of turning a technical research mechanism into inspectable evidence, reusable system boundaries, and follow-on evaluation. The relationship is conceptual: the selected paper remains the primary evidence source, while the three DEP entries provide repository-grounded comparison cues.

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
record = {"paper_id": "arXiv:2602.09413", "baseline": "toy-baseline", "data": "synthetic"}
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

- Source URL: https://arxiv.org/html/2602.09413
  - Applies to: primary research notes, evidence ledger, manuscript, and Report-Mark.
  - Notes: Full-paper HTML inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/pdf/2602.09413
  - Applies to: source integrity verification.
  - Notes: PDF inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/abs/2602.09413
  - Applies to: canonical identifier and metadata.
  - Notes: Abstract page is metadata only.
- Repository file: .lake-data/DEP-A/DEP-A-20260715-Mapping Text to Multiplex
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260715-ObjectCache Layerwise Obj
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260721-ALVTS Layerwise
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
