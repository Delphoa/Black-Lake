---
title: "AFIDAF Vision - DEP-E"
generated_at: "2026-07-15 (date-only public marker; exact local timestamp and timezone withheld)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of alternating image-domain and Fourier-domain adaptive filters as compact attention alternatives for vision backbones."
source_status: "verified local PDF, full-paper HTML, metadata HTML, and source archive; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-15"
temporal_cutoff: "arXiv v2 revised 2024-09-25; Springer chapter first online 2025-01-22; public context inspected through 2026-07-15"
primary_url: "https://arxiv.org/abs/2407.12217"
stable_identifier: "arXiv:2407.12217v2; DOI:10.1007/978-3-031-77392-1_2"
confidence_summary: "High for source identity, method reconstruction, and transcription of reported tables; medium for architectural interpretation; low for independent reproducibility because code and experiments were not run."
safety_scope: "public scholarly review, synthetic evaluation planning, and non-sensitive computer-vision research"
distribution_notes: "Derived Markdown and public URLs only; original source documents, extraction material, repair records, and local execution context are withheld."
---

# AFIDAF Vision - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | AFIDAF arXiv record | Primary metadata | HTML | arXiv:2407.12217v2 | https://arxiv.org/abs/2407.12217 | arXiv non-exclusive distribution license shown; metadata only, not the paper document | 2026-07-15 | Inspected |
| S2 | AFIDAF PDF | Primary paper | PDF | arXiv:2407.12217v2 | https://arxiv.org/pdf/2407.12217 | Complete local copy verified and inspected; file not redistributed | 2026-07-15 | Fully inspected |
| S3 | AFIDAF full-paper HTML | Primary paper | HTML | arXiv:2407.12217v2 | https://arxiv.org/html/2407.12217 | Complete official rendering verified and inspected; file not redistributed | 2026-07-15 | Fully inspected |
| S4 | AFIDAF source package | Primary manuscript source | TeX/source archive | arXiv:2407.12217v2 | https://arxiv.org/e-print/2407.12217 | Archive listing verified locally; file not redistributed | 2026-07-15 | Inventory and sections inspected |
| S5 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2407.12217 | https://doi.org/10.48550/arXiv.2407.12217 | Public DOI locator | 2026-07-15 | Recorded |
| S6 | Springer AFIDAF chapter | Publisher and venue record | Web page | DOI:10.1007/978-3-031-77392-1_2 | https://link.springer.com/chapter/10.1007/978-3-031-77392-1_2 | Publisher metadata; © 2025 authors under exclusive Springer license | 2026-07-15 | Inspected |
| S7 | Shuai Zhang research page | Author-side context | Web page | ISVC 2024 publication entry | https://zsivine.github.io/research/ | Near-primary publication context; no AFIDAF code link established | 2026-07-15 | Inspected |
| S8 | SSP Detection - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260711-SSP Oriented Detection | `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` | Derived public artifact; primary basis arXiv:2506.10601v2 | 2026-07-15 | Inspected |
| S9 | HSD FTI-FDet - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260712-HSD FTI-FDet | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Derived public artifact; primary basis arXiv:2307.00701v1 | 2026-07-15 | Inspected |
| S10 | Physical Data AI - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260710-Physical Data AI | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` | Derived public artifact; primary basis arXiv:2407.14504v3 | 2026-07-15 | Inspected |
| S11 | Black Lake README authorities | Repository rules | Markdown | origin/main | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Live default-branch filing, attribution, index, and source-locality authority | 2026-07-15 | Fetched and read |
| S12 | Black-Lake-Data README | Related-repository authority | Markdown | origin/main | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Live default-branch layout and dedup context | 2026-07-15 | Fetched and read |

Paper/work metadata:

- `Full title`: AFIDAF: Alternating Fourier and Image Domain Adaptive Filters as an Efficient Alternative to Attention in ViTs.
- `Authors`: Yunling Zheng, Zeyi Xu, Fanghui Xue, Biao Yang, Jiancheng Lyu, Shuai Zhang, Yingyong Qi, Jack Xin.
- `Affiliations`: University of California, Irvine; Qualcomm AI Research.
- `arXiv dates`: submitted 2024-07-16; v2 revised 2024-09-25.
- `Publication`: International Symposium on Visual Computing 2024; *Advances in Visual Computing*, LNCS volume 15046, pages 17-30; Springer chapter first online 2025-01-22.
- `Stable identifiers`: arXiv:2407.12217v2; arXiv DOI 10.48550/arXiv.2407.12217; published DOI 10.1007/978-3-031-77392-1_2.
- `Research domain`: lightweight vision backbones, Fourier token mixing, large-kernel convolution, attention alternatives, image classification, object detection, semantic segmentation, and ViT compression.
- `Local source paths`: Withheld by public-output policy. Verified source artifacts remain outside the repository.
- `Code and data`: The paper describes ImageNet-1K, COCO 2017, and PASCAL VOC 2012 experiments. No official AFIDAF code repository was established from inspected canonical and author-side sources; no dataset, code, checkpoint, or experiment was collected or run.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5 | Primary metadata and DOI | Title, authors, subject, abstract, versions, dates, identifiers, license link | Source identity and high-level contribution | High | Abstract does not validate method or results |
| E2 | S2, S3, S4 | Primary complete paper | Equations 1-4, Figures 1-3, block roles, architecture, training settings, Tables 1-6, conclusion | Method reconstruction and main claims | High for source reporting | No independent derivation or experiment |
| E3 | S2/S3 Table 1 | Primary empirical evidence | AFIDAF/AFIDAF-T accuracy, parameters, FLOPs, AFFNet and IDAF ablation | Classification and alternating-domain claim | High for transcription | Single reported recipe; no intervals or seeds |
| E4 | S2/S3 Tables 2-3 | Primary empirical evidence | COCO SSD mAP and PASCAL VOC DeepLabv3 mIoU | Downstream dense-prediction claim | High for transcription | No independent run; limited comparator controls |
| E5 | S2/S3 Tables 4-6 | Primary empirical evidence | HAFIDAF versus Swin-T and other backbones on classification, detection, segmentation | Parameter-compression claim | High for transcription | FLOPs/latency/energy evidence incomplete |
| E6 | S2/S3 method discussion | Primary method evidence | AFFNet code-level limitation, image/Fourier role split, future localization/shrinking note | Mechanism and stated research gap | Medium-high | AFFNet code inspection was author-reported and not repeated here |
| E7 | S6 | Official publisher record | ISVC/LNCS venue, pages, first-online date, DOI, authors, affiliations | Publication status | High | Publisher preview is metadata/abstract context |
| E8 | S7 and exact-title/code searches | Author-side and discovery evidence | Publication listing and absence of a verified AFIDAF code link | Code-availability assessment | Medium | Absence from inspected sources does not prove no code exists anywhere |
| E9 | S8 | Related processed research | Explicit spatial priors, object detection, efficiency costs, code availability, failure cases | Cross-DEP spatial-structure synthesis | Medium | Does not validate AFIDAF |
| E10 | S9 | Related processed research | Compact visual detection, distillation, model size, latency, memory, uneven-lighting failures | Cross-DEP deployment synthesis | Medium | Different architecture and application |
| E11 | S10 | Related processed research | Structured non-attention feature transforms, parameter efficiency, domain-fit limitations | Cross-DEP compact-representation synthesis | Medium | Different modality and mechanism |
| E12 | S11, S12 | Live repository authorities | DEP class/location, required README, source locality, publication index, attribution, dedup scope | Artifact and submission compliance | High | Process evidence only |
| E13 | Private integrity records, summarized publicly | Local process evidence | PDF size/header/EOF; HTML size/body/document/headings/structure; source listing; zero partials | Mandatory complete-source gate | High | Local artifacts and paths intentionally withheld |

## Executive Summary

AFIDAF proposes an attention-free vision backbone that alternates adaptive filtering across the image and Fourier domains. The authors begin from AFFNet, whose practical mask is described as channelwise rather than spatially adaptive over the frequency plane. AFIDAF adds a decomposed large-kernel image-domain path with depthwise convolution, depthwise dilated convolution, pointwise channel convolution, and group shuffling, then applies the AFF-style Fourier channel mask. The intended division of labor is local/high-frequency spatial detail in the image path and global/non-local mixing in the Fourier path.

The paper reports consistent gains over AFFNet. On ImageNet-1K, AFIDAF reaches 80.9% Top-1 with 6.5M parameters and 1.5G FLOPs, compared with AFFNet at 79.8%, 5.5M, and 1.5G. AFIDAF-T reaches 77.6% with 3.0M and 0.8G, compared with AFFNet-T at 77.0%, 2.6M, and 0.8G. On downstream tasks, AFIDAF reports 30.2 mAP with SSD on COCO and 81.6 mIoU with DeepLabv3 on PASCAL VOC, improving AFFNet by 1.8 and 1.1 points respectively.

HAFIDAF adapts the idea to a Swin-shaped hierarchy. It reports 14.8M parameters rather than Swin-T's 28M, with ImageNet Top-1 falling from 81.2% to 79.8% and FLOPs remaining nearly equal at 4.45G versus 4.5G. HAFIDAF's strongest reported trade-off is segmentation: 72.4 mIoU at 46M total parameters versus Swin-T's 71.1 at 60M in the stated UperNet setup.

The reviewer assessment is favorable but bounded. Alternation appears useful relative to both Fourier-only AFFNet and image-only IDAF, especially for dense prediction. Yet AFIDAF itself is not smaller than AFFNet, HAFIDAF does not consistently reduce FLOPs, and the paper provides no device latency, memory, energy, repeated-seed uncertainty, or official code release. The work is best read as a promising operator-allocation hypothesis and parameter/accuracy trade study, not a completed proof of mobile deployment efficiency.

## Detailed Summary

### Problem Context

Vision transformers provide global interaction but can be expensive in parameter count and token-pair computation. Lightweight convolutional networks are efficient but typically rely on local receptive fields and static kernels. Fourier transforms offer global mixing at favorable asymptotic cost, which motivated AFFNet and related attention-free token mixers. AFIDAF asks whether an explicitly spatial filter can compensate for the practical AFF mask's limited action over frequency/image coordinates while preserving a lightweight regime.

The paper distinguishes three design families. Convolutional backbones offer locality and translation-related inductive bias. ViTs offer content-adaptive global interaction. Fourier backbones offer global convolution-like mixing but need a mechanism for spatially selective detail. AFIDAF combines the last and first families rather than approximating attention directly with another attention operator.

### AFF Baseline and Diagnosed Gap

For a feature tensor with height, width, and channels, AFF transforms spatial axes with an FFT, applies a learned nonlinear mask, multiplies the mask and spectrum, then returns through an inverse FFT. The theoretical expression suggests a global adaptive filter. The authors report that the inspected AFFNet implementation applies its learned subnetwork along channels while leaving the frequency plane unchanged. Their diagnosis is therefore not “Fourier mixing fails,” but “channelwise Fourier masking underrepresents spatial adaptation.”

This diagnosis motivates adding an image-domain operator before the Fourier mask. The contribution depends on the difference between a general frequency-selective mask and the implemented channel mask, so an independent reproduction should pin the exact AFFNet code/version and verify dimensions directly.

### AFIDAF Block

The image-domain adaptive filter approximates a large convolutional kernel with three components:

1. Depthwise spatial convolution captures nearby structure.
2. Depthwise dilated convolution expands receptive field without a dense large kernel.
3. A pointwise channel convolution integrates channels.

Channel-group shuffling is inserted to increase cross-group interaction while controlling cost. The output then enters the AFF-style Fourier channel mask. The paper's conceptual explanation assigns local edges, corners, textures, and high-frequency content to the image path, while the Fourier path captures low-frequency and non-local information beyond the kernel's reach.

The block repeats across three feature-extraction stages. Normalization, MLPs, downsampling, fusion, and residual structure surround the alternating filter. The important reviewer interpretation is that “alternating” is an operator split: it avoids asking either a spatial kernel or a channelwise spectrum mask to cover every dimension alone.

### HAFIDAF Hierarchy

HAFIDAF retains a four-stage Swin-like hierarchy but replaces transformer blocks. The first two stages use AFIDAF convolution blocks, including periodic Fourier convolution and group-shuffled MLPs. The latter two stages use channelwise Fourier mask blocks. Layer normalization and shortcuts remain.

The stated aim is model compression rather than exact architectural equivalence. This distinction matters. HAFIDAF's ImageNet table shows a large parameter reduction with a modest accuracy drop but essentially unchanged FLOPs. Its object-detection table shows 72M total parameters and 48.9 APbox versus Swin-T at 86M and 50.5. Its segmentation table shows 46M and 72.4 mIoU versus 60M and 71.1. The evidence supports a task-dependent frontier, not uniform dominance.

### Experimental Design

AFIDAF classification uses ImageNet-1K with more than 1.2 million training images across 1,000 classes. The paper reports 300 training epochs from scratch, 256×256 inputs, eight NVIDIA RTX A6000 GPUs, batch size 1,024, AdamW, weight decay 0.05, and cosine decay from 2e-3 to 2e-4.

COCO object detection uses SSD, ImageNet-pretrained AFIDAF backbones, 320×320 inputs, 200 epochs, AdamW, weight decay 0.05, and SSD Multibox loss. The paper states 118K training, 5K validation, and 20K test-dev images over 80 categories.

PASCAL VOC semantic segmentation uses DeepLabv3, 512×512 inputs, 50 epochs, AdamW, cross-entropy, and COCO augmentation. The paper describes more than 11,000 images and 20 categories. HAFIDAF evaluation uses Cascade Mask R-CNN for detection and UperNet for segmentation.

No repeated seeds, confidence intervals, significance tests, device inference measurements, energy results, or peak-memory results are reported in the inspected paper.

### Classification Results and Ablation

| Model | Parameters (M) | FLOPs (G) | ImageNet Top-1 (%) |
|---|---:|---:|---:|
| AFFNet-T | 2.6 | 0.8 | 77.0 |
| AFIDAF-T | 3.0 | 0.8 | 77.6 |
| AFFNet | 5.5 | 1.5 | 79.8 |
| IDAF | 6.2 | 1.4 | 80.3 |
| AFIDAF | 6.5 | 1.5 | 80.9 |
| RepViT-M1.0 | 6.8 | 1.1 | 80.3 |
| EfficientViT | 7.8 | 0.7 | 79.1 |

The controlled part of Table 1 is the AFFNet/IDAF/AFIDAF trio. Image-only IDAF improves 0.5 points over AFFNet while adding 0.7M parameters. Alternation improves another 0.6 points while adding 0.3M and 0.1G. This supports complementary operator roles, although it does not isolate group shuffle, dilation, or ordering.

### Downstream Results

Object detection:

| Backbone | Parameters (M) | COCO mAP (%) |
|---|---:|---:|
| AFFNet-T | 3.0 | 25.3 |
| AFIDAF-T | 3.1 | 25.4 |
| AFFNet | 5.6 | 28.4 |
| IDAF | 5.9 | 28.2 |
| AFIDAF | 6.2 | 30.2 |

Semantic segmentation:

| Backbone | Parameters (M) | PASCAL VOC mIoU (%) |
|---|---:|---:|
| AFFNet-T | 3.5 | 77.8 |
| AFIDAF-T | 3.9 | 79.6 |
| AFFNet | 6.9 | 80.5 |
| IDAF | 7.5 | 81.1 |
| AFIDAF | 7.8 | 81.6 |

The dense tasks are the most persuasive evidence for the authors' spatial-mixing diagnosis. AFIDAF's full version improves detection and segmentation, while IDAF alone is insufficient on detection. The tiny detection delta is only 0.1 mAP, so the benefit is not uniform across capacity.

### HAFIDAF Compression Results

| Task | HAFIDAF | Swin-T | Reviewer interpretation |
|---|---|---|---|
| ImageNet-1K | 14.8M, 4.45G, 79.8 Top-1, 95.0 Top-5 | 28M, 4.5G, 81.2, 95.5 | 47% fewer parameters; almost equal FLOPs; -1.4 Top-1 |
| COCO detection | 72M, 48.9 APbox | 86M, 50.5 APbox | 17% fewer parameters; -1.6 APbox |
| PASCAL VOC segmentation | 46M, 72.4 mIoU, 80.3 mAcc, 93.8 aAcc | 60M, 71.1, 77.9, 93.4 | 24% fewer parameters with gains across stated metrics |

The parameter-compression narrative is strongest where accuracy is maintained or improved. Classification shows that parameter count can fall without reducing FLOPs, and object detection shows a clear quality cost. A deployment evaluation needs latency, memory bandwidth, FFT efficiency, and energy on the target device.

### Conclusions and Open Questions

The paper concludes that adding image-domain spatial filtering to AFFNet's channelwise Fourier mask improves classification and dense prediction while remaining lightweight, and that HAFIDAF can reduce Swin-T parameter count. The source itself identifies localization of the Fourier operator and smaller image kernels as future work.

Open questions include whether the result survives matched training budgets; whether Fourier operators are efficient on mobile NPUs; how group size and shuffle topology affect gains; whether image-first ordering is essential; how performance changes under corruption and resolution shift; and whether HAFIDAF's parameter reduction improves real latency or only storage.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | AFFNet's practical mask mixes channels but lacks spatial action over the frequency plane. | Author implementation claim | E2, E6 | Central diagnosis; source-supported but AFFNet code was not independently inspected in this run. | Medium-high |
| C2 | Alternating image and Fourier filters form a local-global feature extractor. | Author conceptual claim | E2 | Mechanistically plausible and consistent with the block, but frequency-role attribution is not directly measured. | Medium-high |
| C3 | AFIDAF improves AFFNet on ImageNet-1K while keeping equal reported FLOPs. | Author empirical claim | E3 | 80.9 versus 79.8 at 1.5G; parameters increase from 5.5M to 6.5M. | High for source report |
| C4 | AFIDAF improves AFFNet on COCO detection and PASCAL VOC segmentation. | Author empirical claim | E4 | +1.8 mAP and +1.1 mIoU in the stated setups; not reproduced. | High for source report |
| C5 | Alternation is better than either Fourier-only AFFNet or image-only IDAF. | Author ablation claim | E3, E4 | Supported for classification and segmentation; IDAF detection is slightly worse than AFFNet. Component causality remains incomplete. | Medium-high |
| C6 | HAFIDAF compresses Swin-T while maintaining useful performance. | Author empirical/implementation claim | E5 | Parameters fall substantially; accuracy trade varies and FLOPs barely change for classification. | Medium |
| C7 | AFIDAF is an efficient alternative to attention for edge deployment. | Author implication | E3-E6 | Parameter evidence is promising, but device latency, memory, energy, and kernel support are missing. | Low-medium |
| C8 | Explicitly assigning local and global roles can improve compact vision systems. | Reviewer interpretation | E2-E5, E9-E11 | Coherent across AFIDAF and related DEP entries, not a universal theorem. | Medium |
| C9 | Efficiency claims should be evaluated as Pareto records rather than single parameter counts. | Reviewer interpretation | E3-E5, E10-E11 | Strongly motivated by near-equal FLOPs, training cost, and missing device evidence. | High as review guidance |

## Methodology

- `Research objective`: Randomly select one eligible local arXiv paper, enforce the complete-source gate, review the paper source-first, connect it to exactly three verified DEP entries, and create a public-safe schema-complete DEP-E manuscript.
- `Sources inspected`: Verified local arXiv v2 PDF, official complete full-paper HTML, metadata HTML, source-package inventory and TeX sections; arXiv metadata and DOI; Springer chapter record; author research page; live Black Lake README authorities; live Black-Lake-Data README; and three related Black Lake manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`; treated each PDF parent directory as one paper unit; derived identifiers from PDF filenames and adjacent metadata; built a used-ID index from Black Lake artifacts, automation memory, and Black-Lake-Data; selected a uniform eligible index with PowerShell `Get-Random`; then ran exact ID, DOI, normalized-title, and slug searches.
- `Inclusion criteria`: Included primary or near-primary sources that identify the paper, expose complete methods/results/limitations, establish venue/code status, define live repository rules, or provide concrete conceptual overlap in structured vision, compact deployment, and parameter efficiency.
- `Exclusion criteria`: Excluded abstract-only evidence for substantive claims, recommender widgets, unrelated DEP entries, unverified code claims, local paths, exact local timestamps, source-file redistribution, and claims not traceable to inspected evidence.
- `Analytical approach`: Mixed empirical, conceptual, comparative, implementation, product research, replication, and provenance analysis.
- `Evidence handling`: Source-reported metrics are tied to evidence IDs and table settings. Author claims, reviewer interpretation, and cross-DEP synthesis are labeled separately. Parameter/FLOP comparisons preserve trade-offs rather than converting them to an unqualified efficiency rank.
- `Uncertainty handling`: Missing code, no reruns, absent repeated seeds, mixed training stacks, no device evidence, AFFNet code-inspection dependence, and possible undiscovered code remain visible.
- `Extraction process`: A 12-page PDF was extracted with pypdf and cross-checked against official full-paper HTML and TeX/source inventory. Tables, captions, method sections, conclusions, and references were inspected. No figure pixels were remeasured and no equation was independently proved.
- `Version control`: Primary paper pinned to arXiv:2407.12217v2; publisher record pinned by DOI. No code commit could be pinned because no official AFIDAF repository was established.
- `Cross-checking`: Table values and training details were checked between PDF text and official HTML. Publisher metadata supplied venue/pages/date; author-side context supplied a second publication locator.
- `Safety handling`: Non-sensitive research. Implementation concepts use local/synthetic evaluation and do not claim production readiness.
- `Reviewer stance`: Skeptical paper review, DEP-ready preservation, resource-accounting critique, and bounded implementation planning.
- `Random selection methodology`: `rg --files` found 75,776 PDFs and 75,776 unique parent-directory units. The dedup index observed 541 distinct used arXiv IDs and excluded 119 units, leaving 75,657 eligible units. `Get-Random` selected zero-based eligible index 45,105: arXiv:2407.12217. This was the first completed draw.
- `Deduplication and reselection validation`: Scanned Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data `.lake-data`/`.reports`. Exact-ID, DOI, normalized-title, and `AFIDAF` slug searches found no prior artifact. The 24-hour date-only cutoff was 2026-07-14. Duplicate rejections and reselections were zero.
- `Source-integrity methodology`: Initial state was `partial`: a valid PDF was present but full-paper HTML and companion records were missing. Review paused. A bounded direct-HTTP repair preserved the PDF and collected official HTML, metadata, and source archive, then refreshed the local README, provenance JSON, CSV summary, and verification JSON. The final gate verified PDF size/header/EOF, HTML size/body/document/headings/structure, source archive listing, and zero partial files.

