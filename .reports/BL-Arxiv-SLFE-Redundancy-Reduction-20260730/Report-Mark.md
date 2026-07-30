# Report-Mark — SLFE Redundancy Reduction

## Source Metadata

- Work: *Start Late or Finish Early: A Distributed Graph Processing System with Redundancy Reduction*.
- Authors: Shuang Song, Xu Liu, Qinzhe Wu, Andreas Gerstlauer, Tao Li, and Lizy K. John.
- Identifier: arXiv:1805.12305v1; DOI: https://doi.org/10.48550/arXiv.1805.12305.
- Submitted: 2018-05-31; subject: Distributed, Parallel, and Cluster Computing.
- Inspected sources: canonical arXiv record, complete PDF, validated full-paper HTML fallback, and local extraction-cache public summary.
- Source integrity: the local unit began partial because HTML was absent. Bounded repair preserved the PDF and produced full-paper HTML that passed the complete-source gate. Source documents and cache outputs were withheld locally and not uploaded.

## Concise Research Notes

SLFE argues that iterative distributed graph engines trade work optimality for parallelism. It derives redundancy-reduction guidance (RRG) in preprocessing by recording each vertex's final propagation level. In min/max work, RRG delays computation until a vertex's relevant propagation level; in arithmetic work, it permits an early-stable vertex to stop receiving further computation. The design combines RRG-aware pull operations, reactivation at push transitions, APIs, and work stealing.

The paper evaluates five graph applications over seven real graphs on an eight-node cluster. It reports up to 74.8× speedup and 16.5× average in the abstract/contribution summary. The evaluation further reports a 25.39× geometric mean against PowerGraph/PowerLyra, Gemini improvements of 34.2%, 43.1%, 42.7%, 47.5%, and 41.6% for SSSP, CC, WP, PR, and TR, and a 25.1% end-to-end SSSP improvement over Gemini after preprocessing. These values are author-reported and unreplicated.

## Evidence and Attribution

| Evidence | Inspected basis | What it supports | Qualification |
|---|---|---|---|
| E1 | arXiv metadata and abstract | Identity, stated problem, authors, date, 74.8× headline | Metadata alone is not full-paper evidence. |
| E2 | PDF and full-paper HTML | RRG algorithm, push/pull design, applications, benchmark tables, limitations | No independent implementation or benchmark run. |
| E3 | Extraction-cache public summary | Cache miss-to-cached state and extractor fallback | Cache supports navigation, not a new scientific result. |
| E4 | FeLoG DEP-A | Active-frontier state, communication, and scheduler comparison | Different graph-embedding/model-serving workload. |
| E5 | ObjectCache DEP-A | Avoiding repeated computation through reusable state and scheduled transfer | Different object and latency model. |
| E6 | MemGraphRAG DEP-A | Global graph state preventing fragmented local decisions | Different quality objective. |

## Related DEP Entries

1. [`DEP-A-20260726-FeLoG Feedback Graph`](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/DEP-A-20260726-FeLoG%20Feedback%20Graph) — concrete overlap in active-frontier control, distributed resource placement, communication overlap, and measurable scheduling state.
2. [`DEP-A-20260715-ObjectCache Layerwise Obj`](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/DEP-A-20260715-ObjectCache%20Layerwise%20Obj) — concrete overlap in eliminating redundant work by reusing immutable state and scheduling it around downstream computation.
3. [`DEP-A-20260715-MemGraphRAG Memory based`](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/DEP-A-20260715-MemGraphRAG%20Memory%20based) — concrete overlap in using reusable global graph context to correct decisions that are poor when made only locally.

## Synthesis Note

### Concept Bridge

SLFE turns graph topology into a versioned scheduling signal. FeLoG, ObjectCache, and MemGraphRAG show the same broader systems pattern in different domains: preserve a state representation, make decisions conditionally on that state, execute only the work justified by the decision, and retain enough observability to detect when the state is stale or the decision causes skew. The bridge is conditional work avoidance with a recoverable fallback, not an assertion that these systems implement the same algorithm.

