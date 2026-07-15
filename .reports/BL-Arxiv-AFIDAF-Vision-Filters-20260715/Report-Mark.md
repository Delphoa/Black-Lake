# Report-Mark: AFIDAF Vision Filters

## Source Metadata

| Field | Value |
|---|---|
| Paper | *AFIDAF: Alternating Fourier and Image Domain Adaptive Filters as an Efficient Alternative to Attention in ViTs* |
| Authors | Yunling Zheng; Zeyi Xu; Fanghui Xue; Biao Yang; Jiancheng Lyu; Shuai Zhang; Yingyong Qi; Jack Xin |
| arXiv | arXiv:2407.12217v2; submitted 2024-07-16; revised 2024-09-25 |
| arXiv record | https://arxiv.org/abs/2407.12217 |
| Full-paper HTML | https://arxiv.org/html/2407.12217 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2407.12217 |
| Published chapter | ISVC 2024, *Advances in Visual Computing*, LNCS 15046, pages 17-30; first online 2025-01-22 |
| Published DOI | https://doi.org/10.1007/978-3-031-77392-1_2 |
| Affiliations | University of California, Irvine; Qualcomm AI Research |
| Subject | Computer Vision and Pattern Recognition (cs.CV) |
| Source license visibility | arXiv non-exclusive distribution license; Springer chapter under exclusive license. Source documents were used as evidence and withheld locally. |
| Local source state | Complete after repair: verified PDF and full-paper HTML, plus metadata HTML and a verified source archive |
| Code status | No official AFIDAF implementation was established from the paper, canonical records, author publication page, or exact-title/code searches; code was not run |
| Review date | 2026-07-15 date-only public marker |

## Concise Research Notes

### Problem

AFIDAF targets lightweight visual backbones that need both local spatial detail and long-range feature mixing without the quadratic token-pair operations of self-attention. Its starting point is AFFNet, an attention-free Fourier backbone. The authors inspect AFFNet's implementation and argue that its learned Fourier mask mixes channels but is effectively an identity over the frequency plane, leaving a spatial-mixing gap that becomes visible on dense prediction tasks.

### Method

The proposed block alternates two operators. In the image domain, a decomposed large-kernel approximation uses depthwise local convolution, depthwise dilated convolution, a pointwise channel convolution, and channel-group shuffling. In the Fourier domain, the AFF-style channel mask supplies global mixing. The reviewer interpretation is that AFIDAF deliberately assigns high-frequency/local structure to spatial convolution and low-frequency/non-local structure to the Fourier path.

The paper also proposes HAFIDAF, a Swin-shaped hierarchy that replaces window-attention blocks. Its first two stages use AFIDAF convolution blocks, while later stages use Fourier-mask blocks. Group-shuffled MLPs, normalization, residuals, and periodic Fourier convolution preserve the hierarchical backbone pattern while reducing parameter count.

### Evidence

The strongest direct evidence is the paper's six result tables:

| Evaluation | AFIDAF result | Closest stated comparison | Reviewer reading |
|---|---:|---:|---|
| ImageNet-1K classification | 80.9% Top-1, 6.5M parameters, 1.5G FLOPs | AFFNet 79.8%, 5.5M, 1.5G; IDAF 80.3%, 6.2M, 1.4G | The alternating block gains 1.1 points over AFFNet but adds parameters; it gains 0.6 over image-only IDAF. |
| Tiny ImageNet model | 77.6% Top-1, 3.0M, 0.8G | AFFNet-T 77.0%, 2.6M, 0.8G | Small accuracy gain at equal reported FLOPs and modestly higher parameter count. |
| COCO SSD detection | 30.2 mAP, 6.2M | AFFNet 28.4, 5.6M; IDAF 28.2, 5.9M | The largest AFIDAF-vs-AFFNet gain is 1.8 mAP. |
| PASCAL VOC segmentation | 81.6 mIoU, 7.8M | AFFNet 80.5, 6.9M; IDAF 81.1, 7.5M | Dense prediction supports the local-plus-global hypothesis, but the model is larger. |
| HAFIDAF ImageNet-1K | 79.8% Top-1, 14.8M, 4.45G | Swin-T 81.2%, 28M, 4.5G | Parameters fall 47%, but FLOPs are nearly unchanged and accuracy drops 1.4 points. |
| HAFIDAF VOC segmentation | 72.4 mIoU, 46M | Swin-T 71.1, 60M | The strongest compression result: 24% fewer parameters with +1.3 mIoU in the stated setup. |