## Scope, Constraints, and Assumptions

- `Scope`: AFIDAF and HAFIDAF architecture, reported classification/detection/segmentation evidence, limitations, reproducibility, deployment relevance, random selection provenance, source integrity, and synthesis with three related DEP entries.
- `Temporal boundary`: arXiv v2 revised 2024-09-25; publisher chapter first online 2025-01-22; public context inspected through the date-only 2026-07-15 marker.
- `Evidence limits`: No code or experiment was run; no dataset, checkpoint, profiler output, hardware trace, or raw prediction was inspected; no official AFIDAF repository was established; no statistical uncertainty is reported in the source.
- `Assumptions`: The verified local PDF/HTML/source bundle corresponds to arXiv v2; extracted table text accurately reflects the rendered tables; related DEP manuscripts accurately preserve their cited evidence.
- `Constraints`: Public artifacts must not expose local paths, home names, machine identifiers, exact execution timestamps, local timezone labels, source bytes, or private repair records. Source redistribution is not authorized.
- `Out of scope`: Reimplementing AFIDAF, rerunning ImageNet/COCO/VOC, auditing AFFNet code directly, measuring mobile devices, proving Fourier uncertainty claims, or certifying a production vision system.
- `Intended use`: DEP deposition, research review, reproduction planning, backbone evaluation design, and product/MVP ideation.
- `Audience`: Computer-vision researchers, ML-systems engineers, edge-AI developers, benchmark maintainers, and technical reviewers.
- `Depth target`: Full manuscript report and implementation-oriented critique.
- `Reproducibility boundary`: A reader can reconstruct a study plan from public sources, but cannot reproduce results from this artifact without code, configurations, data, compute, and implementation choices not fully exposed.
- `Operational boundary`: Product ideas are evaluation and research tools, not autonomous surveillance or safety-critical decision systems.
- `Data sensitivity`: Public scholarly sources and derived repository artifacts only.

