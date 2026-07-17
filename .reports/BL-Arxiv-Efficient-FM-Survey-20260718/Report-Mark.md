# Report-Mark: Efficient FM Survey

Public-safe run date: 2026-07-18

## Source Metadata

| Field | Value |
|---|---|
| Full title | *A Survey of Resource-efficient LLM and Multimodal Foundation Models* |
| Authors | Mengwei Xu; Wangsong Yin; Dongqi Cai; Rongjie Yi; Daliang Xu; Qipeng Wang; Bingyang Wu; Yihao Zhao; Chen Yang; Shihe Wang; Qiyang Zhang; Zhenyan Lu; Li Zhang; Shangguang Wang; Yuanchun Li; Yunxin Liu; Xin Jin; Xuanzhe Liu |
| Stable identifier | arXiv:2401.08092v2; DOI:10.48550/arXiv.2401.08092 |
| Dates | Submitted 2024-01-16; v2 revised 2024-09-23 |
| Subjects | Machine Learning; Artificial Intelligence; Distributed, Parallel, and Cluster Computing |
| Primary records | https://arxiv.org/abs/2401.08092; https://arxiv.org/html/2401.08092; https://arxiv.org/pdf/2401.08092 |
| Official companion repository | https://github.com/UbiquitousLearning/Efficient_Foundation_Model_Survey |
| Local source state | Verified complete after repair; PDF, full-paper HTML, metadata HTML, and source package retained locally and withheld from public output |
| Review type | Source-first survey review, evidence-bound critique, and exactly-three-entry DEP synthesis |

## Concise Research Notes

- `Problem`: Foundation models improve with scale but impose large compute, memory, storage, bandwidth, energy, and deployment costs across training and inference. The survey asks how algorithm and system design can reduce these physical-resource demands without treating hardware design itself as the review's main subject.
- `Core method`: This is a structured literature survey rather than a new optimization algorithm. It organizes post-2020 work into three layers: resource-efficient architectures; resource-efficient algorithms across pre-training, fine-tuning, inference, and model compression; and resource-efficient systems across distributed training, federated learning, cloud serving, and edge serving.
- `Evidence/results`: The 65-page v2 paper synthesizes hundreds of cited works, figures, tables, and source-reported measurements. Its strongest evidence for this review is the explicit lifecycle taxonomy and the mechanism-level comparisons among sparse/approximate attention, dynamic networks, prompt and KV-cache compression, pruning/distillation/quantization/low-rank methods, scheduling/offloading, and edge/cloud deployment. Individual speed, energy, or quality numbers remain claims reported by the surveyed sources unless independently cross-checked.
- `Limitations`: The paper is not a formal systematic review with a reproducible search string, screening ledger, risk-of-bias assessment, or common benchmark. It prioritizes top-tier CS venues plus manually selected arXiv work, mainly after 2020. It explicitly excludes hardware design and narrows “resource” to physical resources; it also excludes training data and privacy as resource categories even though privacy reappears as a future deployment concern. Its September 2024 cutoff makes the fast-moving catalog increasingly incomplete.
- `Implementation relevance`: The taxonomy is useful as a design and review checklist. It prevents a team from equating model compression with complete system efficiency and encourages measurement across architecture, algorithm, serving runtime, workload, and hardware placement.
- `Reviewer interpretation`: The most useful unit is an end-to-end resource contract, not a named technique. Each candidate optimization should declare the constrained resource, quality budget, workload/hardware envelope, recovery behavior, and measurement method. The three related DEP entries provide concrete test cases for that contract.

## Evidence and Attribution

| ID | Evidence inspected | Supports | Evidence boundary |
|---|---|---|---|
| E1 | Canonical arXiv metadata and DOI | Identity, complete authorship, v2 date, subjects, public source links | Metadata does not validate technical claims |
| E2 | Complete arXiv full-paper HTML | Scope, taxonomy, mechanisms, reported examples, conclusions, and six future directions | Survey prose summarizes many external works; source-reported numbers are not independent reproductions |
| E3 | Complete 65-page PDF and text layer | Rendered organization figure, section transitions, tables/figures, and consistency with HTML | Visual screenshot tooling was incomplete for several pages; no figure values were digitized |
| E4 | Official companion repository README | Maintained paper/figure list and scope statement | Repository breadth is curation evidence, not benchmark validation |
| E5 | KDFlow DEP manuscript and README | Distillation as workload-specialized execution plus quality preservation | Author-reported speed/quality results were not rerun |
| E6 | CompressKV DEP review and README | KV-cache selection as a memory controller with quality/recovery trade-offs | Newer overlapping arXiv lineage is not independent corroboration; no reproduction performed |
| E7 | llama.cpp Runtime DEP manuscript and README | Quantization/runtime packaging and compatibility as the deployment layer | Release inventory and one commit do not prove performance or production readiness |
| E8 | Live Black Lake and Black-Lake-Data READMEs, Black Lake `.lake-data/README.md`, dedup pointer, and automation memory | Filing, source-withholding, publication-index, selection, and dedup rules | Process evidence, not technical evidence about the paper |

