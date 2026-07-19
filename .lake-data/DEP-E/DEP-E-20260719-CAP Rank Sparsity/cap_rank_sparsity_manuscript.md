---
title: "CAP Compression - DEP-E"
generated_at: "2026-07-19"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of CAP, a two-stage low-rank and sparse LLM weight-compression method."
source_status: "verified local bundle; original source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "arXiv v3 revised 2026-02-26; public context checked through 2026-07-19"
primary_url: "https://arxiv.org/abs/2505.03801"
stable_identifier: "arXiv:2505.03801v3; DOI:10.48550/arXiv.2505.03801"
confidence_summary: "High for paper identity, mechanism, and reported table values; medium for causal and deployment interpretation because experiments were not rerun and code was not established."
safety_scope: "non-sensitive model-compression research and bounded evaluation planning"
distribution_notes: "Public Markdown only; PDF, HTML, metadata, source package, renders, caches, and verification records remain local and were not uploaded."
---

# CAP Compression - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Paper title | *Large Language Model Compression with Global Rank and Sparsity Optimization* |
| Authors | Changhai Zhou; Qian Qiao; Yuhua Zhou; Yuxin Wu; Shichao Weng; Weizhong Zhang; Cheng Jin |
| Organizations shown in the paper | Fudan University; Soul AI Lab/WP Lab; Zhejiang University; Renmin University of China |
| Source platform | arXiv, Computer Science - Machine Learning |
| Submitted | 2025-05-02 |
| Reviewed revision | arXiv v3, revised 2026-02-26 |
| Venue status | ICLR 2026 Poster |
| Stable identifiers | arXiv:2505.03801v3; DOI:10.48550/arXiv.2505.03801; OpenReview forum `ZaPmQ0NHs4` |
| Subjects | Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`) |
| Primary URLs | https://arxiv.org/abs/2505.03801; https://arxiv.org/html/2505.03801; https://arxiv.org/pdf/2505.03801; https://arxiv.org/e-print/2505.03801 |
| Venue URL | https://iclr.cc/virtual/2026/poster/10008795 |
| License visibility | arXiv non-exclusive distribution license; redistribution was not assumed or performed |
| Collected formats | Complete PDF, full-paper HTML, metadata HTML, TeX/source package, and local verification records |
| Collection status | Verified complete after bounded repair of missing full-paper HTML |
| Code/data status | The reproduction statement names implementation files, but no official public repository was established from inspected primary records and exact release searches; no code or experiment was run |
| Access date | 2026-07-19 |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | Verified complete local PDF, HTML, metadata, and TeX/source bundle for arXiv:2505.03801v3 | Primary paper bundle | Full method, equations, Tables 1-11, Figures 1-5, appendix analysis, reproducibility statement, limitations | Mechanism, experimental setup, reported results, ablations, evidence limits | High | Experiments were inspected, not reproduced; source files are withheld from the public DEP |
| E2 | https://arxiv.org/abs/2505.03801 | Official metadata | Title, authors, dates, subjects, DOI, version history, public artifact links, license | Identity and versioning | High | Abstract/metadata alone does not support empirical claims |
| E3 | https://iclr.cc/virtual/2026/poster/10008795 and https://openreview.net/forum?id=ZaPmQ0NHs4 | Official venue records | ICLR poster status, author list, forum identity | Publication context | High for ICLR listing; medium for forum details | Interactive OpenReview content was challenge-gated during inspection |
| E4 | https://qianqiaoai.github.io/ | Author-maintained page | Publication listing and absence of a displayed code link for this paper | Author context and release search | Medium | Page state can change; absence of a link is not proof that code cannot exist elsewhere |
| E5 | Exact GitHub/title/arXiv/forum searches plus source inspection | Release-availability check | No official implementation repository established | Reproducibility boundary | Medium | Search is bounded and cannot prove permanent absence |
| E6 | Three related Black Lake artifacts | Curated research records | Compression taxonomy, adaptive rank control, joint compression allocation | Cross-DEP synthesis | Medium-high | Their experiments were not rerun here; claims remain attributed to each artifact's sources |
| E7 | Live Black Lake and Black-Lake-Data READMEs | Repository authority | DEP layout, naming, attribution, source locality, and dedup scope | Deposit procedure | High | Repository rules, not research evidence |
| E8 | Local source-integrity receipt | Verification record | PDF/HTML structure, sizes, hashes, source inventory, zero partials | Complete-source gate | High | Public artifact preserves metrics but not private paths or source bytes |

## Executive Summary

CAP compresses LLM weight matrices through two coordinated stages. First, robust principal component analysis (RPCA) decomposes each weight matrix into a low-rank component that represents global structure and a sparse component that represents localized residual structure. Second, Bernoulli retention variables over singular directions and sparse entries are optimized by a REINFORCE-style policy gradient on a small calibration set, after which a deterministic global selection produces a budget-constrained low-rank-plus-sparse representation.

The paper's evidence supports a useful, bounded claim: within the reported models and evaluation setup, global allocation over the two component types usually preserves more task performance than uniform or layerwise pruning baselines at matched nominal compression. At 50% sparsity on LLaMA-3.1-8B-Instruct, Table 2 reports CAP at 56.8% GSM8K, 27.2% LongBench-v2, and 6.61 WikiText perplexity, versus Wanda at 45.6%, 25.1%, and 7.26. The dense model remains substantially better at 84.5%, 30.4%, and 6.01. Appendix Table 11 reports 176.5 tokens/s, 5.80 seconds latency, and 14.90 GB peak memory for CAP versus 163.4 tokens/s, 6.28 seconds, and 15.18 GB for Wanda on one A100-80G, batch-one, sequence-length-1,024 configuration.

Confidence is high that the paper reports these mechanisms and numbers: complete PDF, official HTML, TeX source, tables, figures, appendices, and venue records were inspected. Confidence is lower for independent reproducibility, causal attribution, and deployment portability. No experiment was rerun, no public official implementation was established, statistical uncertainty is not foregrounded, sparse acceleration depends on hardware/kernel support, and the final cross-type budget selection is insufficiently specified for a complete cost audit.

## Detailed Summary

### Problem and Motivation

Uniform low-rank truncation assumes similar spectral redundancy across layers, while unstructured sparsity assumes important residual structure can be retained without a coordinated rank budget. The paper argues that LLM layers and modules differ: some need more singular directions, while others can place more capacity in a sparse residual. Manually choosing both a rank and a sparsity ratio for every matrix creates a combinatorial allocation problem.

CAP reframes that problem as structured candidate generation followed by global budget allocation. The first stage reduces the candidate space; the second stage decides which candidates deserve the limited capacity.

### Stage 1 - RPCA Candidate Spaces

For a weight matrix `W`, CAP solves the convex decomposition objective

`min ||L||_* + lambda ||S||_1 subject to W = L + S`,

where the nuclear norm encourages low rank and the L1 norm encourages a sparse residual. The source describes ADMM updates: singular-value thresholding updates `L`, elementwise soft thresholding updates `S`, and a dual variable enforces reconstruction. The default `lambda` is `1 / sqrt(max(m,n))`.

This stage does not enforce the final compression budget. Its purpose is to build low-rank and sparse candidate pools with a principled decomposition objective. The paper correctly limits the global-optimum language to this convex stage; it explicitly states that the second stage is heuristic and non-convex.

### Stage 2 - Probabilistic Global Allocation

Each retained singular direction costs the two factor vectors associated with that direction, while each retained sparse entry costs one stored value plus implementation metadata. CAP assigns Bernoulli retention variables to singular directions and sparse entries, learns their probabilities with a REINFORCE-style estimator, uses a moving-average loss baseline for variance reduction, and projects probabilities toward a parameter budget. The final representation selects high-scoring candidates and factorizes the retained low-rank component into smaller matrices.

The conceptual strength is global coordination: every layer and both representation types compete for one budget. The important ambiguity is cost normalization. The method text recognizes that a singular direction costs `m+n` parameters, yet the projection and final top-budget selection are described in a way that does not fully expose how differently priced candidates become comparable. A reproducible implementation should publish cost-weighted scoring, tie-breaking, exact constraint enforcement, and achieved storage including indices and metadata.

### Experimental Design

The evaluation spans LLaMA-1/2/3, LLaMA-3.1-8B-Instruct, Qwen2.5-7B, OPT, Phi-3, and BERT-base. It uses zero-shot commonsense tasks, WikiText perplexity, GSM8K, LongBench-v2, GLUE, calibration-domain comparisons, low-rank baselines, joint compression baselines, and appendix analyses. The implementation description names PyTorch 2.3.0, Transformers 4.28.0, CUDA 12.1, NVIDIA A100 GPUs, 128 C4 calibration sequences, three policy-gradient iterations, a sliding-window size of five, and learning rate 0.05.

No confidence intervals, repeated-run summaries, or independent artifact execution were established in this review. The paper's results should therefore be treated as source-reported point estimates.

### Main Results

At 50% compression in Table 1, CAP reports higher zero-shot accuracy and lower WikiText perplexity than the displayed pruning baselines across Phi-3 Mini/Medium and LLaMA-3 8B/70B. For Phi-3 Mini, CAP reports 69.12% average accuracy and 14.68 perplexity; OATS reports 68.41% and 15.18, while Wanda reports 65.03% and 17.23. All compressed methods remain below the dense model's 72.85% and 9.42.

For LLaMA-3.1-8B-Instruct at 50% sparsity, CAP improves over Wanda by 11.2 percentage points on GSM8K, 2.1 points on LongBench-v2, and 0.65 lower perplexity. The dense-to-CAP gap remains 27.7 points on GSM8K, showing that CAP is a relative recovery result rather than near-lossless reasoning compression.

Table 6 and Appendix Table 11 report a systems benefit on one hardware setup. CAP's highly sparse residual plus low-rank path reaches 176.5 tok/s versus 163.4 tok/s for Wanda, with 14.90 GB versus 15.18 GB peak memory. The paper attributes the gain to the sparse residual reaching roughly 75%-90% sparsity, where sparse matrix multiplication is more favorable than a uniform 50%-sparse matrix.

### Ablations and Boundary Evidence

Figure 2 shows that one RPCA iteration is inadequate: perplexity is reported as 32,497. Three iterations reduce it to 5.18, with 10 and 100 iterations at 5.13 and 5.16. This supports rapid stabilization after more than one iteration, not cost-free decomposition. The threshold-only ablation reports catastrophic or undefined outcomes for many low-rank/sparse threshold combinations, supporting the need for joint allocation rather than independent hard thresholds.

Appendix lambda sweeps show that extreme values collapse the intended decomposition: very low lambda yields an almost dense sparse component, while very high lambda makes the low-rank component nearly full rank. Appendix rank profiles vary by module and layer, and sequential pruning shows generally increasing perplexity rather than a universal free redundancy reserve.

### Stated and Reviewer-Identified Limitations

The paper states that practical acceleration depends on specialized sparse-computation hardware and frameworks. Reviewer-identified limits add that code availability was not established, point estimates lack visible uncertainty, the cost boundary omits detailed offline decomposition/allocation time, kernel comparisons use one main hardware regime, calibration stability is tested narrowly, and candidate-cost normalization is not sufficiently explicit for an exact reconstruction.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | CAP decomposes weights into low-rank and sparse candidate spaces, then globally allocates retention under a budget. | Author mechanism claim | E1 | Directly supported by method equations and algorithm description. | High |
| C2 | The RPCA stage is globally optimal for its convex decomposition objective. | Author theoretical claim | E1 | Supported only for the stated convex objective and solver conditions, not for final compression quality. | Medium-high |
| C3 | CAP outperforms displayed pruning baselines at matched nominal compression across the tested model suite. | Author empirical claim | E1 | Supported as paper-reported table evidence; not independently reproduced. | Medium-high |
| C4 | CAP recovers 11.2 GSM8K points over Wanda at 50% sparsity on LLaMA-3.1-8B-Instruct. | Author quantitative claim | E1 | Table 2 visually verified; dense model remains 27.7 points above CAP. | High for reported value |
| C5 | CAP improves throughput because the residual enters a kernel-efficient high-sparsity regime. | Author systems explanation | E1 | Plausible and supported by one A100-80G comparison; portability is unestablished. | Medium |
| C6 | The second-stage allocation is globally optimal. | Not claimed by authors | E1 | The paper explicitly calls policy-gradient allocation heuristic and without a global optimum guarantee. | High |
| C7 | The final cross-type selection is fully reproducible from the paper alone. | Reviewer assessment | E1, E5 | Not established; cost-weighted projection and top-budget semantics need more detail and code. | Medium-high |
| C8 | The source gate and dedup process support a complete, non-duplicate DEP review. | Process claim | E7, E8 | Verified complete after repair; exact repository and companion checks found no prior deposit. | High |

## Methodology

- `Research objective`: Randomly select one unused local arXiv paper, enforce a complete-source integrity gate, review it source-first, connect it to exactly three concrete DEP entries, and preserve a public-safe DEP-E manuscript.
- `Sources inspected`: Complete PDF, official full-paper HTML, metadata HTML, TeX/source package, equations, tables, figures, appendices, limitations, local verification records, arXiv metadata, official ICLR listing, OpenReview forum locator, author publication page, live repository READMEs, and the substantive artifact for each related DEP.
- `Discovery strategy`: `rg --files -g "*.pdf"` enumerated local PDFs; PDF-parent directories were unique paper units; PowerShell `Get-Random` selected a uniform raw-unit index; repository and memory scans then applied rejection-based deduplication. Public primary-source searches checked venue and release status.
- `Inclusion criteria`: Evidence had to identify the paper/version, expose full methods/results/limitations, validate source completeness, govern repository deposition, or provide concrete overlap in compression taxonomy, adaptive rank allocation, or joint resource allocation.
- `Exclusion criteria`: Abstract-only evidence, incomplete source documents, duplicate research deposits, tangential DEP entries, unverified code releases, private path disclosure, and original source redistribution were excluded.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, systems, product research, replication, and provenance review.
- `Evidence handling`: Major claims map to evidence IDs. Author claims, table values, reviewer interpretation, and product proposals remain labeled separately. Quantitative results retain model, budget, task, and hardware context.
- `Uncertainty handling`: Non-reproduction, missing code, missing repeated-run statistics, ambiguous cost normalization, and hardware/calibration portability remain explicit.
- `Extraction process`: Searchable full HTML and TeX source reconstructed equations and tables; PDF text and six rendered experiment/ablation pages cross-checked values and layout.
- `Version control`: Paper pinned to arXiv:2505.03801v3; venue status checked against the ICLR 2026 listing and OpenReview forum identity.
- `Random selection`: 75,778 PDFs collapsed to 75,776 parent-directory units. A uniform zero-based raw-unit draw selected index 18,321; no rejection was required.
- `Deduplication`: 969 arXiv IDs were observed across Black Lake artifacts, automation memory, and relevant Black-Lake-Data records. Corpus-level ID exclusion counted 213 units; 185 identifier-incomplete units were withheld; exact selected-paper ID, DOI, title, slug, and recent-marker searches returned no prior research deposit.
- `24-hour validation`: No same-paper marker was found on or after the public-safe cutoff date 2026-07-18.
- `Source repair`: Initial state was partial because full-paper HTML was absent. The valid PDF was preserved; bounded official-arXiv repair collected full-paper HTML, metadata HTML, and source. Final state was complete with zero partials.
- `Reviewer stance`: Schema-complete skeptical paper review, DEP-ready preservation, and bounded translation to cost-aware evaluation tooling.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv v3 identity, CAP mechanism, main and appendix experiments, limitations, runtime evidence, release availability, and synthesis with exactly three related DEP entries.
- `Temporal boundary`: Paper revised 2026-02-26; public context and repository rules checked through 2026-07-19.
- `Evidence limits`: No model, benchmark, optimizer, sparse kernel, calibration sweep, or related-DEP experiment was executed. OpenReview interactive review content was challenge-gated.
- `Assumptions`: Canonical arXiv and ICLR records are authentic primary sources; related DEP artifacts accurately preserve their cited primary evidence subject to their own limitations.
- `Constraints`: No local absolute path, username, machine name, local timezone label, exact local execution timestamp, source document, rendered source image, cache, or extracted source text may appear in public output.
- `Out of scope`: Production recommendation, independent reproduction, energy measurement, formal verification of optimizer convergence, security audit, or redistribution-rights determination.
- `Intended use`: Research review, DEP deposition, replication planning, matched-budget benchmark design, and safe MVP ideation.
- `Audience`: Model-compression researchers, inference/runtime engineers, ML systems reviewers, and Black Lake maintainers.
- `Depth target`: Full manuscript with evidence/claim separation and systems-aware implementation translation.
- `Reproducibility boundary`: A follow-on reviewer can reconstruct the public method and evaluation plan, but cannot reproduce reported tables from this DEP without an implementation and model/hardware assets.
- `Operational boundary`: Product examples are synthetic, local/authorized, evaluation-first, and do not modify production models.
- `Data sensitivity`: Public paper metadata plus private local source artifacts; public output contains no private source location or source bytes.

## Observations

- `Observed pattern`: CAP's strongest contribution is not RPCA alone; it is the separation of candidate-space construction from global capacity allocation.
- `Observed pattern`: Dense-to-CAP gaps remain large on reasoning even when CAP strongly outperforms Wanda, so relative baseline recovery should not be presented as lossless compression.
- `Technical implication`: Kernel efficiency depends on the structure of the result, not only nominal retained parameters. A high-sparsity residual plus low-rank path can behave differently from one uniformly sparse matrix.
- `Contradiction or tension`: The method recognizes unequal candidate costs but does not fully expose how projection and final ranking normalize a singular direction against a sparse scalar.
- `Evidence-quality observation`: Broad model coverage is valuable, but point estimates without repeated-run uncertainty limit inference about small margins and optimizer variance.
- `Open question`: Does a rank/sparse allocation learned on 128 C4 sequences remain stable under domain shift, model fine-tuning, or new instruction-tuning recipes?
- `Reviewer hypothesis`: Cost-aware selection with explicit bytes, index overhead, and kernel feasibility could preserve CAP's conceptual advantage while improving reproducibility and deployment relevance.

## Considerations

Deployment should separate four receipts: offline decomposition cost, allocation/calibration cost, realized representation size, and online runtime outcome. CAP's paper evidence emphasizes the latter two but does not provide a complete amortization model. A model updated by fine-tuning may invalidate singular spectra, sparse residual structure, and learned masks; profiles therefore need version pins and invalidation rules.

Matched nominal compression is not necessarily matched physical cost. Low-rank factors store two dense vectors per retained direction. Sparse values require indices and formats. Fused or specialized kernels impose layout and hardware constraints. A fair benchmark must record bytes, metadata, precision, factor shapes, compilation, warmup, synchronization, and fallback behavior.

Calibration data creates a governance boundary. Although the paper uses public C4 samples, a product adaptation may use sensitive prompts. A safe system should retain only aggregated metrics, avoid logging raw prompts, and keep calibration separated by tenant and model revision.

## Strengths

- Converts a large per-weight search into structured low-rank and sparse candidate pools.
- Coordinates layer and component allocation under one global resource objective.
- Explicitly distinguishes convex RPCA guarantees from heuristic non-convex policy-gradient allocation.
- Evaluates multiple model families and both language-modeling and downstream tasks.
- Includes reasoning, long-context, GLUE, low-rank, joint-compression, calibration, throughput, memory, and appendix analyses.
- Visually and numerically exposes threshold-only failure cases that motivate global allocation.
- Reports an end-to-end throughput comparison rather than only parameter counts.
- Supplies a reproduction statement and source-level implementation outline, even though a public repository was not established.

## Weaknesses

- No official public implementation was established, so the named reproduction steps could not be executed.
- Experimental point estimates are not accompanied by visible confidence intervals or repeated-seed summaries.
- The global cross-type cost and projection semantics are underspecified relative to the stated `m+n` cost of a singular direction.
- Offline RPCA and policy-search wall time, energy, and amortization are not fully integrated into the systems comparison.
- Main throughput evidence is narrow in hardware, batch, sequence length, and baseline implementation.
- Sparse speedups depend on specialized kernels and may not transfer to unsupported runtimes.
- Calibration robustness covers only a limited set of corpora and does not establish mask stability after model updates.
- The stated limitation section is brief and does not foreground code availability, statistical uncertainty, or operational invalidation.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish versioned code and exact commands | Reproducibility | The paper names files but no official repository was established. | Independent table and kernel replication. | Maintenance and asset licensing. | Rebuild the environment from a clean runner and reproduce three named tables. |
| Define cost-weighted candidate projection | Optimization | Singular directions and sparse entries have unequal physical costs. | Auditable budget enforcement and fair ranking. | May change learned allocations. | Compare nominal parameters, actual bytes, and task quality under exact budgets. |
| Report seeds and intervals | Statistics | Policy-gradient and calibration sampling introduce variance. | Distinguishes robust margins from noise. | Added compute. | Use paired seeds and publish task-level intervals. |
| Add end-to-end amortization | Systems | Offline RPCA/search may dominate infrequent deployments. | Honest total-cost decision. | Requires workload assumptions. | Report break-even request counts across model sizes. |
| Expand hardware/kernel matrix | Portability | Sparse and low-rank speedups are runtime-specific. | Clear deployment envelope. | Engineering burden. | Benchmark dense, generic sparse, and fused paths across GPUs and CPUs. |
| Add profile invalidation tests | Operations | Fine-tuning or domain shift can change redundancy. | Safer model lifecycle management. | Ongoing shadow evaluation. | Perturb model revision/calibration mix and trigger fallback when drift thresholds fail. |

## Potential Implementations

### Cost-Aware Rank and Sparse Allocator

- `User`: Compression researchers.
- `Goal`: Reconstruct CAP-style allocation while explicitly charging bytes and index overhead.
- `Core mechanism`: Generate RPCA candidates, estimate marginal validation loss, divide utility by realized storage/runtime cost, and solve an exact budgeted selection problem.
- `Required inputs`: Pinned model weights, public or authorized calibration data, candidate costs, runtime formats.
- `Outputs`: Versioned masks, achieved bytes, factor ranks, sparse layouts, and validation deltas.
- `Risk controls`: No raw calibration logging; exact model/version pin; conservative dense fallback.
- `Evaluation`: Matched-byte accuracy/perplexity plus offline and online latency.

### Compression Frontier Harness

- `User`: ML systems and infrastructure teams.
- `Goal`: Compare dense, Wanda-style sparsity, CAP-style composition, and adaptive-rank alternatives under one evidence contract.
- `Core mechanism`: Sweep budgets and record quality, actual bytes, peak memory, prefill/decode throughput, compilation, and fallback.
- `Required inputs`: Public benchmark subset, model revisions, implementation containers, hardware profile.
- `Outputs`: Pareto frontier, failure ledger, and reproducibility manifest.
- `Risk controls`: Sandboxed execution, budget ceilings, artifact hashes, and no production traffic.
- `Evaluation`: Repeatability across seeds and hardware with confidence intervals.

### Profile Drift Monitor

- `User`: Operators of compressed model services.
- `Goal`: Detect when a stored rank/sparsity profile is no longer safe after a model or workload change.
- `Core mechanism`: Shadow a small sample on a conservative reference path and compare loss, task quality, and runtime metrics.
- `Required inputs`: Versioned profile, model hash, authorized evaluation prompts, fallback policy.
- `Outputs`: Drift score, pass/fail decision, and invalidation record.
- `Risk controls`: Secret-safe telemetry, sampling limits, tenant isolation, and immediate fallback.
- `Evaluation`: Inject controlled model/calibration shifts and measure detection/false-alarm rates.

## Three Ways to Exercise This Research

1. `Synthetic matrix study`: Objective - verify RPCA candidate behavior and cost accounting; inputs - small synthetic low-rank-plus-sparse matrices; method - vary rank, sparsity, corruption, and budget while comparing threshold-only and cost-weighted selection; output - reconstruction and budget ledger; success criterion - exact budget adherence with expected decomposition trends; stop condition - decomposition or solver instability exceeds a declared bound.
2. `Small-model matched-budget benchmark`: Objective - test whether global allocation beats uniform pruning at equal realized bytes; inputs - one openly licensed small transformer and public calibration/evaluation text; method - run dense, uniform sparse, low-rank-only, and composite configurations over three seeds; output - confidence-bounded quality/latency frontier; success criterion - repeatable composite benefit at equal bytes; stop condition - source/license, compute, or statistical gate fails.
3. `Kernel portability probe`: Objective - separate representation savings from runtime realization; inputs - frozen synthetic factor/sparse shapes and two supported runtimes; method - benchmark generic and optimized kernels with warmup and synchronization; output - shape-by-hardware throughput map; success criterion - identify the sparsity/rank region where composition wins; stop condition - unsupported kernels, memory ceiling, or unstable measurements.

## Example MVP Product

- `Product name`: CAP Budget Auditor.
- `Target user`: Model-compression and inference engineers reviewing a candidate compressed model before deployment.
- `Problem`: Nominal parameter ratios hide unequal candidate costs, sparse metadata, calibration variance, and runtime incompatibility.
- `Core workflow`: Import a versioned candidate manifest; verify model/calibration identity; calculate factor, sparse-value, index, and metadata bytes; run a bounded public evaluation; benchmark supported kernels; compare against dense and simple baselines; emit a signed pass/fail report.
- `Data requirements`: Model and profile hashes, public or authorized evaluation prompts, candidate ranks/masks, sparse layout, precision, hardware/runtime metadata, and outcome metrics. Raw sensitive prompts are not retained.
- `Architecture`: Local CLI plus sandboxed workers, immutable manifest store, metric collector, Pareto analyzer, and HTML/Markdown report renderer. No production model mutation occurs.
- `Success metrics`: Exact byte-accounting error below 1%; reproducible results across three runs; all baselines matched on model and workload; no secret leakage; explicit fallback for unsupported kernels.
- `Risk controls`: Local/authorized execution, allowlisted assets, disk/compute ceilings, secret-safe logs, model-version pinning, sandboxing, and conservative rejection when evidence is incomplete.
- `Limitations`: Does not prove generalization beyond evaluated prompts/hardware, does not implement CAP without released code, and cannot certify production safety from offline benchmarks alone.
- `MVP boundary`: One small model, one task suite, two compression baselines, and one hardware target.
- `Deployment model`: Local CLI and batch report; no hosted inference service.
- `Evaluation plan`: Unit tests for byte accounting, synthetic allocation tests, three seeded benchmark runs, and one unsupported-kernel fallback test.
- `Failure modes`: Incorrect sparse-index accounting, stale model/profile hashes, benchmark leakage, noisy runtime measurements, or accidental comparison of unequal budgets.
- `Maintenance plan`: Version schemas, benchmark snapshots, runtime dependencies, and accepted hardware profiles.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| A Survey of Resource-efficient LLM and Multimodal Foundation Models | Related DEP and survey | Places pruning and low-rank decomposition within architecture, algorithm, and systems layers. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Efficient%20FM%20Survey/efficient_fm_survey_manuscript.md; https://arxiv.org/abs/2401.08092 |
| STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control | Related DEP and method neighbor | Learns fine-grained ranks and connects adaptive low-rank storage to custom-kernel throughput. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-STAR-KV%20Ranks/2606.08382-whitepaper-review.md; https://arxiv.org/abs/2606.08382v1 |
| Towards Joint Quantization and Token Pruning of Vision-Language Models | Related DEP and joint-allocation neighbor | Coordinates two compression mechanisms under sensitivity and budget constraints. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-QUOTA%20Joint%20Compression/2604.17320-whitepaper-review.md; https://arxiv.org/abs/2604.17320v1 |
| A Simple and Effective Pruning Approach for Large Language Models (Wanda) | Primary baseline | Activation-aware unstructured pruning baseline used throughout CAP comparisons. | https://arxiv.org/abs/2306.11695 |
| SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot | Primary baseline | Second-order one-shot sparsity baseline. | https://proceedings.mlr.press/v202/frantar23a.html |
| LoSparse: Structured Compression of Large Language Models Based on Low-Rank and Sparse Approximation | Primary method neighbor | Earlier low-rank plus sparse compression with structured/fine-tuned design. | https://proceedings.mlr.press/v202/li23ap.html |
| Robust Principal Component Analysis? | Primary mathematical foundation | Establishes the low-rank-plus-sparse decomposition family used by CAP's first stage. | https://doi.org/10.1145/1970392.1970395 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| E1 | https://arxiv.org/pdf/2505.03801; https://arxiv.org/html/2505.03801; https://arxiv.org/e-print/2505.03801 | Full paper, equations, tables, figures, appendices, limitations | 2026-07-19 | Public equivalents of verified local sources; originals withheld |
| E2 | https://arxiv.org/abs/2505.03801; https://doi.org/10.48550/arXiv.2505.03801 | Identity, dates, authors, version, subjects, DOI, license | 2026-07-19 | Metadata only for empirical-evidence purposes |
| E3 | https://iclr.cc/virtual/2026/poster/10008795; https://openreview.net/forum?id=ZaPmQ0NHs4 | ICLR 2026 poster and forum identity | 2026-07-19 | Forum interaction was challenge-gated |
| E4 | https://qianqiaoai.github.io/ | Author-maintained publication context | 2026-07-19 | No result claim imported |
| E5 | Exact public title, arXiv-ID, forum-ID, and GitHub release searches | Code/release availability boundary | 2026-07-19 | No official implementation established; bounded search only |
| E6 | The three Black Lake paths and their primary arXiv URLs listed in `## Related Research and Reading` | Cross-DEP synthesis | 2026-07-19 | Exactly three related entries; claims remain attributed |
| E7 | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md; https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Layout, source policy, index, dedup context | 2026-07-19 | Live repository authority |
| E8 | Public integrity metrics in this manuscript's appendix | Complete-source gate | 2026-07-19 | Private paths, hashes, and source bytes remain local except public-safe size/status metrics |

