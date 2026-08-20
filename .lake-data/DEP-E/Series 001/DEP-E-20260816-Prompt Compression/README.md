# DEP-E-20260816-Prompt Compression

#prompt-compression #llmlingua #long-context #evidence-replay #agent-memory #provenance #evaluation #context-governance

Public-safe iterative DEP-E research deposit generated from `Black-Lake-Data/.lake-data/DEP-20260706-Tech Intel 1110`. This pass expands the randomly selected LLMLingua thread and preserves its relationship to the source DEP's earlier memory-and-agent-safety and evidence-replay artifacts.

## Contents

- `README.md` - DEP inventory, item summaries, relevance, source policy, and final Attribution Block.
- `prompt-compression.md` - Schema-complete manuscript covering LLMLingua's mechanism, reported evaluation, ablations, overhead, limitations, provenance implications, and safe comparison with evidence replay.

No `.source/` directory is present. No source PDF, TeX package, repository checkout, dataset, model, benchmark payload, dependency, prompt corpus, or execution trace was collected or deposited.

## Summary of Items

### `prompt-compression.md`

The manuscript begins with the selected source DEP, the prior iterative lineage, and the exact selection records. It then expands LLMLingua through the full v2 paper, including its budget controller, iterative token-level compression, distribution alignment, four-dataset evaluation, ablations, latency accounting, and stated limitations.

The main reviewer conclusion is that prompt compression is a resource-optimization layer rather than a trust layer. It can reduce target-model input and reported latency under tested conditions, but it can also remove qualifiers and provenance-bearing context. The artifact therefore frames compression alongside evidence replay, source-span manifests, held-out evaluation, and human review.

## Insights and Relevance

This entry extends the living semantic-web lineage from memory and evidence replay toward auditable context transformation. LLMLingua's component-specific budgets and measurable overhead provide a useful comparison axis for systems that retain full context and replay selected evidence. A future governed gateway should retain immutable originals, source-aware manifests, and escalation rules so that a shorter prompt is never mistaken for a complete evidence record.

## Attribution Block

- Source URL: `Black-Lake-Data/.lake-data/DEP-20260706-Tech Intel 1110/`
  - Applies to: `prompt-compression.md` and this README.
  - Notes: Selected source DEP, original ten-finding synthesis, and prior iterative lineage.
- Source URL: https://arxiv.org/abs/2310.05736
  - Applies to: `prompt-compression.md`.
  - Notes: Canonical LLMLingua record, authors, version, abstract, and stable identifier.
- Source URL: https://arxiv.org/html/2310.05736v2
  - Applies to: `prompt-compression.md`.
  - Notes: Full LLMLingua v2 paper, method, tables, ablations, overhead analysis, and limitations.
- Source URL: https://github.com/microsoft/LLMLingua
  - Applies to: `prompt-compression.md`.
  - Notes: Official implementation context and public package surface; not executed.
- Source URL: `Black-Lake/.lake-data/DEP-E/DEP-E-20260731-Evidence Replay/`
  - Applies to: `prompt-compression.md`.
  - Notes: Prior evidence-replay artifact used for iterative comparison and provenance.
