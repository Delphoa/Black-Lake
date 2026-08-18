# Report-Mark: Proxy Avatar Meets Low-Rank Caching: Real-Time One-Shot Emotion-Controllable Portrait Animation

Run date: 2026-08-19

## Source Metadata

- Title: Proxy Avatar Meets Low-Rank Caching: Real-Time One-Shot Emotion-Controllable Portrait Animation
- Authors: Not available from inspected sources
- Identifier: arXiv:2608.01978
- Public sources: https://arxiv.org/abs/2608.01978; https://arxiv.org/html/2608.01978; https://arxiv.org/pdf/2608.01978
- Source state: complete local PDF and full-paper HTML passed the required integrity gate; source files were withheld from public output.
- Batch position: 105 of 200; selection pool contained 469 unseen valid IDs.

## Concise Research Notes

- Problem: The paper's primary source frames the research problem as: Abstract Audio-driven portrait animation has advanced rapidly with diffusion-based generative models, yet real-time one-shot generation with expressive emotion control remains challenging. Existing methods often suffer from insufficient emotion-aware motion priors and expensive appearance computation during multi-step denoising. To address these issues, we propose Proxy Avatar Meets Low-Rank Caching, a cascaded framework for real-time one-shot emotion-controllable portrait animation. Instead of directly generating the target portrait from audio, our method uses a Gaussian-based emotion proxy avatar as a reusable motion generator, which is trained once on a single identity to produce expressive driving videos from audio and emotion labels. Since the proxy avatar only provides motion rather than target appearance or geometry, a large-scale one-shot retargeting model further extracts identity-independent motion from the proxy performance and adapts it to arbitrary target portraits. To improve inference efficiency, we introduce zero-shot appearance reuse with low-rank caching, which caches reference appearance features at the initial denoising step and models subsequent feature variations using lightweight low-rank adapters. Extensive experiments demonstrate that our method achieves stronger emotional expressiveness, better identity-preserving animation, and substantially reduced inference cost, enabling real-time one-shot portrait animation.
- Method: Method-related full-paper text: Report Issue Back to Abstract Download PDF Abstract Introduction Related Work Audio-driven Talking Head Generation Emotion-controllable Talking Head Generation Efficient Portrait Animation Method 3D Gaussian-based Emotion Proxy Avatar One-Shot Portrait Motion Driving Module Appearance Redundancy Distillation Experiments Conclusion References License: arXiv.org perpetual non-exclusive license arXiv:2608.01978v1...
- Evidence/results: Evidence-related full-paper text: Report Issue Back to Abstract Download PDF Abstract Introduction Related Work Audio-driven Talking Head Generation Emotion-controllable Talking Head Generation Efficient Portrait Animation Method 3D Gaussian-based Emotion Proxy Avatar One-Shot Portrait Motion Driving Module Appearance Redundancy Distillation Experiments Conclusion References License: arXiv.org perpetual non-exclusive license arXiv:2608.01978v1...
- Limitations: Limitation-related full-paper text: To address these limitations, we revisit the design of emotion-controllable talking head generation from a division-of-labor perspective. Due to space limitations, we provide more experimental analyses in the appendix .
- Implementation relevance: The paper can inform a bounded evidence map, evaluation harness, or research-to-prototype workflow, but the batch did not reproduce the experiments.
- Reviewer interpretation: The strongest supported conclusion is that the paper presents a structured research contribution with inspectable full-paper evidence. Transfer to production remains an inference requiring paper-specific validation.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution | Reviewer use |
|---|---|---|---|
| E1 | Full-paper HTML, including title, abstract, headings, and extracted method/evidence text | https://arxiv.org/html/2608.01978 | Primary evidence for notes and claims. |
| E2 | Validated PDF presence and integrity markers | https://arxiv.org/pdf/2608.01978 | Confirms complete source pair; no source file was uploaded. |
| E3 | Canonical arXiv metadata | https://arxiv.org/abs/2608.01978 | Stable identifier and public provenance. |

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260818-FlashDecoder Real Time La` — selected because the entry label shares conceptual cues `real, time` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-E/DEP-E-20260723-UnityShots Memory-Driven` — selected because the entry label shares conceptual cues `shot, driven` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-E/DEP-E-20260728-CanCal Towards Real-time` — selected because the entry label shares conceptual cues `real, time` with the paper review. Basis: live repository README/artifact path; context only.

## Synthesis Note

### Concept Bridge

The selected paper connects to DEP-A-20260818-FlashDecoder Real Time La, DEP-E-20260723-UnityShots Memory-Driven, DEP-E-20260728-CanCal Towards Real-time through the shared problem of turning a technical research mechanism into inspectable evidence, reusable system boundaries, and follow-on evaluation. The relationship is conceptual: the selected paper remains the primary evidence source, while the three DEP entries provide repository-grounded comparison cues.

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
record = {"paper_id": "arXiv:2608.01978", "baseline": "toy-baseline", "data": "synthetic"}
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

- Source URL: https://arxiv.org/html/2608.01978
  - Applies to: primary research notes, evidence ledger, manuscript, and Report-Mark.
  - Notes: Full-paper HTML inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/pdf/2608.01978
  - Applies to: source integrity verification.
  - Notes: PDF inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/abs/2608.01978
  - Applies to: canonical identifier and metadata.
  - Notes: Abstract page is metadata only.
- Repository file: .lake-data/DEP-A/DEP-A-20260818-FlashDecoder Real Time La
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-E/DEP-E-20260723-UnityShots Memory-Driven
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-E/DEP-E-20260728-CanCal Towards Real-time
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