AFIDAF was trained from scratch on ImageNet-1K for 300 epochs using eight NVIDIA RTX A6000 GPUs and batch size 1,024. Detection used SSD on COCO 2017; segmentation used DeepLabv3 on PASCAL VOC 2012 augmented with COCO. HAFIDAF used Cascade Mask R-CNN for detection and UperNet for segmentation. These are source-reported results; no experiment was reproduced.

### Limitations

The paper has no dedicated limitations section. It notes a future need to localize the Fourier mask and shrink the image-domain kernel, but does not report repeated seeds, uncertainty intervals, energy, throughput, latency, peak memory, mobile-device tests, or kernel-level profiling. Parameter count is therefore the strongest efficiency metric; reported FLOPs sometimes weaken the compression narrative. Training a nominally lightweight model on eight A6000 GPUs also separates inference compactness from training cost.

The comparisons mix model families and training stacks, so table rank should not be treated as a controlled universal leaderboard. AFIDAF's ablation distinguishes AFFNet, image-only IDAF, and the alternating design, but it does not independently remove group shuffle, dilated convolution, or each ordering choice. HAFIDAF demonstrates a parameter/accuracy trade, not drop-in equivalence to Swin-T. No official AFIDAF code release was established, limiting independent reproducibility.

### Selection and Deduplication

The local archive was enumerated with `rg --files -g "*.pdf"`, and each PDF parent directory was treated as one paper unit. The run observed 75,776 PDFs and 75,776 paper units. A used-paper index built from Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`, automation memory, and Black-Lake-Data `.lake-data`/`.reports` contained 541 distinct arXiv IDs. It excluded 119 paper units, leaving 75,657 eligible units.

PowerShell `Get-Random` selected eligible zero-based index 45,105, arXiv:2407.12217. Exact-ID, normalized-title, DOI, and `AFIDAF` slug checks found no prior artifact. The 24-hour validation cutoff was 2026-07-14, and no recent same-paper marker was found. Duplicate rejections and reselections were both zero.

The selected archive unit initially had only a valid PDF and a short README, so it was classified `partial` and review stopped. A bounded local-only repair preserved the PDF and collected official full-paper HTML, metadata HTML, and the source archive. Verification then passed: 677,737-byte PDF with `%PDF-` header and trailing `%%EOF`; 200,299-byte HTML with 43,600 body characters, a document marker, 68 heading markers, and seven structure terms; 40,757-byte metadata HTML; 436,334-byte source archive with a valid listing; zero partial files.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Qualification |
|---|---|---|---|---|
| E1 | Verified arXiv v2 PDF, complete HTML, and TeX/source inventory | Equations, block design, experiments, tables, figures, conclusion | High for accurate source reporting | Source files remain local; results were not rerun. |
| E2 | arXiv metadata and DOI | Title, authors, subject, version dates, public identifiers, license link | High | Metadata alone does not validate results. |
| E3 | Springer chapter record | ISVC/LNCS publication status, pages 17-30, first-online date, published DOI | High | Publisher page exposes abstract and metadata, not the full subscribed chapter in this review. |
| E4 | Shuai Zhang publication page and UCI eScholarship record | Near-primary publication context and public author-hosted locator | Medium-high | Neither page established an AFIDAF code release. |
| E5 | Tables 1-3 | AFIDAF classification, detection, segmentation, and single-domain ablation values | High for transcription | No repeated-seed statistics or independent run. |
| E6 | Tables 4-6 | HAFIDAF parameter/accuracy trade-offs against Swin-T and other backbones | High for transcription | Parameter reduction does not always imply FLOP, latency, or energy reduction. |
| E7 | SSP Detection DEP-E | Spatial priors, explicit geometry, object-detection transfer, cost reporting | Medium | Related synthesis, not validation of AFIDAF. |
| E8 | HSD FTI-FDet DEP-E | Compact visual detection, resource metrics, field failure modes, edge deployment | Medium | Different detector and data domain. |
| E9 | Physical Data AI DEP-E | Structured non-attention representations and parameter-efficiency boundaries | Medium | Different modality and equation-based mechanism. |
| E10 | Live Black Lake and Black-Lake-Data README authorities | Filing, attribution, source-locality, dedup, and submission rules | High | Process evidence only. |

## Related DEP Entries

Exactly three existing entries were verified and selected:

1. `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md`
   - Relevance: Both works inject explicit spatial structure into vision pipelines. SSP partitions image space to recover oriented boxes from sparse points; AFIDAF adds decomposed spatial filtering to repair a frequency-only mixing gap. SSP also provides a downstream object-detection and cost-accounting perspective.
   - Source basis: Reviewed manuscript grounded in arXiv:2506.10601v2, publisher DOI, and an official Apache-2.0 implementation.
2. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
   - Relevance: Both pursue compact visual systems and combine specialized paths rather than relying on a single generic operator. HSD contributes latency, memory, model-size, edge-deployment, and uneven-lighting evidence that AFIDAF does not report.
   - Source basis: Reviewed manuscript grounded in arXiv:2307.00701v1 and DOI:10.1016/j.aei.2023.102091.
3. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md`
   - Relevance: Both replace generic learned blocks with structured transforms to reduce representational cost. Physical Data AI sharpens the distinction between small parameter counts, domain-fit assumptions, and actual deployment efficiency.
   - Source basis: Reviewed manuscript grounded in arXiv:2407.14504v3 and its reported parameter/ablation evidence.

