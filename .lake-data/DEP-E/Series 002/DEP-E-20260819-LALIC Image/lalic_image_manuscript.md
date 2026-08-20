---
title: "LALIC - DEP-E"
generated_at: "2026-08-19"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of LALIC, a linear-attention learned image compression architecture using Bi-RWKV transforms and RWKV-SCCTX entropy modeling."
source_status: "mixed; private verified source files withheld and public URLs preserved"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-19"
temporal_cutoff: "arXiv v2 and public repository state inspected through 2026-08-19"
primary_url: "https://arxiv.org/abs/2502.05741"
stable_identifier: "arXiv:2502.05741v2; DOI:10.48550/arXiv.2502.05741"
confidence_summary: "High for source identity, method transcription, and reported table values; medium for generalization, end-to-end efficiency, and reproducibility because no experiment was independently rerun."
safety_scope: "Non-sensitive computer-vision research with bounded, reproducibility-oriented implementation examples"
distribution_notes: "Only public Markdown and public source URLs are deposited; private PDF, HTML, metadata, source package, extracted text, and caches remain local and are withheld."
---

# LALIC - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Primary metadata | HTML | arXiv:2502.05741v2 | https://arxiv.org/abs/2502.05741 | Public locator; metadata used for identity and dates | 2026-08-19 | Inspected |
| S2 | Reviewed paper | Primary artifact | PDF and full-paper HTML | arXiv:2502.05741v2 | Private verified PDF and full-paper HTML; exact local path withheld | Source files not redistributed | 2026-08-19 | Complete and inspected |
| S3 | arXiv-issued DOI | Stable locator | DOI | 10.48550/arXiv.2502.05741 | https://doi.org/10.48550/arXiv.2502.05741 | Public identifier | 2026-08-19 | Inspected |
| S4 | Official implementation | Near-primary implementation | Git repository | RwkvCompress, public repository state | https://github.com/sjtu-medialab/RwkvCompress | Repository displays MIT license; code not executed | 2026-08-19 | Inspected online |
| S5 | CMamba related record | Related DEP evidence | Markdown | arXiv:2502.04988 context | `.reports/BL-Arxiv-CMamba-Learned-Image-Compression-with-State-20260812/Report-Mark.md` | Repository-relative context; source files withheld | 2026-08-19 | Inspected |
| S6 | Conceptual Compression related record | Related DEP evidence | Markdown | arXiv:2011.04976v2 context | `.lake-data/DEP-E/DEP-E-20260804-Conceptual Compression/conceptual_compression_manuscript.md` | Repository-relative context; source files withheld | 2026-08-19 | Inspected |
| S7 | AFIDAF related record | Related report evidence | Markdown | arXiv:2407.12217v2 context | `.reports/BL-Arxiv-AFIDAF-Vision-Filters-20260715/Report-Mark.md` | Repository-relative context; source files withheld | 2026-08-19 | Inspected |

Paper title: *Linear Attention Modeling for Learned Image Compression*. Authors are Donghui Feng, Zhengxue Cheng, Shen Wang, Ronghua Wu, Hongwei Hu, Guo Lu, and Li Song. The canonical record lists Computer Vision and Pattern Recognition, submission on 2025-02-09, revision on 2025-03-22, and acceptance by CVPR 2025. The private source unit contained a valid PDF and, after bounded repair, a verified full-paper HTML document; the source package was unavailable and was not needed for the review.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Official metadata | Title, author list, version history, subject, DOI, abstract, CVPR status, and public links | Paper identity, dates, high-level problem and contribution | High | Metadata is not empirical validation |
| E2 | S2 | Primary paper | Introduction, methods, equations, experiments, tables, figures, appendices, and conclusion | Architecture, training setup, metrics, results, limitations, and internal consistency checks | High | Source files were inspected but experiments were not rerun |
| E3 | S2, Table 1 | Primary evaluation evidence | BD-rate, encoding/decoding time, memory, FLOPs, parameter count, and VTM-9.1 comparison | Reported quality/cost tradeoff | High for transcription | Hardware and mixed checkpoint/reference provenance limit generalization |
| E4 | S2, Tables 2–5 and appendices | Primary ablation and analysis evidence | RWKV-SCCTX ablation, attention variants, VTM anchor details, FLOP caveat, scaling, and subjective results | Mechanistic interpretation and evidence limitations | High for transcription | Some measures are proxies or source-reported comparisons |
| E5 | S4 | Official implementation evidence | Repository structure, training/evaluation commands, result JSONs, model names, and MIT license visibility | Reproduction boundary and implementation relevance | Medium-high | Code and checkpoints were not executed or downloaded |
| E6 | S5 | Related DEP evidence | State-space learned-compression framing and source-grounded limitations | Direct conceptual bridge to CMamba | Medium-high | Related artifact is not independent validation here |
| E7 | S6 | Related DEP evidence | Structure/texture decomposition, perceptual bitrate tradeoffs, and domain-shift caveats | Representation-level compression bridge | Medium-high | Different codec objective and visual regime |
| E8 | S7 | Related report evidence | Alternating local image-domain and global Fourier-domain mixing, parameter/FLOP tradeoffs | Efficient visual-mixing bridge | Medium | Different task and backbone |

