# Report-Mark: CAP Rank Sparsity

## Source Metadata

- `Title`: *Large Language Model Compression with Global Rank and Sparsity Optimization*.
- `Authors`: Changhai Zhou; Qian Qiao; Yuhua Zhou; Yuxin Wu; Shichao Weng; Weizhong Zhang; Cheng Jin.
- `Organizations`: Fudan University; Soul AI Lab/WP Lab; Zhejiang University; Renmin University of China.
- `arXiv`: `2505.03801v3`; submitted 2025-05-02; revised 2026-02-26.
- `DOI`: https://doi.org/10.48550/arXiv.2505.03801.
- `Subjects`: Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`).
- `Venue`: ICLR 2026 Poster, https://iclr.cc/virtual/2026/poster/10008795.
- `OpenReview`: https://openreview.net/forum?id=ZaPmQ0NHs4.
- `Primary sources`: https://arxiv.org/abs/2505.03801, https://arxiv.org/pdf/2505.03801, https://arxiv.org/html/2505.03801, and https://arxiv.org/e-print/2505.03801.
- `License visibility`: arXiv non-exclusive distribution license; no source redistribution performed.
- `Access date`: 2026-07-19.
- `Source state`: verified complete after bounded repair; PDF, official full-paper HTML, metadata HTML, and TeX/source package are present in the private archive.
- `Public-source policy`: all source documents, renders, caches, and local verification records are withheld. Only generated Markdown and public locators are deposited.
- `Release status`: the paper's reproduction statement names `main.py`, `lib/prune_rl.py`, and `main.sh`, but no official public implementation repository was established from the inspected arXiv/ICLR/OpenReview context, author page, and exact public release searches. No code or experiment was run.

## Concise Research Notes

### Research Question

Can a large language model's weight matrices be compressed more effectively by first separating low-rank global structure from sparse local refinements and then allocating one global parameter budget across both component types and all layers?

### Method

CAP uses a two-stage design:

1. RPCA solves a convex nuclear-norm-plus-L1 decomposition `W = L + S`. ADMM, singular-value thresholding, and elementwise shrinkage produce low-rank and sparse candidate spaces. This stage constructs candidates rather than enforcing the final budget.
2. Bernoulli variables model retention of singular directions and sparse entries. A REINFORCE-style policy gradient uses calibration loss and a moving-average baseline to learn retention probabilities; a final deterministic selection produces low-rank factors plus a sparse residual.

The paper explicitly limits global-optimum language to the convex RPCA objective. It describes the policy-gradient stage as heuristic and without a global optimum guarantee.

### Experimental Setup

The evaluation covers LLaMA-1/2/3, LLaMA-3.1-8B-Instruct, Qwen2.5-7B, OPT, Phi-3, and BERT-base. It reports zero-shot commonsense accuracy, WikiText perplexity, GSM8K, LongBench-v2, GLUE, low-rank and joint-compression comparisons, calibration-corpus sensitivity, throughput, memory, and appendix ablations. The implementation description names PyTorch 2.3.0, Transformers 4.28.0, CUDA 12.1, NVIDIA A100 GPUs, 128 C4 calibration sequences, three policy-gradient iterations, a window size of five, and learning rate 0.05.

### Evidence and Results

- Table 1 reports CAP as the strongest displayed method across the four model columns at 50% compression. On Phi-3 Mini, CAP reports 69.12% average zero-shot accuracy and 14.68 WikiText perplexity; OATS reports 68.41% and 15.18; Wanda reports 65.03% and 17.23; dense reports 72.85% and 9.42.
- Table 2 reports LLaMA-3.1-8B-Instruct at 50% sparsity: CAP 56.8% GSM8K, 27.2% LongBench-v2, and 6.61 perplexity; Wanda 45.6%, 25.1%, and 7.26; dense 84.5%, 30.4%, and 6.01.
- The same table reports Qwen2.5-7B gains over Wanda on NarrativeQA, GovReport, Lcc Code, and TriviaQA, while CAP still trails the dense model on every displayed task.
- Table 5 reports CAP's low-rank-plus-sparse representation at 5.85, 6.39, and 7.06 perplexity across the three shown ratios, lower than the displayed SVD-only methods.
- Table 6 and Appendix Table 11 report 176.5 tok/s, 5.80 seconds latency, and 14.90 GB peak memory for CAP versus 163.4 tok/s, 6.28 seconds, and 15.18 GB for Wanda on one A100-80G, batch-one, sequence-length-1,024 setup.
- Figure 2 shows one RPCA iteration is insufficient: perplexity is 32,497 at one iteration, then 5.18 at three, 5.13 at ten, and 5.16 at one hundred. Threshold-only rank/sparse combinations frequently collapse or become undefined.

### Reviewer Assessment

CAP's durable contribution is the separation of candidate construction from budget allocation. RPCA supplies two structured representations; global selection allows layers and component types to compete for capacity. The reported evidence supports better quality than the displayed pruning baselines within the tested models and budgets, and one systems setup shows that the sparse residual can enter a more favorable kernel regime.

The evidence does not establish lossless reasoning compression, universal hardware speedup, independent reproducibility, or globally optimal final allocation. The dense LLaMA-3.1 model remains 27.7 GSM8K points above CAP. Point estimates lack visible repeated-run uncertainty. Offline decomposition/search cost is not fully amortized. Most importantly, the method acknowledges that a retained singular direction costs `m+n` parameters but does not fully specify how that unequal cost is reconciled with sparse scalar candidates during projection and final ranking.

### Principal Strengths

- Structured low-rank-plus-sparse candidate generation rather than one fixed representation.
- Global allocation across layers and component types.
- Clear separation between convex RPCA guarantees and heuristic allocation.
- Broad model and task coverage.
- Reasoning, long-context, calibration, low-rank, joint-compression, and systems evidence.
- Ablations that demonstrate failure of naive threshold-only composition.
- End-to-end throughput and memory measurements in addition to parameter counts.

### Principal Limitations

- No official public implementation was established and no result was independently rerun.
- Statistical uncertainty and seed sensitivity are not foregrounded.
- Cross-type cost normalization and exact final budget enforcement are underspecified.
- Offline RPCA and policy-search costs are not fully included in a deployment break-even analysis.
- Hardware/kernel evidence is narrow and specialized sparse support is required.
- Calibration and mask stability under model revision or workload shift remain open.
- The paper's own limitation section is brief.

## Evidence and Attribution

| Evidence ID | Evidence | Claim Support | Reviewer Handling |
|---|---|---|---|
| E1 | Complete PDF, official full-paper HTML, metadata HTML, and TeX/source for arXiv:2505.03801v3 | Mechanism, equations, tables, figures, appendix, reproducibility statement, limitation | Inspected fully; decisive pages rendered and visually checked; no long quotation copied |
| E2 | https://arxiv.org/abs/2505.03801 | Identity, authors, dates, subjects, DOI, license, version history | Metadata only; not used alone for empirical claims |
| E3 | https://iclr.cc/virtual/2026/poster/10008795 and https://openreview.net/forum?id=ZaPmQ0NHs4 | ICLR 2026 Poster and forum identity | Official venue context; interactive forum content was challenge-gated |
| E4 | https://qianqiaoai.github.io/ plus exact release searches | Author context and no established official code link | Availability boundary, not proof of permanent absence |
| E5 | Three Black Lake artifacts | Compression taxonomy, adaptive rank allocation, and joint compression synthesis | Related-entry claims remain attributed to their reviewed sources |
| E6 | Live Black Lake and Black-Lake-Data READMEs | Layout, attribution, source locality, dedup scope | Repository authority, not research evidence |
| E7 | Local verification receipt | Complete-source gate | Public summary only; private paths, source bytes, and hashes withheld |

### Random Selection and Dedup Evidence

- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, a uniform PowerShell `Get-Random` raw-unit index, then identity/dedup rejection gates.
- Counts: 75,778 PDFs; 75,776 unique units; 969 observed used arXiv IDs; 213 units excluded by used ID; 185 identifier-incomplete units withheld; 75,378 eligible units.
- Selected zero-based raw-unit index: 18,321.
- Selected ID/title: `2505.03801v3`, *Large Language Model Compression with Global Rank and Sparsity Optimization*.
- Dedup scan: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`; this automation's memory; current Black-Lake-Data `.lake-data` and `.reports`.
- Keys: base/versioned arXiv ID, DOI, exact/normalized title, and slug.
- Duplicate reselections: zero.
- Public-safe 24-hour cutoff: 2026-07-18; no same-paper or same-unit marker was found on or after the cutoff.

