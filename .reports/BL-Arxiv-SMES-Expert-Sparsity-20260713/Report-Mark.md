# Report-Mark: SMES Expert Sparsity

## Source Metadata

| Field | Value |
|---|---|
| Work | SMES: Towards Scalable Multi-Task Recommendation via Expert Sparsity |
| Authors | Yukun Zhang, Si Dong, Xu Wang, Bo Chen, Qinglin Jia, Shengzhe Wang, Jinlong Jiao, Runhan Li, Jiaqing Liu, Chaoyi Ma, Ruiming Tang, Guorui Zhou, Han Li, Kun Gai |
| Organization | Kuaishou Technology Co., Ltd. |
| Platform | arXiv, Computer Science — Information Retrieval |
| Identifier | arXiv:2602.09386v1 |
| DOI | 10.48550/arXiv.2602.09386 (arXiv-issued DOI) |
| Submitted | 2026-02-10 |
| Primary URL | https://arxiv.org/abs/2602.09386 |
| Full-text URLs | https://arxiv.org/pdf/2602.09386 ; https://arxiv.org/html/2602.09386 |
| Evidence access date | 2026-07-13 |
| Source status | Private archive PDF inspected; public arXiv metadata inspected; no source file redistributed |
| License/usage note | A license link is exposed by arXiv, while the PDF carries ACM-style permission language and placeholder publication fields; redistribution permission was not assumed. |

## Concise Research Notes

SMES targets a systems problem in industrial multi-task recommendation: scaling every task with the same dense expert capacity raises serving cost and can degrade sparse-label tasks. The paper argues that independent per-task top-k routing is also insufficient because the union of selected experts can approach dense execution and cross-task traffic can overload a small expert subset.

The proposed progressive expert routing first selects a task-shared expert set using pooled router probabilities, then gives each task a bounded private set chosen outside the shared set. Deduplicated execution evaluates each unique expert at most once per instance. A multi-task load-balancing regularizer operates on traffic and probability mass aggregated across tasks. Deployment support includes a reindexed grouped-GEMM path for ragged expert traffic and a profiling-guided GPU workspace allocator.

The authors evaluate KuaiRand-1K and a proprietary Kuaishou dataset. Table 2 reports that SMES-S exceeds listed baselines across the shown tasks at a similar parameter budget, while SMES-L scales to 510M public-dataset parameters and 633M industrial-dataset parameters at 8% expert sparsity. Figure 3 reports a 0.84% average GAUC improvement at 0.6B parameters with a 4 ms latency increase. A production A/B test on 3.5% traffic from 2025-10-25 through 2025-10-31 reports +0.31% user watch time, +0.64% Like, +1.56% Follow, +2.45% Comment, and 50% lower latency than a comparable-capacity dense MoE baseline. These remain author-reported results.

Evidence strength is mixed. The method, equations, table values, and experiment descriptions are directly inspectable in the PDF. Independent validation is limited by absent code, proprietary data and serving infrastructure, missing variance and detailed significance procedures, an unreported configuration manifest, and placeholder conference metadata.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limitations |
|---|---|---|---|---|
| E1 | arXiv abstract and metadata | Identity, authorship, date, abstract claims, arXiv DOI | High | Abstract alone cannot validate experiments. |
| E2 | Full PDF sections 1–3 and Figures 1–2 | Problem formulation, routing mechanism, load regularizer, execution design | High for source reporting | Equations and implementation were not independently executed. |
| E3 | Full PDF section 4, Tables 1–3, Figures 3–5 | Dataset scale, baselines, offline results, ablations, sensitivity, activation analysis | High for transcription; low for reproduction | Industrial data and detailed configuration are unavailable. |
| E4 | Full PDF section 4.7 and conclusion | Online A/B scope and reported production metrics | Medium-high for source reporting | No confidence intervals, raw telemetry, or independent audit. |
| E5 | Private public-safe extraction summary | PDF identity, successful `pypdf` extraction, absent local HTML/source package | High | Private locations intentionally withheld. |
| E6 | Three inspected DEP entries and their stated primary bases | Routing, sparse-runtime, and systems-overlap synthesis | Medium | Related entries provide context, not validation of SMES. |
| E7 | Live Black Lake and Black-Lake-Data READMEs | Packaging, naming, attribution, and stability rules | High | Process evidence only. |