Source claims, repository observations, and reviewer inference are labeled separately throughout. No experimental result in this Report-Mark is presented as independently reproduced.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` — selected because KDFlow makes the survey's knowledge-distillation and distributed-systems categories concrete: teacher inference uses SGLang, student training uses FSDP2, Ray coordinates the roles, and hidden-state transfer reduces communication. Source basis: arXiv:2603.01875v2 and https://github.com/songmzhang/KDFlow.
2. `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/2606.24467-whitepaper-review.md` — selected because it operationalizes the survey's inference-compression and KV-cache categories through semantic-retrieval-head token selection and layer-sensitive budgets. Source basis: arXiv:2606.24467v1 and https://github.com/TUDa-HWAI/CompressKV.
3. `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md` — selected because it grounds the survey's model-compression, cloud/edge serving, and local-runtime categories in an official llama.cpp release and quantization correction. Source basis: https://github.com/ggml-org/llama.cpp/releases/tag/b9789 and its linked commit.

## Synthesis Note

### Concept Bridge

The survey supplies the map; the three DEP entries expose the interfaces between map regions. KDFlow starts before deployment by deciding where teacher inference and student optimization should execute and what representation should cross the process boundary. CompressKV acts during autoregressive serving by deciding which history remains in fast memory and which semantic signals control eviction. llama.cpp Runtime is the final executable boundary, where quantized model representation, platform packaging, kernels, and compatibility corrections determine whether an efficiency claim survives contact with real hardware.

The bridge is therefore a resource-aware lifecycle: distill or otherwise adapt a model under a quality gate; manage runtime state under a recoverability-aware memory gate; then deploy through a versioned runtime under compatibility and provenance gates. None of these layers can be optimized in isolation. A smaller student may still carry an expensive KV cache; an aggressive cache policy may erase evidence; a compact model and cache may still fail on a runtime's quantization edge case. The survey's broad taxonomy becomes actionable when every transition has explicit measures and stop conditions.

### Potential Implementations

1. `Cross-Layer Efficiency Ledger`: Join model/adaptation configuration, cache policy, runtime build, workload, hardware, and quality metrics in one signed record; reject comparisons whose envelopes differ materially.
2. `Adaptive Local Serving Planner`: Choose student checkpoint, cache budget, quantization, and platform target from declared latency/memory/quality constraints, then require a bounded smoke test before recommendation.
3. `Recoverable Compression Gateway`: Combine distillation and semantic cache selection with cold-tier or recomputation pointers so low-confidence requests can restore evicted evidence instead of silently failing.

### Deeper Relationship Observations

1. All three DEP entries move information across a constrained boundary: teacher hidden states cross processes, selected semantic tokens cross time through the KV cache, and quantized weights cross storage/hardware/runtime boundaries.
2. Each optimization depends on a proxy for value—teacher distributions, attention-derived token relevance, or quantization/runtime compatibility—and each proxy can fail outside its calibration envelope.
3. The survey's architecture/algorithm/system separation is analytically useful, but implementation risk concentrates at their interfaces, where version drift, workload mismatch, and hidden resource transfers appear.

### Conceptual Similarities

1. `Selective preservation`: KDFlow preserves teacher knowledge in a compact transfer representation; CompressKV preserves selected prompt evidence; llama.cpp preserves model behavior under a compact runtime representation.
2. `Workload specialization`: Teacher and student use different engines, attention heads/layers receive different cache roles or budgets, and runtime packages target different platforms and accelerators.
3. `Quality-constrained efficiency`: Every approach claims resource improvement while intending to retain behavior, but each needs a separately measured quality or correctness gate.

### MVP Implementations with Code Mock-Ups

#### MVP 1: Pareto release gate

Score a candidate only inside declared budgets; retain the full metric vector instead of collapsing it to one opaque number.

```python
def release_gate(candidate, limits):
    checks = {
        "quality": candidate["quality"] >= limits["quality_min"],
        "latency": candidate["latency_ms"] <= limits["latency_max_ms"],
        "memory": candidate["memory_mb"] <= limits["memory_max_mb"],
        "energy": candidate["energy_j"] <= limits["energy_max_j"],
    }
    return {"pass": all(checks.values()), "checks": checks}
```

#### MVP 2: Recoverable cache controller

Keep high-value tokens hot and preserve a cold-tier pointer for every eviction candidate.

```python
def tier_tokens(tokens, relevance, hot_budget):
    ranked = sorted(range(len(tokens)), key=lambda i: relevance[i], reverse=True)
    hot_ids = set(ranked[:hot_budget])
    hot = [tokens[i] for i in range(len(tokens)) if i in hot_ids]
    cold = [{"index": i, "token": tokens[i]} for i in range(len(tokens)) if i not in hot_ids]
    return hot, cold