## Executive Summary

LALIC is a learned image-compression architecture that uses Bi-RWKV blocks in the transform path and an RWKV-based Spatial-Channel ConTeXt model for latent entropy modeling. The design combines global context propagation with linear-complexity state updates, local two-dimensional depthwise mixing, channel mixing, checkerboard spatial context, and causal channel chunks. The paper's central author claim is that this combination can approach or exceed strong learned-codec rate-distortion performance with a more moderate compute profile.

In the reported setting, LALIC reaches BD-rate values of -15.26% on Kodak, -15.41% on CLIC, and -17.63% on Tecnick relative to VTM-9.1, while Table 1 lists 0.274 s encoding, 0.150 s decoding, 0.841 GB memory, 286.16 GFLOPs, and 63.24M parameters. These are source-reported point estimates from one stated evaluation setup. Reviewer confidence is high for identity, method transcription, and table transcription, but medium for general deployment efficiency because kernel behavior, energy, repeated-seed uncertainty, and independent reproduction are not established here.

## Detailed Summary

### Problem context

Learned image compression typically uses nonlinear transforms and learned entropy models to reduce visual redundancy. Stronger context models can improve coding efficiency, but transformer-like global mixing may increase memory and computation. LALIC targets the gap between high rate-distortion quality and low-complexity deployment.

### Method and mechanism

The analysis transform maps an image to a latent `y`, while a hyper-analysis transform produces `z`. Quantized latents are entropy coded, and a synthesis transform reconstructs the image. Bi-RWKV blocks are inserted after downsampling or upsampling operations in the analysis, synthesis, hyper-analysis, and hyper-synthesis transforms.

The Spatial-Mix branch applies layer normalization, Omni-Shift, projections to receptance/key/value terms, and BiWKV attention. The Channel-Mix branch performs gated cross-channel fusion with a squared-ReLU-derived value path. Omni-Shift is a reparameterized 5 × 5 depthwise convolution that supplies local two-dimensional context while retaining a simpler inference form. The paper presents BiWKV as a linear-complexity alternative to quadratic query-key attention for long-range dependencies.

RWKV-SCCTX models latent redundancy in both spatial and channel dimensions. A checkerboard partition separates anchors and non-anchors for spatial context. Latent channels are split into five chunks with allocations `{16, 16, 32, 64, M-128}`. Previously decoded chunks feed the channel context; the combined spatial, channel, and hyperprior context predicts Gaussian mean and scale parameters for entropy coding.

### Data and training

The paper trains on the first 400,000 OpenImages images with batch size 8 and Adam. MSE and MS-SSIM objectives use separate Lagrange multiplier sets. Training runs for 40 epochs at `1e-4`, four additional epochs at `1e-5`, and four fine-tuning epochs on 512 × 512 crops. The reported experiments use an NVIDIA GeForce RTX 4090. The paper evaluates Kodak, Tecnick, and CLIC Professional Validation with PSNR, MS-SSIM, and bits per pixel.

### Results