## Observations

- `Observed pattern`: AFIDAF's strongest gains appear on dense tasks, consistent with the diagnosis that a channelwise Fourier mask underuses spatial detail.
- `Observed trade-off`: AFIDAF improves accuracy but increases parameters relative to AFFNet; it is an attention alternative, not a direct compression of its baseline.
- `Observed trade-off`: HAFIDAF sharply reduces parameters versus Swin-T, but ImageNet FLOPs barely change and accuracy declines.
- `Technical implication`: FFT complexity alone cannot predict device efficiency; kernel support, complex layout, memory traffic, padding, synchronization, and batch size matter.
- `Evidence-quality implication`: Tables are internally usable, but absence of seeds, intervals, code, and matched device tests prevents strong generalization or deployment claims.
- `Cross-source pattern`: SSP, HSD, Physical Data AI, and AFIDAF all improve compactness by assigning capacity to explicit structure, and all require a visible domain-fit boundary.
- `Open question`: Does image-first then Fourier mixing matter, or would reversed/parallel order match the result under equal budgets?
- `Reviewer hypothesis`: Dataset spectral/locality statistics may predict when AFIDAF improves over pure spatial or pure Fourier mixers.

## Considerations

An implementation should distinguish storage compactness, arithmetic count, and measured deployment cost. Parameters affect model storage and sometimes memory bandwidth. FLOPs approximate arithmetic but ignore FFT library quality and data movement. Latency and energy depend on the target device. Training cost is separate again: the source uses eight A6000 GPUs for 300 ImageNet epochs. A credible “edge efficient” claim needs all four layers of evidence.

