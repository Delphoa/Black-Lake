# Report-Mark: Certifying when decision-time information justifies adaptive experimentation

Run date: 2026-08-19

## Source Metadata

- Title: Certifying when decision-time information justifies adaptive experimentation
- Authors: Not available from inspected sources
- Identifier: arXiv:2607.27651
- Public sources: https://arxiv.org/abs/2607.27651; https://arxiv.org/html/2607.27651; https://arxiv.org/pdf/2607.27651
- Source state: complete local PDF and full-paper HTML passed the required integrity gate; source files were withheld from public output.
- Batch position: 76 of 200; selection pool contained 469 unseen valid IDs.

## Concise Research Notes

- Problem: The paper's primary source frames the research problem as: Abstract Adaptive laboratories choose measurements during experiments, yet most methods begin after adaptation is permitted. We introduce Opportunity-aware Policy Authorization for Laboratories ( Opal ), a framework that decides whether adaptation should be enabled at all. Opal uses a precommitted contract to require non-trivial adaptation, controlled target risk and positive executed value after cost. We establish an impossibility boundary: source outcomes and unlabelled target covariates cannot uniformly support non-trivial authorization under unrestricted conditional outcome shift, and derive a target-calibrated recovery. Applied to an unseen 11,265-compound Cell Painting partition, the frozen gate selected 595 compounds, captured 384 positive opportunities and achieved strictly positive executed value under least-favourable completion; its 5.18% false-activation upper bound remained below a 7.5% limit. Among six methods, only Opal combined non-zero activation with this risk control. Locked pharmacogenomic and finite-campaign studies distinguish policy misalignment from non-certifiability, establishing authorization as a distinct layer for safe adaptive science.
- Method: Method-related full-paper text: 2.4 Finite campaigns create an exact certification boundary 2.5 Held-out calibration controls simulator activation risk 2.6 Measured opportunity exceeds the locked policy score 3 Discussion 4 Methods 4.1 Decision setting and information value Information opportunity. 5 Extended Figures 6 Extended Tables References License: CC BY 4.0 arXiv:2607.27651v1 [cs.LG] 30 Jul 2026 [1] \fnm Jia \sur Bi [3] \fnm Chenyang...
- Evidence/results: Evidence-related full-paper text: Certifying when decision-time information justifies adaptive experimentation Report GitHub Issue × Title: Content selection saved. Report Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Results 2.1 Adaptive capacity as a certification problem 2.2 Target calibration recovers a valuable active branch 2.3 Execution audit bounds adaptive value Probe and expert diagnostics.
- Limitations: Limitation-related full-paper text: The empirical studies follow this authorization chain and distinguish failure modes rather than pooling them into one score. Failure at any link returns the experiment to its study-specific best fixed capacity K 0 K_{0} , not to “no experimentation”.
- Implementation relevance: The paper can inform a bounded evidence map, evaluation harness, or research-to-prototype workflow, but the batch did not reproduce the experiments.
- Reviewer interpretation: The strongest supported conclusion is that the paper presents a structured research contribution with inspectable full-paper evidence. Transfer to production remains an inference requiring paper-specific validation.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution | Reviewer use |
|---|---|---|---|
| E1 | Full-paper HTML, including title, abstract, headings, and extracted method/evidence text | https://arxiv.org/html/2607.27651 | Primary evidence for notes and claims. |
| E2 | Validated PDF presence and integrity markers | https://arxiv.org/pdf/2607.27651 | Confirms complete source pair; no source file was uploaded. |
| E3 | Canonical arXiv metadata | https://arxiv.org/abs/2607.27651 | Stable identifier and public provenance. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-ADReFT Adaptive Decision` — selected because the entry label shares conceptual cues `decision, adaptive` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260714-Agent Memory Forensics` — selected because the entry label shares conceptual cues `agent, memory` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260717-Agent Memory Systems` — selected because the entry label shares conceptual cues `agent, memory` with the paper review. Basis: live repository README/artifact path; context only.

## Synthesis Note

### Concept Bridge

The selected paper connects to DEP-E-20260803-ADReFT Adaptive Decision, DEP-A-20260714-Agent Memory Forensics, DEP-A-20260717-Agent Memory Systems through the shared problem of turning a technical research mechanism into inspectable evidence, reusable system boundaries, and follow-on evaluation. The relationship is conceptual: the selected paper remains the primary evidence source, while the three DEP entries provide repository-grounded comparison cues.

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
record = {"paper_id": "arXiv:2607.27651", "baseline": "toy-baseline", "data": "synthetic"}
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

- Source URL: https://arxiv.org/html/2607.27651
  - Applies to: primary research notes, evidence ledger, manuscript, and Report-Mark.
  - Notes: Full-paper HTML inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/pdf/2607.27651
  - Applies to: source integrity verification.
  - Notes: PDF inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/abs/2607.27651
  - Applies to: canonical identifier and metadata.
  - Notes: Abstract page is metadata only.
- Repository file: .lake-data/DEP-E/DEP-E-20260803-ADReFT Adaptive Decision
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260714-Agent Memory Forensics
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260717-Agent Memory Systems
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
