# Report-Mark: [1204.1113] Sub-Linear Root Detection, and New Hardness Results, for Sparse Polynomials Over Finite Fields

Run date: 2026-08-19

## Source Metadata

- Title: [1204.1113] Sub-Linear Root Detection, and New Hardness Results, for Sparse Polynomials Over Finite Fields
- Authors: Not available from inspected sources
- Identifier: arXiv:1204.1113
- Public sources: https://arxiv.org/abs/1204.1113; https://arxiv.org/html/1204.1113; https://arxiv.org/pdf/1204.1113
- Source state: complete local PDF and full-paper HTML passed the required integrity gate; source files were withheld from public output.
- Batch position: 132 of 200; selection pool contained 469 unseen valid IDs.

## Concise Research Notes

- Problem: The paper's primary source frames the research problem as: Abstract. We present a deterministic 2 O ​ ( t ) ​ q t − 2 t − 1 + o ​ ( 1 ) superscript 2 𝑂 𝑡 superscript 𝑞 𝑡 2 𝑡 1 𝑜 1 2^{O(t)}q^{\frac{t-2}{t-1}+o(1)} algorithm to decide whether a univariate polynomial f 𝑓 f , with exactly t 𝑡 t monomial terms and degree < q absent 𝑞 <\!q , has a root in 𝔽 q subscript 𝔽 𝑞 \mathbb{F}_{q} . A corollary of our method — the first with complexity sub-linear in q 𝑞 q when t 𝑡 t is fixed — is that the nonzero roots in 𝔽 q subscript 𝔽 𝑞 \mathbb{F}_{q} can be partitioned into no more than 2 ​ t − 1 ​ ( q − 1 ) t − 2 t − 1 2 𝑡 1 superscript 𝑞 1 𝑡 2 𝑡 1 2\sqrt{t-1}(q-1)^{\frac{t-2}{t-1}} cosets of two proper subgroups S 1 ⊆ S 2 subscript 𝑆 1 subscript 𝑆 2 S_{1}\subseteq S_{2} of 𝔽 q ∗ subscript superscript 𝔽 𝑞 \mathbb{F}^{*}_{q} . Another corollary is the first deterministic sub-linear algorithm for detecting common degree one factors of k 𝑘 k -tuples of t 𝑡 t -nomials in 𝔽 q ​ [ x ] subscript 𝔽 𝑞 delimited-[] 𝑥 \mathbb{F}_{q}[x] when k 𝑘 k and t 𝑡 t are fixed. When t 𝑡 t is not fixed we show that each of the following problems is 𝐍𝐏 𝐍𝐏 {\mathbf{NP}} -hard with respect to 𝐁𝐏𝐏 𝐁𝐏𝐏 {\mathbf{BPP}} -reductions, even when p 𝑝 p is prime: ∙ ∙ \bullet detecting roots in 𝔽 p subscript 𝔽 𝑝 \mathbb{F}_{p} for f 𝑓 f
- Method: Method-related full-paper text: We present a deterministic 2 O ​ ( t ) ​ q t − 2 t − 1 + o ​ ( 1 ) superscript 2 𝑂 𝑡 superscript 𝑞 𝑡 2 𝑡 1 𝑜 1 2^{O(t)}q^{\frac{t-2}{t-1}+o(1)} algorithm to decide whether a univariate polynomial f 𝑓 f , with exactly t 𝑡 t monomial terms and degree < q absent 𝑞 <\!q , has a root in 𝔽 q subscript 𝔽 𝑞 \mathbb{F}_{q} . A corollary of our method — the first with complexity sub-linear in q 𝑞 q when t 𝑡 t is fixed — is...
- Evidence/results: Evidence-related full-paper text: [1204.1113] Sub-Linear Root Detection, and New Hardness Results, for Sparse Polynomials Over Finite Fields Abstract. Key words and phrases: solvability, sparse polynomial, finite fields, 𝐍𝐏 𝐍𝐏 {\mathbf{NP}} -hardness, gcd, square-free, discriminant, resultant School of Mathematics, Shandong University, Jinan, 250100, P.R.
- Limitations: Limitation-related full-paper text: Not available from inspected full-paper text.
- Implementation relevance: The paper can inform a bounded evidence map, evaluation harness, or research-to-prototype workflow, but the batch did not reproduce the experiments.
- Reviewer interpretation: The strongest supported conclusion is that the paper presents a structured research contribution with inspectable full-paper evidence. Transfer to production remains an inference requiring paper-specific validation.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution | Reviewer use |
|---|---|---|---|
| E1 | Full-paper HTML, including title, abstract, headings, and extracted method/evidence text | https://arxiv.org/html/1204.1113 | Primary evidence for notes and claims. |
| E2 | Validated PDF presence and integrity markers | https://arxiv.org/pdf/1204.1113 | Confirms complete source pair; no source file was uploaded. |
| E3 | Canonical arXiv metadata | https://arxiv.org/abs/1204.1113 | Stable identifier and public provenance. |

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
record = {"paper_id": "arXiv:1204.1113", "baseline": "toy-baseline", "data": "synthetic"}
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

- Source URL: https://arxiv.org/html/1204.1113
  - Applies to: primary research notes, evidence ledger, manuscript, and Report-Mark.
  - Notes: Full-paper HTML inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/pdf/1204.1113
  - Applies to: source integrity verification.
  - Notes: PDF inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/abs/1204.1113
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