Benchmark fairness is another concern. AFIDAF, RepViT, EfficientViT, AFFNet, and other table entries may differ in augmentation, optimization, distillation, resolution, and code quality. The controlled AFFNet/IDAF/AFIDAF ablation is more probative than the full leaderboard. Future work should run all mixer variants inside one harness.

Fourier operations introduce operational details absent from parameter counts: real-to-complex transforms, conjugate symmetry, padding, numerical precision, export support, and accelerator scheduling. Some mobile runtimes may lack optimized FFT or complex kernels. An AFIDAF deployment should provide a convolution-only fallback and compare both at equal quality.

The paper does not present safety-sensitive applications, but any downstream camera deployment inherits privacy, fairness, reliability, and misuse risks. The MVP below processes public/synthetic benchmark metrics rather than raw personal imagery and does not automate consequential decisions.

## Strengths

- The paper starts from a concrete implementation-level limitation rather than proposing an arbitrary hybrid.
- The AFIDAF/IDAF/AFFNet trio gives a useful first ablation of Fourier-only, image-only, and alternating designs.
- Evaluation spans classification, object detection, and semantic segmentation rather than relying on ImageNet alone.
- HAFIDAF extends the mechanism to a recognizable hierarchical backbone and exposes parameter/accuracy trade-offs.
- The mechanism is conceptually legible: local/high-frequency image filtering and global/non-local Fourier mixing have distinct roles.
- The model family stays in genuinely small parameter ranges for AFIDAF and AFIDAF-T.
- The complete paper, HTML, and source package are publicly locatable and internally consistent enough for a detailed review.