## Appendix

### Selection and Dedup Receipt

| Field | Result |
|---|---|
| Enumeration | `rg --files -g "*.pdf"` |
| PDF candidates | 75,778 |
| Unique PDF-parent units | 75,776 |
| Used arXiv IDs observed | 969 |
| Units excluded by used ID | 213 |
| Identifier-incomplete units withheld | 185 |
| Eligible units | 75,378 |
| Random draw | Uniform zero-based raw-unit index 18,321 |
| Reselections | 0 |
| Exact selected-paper matches | 0 across Black Lake, automation memory, relevant Black-Lake-Data records, and recent markers |

### Source-Integrity Receipt

| Check | Result |
|---|---|
| Initial classification | Partial; valid PDF present, full-paper HTML absent |
| PDF | 1,957,758 bytes; `%PDF-`; trailing `%%EOF`; preserved unchanged |
| Full-paper HTML | 507,233 bytes; 112,922 body characters; document marker; 219 heading/section markers; eight structure terms |
| Metadata HTML | 44,536 bytes; metadata only |
| Source package | 1,397,382 bytes; 26 readable entries |
| Partial files after repair | 0 |
| Final classification | Complete |
| Public-source policy | All source documents, renders, caches, and verification records withheld locally; no `.source/` directory |

### Key Quantitative Receipt

