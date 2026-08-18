# Report-Mark: LALIC Linear Compression

Run date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Linear Attention Modeling for Learned Image Compression* |
| Authors | Donghui Feng; Zhengxue Cheng; Shen Wang; Ronghua Wu; Hongwei Hu; Guo Lu; Li Song |
| Identifier | arXiv:2502.05741v2; DOI: 10.48550/arXiv.2502.05741 |
| Submitted / revised | 2025-02-09 / 2025-03-22 |
| Venue status | Accepted by CVPR 2025, as stated on the canonical arXiv record |
| Subject | Computer Vision and Pattern Recognition (`cs.CV`) |
| Primary record | https://arxiv.org/abs/2502.05741 |
| Full paper | https://arxiv.org/html/2502.05741 |
| PDF | https://arxiv.org/pdf/2502.05741 |
| DOI | https://doi.org/10.48550/arXiv.2502.05741 |
| Official code | https://github.com/sjtu-medialab/RwkvCompress |
| Source state | Verified private PDF and full-paper HTML; metadata and provenance retained privately; source package unavailable; original source files withheld |

## Concise Research Notes

### Problem

Learned image compression improves rate-distortion performance but often pays for large nonlinear backbones and quadratic or high-cost global mixing. The paper asks whether a linear-attention backbone can preserve long-range spatial context and entropy-modeling quality at lower computational cost.

### Method

LALIC replaces parts of the analysis, synthesis, hyper-analysis, and hyper-synthesis transforms with Bi-RWKV blocks. Each block combines Spatial-Mix for long-range spatial interactions, Channel-Mix for cross-channel fusion, and a reparameterized depthwise Omni-Shift layer for local two-dimensional context. The entropy model, RWKV-SCCTX, combines checkerboard spatial context, channel chunks, hyperprior context, and causal RWKV channel modeling.

### Evidence and Results

The source reports training on the first 400,000 OpenImages images, batch size 8, Adam, staged learning rates, 512 × 512 fine-tuning, and a single RTX 4090. On its Kodak/CLIC/Tecnick comparison, Table 1 reports LALIC BD-rate values of -15.26%, -15.41%, and -17.63% relative to VTM-9.1, with 0.274 s encoding, 0.150 s decoding, 0.841 GB memory, 286.16 GFLOPs, and 63.24M parameters. The paper also reports an RWKV-SCCTX ablation of -3.50% relative to its Conv baseline on Kodak and a BiWKV+Shift loss of 0.5551 versus 0.5657 for AFT.

These are source-reported values, not independently reproduced results. The official `RwkvCompress` repository exposes training, evaluation, result JSON files, pretrained-model names, and an MIT license, which improves the reproduction boundary but does not establish that this run executed the code.

### Limitations and Reviewer Interpretation

The comparison mixes methods with different checkpoints, evaluation sources, hardware assumptions, and implementation maturity. The paper notes that some reference curves or checkpoints were used and that the FAT runtime discrepancy is unresolved. The appendix also warns that `thop` does not capture every matrix-multiplication, mathematical, or CUDA-specific operation, so FLOPs are a proxy rather than a complete systems-cost measure.

The paper contains an internal numerical tension: the abstract and Table 1 report three dataset-specific BD-rate values, while the conclusion states an aggregate `-14.84%` figure. The discrepancy is preserved as an evidence-quality issue rather than silently averaged away. Reviewer interpretation is that LALIC's durable contribution is a design pattern: pair a global, linear-complexity state mechanism with explicit local mixing and causal entropy context, then evaluate quality and cost together.

## Evidence and Attribution

| ID | Evidence | Supports | Limits |
|---|---|---|---|
| E1 | Official arXiv metadata and abstract | Identity, authors, version dates, subject, DOI, CVPR status, public locators | Metadata does not validate empirical results |
| E2 | Verified private PDF and full-paper HTML | Architecture, equations, training setup, tables, ablations, appendices, conclusion | Source files remain private; no independent rerun |
| E3 | Table 1 and Table 2 | Reported rate-distortion and complexity comparisons; entropy-model ablation | Single stated hardware/evaluation setting and mixed reference provenance |
| E4 | Appendix A–F | VTM anchor choice, runtime discrepancy, FLOP caveat, scaling, entropy architecture, subjective comparisons | Supplementary claims remain source-reported |
| E5 | Official `RwkvCompress` repository | Public implementation, evaluation interface, result JSONs, model names, MIT license | Code was inspected online but not executed here |
| E6 | Three related Black Lake records | Cross-DEP synthesis on state-space visual mixing, layered compression, and efficient attention alternatives | Related records are not independent validation of LALIC |