### Source-Integrity Evidence

- Initial classification: partial because full-paper HTML was missing.
- Preserved PDF: 1,957,758 bytes, `%PDF-` header, trailing `%%EOF`.
- Repaired official full-paper HTML: 507,233 bytes, 112,922 body characters, a full-document marker, 219 headings/sections, and eight structure terms.
- Metadata HTML: 44,536 bytes; metadata only.
- Source package: 1,397,382 bytes with 26 readable entries.
- Partials after repair: zero.
- Local records updated: README, attribution/provenance note, CSV summary, and JSON verification report.
- Final classification: complete; review began only after the gate passed.
- Source policy: original source files, rendered pages, caches, and extracted source content remain local and were not uploaded.

## Related DEP Entries

Exactly three related entries were selected from current repository state:

| Entry | Concrete Relevance | Source Basis |
|---|---|---|
| [Efficient FM Survey](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Efficient%20FM%20Survey/efficient_fm_survey_manuscript.md) | Places CAP's pruning and low-rank mechanisms inside an architecture-algorithm-system efficiency lifecycle, making clear that representation savings need runtime evidence. | Review of https://arxiv.org/abs/2401.08092 and its official companion context |
| [STAR-KV Ranks](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-STAR-KV%20Ranks/2606.08382-whitepaper-review.md) | Like CAP, makes rank an adaptive resource variable across heterogeneous components; it extends the idea to KV state and custom kernels. | Review of https://arxiv.org/abs/2606.08382v1 and its author-linked implementation |
| [QUOTA Joint Compression](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-QUOTA%20Joint%20Compression/2604.17320-whitepaper-review.md) | Like CAP, rejects independent fixed-stage compression and allocates a shared budget across two interacting mechanisms using sensitivity information. | Review of https://arxiv.org/abs/2604.17320v1 |

