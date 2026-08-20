# DEP-E-20260719-Memory Depth

#agent-memory #long-running-agents #parametric-memory #retrieval #lora #continual-learning #agent-evaluation

Public-safe deposition context: this DEP-E entry preserves a source-first expansion of arXiv:2606.26806v1, *Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents*. The paper was selected from `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102` after a uniform random DEP draw and a second uniform draw over that DEP's ten primary papers. Public provenance uses repository-relative paths, canonical URLs, date-only values, and UTC-only timestamps. No original paper or supplementary PDF is redistributed.

## Contents

- `README.md`
  - DEP inventory, subject tags, item summaries, insights, source-collection policy, and final attribution.
- `memory-depth.md`
  - Schema-complete manuscript reviewing memory access versus memory depth, the EVAF selection gate, actuation controls, loop-drift results, negative evidence, Memora boundary diagnostic, and safe implementation paths.

No `.source/` directory is included. The canonical paper HTML, main PDF, and five-page ancillary supplement were inspected, but the temporary review copy was not collected into this public deposit.

## Summary of Items

- `README.md` records the DEP-E class, two-file inventory, source policy, relationship to the selected Black-Lake-Data DEP, and public source attribution.
- `memory-depth.md` preserves source metadata, an evidence ledger, table-level metrics, selection-versus-actuation controls, model-specific behavior, negative and boundary results, exactly three exercise paths, a bounded evaluation MVP, related reading, source references, and a replication checklist.

## Insights and Relevance

The paper's most useful contribution is a sharper systems distinction: retrieval can preserve access to old facts while a small parametric store preserves goal-conditioned behavior after working context is cleared. The evidence supports that split only within a controlled synthetic protocol. EVAF writes roughly two to three times per 200 events in the main GPT-2 and TinyLlama runs, but its success depends on both semantic event selection and model-calibrated actuation. The supplement makes the boundary unusually visible: held-out paraphrase is weak, Mistral's original five-step controller is miscalibrated, high-performing actuation can saturate sibling contamination, and Memora stale-memory results are not statistically significant. For Black Lake, this creates a concrete review thread connecting retrieval, persistent behavior, deletion validity, consent, and provenance-aware memory governance.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.26806
  - Applies to: `memory-depth.md`
  - Notes: Canonical metadata, author, v1 history, abstract, DOI marker, license link, and ancillary-file locator.
- Source URL: https://arxiv.org/html/2606.26806
  - Applies to: `memory-depth.md`
  - Notes: Complete public full text used for method, protocol, main results, mechanism controls, limitations, and references.
- Source URL: https://arxiv.org/pdf/2606.26806
  - Applies to: `memory-depth.md`
  - Notes: Primary six-page PDF inspected for formulas, table values, affiliation, and layout; no PDF is redistributed.
- Source URL: https://arxiv.org/src/2606.26806v1/anc/EVAF_supplement.pdf
  - Applies to: `memory-depth.md`
  - Notes: Official five-page ancillary supplement inspected for protocol constants, aggregate and seed-level tables, negative results, and reproducibility paths; no PDF is redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2606.26806
  - Applies to: `memory-depth.md`
  - Notes: Persistent arXiv DOI marker.
- Repository source: `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/README.md`
  - Applies to: `memory-depth.md`
  - Notes: Selected source DEP identity, inventory, source URLs, and original topical synthesis.
- Repository source: `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md`
  - Applies to: `memory-depth.md`
  - Notes: Original finding 2 and the ten-paper expansion pool.
- Repository source: `Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md`
  - Applies to: `memory-depth.md`
  - Notes: Prior abstract-level review; this pass adds full-paper, supplement, and table-level evidence.
- Repository source: `Black-Lake/.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md`
  - Applies to: `memory-depth.md`
  - Notes: Latest prior DEP-Class context linked to the selected source DEP; used only for cross-DEP continuity.