Table 1 reports LALIC with 0.274 s encoding, 0.150 s decoding, 0.841 GB memory, 286.16 GFLOPs, 63.24M parameters, and BD-rate values of -15.26%, -15.41%, and -17.63% for Kodak, CLIC, and Tecnick. Table 2 reports an RWKV-SCCTX configuration at -3.50% BD-rate relative to its Conv baseline. Table 3 reports test R-D loss of 0.5657 for AFT, 0.5604 for AFT+Shift, and 0.5551 for BiWKV+Shift. Appendix B reports LALIC MS-SSIM BD-rate values of -51.23%, -46.97%, and -49.47% relative to VTM-9.1 across Kodak, CLIC, and Tecnick.

The official repository supplies training and evaluation commands, result JSONs, pretrained-model names, and notes about automatic BiWKV compilation. It is a meaningful reproduction aid, but repository availability alone does not prove that the source results can be reproduced on a different environment.

### Limitations

The evaluation compares methods with different checkpoints, source curves, anchors, and implementation conditions. It reports one hardware configuration and does not establish energy, power, multi-request throughput, or mobile/edge behavior. The appendix says `thop` omits some mathematical, matrix-multiplication, and CUDA-specific operations, so FLOPs do not equal full runtime cost. The FAT comparison also contains an unresolved discrepancy between a reported decoding time and the review authors' measurement.

The source contains a numerical consistency issue: the abstract and Table 1 provide three dataset-specific BD-rate values, while the conclusion states a separate aggregate `-14.84%` figure. The artifact preserves both as source claims and does not infer an aggregation rule. No independent reproduction was performed.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | LALIC uses Bi-RWKV transform blocks and an RWKV-SCCTX entropy model to combine global context, local mixing, and causal latent context. | Author claim | E2 | Directly supported by the method sections and architecture figures. | High |
| C2 | LALIC reports BD-rate improvements of -15.26%, -15.41%, and -17.63% against VTM-9.1 on Kodak, CLIC, and Tecnick. | Author-reported result | E3 | Supported as table transcription; not independently reproduced. | High for transcription |
| C3 | LALIC offers a favorable quality/compute tradeoff in the stated single-GPU comparison. | Author claim | E3, E4 | Plausible within the table, but deployment readiness requires real-kernel, energy, and repeated-run measurements. | Medium |
| C4 | The RWKV entropy model contributes beyond the transform backbone. | Author claim | E4, especially Table 2 | The ablation supports an incremental contribution, though the full component interaction is not isolated by every possible control. | Medium-high |
| C5 | The durable design principle is to separate global context propagation from local spatial inductive bias and causal entropy context. | Reviewer interpretation | E2, E4, E6, E8 | A coherent cross-source synthesis rather than a single-paper claim. | Medium-high |
| C6 | Public code availability materially improves the reproduction boundary. | Reviewer interpretation | E5 | The repository provides useful scaffolding, but no execution was performed here. | Medium-high |
| C7 | The paper's conclusion and table values require a consistency check before being used as a single headline metric. | Reviewer observation | E2, E3 | Directly motivated by the internal numerical tension. | High |

## Methodology