## Weaknesses

- No official AFIDAF code repository, configurations, checkpoints, or environment pins were established.
- No repeated seeds, uncertainty intervals, or statistical tests are reported.
- The paper lacks latency, throughput, memory, energy, thermal, and real-device measurements.
- AFIDAF itself adds parameters over AFFNet; its “efficient” claim is primarily about avoiding attention, not compressing the AFF baseline.
- HAFIDAF's ImageNet FLOPs are almost equal to Swin-T despite 47% fewer parameters.
- The ablation does not isolate group shuffle, dilation, kernel decomposition, stage placement, or alternation order.
- Mixed model families and training recipes limit leaderboard interpretation.
- Training compute is substantial for a lightweight-inference paper and is not included in the efficiency narrative.
- The paper has no dedicated limitations, robustness, ethics, or failure-case section.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code, configs, checkpoints, and hashes | Reproducibility | Block details and training recipes are not fully recoverable from prose | Independent reruns and implementation audit | Maintenance and dependency burden | Clean-room reproduction of Tables 1-6 |
| Matched mixer benchmark | Causal evidence | Full leaderboard mixes training stacks | Isolates operator value | Expensive multi-task training | AFF, IDAF, AFIDAF, reversed order, parallel fusion under one recipe |
| Component ablations | Architecture | Alternation gain may include shuffle/dilation/kernel effects | Identifies causal components | Large experiment matrix | Remove one component at a time with repeated seeds |
| Device profiling | Systems evidence | Parameters/FLOPs do not establish latency or energy | Honest edge Pareto frontier | Hardware access and kernel variance | CPU, mobile GPU, NPU, embedded GPU profiling with latency tails |
| Training-cost ledger | Sustainability and economics | Eight-GPU 300-epoch training is material | Separates training and inference efficiency | Instrumentation overhead | GPU-hours, energy, peak memory, and carbon-estimate reporting |
| Robustness suite | Generalization | Frequency/spatial split may react differently to corruptions | Reveals boundary conditions | Additional datasets and tuning | ImageNet-C, resolution shift, blur, noise, compression, occlusion |
| Spectral diagnostics | Mechanistic evidence | Local/high versus global/low role is asserted more than measured | Tests the proposed mechanism | Analysis complexity | Feature spectra, effective receptive fields, frequency interventions |
| Regularized/local Fourier mask | Model design | Source identifies localization and kernel size as open problems | Lower cost and clearer selectivity | May reduce global context | Frequency support constraints and Pareto comparison |