## Synthesis Note

### Concept Bridge

AFIDAF, SSP, HSD FTI-FDet, and Physical Data AI converge on one design rule: compact models improve when capacity is assigned to a problem-aligned structure rather than uniformly distributed across a generic backbone. AFIDAF divides local/high-frequency and global/low-frequency mixing across image and Fourier domains. SSP divides weak supervision into spatial partitions and semantic extraction. HSD divides feature and localization knowledge across heterogeneous paths. Physical Data AI embeds a known equation family. The bridge is not “structured models are always better”; it is “a claimed efficiency gain is credible only when the inductive bias, resource ledger, failure boundary, and controlled ablation are all visible.”

### Potential Implementations

1. **Dual-domain backbone workbench:** A local research harness that swaps attention, AFF, IDAF, and AFIDAF-style token mixers under matched parameter, FLOP, training-recipe, and resolution budgets. It would emit per-stage feature spectra, receptive-field diagnostics, accuracy, memory, and latency.
2. **Edge vision Pareto evaluator:** A deployment lab that combines AFIDAF backbones with HSD-style resource reporting and SSP-style detection tasks, measuring device latency tails, peak memory, energy, calibration, and failure slices rather than parameter count alone.
3. **Structure-fit recommender:** An offline experiment planner that characterizes dataset geometry and spectrum, then recommends image-domain, Fourier-domain, mixed, or task-specific structured blocks with explicit uncertainty and mandatory matched baselines.

### Deeper Relationship Observations

1. AFIDAF and SSP both repair an information-allocation problem: AFFNet underuses spatial variation, while point supervision omits object extent and orientation. Each method adds an explicit spatial mechanism instead of simply scaling a backbone.
2. AFIDAF and HSD illustrate that heterogeneous paths are valuable when their roles are auditable. AFIDAF separates local and global mixing; HSD separates feature and localization knowledge. In both, deployment claims depend on measuring the cost of every path, not naming the model “lightweight.”
3. AFIDAF and Physical Data AI make compactness conditional on domain fit. Fourier/image alternation assumes visual energy and spatial detail benefit from the chosen decomposition; equation-based embeddings assume data align with the physical family. Misfit can erase the parameter advantage.

### Conceptual Similarities

1. All four artifacts use a strong inductive bias to reduce what must be learned from data.
2. All separate representation quality from downstream decision quality through classification, detection, segmentation, or task-specific evaluation.
3. All expose a multi-objective frontier among accuracy, parameter count, compute, memory, robustness, and reproducibility; none justifies collapsing that frontier into one “efficient” label.

### MVP Implementations with Code Mock-Ups

1. **Matched Pareto recorder:** Store comparable accuracy-resource records and reject comparisons that omit required metrics.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Run:
    name: str
    top1: float
    params_m: float
    flops_g: float
    latency_ms: float

def pareto_ready(run: Run) -> bool:
    return all(value >= 0 for value in (run.params_m, run.flops_g, run.latency_ms))