- `Research objective`: Preserve a source-grounded DEP-E manuscript for LALIC and synthesize it with exactly three technically overlapping Black Lake records.
- `Sources inspected`: The verified private PDF and full-paper HTML for arXiv:2502.05741v2; the official arXiv metadata record and DOI; the official `RwkvCompress` repository; and three repository-relative related records with their cited public sources.
- `Discovery strategy`: Enumerated the local archive with `rg --files -g "*.pdf"`; treated each PDF parent directory as a paper unit; selected a uniform random zero-based index; inspected local metadata; verified the canonical arXiv record online; inspected the official implementation repository; and searched Black Lake public Markdown for related entries.
- `Inclusion criteria`: A candidate needed a PDF parent unit, a unique paper identity, no prior matching ID/DOI/title/slug or recent marker, and a complete PDF/full-paper HTML pair after the mandatory integrity gate. Related entries needed concrete overlap with learned compression, visual global/local mixing, or state-space context and an inspectable repository record.
- `Exclusion criteria`: Duplicate or recently marked papers, abstract-only units, units missing a valid PDF or full-paper HTML after bounded repair, unrelated background citations, and any source file for public deposition were excluded.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, reproducibility, and safety/ethics-aware source handling.
- `Evidence handling`: Evidence IDs separate metadata, primary paper claims, table transcription, official implementation observations, related DEP context, and reviewer synthesis. Author claims are labeled as claims; interpretations and unresolved inconsistencies are labeled separately.
- `Uncertainty handling`: No result was treated as independently reproduced. Missing energy, repeated-seed, cross-device, and full-kernel evidence is preserved as a limitation. The internal BD-rate tension is reported without choosing an unsupported aggregate.
- `Extraction process`: The PDF was parsed for page-level text and tables; the full-paper HTML was inspected for sections, equations, figures, experiments, appendices, and references; the official repository README and file inventory were inspected online.
- `Version control`: The reviewed paper is arXiv v2; public related records are identified by their repository paths and cited paper versions. Public artifacts are date-marked 2026-08-19 without a local execution timestamp.
- `Claim selection`: Priority was given to the core architecture, dataset/training setup, directly tabulated quality and complexity values, ablations, source-disclosed caveats, implementation availability, and cross-source design implications.
- `Cross-checking`: Paper metadata was cross-checked against the official arXiv record; method and results were cross-checked between local PDF extraction and official full-paper HTML; code availability was checked against the official repository; related context was read from the three selected Black Lake records.
- `Safety handling`: The implementation examples are offline, bounded, public-dataset, reproducibility-oriented sketches. No private data, credentials, exploit logic, or source payloads are included.
- `Reviewer stance`: DEP-ready paper review, comparative synthesis, implementation brief, and bounded replication planning.
- `Selection validation`: The successful draw used 75,967 PDF candidates, 75,964 unique parent units, and zero-based index 51,142. One earlier helper invocation failed before producing a candidate; the same required enumeration and uniform-index method then succeeded without manual selection.
- `Deduplication validation`: `.logs`, `.reports`, `.lake-data`, and automation memory were scanned for `2502.05741`, the arXiv DOI, normalized title, and `LALIC`/title slugs. No matching file or public 24-hour marker was found; cutoff date was 2026-08-18; exclusions and reselections were zero.

## Scope, Constraints, and Assumptions

- `Scope`: Source-grounded review of LALIC's architecture, evidence, limitations, implementation relevance, and relationships to three selected Black Lake records.
- `Temporal boundary`: Paper revision v2 and public source/repository state inspected through 2026-08-19.
- `Evidence limits`: No independent code execution, no checkpoint download, no dataset redistribution, no energy or mobile-device measurement, and no independent validation of the reported BD-rate curves.
- `Assumptions`: The official arXiv v2 HTML and private verified PDF represent the same paper revision; the official repository is the implementation linked from the canonical abstract; the three related records accurately preserve their own source-grounded findings.
- `Constraints`: Public-output sanitization, source-locality, copyright and redistribution limits, hardware access, and the requirement to avoid exposing local archive paths or machine context.
- `Out of scope`: Training a codec, downloading checkpoints, reproducing benchmarks, publishing original paper files, or claiming production readiness.
- `Intended use`: DEP deposition, future reproducibility work, efficient-codec design review, and cross-paper research synthesis.
- `Audience`: Computer-vision researchers, codec engineers, systems evaluators, and reviewers planning bounded reproduction.
- `Depth target`: Full manuscript research artifact with implementation and replication implications.
- `Reproducibility boundary`: The public repository and paper provide a starting point, but exact environment, checkpoint, dataset snapshot, kernel behavior, and hardware parity remain to be established.
- `Operational boundary`: Examples remain offline and evaluation-oriented; they do not operationalize a hosted codec or claim safety-critical use.
- `Data sensitivity`: Public research metadata and public dataset references; no private images or source payloads are deposited.

## Observations

### Observed pattern

LALIC's strongest design choice is not simply replacing attention with RWKV. It layers three distinct context mechanisms: global state propagation, local depthwise spatial mixing, and causal entropy-context prediction. This decomposition makes it possible to ablate and profile the mechanisms separately.

### Technical implication

The paper's table suggests that a moderate FLOP count can coexist with a stronger rate-distortion point, but the appendix caveat about operation counters means a follow-up should report kernel time, memory traffic, energy, and actual arithmetic-coding time alongside FLOPs.

### Contradiction or tension

The source's three dataset-specific BD-rate values do not obviously reconcile with the conclusion's `-14.84%` aggregate statement. This is a small textual inconsistency, but it matters because aggregate headline metrics are often copied into downstream comparisons.

### Cross-source observation