## Potential Implementations

### 1. Dual-Domain Backbone Workbench

- `User`: Computer-vision researcher comparing attention and attention-free mixers.
- `Goal`: Run AFF, IDAF, AFIDAF, reversed-order, and parallel variants under one training/evaluation contract.
- `Core mechanism`: A registry swaps only the mixer while keeping backbone width, heads, optimizer, augmentation, resolution, and seeds fixed.
- `Required inputs`: Public benchmark configs, mixer implementations, hardware profile, seed list, measurement protocol.
- `Outputs`: Accuracy-resource Pareto tables, feature-spectrum diagnostics, ablation report, reproducibility manifest.
- `Risk controls`: Public/synthetic data only; explicit non-production label; no hidden recipe changes; source/license ledger.
- `Evaluation`: Repeated seeds on classification and a compact downstream detection/segmentation subset.

### 2. Edge Vision Pareto Evaluator

- `User`: ML-systems engineer choosing a backbone for constrained hardware.
- `Goal`: Determine whether parameter reductions translate to actual device improvements.
- `Core mechanism`: Export candidate backbones, run fixed image batches, capture warm/cold latency, tail latency, peak memory, energy, accuracy, and fallback behavior.
- `Required inputs`: Exported models, device adapters, public images, calibration sets, power/telemetry access.
- `Outputs`: Device-specific Pareto frontier and unsupported-operator report.
- `Risk controls`: No private imagery; local-only telemetry; model/input hashes; thermal-state checks; fail closed when FFT support differs.
- `Evaluation`: Compare attention, convolution, AFF, and AFIDAF-style models across at least three device classes.

### 3. Structure-Fit Experiment Recommender

- `User`: Research lead planning compact-model experiments.
- `Goal`: Estimate whether local, global, spectral, or task-specific structure deserves the first ablation budget.
- `Core mechanism`: Compute dataset locality, spectrum, resolution, object-scale, and label-geometry summaries, then map them to transparent experiment templates.
- `Required inputs`: De-identified/public dataset samples and task metadata.
- `Outputs`: Ranked experiment plan with uncertainty, required controls, and stop conditions.
- `Risk controls`: No automatic architecture selection for consequential use; no raw-image export; recommendation provenance visible.
- `Evaluation`: Retrospective prediction of which mixer wins across public benchmark families, followed by prospective tests.

### 4. Compact Vision Evidence Card

- `User`: Reviewer assessing a “lightweight” computer-vision claim.
- `Goal`: Prevent parameter count from substituting for complete deployment evidence.
- `Core mechanism`: Validate a schema requiring accuracy, seeds, parameters, FLOPs, latency, memory, energy, training cost, robustness, and code/artifact status.
- `Required inputs`: Result tables, profiler outputs, manifests, environment pins, source URLs.
- `Outputs`: Markdown/JSON evidence card with missing-evidence blockers and Pareto plots.
- `Risk controls`: Claims remain reviewer-approved; unverifiable values stay marked; no benchmark scraping without license review.
- `Evaluation`: Golden fixtures for complete, inconsistent, and selectively reported studies.

## Three Ways to Exercise This Research

1. **Controlled mixer ablation:** Objective—test whether alternation adds value beyond its component filters. Inputs—a public small-scale vision dataset, matched backbone, AFF/IDAF/AFIDAF/reversed/parallel mixers, three seeds, and a fixed optimizer. Steps—train each variant under equal parameter/FLOP targets, record accuracy and feature spectra, then run paired comparisons. Output—a causal ablation table. Success criterion—alternation improves the matched alternatives with uncertainty reported. Stop condition—implementations cannot be budget-matched or recipe drift is detected.
2. **Device-efficiency audit:** Objective—test whether HAFIDAF-like parameter compression improves deployment. Inputs—exported attention and dual-domain backbones, public evaluation images, at least one CPU and one accelerator, power and memory telemetry. Steps—validate numerical parity, warm devices, measure latency distributions, peak memory, energy, and accuracy, then identify unsupported FFT/complex operations. Output—a device-specific Pareto report. Success criterion—claimed improvement survives warm/cold and tail-latency checks without accuracy mismatch. Stop condition—operator fallback changes model semantics or telemetry cannot be trusted.
3. **Dense-task transfer probe:** Objective—test the hypothesis that explicit spatial filtering helps dense prediction more than classification. Inputs—a matched pretrained mixer set, a compact detection dataset, a compact segmentation dataset, and frozen/fine-tuned protocols. Steps—measure classification, localization, boundary accuracy, object-scale slices, and corruption slices. Output—a task-by-mixer transfer matrix. Success criterion—spatial-plus-Fourier gains concentrate in localization/boundary metrics and reproduce across seeds. Stop condition—head or pretraining differences dominate the backbone comparison.