## Related DEP Entries

1. [Black-Lake-Data DEP-20260703-Tech Intel 0103](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260703-Tech%20Intel%200103) — Finding 7 summarizes ELDR, which uses predicted expert locality to route disaggregated MoE decode requests and reports lower time per output token than load-balancing baselines. It overlaps with SMES through expert-aware routing, load distribution, and the requirement that sparse activation translate into real serving gains. Source basis: the DEP finding and arXiv:2607.00466.
2. `.lake-data/DEP-E-20260712-KDFlow LLM Distill` — KDFlow identifies forward-only MoE teacher inference as a throughput bottleneck when forced through a training-oriented backend. It overlaps with SMES through conditional computation, workload-specific execution, communication/memory tradeoffs, and the need to test sparse-model efficiency at system level. Source basis: the processed manuscript and arXiv:2603.01875.
3. `.lake-data/DEP-E-20260712-LlamaCpp-Runtime` — This entry inspects a llama.cpp release whose linked change corrects layer counting for MoE-with-MTP quantization. It overlaps with SMES by showing that sparse-expert topology must remain correct through quantization and runtime packaging; model-level sparsity claims are insufficient without configuration-specific regression tests. Source basis: the processed runtime report, official release b9789, and commit `b3ce5ce`.

## Synthesis Note

### Concept Bridge

SMES, ELDR, KDFlow, and the llama.cpp runtime record occupy different layers of one conditional-computation stack. SMES decides which experts should execute for multiple recommendation objectives; ELDR places requests where likely experts are local; KDFlow assigns sparse inference to an inference-specialized runtime; and the llama.cpp record preserves expert topology through quantization/runtime changes. Together they suggest that sparse capacity is valuable only when routing semantics, placement, kernels, memory, and validation remain aligned.

### Potential Implementations

1. **Multi-task routing audit harness:** replay synthetic task/router scores, measure unique-expert union size, expert load skew, and task coverage, then compare naive independent top-k with progressive shared/private routing.
2. **Sparse serving capacity planner:** combine predicted expert activation, locality, kernel cost, workspace demand, and latency budgets to produce a Pareto frontier before deployment.
3. **Recommendation release evidence gate:** join offline GAUC/AUC, per-task calibration, routing balance, latency, memory, and bounded online experiment results into a human-reviewed release record.

### Deeper Relationship Observations

1. Model sparsity is a cross-layer contract: a bounded routing union can still lose its advantage if runtime kernels, memory allocation, or placement convert irregular work into overhead.
2. Load balancing and locality are complementary rather than interchangeable: globally balanced experts can still be remote, while locality-only routing can create hotspots or distort task coverage.
3. Heterogeneous tasks and heterogeneous system roles share the same design principle: allocate capacity according to demand, then measure the boundary costs introduced by specialization.

### Conceptual Similarities

1. SMES and ELDR both treat expert activation history or probabilities as operational signals, not merely internal model details.
2. SMES and KDFlow both separate total parameter capacity from the computation that should be active for a specific workload.
3. SMES and the llama.cpp runtime entry both require topology-aware correctness checks because generic dense-model assumptions can miscount or misexecute expert structures.

### MVP Implementations With Code Mock-Ups

1. **Routing Union Explorer** — compare naive and progressive routing on synthetic scores.

   ```python
   def union_size(task_routes):
       return len(set().union(*map(set, task_routes)))

   before = union_size([[0, 3], [2, 5], [1, 4]])
   after = union_size([[0, 3], [0, 5], [0, 4]])
   assert after <= before
   ```

2. **Expert Load Monitor** — flag cross-task expert skew without storing user features.

   ```python
   from collections import Counter

   def load_ratio(expert_ids):
       loads = Counter(expert_ids).values()
       return max(loads) / max(1, sum(loads) / len(loads))

   alert = load_ratio([0, 0, 0, 1, 2, 3]) > 2.0
   ```