CMamba and LALIC both use state-space-style global context for visual compression, while AFIDAF alternates image-domain and frequency-domain operators and Conceptual Compression separates structure from texture. The common pattern is specialization of representation and context rather than a single universal mixer.

### Open question

It remains unclear whether LALIC's advantage is primarily due to Bi-RWKV's global context, Omni-Shift's local inductive bias, the RWKV-SCCTX entropy model, or the interaction among them under the chosen training recipe.

## Considerations

Deployment comparisons should report actual encode/decode latency, steady-state memory, batch throughput, energy, and codec compatibility, not only parameters and `thop` FLOPs. The model also relies on a compiled BiWKV operator and on public checkpoints or retraining, which create environment and maintenance costs.

The public code repository is useful but does not remove dataset and license obligations. OpenImages access, Kodak/Tecnick/CLIC evaluation terms, pretrained-model distribution, and downstream image privacy must be reviewed before operational use. For sensitive imagery, local-only execution and retention controls are preferable.

The structure/texture bridge suggests a product tradeoff. Semantically inspectable side channels can support retrieval or editing, but generative reconstruction can hallucinate texture and should not be used as an authoritative pixel record. A source-preserving architecture should retain original evidence when exact recovery matters.

## Strengths

- The paper unifies a global linear-complexity state mechanism with explicit local spatial processing and a causal entropy context model.
- The main table reports both rate-distortion and multiple cost proxies, making the quality/complexity tradeoff inspectable.
- The ablations vary block depth, entropy-model type, and attention mechanism, which provides mechanism-level evidence rather than only a final leaderboard.
- The official repository exposes training/evaluation interfaces, result files, model names, and a visible MIT license, improving the reproduction starting point.
- The related DEP synthesis broadens the design space from one backbone to representation decomposition and alternating visual operators.

## Weaknesses

- Results were not independently reproduced, and the paper does not provide uncertainty intervals or repeated-seed summaries.
- The comparisons combine source curves, checkpoints, and implementations with different maturity and may not be fully apples-to-apples.
- `thop`-based FLOPs omit some operations, and the paper does not provide energy, power, mobile, or kernel-level profiling.
- The source's internal aggregate BD-rate statement is not transparently reconciled with its dataset-specific table values.
- The contribution of each major component is not fully isolated across all combinations, and domain-shift performance is not established.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a versioned reproduction bundle | Reproducibility | Fixes checkpoint, config, data, and environment ambiguity | Independent reruns and fairer comparisons | Maintenance burden and storage | Hash configs, checkpoints, result JSONs, and environment lock files |
| Add end-to-end systems profiling | Efficiency | FLOPs are an incomplete proxy | Better deployment decisions | Hardware and instrumentation cost | Measure latency, throughput, memory traffic, energy, and real entropy coding |
| Expand component isolation | Method attribution | Bi-RWKV, Omni-Shift, and RWKV-SCCTX interact | Clearer causal explanation | More training runs | Matched ablations with fixed seeds and cost budgets |
| Reconcile reported aggregates | Evidence quality | Headline values must be auditable | Prevents citation drift | Small authoring effort | State the aggregation formula and table/source used |
| Test domain and resolution shift | Generalization | Global context may behave differently outside benchmarks | Better transfer boundaries | Dataset and compute cost | Evaluate out-of-domain, high-resolution, and edge-device subsets |

## Potential Implementations

1. **Offline codec comparison harness** — `User`: codec researcher. `Goal`: compare context mechanisms under fixed budgets. `Core mechanism`: run convolution, window, Bi-RWKV, and CMamba-style variants with identical data and evaluation. `Required inputs`: public images, pinned configs, checkpoints, and codec metrics. `Outputs`: bitstreams, reconstructions, BD-rate, latency, memory, energy, and provenance records. `Risk controls`: public datasets only, deterministic configs, no source-file redistribution, and explicit hardware scope. `Evaluation`: repeated seeds, matched anchors, and negative controls.
2. **Structure-aware compression interface** — `User`: visual-archive or editing-tool engineer. `Goal`: preserve a cheap structural representation while synthesizing texture on demand. `Core mechanism`: route structure maps through a compact side channel and texture latents through a learned decoder. `Required inputs`: public or synthetic images and structure extractors. `Outputs`: reconstructed image, structure map, texture code, and rate-distortion report. `Risk controls`: keep authoritative originals, label generative outputs, and use local processing for sensitive images. `Evaluation`: perceptual quality, structure fidelity, edit consistency, and exact-recovery abstention.
3. **Adaptive context scheduler** — `User`: edge-inference engineer. `Goal`: spend context-compute budget where latent uncertainty is highest. `Core mechanism`: choose convolution, RWKV, or an attention fallback using calibrated latent entropy and resolution features. `Required inputs`: latent statistics, route policy, and compute budget. `Outputs`: route decisions, quality/cost curves, and fallback counts. `Risk controls`: calibrated thresholds, deterministic fallback, route logging without image retention, and no deployment claim outside the measured envelope. `Evaluation`: held-out resolutions, shift tests, and resource-vector reporting.