```

2. **Alternation ablation planner:** Generate only controlled mixer variants so the local, Fourier, and ordering effects can be isolated.

```python
def ablation_matrix():
    return [
        {"name": "fourier_only", "image_filter": False, "fourier_filter": True},
        {"name": "image_only", "image_filter": True, "fourier_filter": False},
        {"name": "image_then_fourier", "image_filter": True, "fourier_filter": True},
    ]
```

3. **Release gate:** Require completeness, matched baselines, and device evidence before a compact-backbone result is labeled deployment-ready.

```python
def release_gate(report):
    required = {"accuracy", "params", "flops", "latency", "memory", "seeds", "failures"}
    missing = sorted(required.difference(report))
    return {"status": "review" if missing else "candidate", "missing": missing}
```

### Developer Challenges

1. FFT kernels, complex tensors, padding, and layout conversions may erase theoretical savings on target hardware; profiling must include memory traffic and synchronization.
2. Reproducing paper tables without an official code release requires reconstructing block ordering, group sizes, training schedules, and framework details while avoiding accidental benchmark advantages.
3. A single API must represent classification, detection, and segmentation fairly enough to compare backbones without hiding head-specific compute, preprocessing, or tuning.

### Author Challenges

1. Establish which component causes each gain through matched ablations for group shuffle, dilation, large-kernel decomposition, Fourier mask, alternation order, and stage placement.
2. Expand efficiency evidence from parameters/FLOPs to repeated-seed accuracy, throughput, latency tails, memory, energy, training cost, and real edge hardware.
3. Publish code, configurations, checkpoints, environment pins, and expected hashes while documenting negative results, failure cases, and the boundary between an attention alternative and a Swin compression proxy.

## Validation Notes

- Required source-integrity gate passed before synthesis; the `/abs/` page was treated only as metadata.
- Candidate count, used-ID exclusion, selected index, eligible count, cutoff date, and zero-reselection result were recorded without local paths.
- Exact-title, arXiv ID, DOI, and slug searches found no duplicate in either repository or automation memory.
- Quantitative claims were cross-checked between the verified PDF and full-paper HTML tables.
- Author claims and reviewer interpretations are labeled separately; no experiment, model, or code was run.
- Exactly three related DEP entries were inspected and used.
- The synthesis subsections each contain exactly three requested items.
- All source documents and repair/integrity records remain local. No source file or `.source/` directory is included.
- Public text uses repository-relative paths and public URLs only; local machine context and exact execution timestamps are withheld.

## Attribution Block

- Source URL: https://arxiv.org/abs/2407.12217
  - Applies to: source identity, authors, version history, subject, abstract, DOI, and license visibility.
  - Notes: Official metadata page; not treated as the full paper.
- Source URL: https://arxiv.org/pdf/2407.12217
  - Applies to: complete paper review, equations, figures, experimental setup, tables, and conclusion.
  - Notes: Verified local copy was inspected and withheld; no PDF is deposited.
- Source URL: https://arxiv.org/html/2407.12217
  - Applies to: complete paper structure, method, experiments, tables, and references.
  - Notes: Official full-paper HTML passed the integrity gate; local copy withheld.
- Source URL: https://arxiv.org/e-print/2407.12217
  - Applies to: source inventory and equation/section cross-checking.
  - Notes: Verified source archive was inspected locally and withheld.
- Source URL: https://doi.org/10.48550/arXiv.2407.12217
  - Applies to: persistent arXiv identifier.
  - Notes: Public DOI locator.
- Source URL: https://link.springer.com/chapter/10.1007/978-3-031-77392-1_2
  - Applies to: publication status, ISVC/LNCS venue, pages, first-online date, published DOI, and author affiliations.
  - Notes: Official publisher chapter record.
- Source URL: https://zsivine.github.io/research/
  - Applies to: author-side publication context and code-availability check.
  - Notes: Near-primary publication page; no AFIDAF code link was established.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md
  - Applies to: related spatial-prior and object-detection synthesis.
  - Notes: Existing processed Black Lake artifact.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md
  - Applies to: related compact visual deployment and resource-ledger synthesis.
  - Notes: Existing processed Black Lake artifact.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md
  - Applies to: related structured-representation and parameter-efficiency synthesis.
  - Notes: Existing processed Black Lake artifact.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: target repository rules and public source-locality policy.
  - Notes: Live default-branch authority read before drafting.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: companion repository dedup scope and layout context.
  - Notes: Live default-branch authority read before reliance.