### Potential Implementations — Exactly 3

1. A graph-job scheduler that shadows RRG-style readiness rules against a full baseline before permitting avoided work.
2. A convergence-aware analytics runtime that records per-vertex stable counts, reactivation events, and output-equivalence checks.
3. An observability service that joins state-version, avoided-work, communication, imbalance, and tail-latency telemetry for iterative jobs.

### Deeper Relationship Observations — Exactly 3

1. SLFE's `lastIter`, FeLoG's active frontier, ObjectCache's matched prefix, and MemGraphRAG's global memory are all decision states whose provenance matters as much as their value.
2. Work avoidance shifts cost rather than deleting it: preprocessing, state maintenance, scheduling, verification, and fallback must appear in the same end-to-end ledger.
3. The primary failure mode is not merely lower throughput; it is stale or uneven state producing missed work, rework, skew, or unjustified confidence.

### Conceptual Similarities — Exactly 3

1. Each system exposes a reusable intermediate representation instead of recomputing from raw inputs for every downstream step.
2. Each benefits only when the representation is valid for the current workload and inexpensive enough to amortize.
3. Each needs a bounded transition or fallback path when a previously inactive item becomes relevant again.

### MVP Implementations with Code Mock-ups — Exactly 3

1. `Readiness-gated work queue`

```python
def eligible(vertex, iteration, guidance):
    return iteration >= guidance[vertex].last_relevant_iteration

work = [v for v in active_vertices if eligible(v, iteration, rrg)]
```

2. `Stable-state guard`

```python
def should_compute(state, guidance):
    if state.changed:
        state.stable_count = 0
    else:
        state.stable_count += 1
    return state.stable_count <= guidance.last_relevant_iteration
```

3. `Shadow equivalence receipt`

```python
receipt = compare_outputs(full_run(), gated_run())
if not receipt.equal:
    disable_policy("output-mismatch")
```

### Developer Challenges — Exactly 3

1. Define aggregation-specific correctness invariants rather than applying a generic skip rule.
2. Keep graph, partition, and guidance versions synchronized across workers and topology updates.
3. Measure preprocessing, reactivation, communication, and tail effects so a mean speedup cannot conceal regressions.

### Author Challenges — Exactly 3

1. Release a reproducible implementation, environment specification, and benchmark scripts for the reported comparisons.
2. Quantify dynamic-topology, failure, energy, and tail-latency boundaries alongside aggregate runtime.
3. Test and report inter-node balancing controls under stronger skew and modern heterogeneous hardware.

## Validation Notes

- Source claims were cross-checked against the inspected full paper rather than treated as abstract-only facts.
- The source gate passed only after repair yielded both a valid PDF and a structurally complete full-paper HTML document.
- The related-entry list is exactly three, uses repository-relative public locations, and does not claim same-paper identity.
- This record contains only public URLs and generated analysis; no local path, source file, cache output, username, machine name, timezone, or exact execution timestamp is included.

## Attribution Block

- Source URL: https://arxiv.org/abs/1805.12305
  - Applies to: this Report-Mark.
  - Notes: canonical metadata and abstract record.
- Source URL: https://arxiv.org/pdf/1805.12305
  - Applies to: evidence review in this Report-Mark.
  - Notes: complete source was reviewed locally and withheld from the repository.
- Source URL: https://ar5iv.labs.arxiv.org/html/1805.12305
  - Applies to: evidence review in this Report-Mark.
  - Notes: approved full-paper fallback was locally validated and withheld from the repository.
- Source URL: https://doi.org/10.48550/arXiv.1805.12305
  - Applies to: paper identity in this Report-Mark.
  - Notes: canonical arXiv DOI.
- Related public records: FeLoG, ObjectCache, and MemGraphRAG DEP paths listed above.
  - Applies to: Synthesis Note and related-entry comparison.
  - Notes: conceptual context only; no source files were uploaded.
