# Report-Mark: [2511.12152] A Digital SRAM-Based Compute-In-Memory Macro for Weight-Stationary Dynamic Matrix Multiplication in Transformer Attention Score Computation

Run date: 2026-08-19

## Source Metadata

- Title: [2511.12152] A Digital SRAM-Based Compute-In-Memory Macro for Weight-Stationary Dynamic Matrix Multiplication in Transformer Attention Score Computation
- Authors: Yu, Jianyi; Wang, Tengxiao; Wang, Yuxuan; et al.
- Identifier: arXiv:2511.12152
- Public sources: https://arxiv.org/abs/2511.12152; https://arxiv.org/html/2511.12152; https://arxiv.org/pdf/2511.12152
- Source state: complete local PDF and full-paper HTML passed the required integrity gate; source files were withheld from public output.
- Batch position: 152 of 200; selection pool contained 469 unseen valid IDs.

## Concise Research Notes

- Problem: The paper's primary source frames the research problem as: Abstract: Compute-in-memory (CIM) techniques are widely employed in energy-efficient artificial intelligent (AI) processors. They alleviate power and latency bottlenecks caused by extensive data movements between compute and storage units. To extend these benefits to Transformer, this brief proposes a digital CIM macro to compute attention score. To eliminate dynamic matrix multiplication (MM), we reconstruct the computation as static MM using a combined QK-weight matrix, so that inputs can be directly fed to a single CIM macro to obtain the score results. However, this introduces a new challenge of 2-input static MM. The computation is further decomposed into four groups of bit-serial logical and addition operations. This allows 2-input to directly activate the word line via AND gate, thus realizing 2-input static MM with minimal overhead. A hierarchical zero-value bit skipping mechanism is introduced to prioritize skipping zero-value bits in the 2-input case. This mechanism effectively utilizes data sparsity of 2-input, significantly reducing redundant operations. Implemented in a 65-nm process, the 0.35 mm2 macro delivers 42.27 GOPS at 1.24 mW, yielding 34.1 TOPS/W energy and 120.77 GOPS/mm2 area efficiency. Compared to CPUs and GPUs, it achieves ~25x and ~13x higher efficiency, respectively. Against other Transformer-CIMs, it demonstrates at least 7x energy and 2x area efficiency gains, highlighting its strong potential for edge intelligence.
- Method: Method-related full-paper text: [2511.12152] A Digital SRAM-Based Compute-In-Memory Macro for Weight-Stationary Dynamic Matrix Multiplication in Transformer Attention Score Computation Skip to main content Search Submit Donate Log in Search arXiv Press Enter to search · Advanced search --> Computer Science > Hardware Architecture arXiv:2511.12152 (cs) [Submitted on 15 Nov 2025 ( v1 ), last revised 12 Dec 2025 (this version, v3)] Title: A...
- Evidence/results: Evidence-related full-paper text: To eliminate dynamic matrix multiplication (MM), we reconstruct the computation as static MM using a combined QK-weight matrix, so that inputs can be directly fed to a single CIM macro to obtain the score results. ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features...
- Limitations: Limitation-related full-paper text: Not available from inspected full-paper text.
- Implementation relevance: The paper can inform a bounded evidence map, evaluation harness, or research-to-prototype workflow, but the batch did not reproduce the experiments.
- Reviewer interpretation: The strongest supported conclusion is that the paper presents a structured research contribution with inspectable full-paper evidence. Transfer to production remains an inference requiring paper-specific validation.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution | Reviewer use |
|---|---|---|---|
| E1 | Full-paper HTML, including title, abstract, headings, and extracted method/evidence text | https://arxiv.org/html/2511.12152 | Primary evidence for notes and claims. |
| E2 | Validated PDF presence and integrity markers | https://arxiv.org/pdf/2511.12152 | Confirms complete source pair; no source file was uploaded. |
| E3 | Canonical arXiv metadata | https://arxiv.org/abs/2511.12152 | Stable identifier and public provenance. |

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260722-ProjAgent Code Retrieval` — selected because the entry label shares conceptual cues `agent, retrieval` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260727-Agent Control Intake` — selected because the entry label shares conceptual cues `agent, control` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260729-Express Language Modeling` — selected because the entry label shares conceptual cues `language, model` with the paper review. Basis: live repository README/artifact path; context only.

## Synthesis Note

### Concept Bridge

The selected paper connects to DEP-A-20260722-ProjAgent Code Retrieval, DEP-A-20260727-Agent Control Intake, DEP-A-20260729-Express Language Modeling through the shared problem of turning a technical research mechanism into inspectable evidence, reusable system boundaries, and follow-on evaluation. The relationship is conceptual: the selected paper remains the primary evidence source, while the three DEP entries provide repository-grounded comparison cues.

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
record = {"paper_id": "arXiv:2511.12152", "baseline": "toy-baseline", "data": "synthetic"}
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

- Source URL: https://arxiv.org/html/2511.12152
  - Applies to: primary research notes, evidence ledger, manuscript, and Report-Mark.
  - Notes: Full-paper HTML inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/pdf/2511.12152
  - Applies to: source integrity verification.
  - Notes: PDF inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/abs/2511.12152
  - Applies to: canonical identifier and metadata.
  - Notes: Abstract page is metadata only.
- Repository file: .lake-data/DEP-A/DEP-A-20260722-ProjAgent Code Retrieval
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260727-Agent Control Intake
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260729-Express Language Modeling
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
