# Report-Mark: Scalar-pathway fidelity improves physical accuracy in short-range equivariant interatomic potentials

Run date: 2026-08-19

## Source Metadata

- Title: Scalar-pathway fidelity improves physical accuracy in short-range equivariant interatomic potentials
- Authors: Not available from inspected sources
- Identifier: arXiv:2606.15892
- Public sources: https://arxiv.org/abs/2606.15892; https://arxiv.org/html/2606.15892; https://arxiv.org/pdf/2606.15892
- Source state: complete local PDF and full-paper HTML passed the required integrity gate; source files were withheld from public output.
- Batch position: 130 of 200; selection pool contained 469 unseen valid IDs.

## Concise Research Notes

- Problem: The paper's primary source frames the research problem as: Abstract Accurate interatomic potentials enable molecular dynamics of materials, molecules, and interfaces beyond density-functional-theory length and time scales. Equivariant neural network potentials have improved the representation of local geometry. However, their deployable energy surfaces ultimately manifest through invariant scalar channels, whose aggregation and spectral resolution remain comparatively underexamined. Here we use Physics-Aware Neighborhood (PAN) pooling and Physics-Guided Spectral (PGS) mixers as controlled scalar-pathway probes: lightweight, symmetry-preserving modifications that act only on ℓ = 0 \ell=0 channels while leaving the equivariant tensor backbone unchanged. Using MACE as a high-body-order mechanistic scaffold, PAN adds coordination-sensitive amplitude modulation, whereas PGS augments edge and readout scalar features with radial and tapered spectral bases. Across metallic Ag, covalent Si, a short-range ionic LiF/Li–F subset, and MD17/rMD17 molecules, this scalar-pathway correction reduces MACE force errors by 22–27% and energy errors by 19–22%; on systems with stress labels, stress errors decrease by 27–28%, at approximately 5% additional inference-FLOPs cost. Directionally consistent gains in Allegro and NequIP further indicate that the correction is portable across distinct short-range equivariant backbones, although effect sizes remain architecture-dependent. These results identify scalar-pathway fidelity as a practical design dimension for short-range equivariant interatomic potentials.
- Method: Method-related full-paper text: Report Issue Back to Abstract Download PDF Abstract S1 Introduction S2 Results S2.1 A scalar compression interface in short-range equivariant MLIPs S2.2 Scalar-channel corrections: accuracy gains, minimal overhead S2.3 Geometric and spectral corrections operate via distinct scalar pathways S2.4 Scalar-pathway fidelity transfers to physical observables S3 Discussion S4 Methods S4.1 Scalar-pathway architecture S4.2...
- Evidence/results: Evidence-related full-paper text: Scalar-pathway fidelity improves physical accuracy in short-range equivariant interatomic potentials Report GitHub Issue × Title: Content selection saved. Report Issue Back to Abstract Download PDF Abstract S1 Introduction S2 Results S2.1 A scalar compression interface in short-range equivariant MLIPs S2.2 Scalar-channel corrections: accuracy gains, minimal overhead S2.3 Geometric and spectral corrections operate...
- Limitations: Limitation-related full-paper text: Two systemic limitations arise. The messages being summed are themselves learned distance-, species-, and feature-dependent quantities; the limitation is that the final scalar aggregation lacks an explicit adaptive amplitude gate conditioned on local coordination, density, or geometric distortion.
- Implementation relevance: The paper can inform a bounded evidence map, evaluation harness, or research-to-prototype workflow, but the batch did not reproduce the experiments.
- Reviewer interpretation: The strongest supported conclusion is that the paper presents a structured research contribution with inspectable full-paper evidence. Transfer to production remains an inference requiring paper-specific validation.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution | Reviewer use |
|---|---|---|---|
| E1 | Full-paper HTML, including title, abstract, headings, and extracted method/evidence text | https://arxiv.org/html/2606.15892 | Primary evidence for notes and claims. |
| E2 | Validated PDF presence and integrity markers | https://arxiv.org/pdf/2606.15892 | Confirms complete source pair; no source file was uploaded. |
| E3 | Canonical arXiv metadata | https://arxiv.org/abs/2606.15892 | Stable identifier and public provenance. |

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260714-Agent Memory Forensics` — selected because the entry label shares conceptual cues `agent, memory` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260717-Agent Memory Systems` — selected because the entry label shares conceptual cues `agent, memory` with the paper review. Basis: live repository README/artifact path; context only.
1. `.lake-data/DEP-A/DEP-A-20260719-Agent Memory Benchmark` — selected because the entry label shares conceptual cues `agent, memory` with the paper review. Basis: live repository README/artifact path; context only.

## Synthesis Note

### Concept Bridge

The selected paper connects to DEP-A-20260714-Agent Memory Forensics, DEP-A-20260717-Agent Memory Systems, DEP-A-20260719-Agent Memory Benchmark through the shared problem of turning a technical research mechanism into inspectable evidence, reusable system boundaries, and follow-on evaluation. The relationship is conceptual: the selected paper remains the primary evidence source, while the three DEP entries provide repository-grounded comparison cues.

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
record = {"paper_id": "arXiv:2606.15892", "baseline": "toy-baseline", "data": "synthetic"}
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

- Source URL: https://arxiv.org/html/2606.15892
  - Applies to: primary research notes, evidence ledger, manuscript, and Report-Mark.
  - Notes: Full-paper HTML inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/pdf/2606.15892
  - Applies to: source integrity verification.
  - Notes: PDF inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/abs/2606.15892
  - Applies to: canonical identifier and metadata.
  - Notes: Abstract page is metadata only.
- Repository file: .lake-data/DEP-A/DEP-A-20260714-Agent Memory Forensics
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260717-Agent Memory Systems
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
- Repository file: .lake-data/DEP-A/DEP-A-20260719-Agent Memory Benchmark
  - Applies to: related-context synthesis.
  - Notes: Public Black Lake context entry; conceptual neighbor, not primary evidence.