## Three Ways to Exercise This Research

1. **Paper-to-table audit**: use the public paper HTML and repository result files to transcribe Table 1 and Table 2 into a structured ledger; success means every copied value has a paper/table locator and no aggregate is inferred; stop if checkpoint or anchor provenance is unclear.
2. **Synthetic mixer ablation**: build a toy image-like tensor benchmark comparing local depthwise convolution, window attention, and a recurrent linear-context surrogate; success means the same input/compute budget produces reproducible receptive-field and runtime traces; stop before treating toy results as codec evidence.
3. **Public-code smoke test**: in an authorized isolated environment, follow the repository's documented evaluation interface on a permitted public image subset; success means the operator compiles and produces a machine-readable result with configuration provenance; stop on missing checkpoint/license/data conditions and report the gap.

## Example MVP Product

- `Product name`: Local Codec Evidence Lab
- `Target user`: Research teams comparing learned image codecs for constrained inference.
- `Problem`: Rate-distortion tables alone do not reveal whether a codec will meet a device's memory, latency, energy, and exact-recovery requirements.
- `Core workflow`: ingest pinned public images and configs, run selected codec variants, collect bitstreams and reconstructions, compute rate-distortion and systems metrics, and publish an auditable comparison card.
- `Data requirements`: public benchmark images, explicit dataset licenses, codec checkpoints or reproducible training recipes, hardware metadata, and versioned metric definitions.
- `Architecture`: local Python runner, isolated codec adapters, deterministic config registry, metric worker, resource sampler, provenance ledger, and Markdown/JSON report writer.
- `Success metrics`: reproducible table values, per-run provenance completeness, BD-rate agreement within a declared tolerance, latency variance, memory peak, energy per image, and clear abstention on missing evidence.
- `Risk controls`: no source-file upload, local-only sensitive inputs, immutable configuration hashes, dataset/license checks, authoritative-original retention, and visible distinction between source-reported and reproduced values.
- `Limitations`: an MVP cannot guarantee cross-device portability, model quality outside tested domains, or lossless recovery; compiled kernels and checkpoints remain environment-specific.
- `MVP boundary`: compare a small set of public models and public image subsets; exclude large-scale retraining, hosted image processing, and safety-critical image decisions.
- `Deployment model`: local CLI or notebook with Markdown/JSON outputs.
- `Evaluation plan`: smoke tests, two repeated runs, table-level source audit, resource sampling, and reviewer sign-off on any headline comparison.
- `Failure modes`: missing checkpoints, incompatible kernels, unfair baseline settings, hidden dataset transformations, metric mismatch, and generative artifacts mistaken for source fidelity.
- `Maintenance plan`: pin repository revisions, refresh public benchmark metadata, retain result hashes, and review metric definitions whenever a codec implementation changes.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| LALIC | Primary paper | Linear-attention learned image compression with Bi-RWKV and RWKV-SCCTX | https://arxiv.org/abs/2502.05741; https://arxiv.org/html/2502.05741 |
| RwkvCompress | Official implementation | Training/evaluation interface, result JSONs, checkpoints, and operator notes | https://github.com/sjtu-medialab/RwkvCompress |
| CMamba related Black Lake record | Related DEP/report | State-space learned image compression and evidence limits | `.reports/BL-Arxiv-CMamba-Learned-Image-Compression-with-State-20260812/Report-Mark.md`; https://arxiv.org/abs/2502.04988 |
| Conceptual Compression related Black Lake record | Related DEP | Structure/texture decomposition and perceptual rate-distortion tradeoffs | `.lake-data/DEP-E/DEP-E-20260804-Conceptual Compression/conceptual_compression_manuscript.md`; https://arxiv.org/abs/2011.04976 |
| AFIDAF related Black Lake report | Related report | Alternating local image-domain and global Fourier-domain mixing | `.reports/BL-Arxiv-AFIDAF-Vision-Filters-20260715/Report-Mark.md`; https://arxiv.org/abs/2407.12217 |
| Vision-RWKV | Cited methodological neighbor | Visual RWKV lineage used by the paper | https://arxiv.org/abs/2403.02308 |
| MambaVC | Cited codec neighbor | State-space learned compression comparison | https://arxiv.org/abs/2405.15413 |
| CompressAI | Implementation context | Public learned-compression evaluation platform used as a reference in the paper | https://github.com/InterDigitalInc/CompressAI |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2502.05741 | Identity, authors, dates, subject, abstract, DOI, version, and CVPR status | 2026-08-19 | Canonical metadata; public source |
| R2 | https://arxiv.org/html/2502.05741 | Full method, equations, experiments, tables, appendices, figures, and conclusion | 2026-08-19 | Full-paper HTML inspected; local copy withheld |
| R3 | https://arxiv.org/pdf/2502.05741 | Primary PDF integrity and page-level text inspection | 2026-08-19 | Private source file withheld and not redistributed |
| R4 | https://doi.org/10.48550/arXiv.2502.05741 | Stable identifier | 2026-08-19 | arXiv-issued DOI |
| R5 | https://github.com/sjtu-medialab/RwkvCompress | Official code, commands, result JSONs, checkpoints, operator notes, and license visibility | 2026-08-19 | Online repository inspected; code not run |
| R6 | `.reports/BL-Arxiv-CMamba-Learned-Image-Compression-with-State-20260812/Report-Mark.md` | Related state-space image-compression context | 2026-08-19 | Repository-relative source; cited paper arXiv:2502.04988 |
| R7 | `.lake-data/DEP-E/DEP-E-20260804-Conceptual Compression/conceptual_compression_manuscript.md` | Related structure/texture compression context | 2026-08-19 | Repository-relative source; cited paper arXiv:2011.04976v2 |
| R8 | `.reports/BL-Arxiv-AFIDAF-Vision-Filters-20260715/Report-Mark.md` | Related efficient visual-mixing context | 2026-08-19 | Repository-relative source; cited paper arXiv:2407.12217v2 |
| R9 | `2502.05741.pdf` and `2502.05741-full.html` | Private source-integrity gate and source-first review | 2026-08-19 | Local archive filenames only; absolute paths and source bytes withheld |