3. **Pareto Release Gate** — require quality gain without a latency-budget breach.

   ```python
   def release_ok(gauc_gain_pct, latency_delta_ms, max_delta_ms=5.0):
       return gauc_gain_pct > 0 and latency_delta_ms <= max_delta_ms

   assert release_ok(0.84, 4.0)
   ```

### Developer Challenges

1. Implement ragged deduplicated expert execution without making gather/scatter, synchronization, or workspace contention dominate latency.
2. Keep routing balance and task coverage stable under shifting traffic, label sparsity, and changing task importance.
3. Build privacy-safe telemetry that connects per-task quality, expert utilization, kernel behavior, and end-to-end latency without retaining sensitive user features.

### Author Challenges

1. Publish a pinned implementation and complete configuration manifest that maps every table and figure to code, seeds, preprocessing, hardware, and router budgets.
2. Resolve placeholder venue/DOI fields and report the statistical procedures, uncertainty intervals, and repeated-run variation behind offline and online claims.
3. Provide a reproducible public proxy for the industrial evaluation, including controlled ablations that isolate routing, load regularization, grouped GEMM, and workspace allocation.

## Validation Notes

- Required paper identity, dates, authors, arXiv ID, DOI, problem, method, evidence, limitations, and implementation relevance were extracted from inspected evidence.
- Quantitative claims were transcribed from the abstract, Table 2, Figure 3, Table 3, and section 4.7; none are presented as independently reproduced.
- Exactly three related DEP entries are included, each with a concrete overlap reason and source basis.
- The Synthesis Note contains exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP implementations with code mock-ups, three developer challenges, and three author challenges.
- Selection used 75,761 unique PDF-parent paper units, zero-based random index 48,963, zero exclusions, and zero reselections.
- Deduplication found no ID, DOI, title, slug, or same-paper 24-hour match.
- No source file was added because redistribution permission was not assumed.
- Public-safe review found no local absolute path, home directory, username, drive path, machine name, workspace root, local timezone label, or exact local execution timestamp.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.09386
  - Applies to: paper identity, metadata, abstract claims, submission history, DOI, and public full-text links.
  - Notes: Primary arXiv record inspected on 2026-07-13.
- Source URL: https://arxiv.org/pdf/2602.09386
  - Applies to: method, equations, experiments, tables, figures, limitations, and references.
  - Notes: Public locator for the full PDF; the reviewed copy was already present in a private archive and was not redistributed.
- Source URL: https://arxiv.org/html/2602.09386
  - Applies to: public full-text availability context.
  - Notes: Public locator; direct web retrieval was unavailable during this run, so claims rely on the inspected PDF.
- Source URL: https://doi.org/10.48550/arXiv.2602.09386
  - Applies to: stable arXiv-issued DOI.
  - Notes: Identifier link exposed by the arXiv record.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260703-Tech%20Intel%200103
  - Applies to: ELDR related-entry synthesis.
  - Notes: Related DEP containing the inspected ELDR finding.
- Source URL: https://arxiv.org/abs/2607.00466
  - Applies to: ELDR primary source basis as recorded by the related DEP.
  - Notes: Used only for related-entry context.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260712-KDFlow%20LLM%20Distill
  - Applies to: KDFlow related-entry synthesis.
  - Notes: Processed Black Lake DEP inspected from the live default branch.
- Source URL: https://arxiv.org/abs/2603.01875
  - Applies to: KDFlow primary source basis as recorded by the related DEP.
  - Notes: Used only for related-entry context.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260712-LlamaCpp-Runtime
  - Applies to: llama.cpp runtime related-entry synthesis.
  - Notes: Processed Black Lake DEP inspected from the live default branch.
- Source URL: https://github.com/ggml-org/llama.cpp/releases/tag/b9789
  - Applies to: related runtime release basis.
  - Notes: Official release recorded by the related DEP.
- Source URL: https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b
  - Applies to: MoE-with-MTP quantization fix basis.
  - Notes: Official commit recorded by the related DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: artifact location, DEP class, naming, attribution, and commit rules.
  - Notes: Live default-branch README fetched before drafting.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related repository context and provenance rules.
  - Notes: Live default-branch README fetched before drafting.
