# Report-Mark: [2011.00667] Asynchronous Parallel Stochastic Quasi-Newton Methods

Run date: 2026-08-19

## Source Metadata

- Title: [2011.00667] Asynchronous Parallel Stochastic Quasi-Newton Methods
- Authors: Not available from inspected sources
- Identifier: arXiv:2011.00667
- Public sources: https://arxiv.org/abs/2011.00667; https://arxiv.org/html/2011.00667; https://arxiv.org/pdf/2011.00667
- Source state: complete local PDF and full-paper HTML passed the required integrity gate; source files were withheld from public output.
- Batch position: 38 of 200; selection pool contained 469 unseen valid IDs.

## Concise Research Notes

- Problem: The paper's primary source frames the research problem as: Abstract Although first-order stochastic algorithms, such as stochastic gradient descent, have been the main force to scale up machine learning models, such as deep neural nets, the second-order quasi-Newton methods start to draw attention due to their effectiveness in dealing with ill-conditioned optimization problems. The L-BFGS method is one of the most widely used quasi-Newton methods. We propose an asynchronous parallel algorithm for stochastic quasi-Newton (AsySQN) method. Unlike prior attempts, which parallelize only the calculation for gradient or the two-loop recursion of L-BFGS, our algorithm is the first one that truly parallelizes L-BFGS with a convergence guarantee. Adopting the variance reduction technique, a prior stochastic L-BFGS, which has not been designed for parallel computing, reaches a linear convergence rate. We prove that our asynchronous parallel scheme maintains the same linear convergence rate but achieves significant speedup. Empirical evaluations in both simulations and benchmark datasets demonstrate the speedup in comparison with the non-parallel stochastic L-BFGS, as well as the better performance than first-order methods in solving ill-conditioned problems.
- Method: Method-related full-paper text: [2011.00667] Asynchronous Parallel Stochastic Quasi-Newton Methods Asynchronous Parallel Stochastic Quasi-Newton Methods Qianqian Tong 1 qianqian.tong@uconn.edu Guannan Liang 1 guannan.liang@uconn.edu Xingyu Cai 2 xingyucai@baidu.com Chunjiang Zhu 1 chunjiang.zhu@uconn.edu Jinbo Bi 1 jinbo.bi@uconn.edu 1 University of Connecticut, Storrs, CT 06269, 2 Baidu USA, Sunnyvale, CA 94089 Abstract Although first-order...
- Evidence/results: Evidence-related full-paper text: Empirical evaluations in both simulations and benchmark datasets demonstrate the speedup in comparison with the non-parallel stochastic L-BFGS, as well as the better performance than first-order methods in solving ill-conditioned problems. Notice that in the analysis of DAve-QN method, they have a strong requirement for condition number of the objective functions in Lemma 2 of [ 34 ] , which is hard to satisfied...
- Limitations: Limitation-related full-paper text: The idea of using overlapping sets to evaluate curvature information helps if a node failure is encountered. However, when dealing with machine learning problems under big datasets, or considering the possibility of node failures, deterministic algorithms like the decentralized ones perform no better than stochastic ones.
- Implementation relevance: The paper can inform a bounded evidence map, evaluation harness, or research-to-prototype workflow, but the batch did not reproduce the experiments.
- Reviewer interpretation: The strongest supported conclusion is that the paper presents a structured research contribution with inspectable full-paper evidence. Transfer to production remains an inference requiring paper-specific validation.

## Evidence and Attribution

| Evidence ID | Evidence | Attribution | Reviewer use |
|---|---|---|---|
| E1 | Full-paper HTML, including title, abstract, headings, and extracted method/evidence text | https://arxiv.org/html/2011.00667 | Primary evidence for notes and claims. |
| E2 | Validated PDF presence and integrity markers | https://arxiv.org/pdf/2011.00667 | Confirms complete source pair; no source file was uploaded. |
| E3 | Canonical arXiv metadata | https://arxiv.org/abs/2011.00667 | Stable identifier and public provenance. |

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
record = {"paper_id": "arXiv:2011.00667", "baseline": "toy-baseline", "data": "synthetic"}
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

- Source URL: https://arxiv.org/html/2011.00667
  - Applies to: primary research notes, evidence ledger, manuscript, and Report-Mark.
  - Notes: Full-paper HTML inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/pdf/2011.00667
  - Applies to: source integrity verification.
  - Notes: PDF inspected locally; source file withheld from the public repository.
- Source URL: https://arxiv.org/abs/2011.00667
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