## Synthesis Note

### Concept Bridge

CAP, STAR-KV, and QUOTA all treat compression as allocation rather than deletion. They first expose a structured decision space, then distribute scarce capacity according to an estimated effect on quality. The Efficient FM Survey adds the missing lifecycle frame: a better representation is only one layer of efficiency, and its value depends on model architecture, calibration, kernels, serving runtime, and recovery behavior. The common engineering object is therefore a versioned resource contract containing candidate identity, cost, evidence, chosen budget, achieved representation, runtime compatibility, and downstream outcome.

### Potential Implementations

1. `Cost-aware CAP allocator`: Reconstruct RPCA candidates, assign actual byte and kernel costs, optimize a matched-byte budget, and export an auditable allocation manifest with a dense fallback.
2. `Cross-method frontier harness`: Compare CAP-style weight composition, STAR-KV-style adaptive ranks, QUOTA-style joint allocation, and simple baselines under one quality-memory-latency evidence contract.
3. `Profile lifecycle gate`: Pin masks/ranks to model and calibration hashes, shadow a conservative path after model/workload changes, and invalidate profiles when quality or runtime drift exceeds policy.

### Deeper Relationship Observations

1. `Candidate-space quality precedes allocation quality`: CAP's RPCA, STAR-KV's singular bases, and QUOTA's layer sensitivities all determine which choices the optimizer can make; a perfect allocator cannot recover information excluded by the candidate construction stage.
2. `Nominal budget and physical budget diverge`: Rank directions, sparse entries, quantized tensors, token counts, indices, factors, and custom metadata have different costs. Each method needs a cost model grounded in its runtime format.
3. `Adaptation creates invalidation obligations`: Learned masks, ranks, and token policies depend on model and calibration state. Their benefit is inseparable from versioning, drift detection, and fallback behavior.

### Conceptual Similarities

1. Each method replaces a uniform compression ratio with heterogeneous allocation across layers, heads, modules, tokens, or representation types.
2. Each uses a proxy measured on calibration data to predict which retained capacity best preserves downstream quality.
3. Each needs matched-budget baselines and end-to-end runtime measurements before a representation-level advantage becomes a deployment claim.

### MVP Implementations with Code Mock-ups

1. `Weighted candidate selector`: A toy exact-budget selector that makes unequal candidate costs visible.

```python
candidates = [
    {"name": "rank_l0", "utility": 9.0, "bytes": 8},
    {"name": "sparse_l0_a", "utility": 4.0, "bytes": 2},
    {"name": "sparse_l1_b", "utility": 3.0, "bytes": 2},
]
budget = 10
chosen = []
used = 0
for item in sorted(candidates, key=lambda x: x["utility"] / x["bytes"], reverse=True):
    if used + item["bytes"] <= budget:
        chosen.append(item["name"])
        used += item["bytes"]
print({"chosen": chosen, "used_bytes": used})
```

2. `Matched-budget result gate`: A small comparator that rejects gains when quality or realized bytes miss policy.

```python
reference = {"accuracy": 70.0, "bytes": 100, "throughput": 160.0}
candidate = {"accuracy": 69.2, "bytes": 50, "throughput": 176.5}
policy = {"max_accuracy_drop": 1.0, "max_bytes": 50, "min_throughput": 165.0}
passed = (
    reference["accuracy"] - candidate["accuracy"] <= policy["max_accuracy_drop"]
    and candidate["bytes"] <= policy["max_bytes"]
    and candidate["throughput"] >= policy["min_throughput"]
)
print({"passed": passed, "candidate": candidate})
```

3. `Profile invalidation gate`: A local-only drift rule tied to model and calibration identities.