| Setting | Dense | Wanda | CAP | Reviewer note |
|---|---:|---:|---:|---|
| LLaMA-3.1-8B-Instruct GSM8K, 50% sparsity | 84.5% | 45.6% | 56.8% | CAP recovers 11.2 points over Wanda but remains 27.7 points below dense |
| LongBench-v2 average, 50% sparsity | 30.4% | 25.1% | 27.2% | Bounded improvement, not dense equivalence |
| WikiText perplexity, 50% sparsity | 6.01 | 7.26 | 6.61 | Lower is better |
| A100-80G throughput | Not reported in the comparison | 163.4 tok/s | 176.5 tok/s | Batch one, sequence length 1,024; source-reported |

### Replication Checklist

- Pin model revisions, tokenizer, calibration corpus, framework versions, CUDA, kernels, and hardware.
- Publish exact RPCA stopping conditions, candidate costs, budget projection, probability initialization, top-budget selection, and tie-breaking.
- Compare nominal parameters with actual factor, sparse value, index, metadata, and precision bytes.
- Run at least three seeds and report task-level intervals.
- Separate offline decomposition/allocation cost from online inference.
- Include dense, uniform sparse, low-rank-only, threshold-only, and cost-matched composite baselines.
- Retain a conservative fallback when hardware or drift gates fail.