## Related DEP Entries

1. `.reports/BL-Arxiv-CMamba-Learned-Image-Compression-with-State-20260812/Report-Mark.md` — direct overlap: learned image compression with a state-space backbone; its source basis is arXiv:2502.04988 and its verified full-paper review.
2. `.lake-data/DEP-E/DEP-E-20260804-Conceptual Compression/conceptual_compression_manuscript.md` — direct overlap: learned visual compression under a bitrate constraint, with an explicit separation between structural evidence and generative texture; its source basis is arXiv:2011.04976v2 and the linked full-paper sources.
3. `.reports/BL-Arxiv-AFIDAF-Vision-Filters-20260715/Report-Mark.md` — methodological overlap: efficient visual feature mixing that combines local spatial operators with global Fourier-domain context instead of relying only on quadratic attention; its source basis is arXiv:2407.12217v2, the published DOI, and the reviewed implementation search.

## Synthesis Note

### Concept Bridge

LALIC and CMamba ask the same immediate systems question: how can a visual codec retain broad spatial context without paying the full cost of dense attention. Conceptual Compression adds a different axis by separating structural information from synthesized texture, making the retained representation semantically inspectable and editable. AFIDAF supplies a complementary mixer design in which local image-domain processing and global frequency-domain processing alternate across stages. The combined bridge is a three-part design space: stateful global context, explicit content decomposition, and local/global operator specialization. A future codec can use these as separable knobs rather than treating “attention versus convolution” as one binary choice.

### Potential Implementations

1. **Stateful codec workbench:** Build a public, offline benchmark harness that compares Bi-RWKV, CMamba-style state-space blocks, convolution, and window attention under matched parameter, FLOP, memory, and resolution budgets. Inputs are public image datasets; outputs are bitstreams, reconstructed images, BD-rate, latency, memory, and per-stage receptive-field diagnostics. Risk control is strict dataset/version pinning and no claim beyond the measured hardware.
2. **Structure-aware latent service:** Add a structure/texture side channel to a linear-attention codec so the decoder can reconstruct ordinary images while downstream tools can inspect structural maps without decoding every texture detail. Inputs are public or synthetic images; outputs are codec rate, perceptual distortion, structure fidelity, and editability. Risk control is an explicit warning that generative reconstruction is not pixel-faithful recovery.
3. **Adaptive context scheduler:** Use a low-cost local/global routing policy to select between causal RWKV context, convolutional context, and a richer attention fallback for high-entropy latent regions. Inputs are latent entropy, resolution, and a fixed compute budget; outputs are route decisions and quality/cost curves. Risk control is an abstaining fallback when calibration coverage or rate-distortion confidence is insufficient.

### Deeper Relationship Observations

1. The three related records move compression decisions from a single scalar bitrate toward a resource vector that includes representation type, context access, compute, and recoverability.
2. Global receptive field is useful only when paired with a local inductive bias or a causal decoding order; LALIC's Omni-Shift and RWKV-SCCTX, CMamba's state-space framing, and AFIDAF's alternating domains all encode this complementarity.
3. A compressed representation becomes more operationally valuable when its semantics are visible: Conceptual Compression exposes structure and texture, while the linear/state-space systems expose efficiency and context pathways that can be profiled.

### Conceptual Similarities

1. All four artifacts replace or constrain dense attention with a cheaper mechanism for propagating information over long spatial or sequential ranges.
2. All four treat compression as task-conditioned: rate-distortion, perceptual fidelity, downstream utility, and compute are evaluated together rather than as isolated reconstruction quality.
3. All four require evidence-aware comparison because parameter count or theoretical complexity alone does not establish latency, energy, or deployment readiness.

### MVP Implementations with Code Mock-Ups