## Appendix

### Selection and eligibility record

The successful random draw used `rg --files -g "*.pdf"` over the private archive, counted 75,967 PDF candidates, collapsed them to 75,964 unique PDF-parent paper units, and selected uniform zero-based index 51,142. One earlier helper invocation failed while deriving parent directories; it produced no candidate and did not cause manual selection. The corrected invocation completed the draw. The selected paper was identified from its archive metadata and PDF filename as arXiv:2502.05741.

The deduplication scan covered `.logs`, `.reports`, `.lake-data`, and automation memory. It searched for the canonical arXiv ID, DOI, normalized title, and `LALIC`/title slug. The scan found no prior artifact or recent marker. The public 24-hour cutoff was 2026-08-18; duplicate exclusions and reselections were zero.

### Source-integrity record

The initial local unit was `partial`: a valid PDF was present but full-paper HTML was missing. A bounded single-paper repair used the approved arXiv collection process. The PDF passed the minimum size, `%PDF-` header, and trailing `%%EOF` checks. The full-paper HTML passed the minimum byte count, body-character threshold after script/style removal, article/document marker, heading count, and paper-structure-term checks. Metadata, README, provenance, machine-readable summary, and verification records were updated privately. The source package was unavailable because the publisher route did not provide it through the approved broker, and no review claim depends on it.

### Public-source locality and no-upload gate

The public DEP contains only generated Markdown. The PDF, full-paper HTML, metadata HTML, source-package attempt record, extracted text, caches, and verification companions remain local. No original source file was staged, committed, pushed, attached to a pull request, or sent to Slack.