```python
profile = {"model_hash": "model-v1", "calibration_hash": "cal-v1", "max_loss_delta": 0.05}
run = {"model_hash": "model-v2", "calibration_hash": "cal-v1", "loss_delta": 0.02}
identity_ok = (
    profile["model_hash"] == run["model_hash"]
    and profile["calibration_hash"] == run["calibration_hash"]
)
allowed = identity_ok and run["loss_delta"] <= profile["max_loss_delta"]
print({"use_compressed_profile": allowed, "fallback": not allowed})
```

### Developer Challenges

1. Implement exact cost-aware selection for rank directions and sparse entries without hiding index, precision, alignment, or factor overhead.
2. Build kernels whose supported shapes and sparsity regimes realize the representation advantage across target runtimes rather than one benchmark environment.
3. Produce reproducible calibration and benchmark manifests with seeds, model/data hashes, offline cost, warmup, synchronization, and conservative fallback.

### Author Challenges

1. Publish the named implementation files, environment lock, model revisions, and commands needed to reproduce at least three central tables.
2. Formalize the projection and final top-budget selection when candidate types have unequal parameter and byte costs, including tie-breaking and exact budget proof.
3. Report optimizer/calibration variance, offline amortization, and a broader hardware/kernel portability matrix with task-level failure tails.

## Validation Notes

- Manuscript schema: all required headings and front matter fields present; YAML title and H1 are identical and under 40 characters.
- DEP path: `CAP Rank Sparsity` is 17 characters and within the 25-character description limit.
- Exact-count contracts: three related DEP entries; three Synthesis Note potential implementations; three deeper relationship observations; three conceptual similarities; three MVP implementations with three code mock-ups; three developer challenges; three author challenges.
- Code validation target: all three Python mock-ups are dependency-free, bounded, and use synthetic metadata only.
- Source locality: no `.source/` directory and no PDF, HTML, source archive, cache, render, extracted source text, or private path is present in the public artifact set.
- Reproduction boundary: reported table values were inspected and visually cross-checked; no experiment was rerun.
- Submission allowlist: generated Markdown under `.logs`, `.reports`, and `.lake-data`, including the required DEP-E publication-index update.

## Attribution Block

- Source URL: https://arxiv.org/abs/2505.03801
  - Applies to: `Report-Mark.md`.
  - Notes: Canonical identity, authors, dates, subjects, DOI, license, and artifact links.
- Source URL: https://arxiv.org/pdf/2505.03801
  - Applies to: `Report-Mark.md`.
  - Notes: Public equivalent of the complete PDF used for method, result, appendix, and visual review; not redistributed.
- Source URL: https://arxiv.org/html/2505.03801
  - Applies to: `Report-Mark.md`.
  - Notes: Official full-paper HTML used for searchable full-text inspection; not redistributed.
- Source URL: https://arxiv.org/e-print/2505.03801
  - Applies to: `Report-Mark.md`.
  - Notes: TeX/source used locally for equations, tables, appendices, and bibliography checks; not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2505.03801
  - Applies to: `Report-Mark.md`.
  - Notes: Persistent arXiv DOI.
- Source URL: https://iclr.cc/virtual/2026/poster/10008795
  - Applies to: `Report-Mark.md`.
  - Notes: Official ICLR 2026 poster record.
- Source URL: https://openreview.net/forum?id=ZaPmQ0NHs4
  - Applies to: `Report-Mark.md`.
  - Notes: OpenReview forum identity; interactive content was challenge-gated.
- Source URL: https://qianqiaoai.github.io/
  - Applies to: `Report-Mark.md`.
  - Notes: Author-maintained publication listing and release-context check.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `Report-Mark.md`.
  - Notes: Live repository authority for processed artifacts, source locality, and attribution.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `Report-Mark.md`.
  - Notes: DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `Report-Mark.md`.
  - Notes: Companion-repository authority used for dedup context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Efficient%20FM%20Survey/efficient_fm_survey_manuscript.md
  - Applies to: `Report-Mark.md`.
  - Notes: Related DEP entry for the resource-efficient foundation-model taxonomy.
- Source URL: https://arxiv.org/abs/2401.08092
  - Applies to: `Report-Mark.md`.
  - Notes: Primary source named by the Efficient FM Survey DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-STAR-KV%20Ranks/2606.08382-whitepaper-review.md
  - Applies to: `Report-Mark.md`.
  - Notes: Related DEP entry for adaptive rank control and kernel realization.
- Source URL: https://arxiv.org/abs/2606.08382v1
  - Applies to: `Report-Mark.md`.
  - Notes: Primary source named by the STAR-KV Ranks DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-QUOTA%20Joint%20Compression/2604.17320-whitepaper-review.md
  - Applies to: `Report-Mark.md`.
  - Notes: Related DEP entry for joint compression allocation.
- Source URL: https://arxiv.org/abs/2604.17320v1
  - Applies to: `Report-Mark.md`.
  - Notes: Primary source named by the QUOTA Joint Compression DEP.