1. **Matched codec scoreboard**

   ```python
   candidates = ["conv", "window", "bi_rwkv", "cmamba"]
   for model in candidates:
       result = evaluate(model, dataset="kodak", budget="matched")
       record(model, result, provenance="config-and-checkpoint-id")
   ```

2. **Structure-texture routing record**

   ```python
   latent = encode(image)
   route = {"structure": encode_structure(image), "texture": latent}
   assert route["structure"].shape[-2:] == image.shape[-2:]
   decoded = decode(route)
   score = score_codec(decoded, image, metrics=["bpp", "lpips", "structure_fidelity"])
   print(score)
   ```

3. **Bounded context scheduler**

   ```python
   def choose_context(entropy, budget):
       if entropy < 0.25:
           return "conv"
       if entropy < 0.60 and budget >= 2:
           return "bi_rwkv"
       return "attention_fallback"
   ```

### Developer Challenges

1. Reproduce all baselines with identical checkpoints, anchors, image preprocessing, entropy-coding mode, and hardware counters.
2. Separate theoretical linear scaling from real kernel, memory-traffic, compilation, and batch-throughput behavior.
3. Preserve source lineage and public-safe provenance while publishing enough configuration for an independent reviewer to rerun the comparison.

### Author Challenges

1. Resolve the aggregate BD-rate statement against the dataset-specific values and state the aggregation rule explicitly.
2. Release versioned checkpoints, exact evaluation scripts, result files, and hardware/energy measurements that cover real entropy coding.
3. Test whether the state-space and local/global mixing gains transfer to out-of-domain images, larger resolutions, and constrained edge devices.

## Validation Notes

- The local archive unit was initially partial because full-paper HTML was missing; bounded repair completed the PDF/full-HTML integrity gate.
- PDF validation passed the minimum size, `%PDF-` header, and trailing `%%EOF` checks.
- Full-paper HTML validation passed the minimum size, body-character, document-marker, heading, and paper-structure-term checks.
- Source package acquisition was unavailable; it was not required for review because the PDF and full-paper HTML were complete.
- No PDF, HTML, metadata page, source archive, extracted text, cache, local path, or `.source/` directory is included in the public artifact.
- Public output is restricted to generated Markdown and the required publication-index row; final staged scans must find no local system or execution-context leaks.

## Attribution Block

- Source URL: https://arxiv.org/abs/2502.05741
  - Applies to: source identity, authors, version history, subject, abstract, DOI, and CVPR status.
  - Notes: Canonical public metadata record.
- Source URL: https://arxiv.org/html/2502.05741
  - Applies to: method, experiments, tables, figures, appendices, and conclusion.
  - Notes: Full-paper HTML inspected online; private local copy withheld.
- Source URL: https://arxiv.org/pdf/2502.05741
  - Applies to: verified primary PDF used for private integrity and text inspection.
  - Notes: Source file withheld locally and not uploaded.
- Source URL: https://doi.org/10.48550/arXiv.2502.05741
  - Applies to: persistent paper identifier.
  - Notes: arXiv-issued DOI.
- Source URL: https://github.com/sjtu-medialab/RwkvCompress
  - Applies to: public implementation, evaluation interface, result JSONs, model names, and MIT license visibility.
  - Notes: Repository inspected online; code was not executed.
- Repository file: `.reports/BL-Arxiv-CMamba-Learned-Image-Compression-with-State-20260812/Report-Mark.md`
  - Applies to: related state-space learned-compression synthesis.
  - Notes: Repository-relative related record; its cited source is arXiv:2502.04988.
- Repository file: `.lake-data/DEP-E/DEP-E-20260804-Conceptual Compression/conceptual_compression_manuscript.md`
  - Applies to: layered structure/texture compression synthesis.
  - Notes: Repository-relative related record; its cited source is arXiv:2011.04976v2.
- Repository file: `.reports/BL-Arxiv-AFIDAF-Vision-Filters-20260715/Report-Mark.md`
  - Applies to: efficient local/global visual mixing synthesis.
  - Notes: Repository-relative related record; its cited sources include arXiv:2407.12217v2 and the published DOI.
- Private source files: `2502.05741.pdf`, `2502.05741-full.html`, and `2502.05741.abs.html`.
  - Applies to: source-integrity validation and private paper review.
  - Notes: Retained in the local archive only; no source files were committed, pushed, or sent to Slack.
