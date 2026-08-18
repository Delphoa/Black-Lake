# Report-Mark: [1910.04214] Who’s responsible? Jointly quantifying the contribution of the learning algorithm and data

Run date: 2026-08-19

## Source Metadata

- Title: [1910.04214] Who’s responsible? Jointly quantifying the contribution of the learning algorithm and data
- Authors: Not available from inspected sources
- Identifier: arXiv:1910.04214
- Public sources: https://arxiv.org/abs/1910.04214; https://arxiv.org/html/1910.04214; https://arxiv.org/pdf/1910.04214
- Source state: complete local PDF and full-paper HTML passed the required integrity gate; source files were withheld from public output.
- Batch position: 135 of 200; selection pool contained 469 unseen valid IDs.

## Concise Research Notes

- Problem: The paper's primary source frames the research problem as: Abstract A learning algorithm A 𝐴 A trained on a dataset D 𝐷 D is revealed to have poor performance on some subpopulation at test time. Where should the responsibility for this lay? It can be argued that the data is responsible, if for example training A 𝐴 A on a more representative dataset D ′ superscript 𝐷 ′ D^{\prime} would have improved the performance. But it can similarly be argued that A 𝐴 A itself is at fault, if training a different variant A ′ superscript 𝐴 ′ A^{\prime} on the same dataset D 𝐷 D would have improved performance. As ML becomes widespread and such failure cases more common, these types of questions are proving to be far from hypothetical. With this motivation in mind, in this work we provide a rigorous formulation of the joint credit assignment problem between a learning algorithm A 𝐴 A and a dataset D 𝐷 D . We propose Extended Shapley as a principled framework for this problem, and experiment empirically with how it can be used to address questions of ML accountability.
- Method: Method-related full-paper text: Jointly quantifying the contribution of the learning algorithm and data Who’s responsible? Jointly quantifying the contribution of the learning algorithm and data Gal Yona Weizmann Institute of Science gal.yona@weizmann.ac.il Amirata Ghorbani Stanford University gal.yona@weizmann.ac.il James Zou Stanford University gal.yona@weizmann.ac.il Gal Yona Weizmann Institute of Science Amirata Ghorbani James Zou Stanford...
- Evidence/results: Evidence-related full-paper text: Jointly quantifying the contribution of the learning algorithm and data Gal Yona Weizmann Institute of Science gal.yona@weizmann.ac.il Amirata Ghorbani Stanford University gal.yona@weizmann.ac.il James Zou Stanford University gal.yona@weizmann.ac.il Gal Yona Weizmann Institute of Science Amirata Ghorbani James Zou Stanford University Correspondence: jamesz@stanford.edu Abstract A learning algorithm A 𝐴 A trained...
- Limitations: Limitation-related full-paper text: As ML becomes widespread and such failure cases more common, these types of questions are proving to be far from hypothetical. These findings sparked internet controversy around the source of these failures (see [ Gradient, 2020 ] for a comprehensive overview).
- Implementation relevance: The paper can inform a bounded evidence map, evaluation harness, or research-to-prototype workflow, but the batch did not reproduce the experiments.
- Reviewer interpretation: The strongest supported conclusion is that the paper presents a structured research contribution with inspectable full-paper evidence. Transfer to production remains an inference requiring paper-specific validation.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution | Reviewer use |
|---|---|---|---|
| E1 | Full-paper HTML, including title, abstract, headings, and extracted method/evidence text | https://arxiv.org/html/1910.04214 | Primary evidence for notes and claims. |
| E2 | Validated PDF presence and integrity markers | https://arxiv.org/pdf/1910.04214 | Confirms complete source pair; no source file was uploaded. |
| E3 | Canonical arXiv metadata | https://arxiv.org/abs/1910.04214 | Stable identifier and public provenance. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Dataset Baselines` — selected because the entry label shares conceptual cues `data, dataset` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260714-Agent Memory Forensics` — selected because the entry label shares conceptual cues `agent, memory` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260717-Agent Memory Systems` — selected because the entry label shares conceptual cues `agent, memory` with the paper review. Basis: live repository README/artifact path; context only.

## Synthesis Note

### Concept Bridge

The selected paper connects to DEP-E-20260721-Dataset Baselines, DEP-A-20260714-Agent Memory Forensics, DEP-A-20260717-Agent Memory Systems through the shared problem of turning a technical research mechanism into inspectable evidence, reusable system boundaries, and follow-on evaluation. The relationship is conceptual: the selected paper remains the primary evidence source, while the three DEP entries provide repository-grounded comparison cues.

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
record = {"paper_id": "arXiv:1910.04214", "baseline": "toy-baseline", "data": "synthetic"}
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

- Source URL: https://arxiv.org/html/1910.04214
  - Applies to: primary research notes, evidence ledger, manuscript, and Report-Mark.
  - Notes: Full-paper HTML inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/pdf/1910.04214
  - Applies to: source integrity verification.
  - Notes: PDF inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/abs/1910.04214
  - Applies to: canonical identifier and metadata.
  - Notes: Abstract page is metadata only.
- Repository file: .lake-data/DEP-E/DEP-E-20260721-Dataset Baselines
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260714-Agent Memory Forensics
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260717-Agent Memory Systems
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