```

#### MVP 3: Runtime evidence matrix

Separate published packages from locally verified combinations.

```python
def compatibility_status(release_assets, test_records):
    tested = {(r["asset"], r["model"]) for r in test_records if r["passed"]}
    return [
        {"asset": asset, "model": model, "verified": (asset, model) in tested}
        for asset in release_assets
        for model in ("dense", "moe")
    ]
```

### Developer Challenges

1. Build a benchmark manifest that pins model, tokenizer, dataset, cache policy, runtime commit, hardware, kernels, seeds, and measurement window for every comparison.
2. Demonstrate that a combined KDFlow/CompressKV/runtime stack improves a Pareto frontier rather than one metric, including recovery behavior after an intentionally bad cache decision.
3. Make the planner refuse unsupported hardware/model combinations and emit a source-linked evidence gap instead of guessing compatibility.

### Author Challenges

1. Extend the survey into a versioned systematic evidence map with reproducible inclusion/exclusion rules, update deltas, and claim-level links to primary benchmarks.
2. Add a cross-layer evaluation protocol that measures architecture, algorithm, and system optimizations jointly under fixed quality, cost, and energy budgets.
3. Treat recovery, privacy, and provenance as first-class resource-efficiency dimensions, then test whether the original physical-resource taxonomy still explains deployment decisions.

## Validation Notes

- Random selection was real and reproducible as a method: 75,777 PDFs, 75,776 unique paper units, uniform zero-based index 52,398, excluded count 0, reselections 0.
- Deduplication covered repository logs, reports, deposits, public pointer index, automation memory, and live related-repository context by arXiv ID, DOI, normalized title, and slug; no prior same-paper artifact or 24-hour marker was found.
- Source integrity was repaired before review. The preserved 2,100,133-byte PDF begins with `%PDF-` and contains trailing `%%EOF`. The 966,294-byte full-paper HTML contains 305,921 body characters, 130 heading/section markers, seven paper-structure terms, and an accepted document marker. No partial remained.
- Exactly three related DEP entries were inspected and are listed above. The Report-Mark has exactly three potential implementations, three deeper observations, three similarities, three MVP code mock-ups, three developer challenges, and three author challenges.
- Original PDF, HTML, metadata, source package, caches, extracted text, and private paths were excluded from repository output. Public artifacts use repository-relative paths and canonical URLs only.
- The three Python mock-ups are illustrative, synthetic, bounded, and designated for syntax validation before commit. No paper experiment, runtime build, model, or benchmark was executed.
- Public-output sanitization and staged allowlist validation are required before submission; any path, username, timezone, precise-run-time, source-file, or non-Markdown leak is a stop condition.

## Attribution Block

- Source URL: https://arxiv.org/abs/2401.08092
  - Applies to: source identity, complete authorship, dates, subjects, DOI, and source availability.
- Source URL: https://arxiv.org/html/2401.08092
  - Applies to: the survey scope, taxonomy, mechanism descriptions, examples, limitations, and future directions.
- Source URL: https://arxiv.org/pdf/2401.08092
  - Applies to: the 65-page rendered paper, organization figure, tables/figures, and PDF/full-text cross-check; local copy withheld.
- Source URL: https://doi.org/10.48550/arXiv.2401.08092
  - Applies to: persistent paper identity.
- Source URL: https://github.com/UbiquitousLearning/Efficient_Foundation_Model_Survey
  - Applies to: official companion paper/figure list, stated scope, and maintenance context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: public repository layout, source-withholding policy, naming, attribution, log, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E container path and publication-index requirement.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related-repository authority and dedup context.
- Repository path: `.staging/arxiv-dep-dedup-index.json`
  - Applies to: prior-paper eligibility and public dedup validation.
- Repository path: `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/README.md`
  - Applies to: KDFlow DEP identity, contents, source boundaries, and primary-source attribution.
- Repository path: `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md`
  - Applies to: related-entry method, evidence, reported results, limitations, and synthesis basis; primary sources include https://arxiv.org/abs/2603.01875 and https://github.com/songmzhang/KDFlow.
- Repository path: `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/README.md`
  - Applies to: CompressKV DEP identity, lineage qualification, contents, and primary-source attribution.
- Repository path: `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/2606.24467-whitepaper-review.md`
  - Applies to: related-entry semantic cache controller, evidence, limitations, and recovery synthesis; primary sources include https://arxiv.org/abs/2606.24467 and https://github.com/TUDa-HWAI/CompressKV.
- Repository path: `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/README.md`
  - Applies to: llama.cpp Runtime DEP identity, contents, and primary-source attribution.
- Repository path: `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md`
  - Applies to: related-entry runtime packaging, quantization correction, and validation boundary; primary sources include https://github.com/ggml-org/llama.cpp/releases/tag/b9789 and https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b.