## Example MVP Product

- `Product name`: Compact Vision Evidence Card.
- `Target user`: Computer-vision researcher, edge-ML engineer, or technical reviewer.
- `Problem`: “Lightweight” papers often report only parameters or FLOPs, making attention, convolution, Fourier, and hybrid backbones difficult to compare on actual devices.
- `Core workflow`: Import a versioned result bundle; validate required fields; reconcile model and dataset hashes; compare accuracy, parameters, FLOPs, latency, memory, energy, training cost, robustness, and seed uncertainty; generate a public-safe Markdown/JSON card; require human review before any deployment claim.
- `Data requirements`: Aggregate metrics, public benchmark identifiers, model/config hashes, device/software version, seed-level results, profiler traces without private inputs, source URLs, and license notes.
- `Architecture`: Local CLI and static report generator; schema validator; result normalizer; Pareto calculator; provenance ledger; optional plotting module. No remote upload is required.
- `Success metrics`: Zero silent missing fields; deterministic report hash; device and recipe versions present; seed uncertainty reported; Pareto dominance calculated correctly; unsupported claims flagged; reviewer decision recorded.
- `Risk controls`: Local-only default, no raw image ingestion, public/synthetic fixtures, no automated production approval, immutable provenance, explicit uncertainty and missing-evidence states.
- `Limitations`: The MVP audits supplied evidence; it cannot prove training fairness, detect fabricated metrics without raw artifacts, or establish safety for a deployment domain.
- `MVP boundary`: No model training, no camera integration, no personal-image processing, no autonomous architecture selection, and no production certification.
- `Deployment model`: Local Python CLI or notebook producing Markdown and JSON.
- `Evaluation plan`: Unit tests for schema and Pareto calculations; golden fixtures for Tables 1-6; synthetic missing-evidence cases; cross-device trace import; reviewer usability test.
- `Failure modes`: Incomparable training recipes, mislabeled units, profiler warm-up errors, hidden operator fallbacks, missing seeds, inconsistent hashes, and selective result submission.
- `Maintenance plan`: Version the schema, benchmark taxonomy, metric definitions, and device adapters; add migration tests; preserve source URLs and report hashes.

Illustrative bounded interface:

```python
REQUIRED = {"accuracy", "params_m", "flops_g", "latency_ms", "memory_mb", "seeds"}

def audit_record(record):
    missing = sorted(REQUIRED.difference(record))
    return {
        "status": "needs_evidence" if missing else "review_candidate",
        "missing": missing,
        "production_approval": False,
    }
```

Dependencies are standard Python only. Failure mode: a complete schema does not make the underlying measurements true; hashes, raw traces, and human review remain necessary.

## Related Research and Reading

Exactly three Black Lake DEP entries were selected for synthesis:

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| SSP Detection - DEP-E | Related Black Lake manuscript | Adds explicit spatial partitioning to recover missing geometry, evaluates oriented detection, reports training/memory costs, and exposes dataset-specific spatial-prior failures | `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md`; primary basis https://arxiv.org/abs/2506.10601 |
| HSD FTI-FDet - DEP-E | Related Black Lake manuscript | Supplies compact visual detection, heterogeneous-path design, latency/memory/model-size reporting, edge constraints, and uneven-lighting failures | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`; primary basis https://arxiv.org/abs/2307.00701 |
| Physical Data AI - DEP-E | Related Black Lake manuscript | Supplies a second structured non-attention representation, extreme parameter efficiency, ablations, and a clear domain-fit limitation | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md`; primary basis https://arxiv.org/abs/2407.14504 |

Primary and near-primary reading:

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| AFIDAF | Primary reviewed paper | Alternating image/Fourier filters and HAFIDAF hierarchy | https://arxiv.org/abs/2407.12217; https://doi.org/10.1007/978-3-031-77392-1_2 |
| Adaptive Frequency Filters as Efficient Global Token Mixers | Direct baseline | AFFNet mechanism and baseline diagnosed by AFIDAF | ICCV 2023; cited as reference 12 in AFIDAF |
| Visual Attention Network | Image-domain method neighbor | Large-kernel approximation used by the AFIDAF image path | https://doi.org/10.1007/s41095-023-0364-2 |
| Swin Transformer | Hierarchical baseline | Backbone structure compressed by HAFIDAF | https://arxiv.org/abs/2103.14030 |
| GFNet | Fourier vision baseline | Global learned frequency filters for visual recognition | https://doi.org/10.1109/TPAMI.2023.3240462 |
| RepViT | Mobile-convolution comparator | Strong compact convolutional reference in Table 1 | https://arxiv.org/abs/2307.09283 |

Synthesis: SSP and AFIDAF both encode spatial constraints explicitly; HSD and AFIDAF both split roles across heterogeneous paths; Physical Data AI and AFIDAF both replace generic blocks with structured transforms. The shared opportunity is a structure-aware compact backbone. The shared risk is treating parameter count as proof of device efficiency or treating one benchmark family as proof of domain fit.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2407.12217 | Title, authors, dates, subject, abstract, version, DOI, license, source navigation | 2026-07-15 | Official metadata only |
| R2 | https://arxiv.org/pdf/2407.12217 | Full method, equations, figures, experimental settings, tables, conclusion | 2026-07-15 | Verified complete local copy withheld |
| R3 | https://arxiv.org/html/2407.12217 | Full public paper structure, method, tables, references | 2026-07-15 | Verified complete local copy withheld |
| R4 | https://arxiv.org/e-print/2407.12217 | TeX/source inventory and section cross-check | 2026-07-15 | Verified source archive withheld |
| R5 | https://doi.org/10.48550/arXiv.2407.12217 | Persistent arXiv identifier | 2026-07-15 | Public DOI |
| R6 | https://link.springer.com/chapter/10.1007/978-3-031-77392-1_2 | Venue, pages, first-online date, authors, affiliations, published DOI | 2026-07-15 | Official publisher record |
| R7 | https://zsivine.github.io/research/ | Author-side publication context and code check | 2026-07-15 | No AFIDAF code link established |
| R8 | `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` | Related spatial-prior, object-detection, and cost synthesis | 2026-07-15 | Existing Black Lake artifact |
| R9 | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Related compact vision, resource, and field-robustness synthesis | 2026-07-15 | Existing Black Lake artifact |
| R10 | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` | Related structured-representation and parameter-efficiency synthesis | 2026-07-15 | Existing Black Lake artifact |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | DEP, attribution, naming, stability, source-locality, and commit rules | 2026-07-15 | Live default-branch authority |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E container and publication-index rules | 2026-07-15 | Live default-branch authority |
| R13 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository layout and dedup context | 2026-07-15 | Live default-branch authority |
| R14 | https://doi.org/10.1007/s41095-023-0364-2 | Visual Attention Network and large-kernel image-domain method context | 2026-07-15 | Methodological neighbor cited by AFIDAF |
| R15 | https://arxiv.org/abs/2103.14030 | Swin Transformer hierarchy compressed by HAFIDAF | 2026-07-15 | Direct architecture baseline |
| R16 | https://doi.org/10.1109/TPAMI.2023.3240462 | GFNet frequency-domain visual-recognition context | 2026-07-15 | Fourier-method neighbor cited by AFIDAF |
| R17 | https://arxiv.org/abs/2307.09283 | RepViT compact convolutional comparator | 2026-07-15 | Table-1 methodological comparator |

## Appendix

### A. Random Selection and Eligibility Record

| Field | Value |
|---|---|
| Enumeration command | `rg --files -g "*.pdf"` |
| Candidate paper-unit rule | Unique parent directory of each PDF |
| PDF files | 75,776 |
| Candidate paper units | 75,776 |
| Used arXiv IDs observed | 541 |
| Units excluded by used ID | 119 |
| Units without a filename/path-derived modern arXiv ID | 185; retained for possible metadata-based identity in the eligible pool |
| Eligible units | 75,657 |
| Random method | PowerShell `Get-Random` uniform zero-based eligible index |
| Selected index | 45,105 |
| Selected paper | arXiv:2407.12217v2, AFIDAF |
| Duplicate keys | arXiv ID, DOI, normalized title, `AFIDAF` slug |
| Dedup scan | Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`; automation memory; Black-Lake-Data `.lake-data`, `.reports` |
| 24-hour cutoff | 2026-07-14 date-only public marker |
| Duplicate rejections | 0 |
| Reselections | 0 |

### B. Source Integrity Record

| Artifact role | Result |
|---|---|
| Initial classification | Partial: valid full PDF, missing full-paper HTML and companion records |
| Repair strategy | One bounded direct-HTTP strategy; at most two attempts per endpoint; existing PDF preserved |
| PDF | 677,737 bytes; `%PDF-` header; trailing `%%EOF`; passed |
| Full-paper HTML | Official arXiv HTML; 200,299 bytes; 43,600 body characters; document marker; 68 heading/section markers; seven structure terms; passed |
| Metadata HTML | 40,757 bytes; classified metadata-only |
| Source archive | 436,334 bytes; archive listing verified |
| Partial files | 0 |
| Final classification | Complete; mandatory review gate passed |
| Public upload | Not authorized; all source documents and integrity records withheld |

### C. Reproduction Checklist

- [ ] Establish or create a public implementation with an explicit license.
- [ ] Pin AFFNet baseline code and confirm the reported channelwise-mask dimensions.
- [ ] Pin AFIDAF block order, group counts, kernel sizes, dilation, channel widths, and stage repetition.
- [ ] Reproduce AFFNet, IDAF, and AFIDAF under one ImageNet recipe with at least three seeds.
- [ ] Add reversed-order and parallel image/Fourier variants.
- [ ] Report mean, dispersion, and paired differences.
- [ ] Reproduce SSD COCO and DeepLabv3 PASCAL VOC tables with identical heads and preprocessing.
- [ ] Reproduce HAFIDAF versus Swin-T using matched pretraining, heads, schedules, and resolutions.
- [ ] Measure wall-clock training cost, inference throughput, latency tails, peak memory, and energy.
- [ ] Profile FFT and complex-layout kernels on CPU, mobile GPU, NPU, and embedded GPU targets.
- [ ] Test corruption, compression, blur, resolution, occlusion, and object-scale slices.
- [ ] Publish configs, logs, prediction files, profiler traces, environment lockfiles, and expected hashes.

### D. Source Inventory and Public-Output Gate

- Public DEP contents are limited to `README.md` and `afidaf_vision_filters_manuscript.md`.
- No `.source/` directory exists.
- PDF, full-paper HTML, metadata HTML, TeX/source archive, extracted text, and local integrity records remain outside the repository.
- Public artifacts cite canonical arXiv, DOI, publisher, author, and repository URLs.
- No local absolute path, home directory, username, machine name, workspace root, local timezone label, or exact local execution timestamp is intentionally included.
- No source document was copied, staged, uploaded, attached, or committed.
