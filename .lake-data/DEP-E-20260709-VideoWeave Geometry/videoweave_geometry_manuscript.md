---
title: "VideoWeave - DEP-E"
generated_at: "2026-07-09"
artifact_type: "DEP research artifact"
primary_subject: "Review of VideoWeave, a latent-space geometry-video post-training framework for geometrically consistent video generation."
source_status: "URLs plus local archive metadata; source files not deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-09"
temporal_cutoff: "2026-07-09"
primary_url: "https://arxiv.org/abs/2606.14162"
stable_identifier: "arXiv:2606.14162"
confidence_summary: "Medium-high for metadata, method, reported metrics, and ablations from arXiv HTML; lower for reproducibility because code and dataset release were not found in inspected sources."
safety_scope: "Research review, evaluation planning, synthetic media provenance, and non-operational implementation ideation."
distribution_notes: "Public-safe artifact; no local paths or local execution details are published."
---

# VideoWeave - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | VideoWeave arXiv abstract | Primary paper metadata | HTML | arXiv:2606.14162v1; DOI 10.48550/arXiv.2606.14162 | https://arxiv.org/abs/2606.14162 | arXiv public page with visible license link; exact redistribution terms not used for file copying | 2026-07-09 | Inspected |
| S2 | VideoWeave arXiv HTML | Primary paper full text | HTML | arXiv:2606.14162v1 | https://arxiv.org/html/2606.14162 | Public arXiv HTML; equations and tables inspected through browser text | 2026-07-09 | Inspected |
| S3 | VideoWeave project page | Official project context | HTML | Project page | https://videoweave.github.io/ | Public project page; no code link found in inspected page text | 2026-07-09 | Inspected |
| S4 | Local archive metadata | Selection evidence | README plus PDF presence | PDF filename `2606.14162.pdf` | Local archive metadata only; no local path published | Used for selection identity only; no file deposited | 2026-07-09 | Inspected |
| S5 | Black-Lake Agent State Review | Related DEP entry | Markdown | DEP-E-20260708-Agent State Review | Delphoa/Black-Lake/.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md | Repository-relative processed artifact | 2026-07-09 | Inspected |
| S6 | Visual world-model hallucination entry | Related DEP entry | Markdown | DEP-20260628-Tech Intel 0102 | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md | Repository-relative source package artifact | 2026-07-09 | Inspected |
| S7 | HoloAgent-0 3D spatial memory entry | Related DEP entry | Markdown | DEP-20260625-Tech Intel 1446 | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260625-Tech Intel 1446/daily_research_findings_2026-06-25_1446.md | Repository-relative source package artifact | 2026-07-09 | Inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary arXiv metadata | Title, authors, submission date, DOI, abstract, project page link | Identity, bibliographic metadata, high-level contribution | High | Abstract cannot support detailed empirical claims alone |
| E2 | S2 | Primary arXiv full text | Introduction, method, dataset construction, experiments, tables, ablations, conclusion | Paper mechanism, dataset, reported results, limitations by inference | High | HTML extraction may omit figure nuance; experiments not reproduced |
| E3 | S3 | Official project page | Overview, result framing, qualitative comparison descriptions | Author/project context and public availability check | Medium | Page text did not expose code or dataset download links in inspected content |
| E4 | S4 | Local archive metadata | PDF filename and nearby README title/URL | Random-selection identity confirmation | Medium | Local PDF was not text-extracted; no local paths are published |
| E5 | S5 | Processed DEP artifact | Agent state review discussion of WorldDirector and persistent dynamic object memory | Related-entry synthesis | Medium | Prior artifact is a synthesis, not primary evidence for VideoWeave |
| E6 | S6 | Raw data DEP artifact | Visual world-model hallucination finding with coverage diagnostics | Related-entry synthesis | Medium | Prior finding is a source package summary; primary paper not re-reviewed here |
| E7 | S7 | Raw data DEP artifact | HoloAgent-0 3D spatial memory finding | Related-entry synthesis | Medium | Prior finding is a source package summary; primary paper not re-reviewed here |

## Executive Summary

VideoWeave proposes a latent-space post-training framework for improving geometric consistency in video generation. The paper's central claim is that explicit geometry guidance through decoded depth, point clouds, reconstructed 3D structures, conditions, supervision targets, or rewards can introduce upstream reconstruction errors and scaling overhead. Instead, VideoWeave adapts implicit geometry-model features into geometry latents, jointly models geometry and video latents in a shared denoising space, and distills the resulting joint score field into a compact generator. At inference, the geometry latent is discarded, so the generated video is expected to carry the distilled geometry-aware prior without running an explicit geometry pipeline.

The strongest inspected evidence is the arXiv HTML full text. It reports GeoVid-80K, a curated 80K-video dataset with paired appearance and geometry representations, plus evaluations in text-to-video and image-to-video settings. Reported T2V results show VideoWeave-T2V achieving PSNR 21.4994, SSIM 0.7082, LPIPS 0.2987, MSE 500.8694, epipolar error 7.2780, and inlier rate 0.7068. Reported I2V results show VideoWeave-I2V achieving PSNR 21.1826, SSIM 0.7275, LPIPS 0.3109, MSE 565.2975, epipolar error 5.3582, and inlier rate 0.7788. Ablations support the learnable geometry adapter, joint geometry-video modeling, and score distillation as important components.

Reviewer confidence is medium-high for describing the paper's method and reported results, because the full HTML text was inspected. Confidence is lower for reproduction and deployment conclusions because official code, model artifacts, and GeoVid-80K release files were not found in inspected sources, the local PDF was not text-extracted with available tooling, and experiments were not reproduced.

## Detailed Summary

### Problem

Large-scale video diffusion models can generate realistic-looking frames while failing to preserve stable 3D scene structure across time, viewpoint change, and camera motion. The paper frames this as a bottleneck for world-level simulation, autonomous-driving-style scene modeling, embodied AI, and long-horizon video generation. Appearance quality alone is not sufficient if the generated video has drifting geometry, implausible parallax, or inconsistent object structure.

### Prior Approach and Motivation

The paper describes explicit geometry guidance as the direct remedy: use depth maps, camera poses, point clouds, reconstructed 3D structures, or rendered geometry as conditions, supervision targets, or reward signals. The authors argue that this creates two bottlenecks. First, errors from off-the-shelf geometry estimators can propagate into the generator. Second, repeated decoding, reconstruction, rendering, or geometry extraction creates computational overhead. VideoWeave's motivation is to avoid turning decoded geometry into an inference-time dependency.

### Method

VideoWeave uses implicit features from a geometry foundation model as a training-time structural signal. A lightweight geometry adapter aligns raw geometry features with video-latent temporal, spatial, and channel dimensions. The pipeline then performs geometry-latent warm-up, joint geometry-video diffusion modeling, and joint-distribution distillation. The joint modeling stage treats adapted geometry and video latents as a coupled denoising state, while a layer-aware design predicts video velocity through the original final head and geometry velocity through an intermediate geometry head. The distillation stage transfers the joint teacher's score field into a few-step student generator.

### Dataset

The paper introduces GeoVid-80K, described as a curated dataset of 80K videos with paired appearance and implicit geometry representations. The source text says the dataset combines spatial-aware public benchmarks, licensed commercial footage, and open-access web sources, followed by filtering for visual quality, subject motion, camera motion, semantic content, and expert review. The authors state they plan to release the dataset and processing pipeline after licensing and release checks, but no release artifact was found in inspected sources.

### Experiments and Results

The inspected HTML reports both T2V and I2V experiments. T2V baselines include OmniVDiff, GeoVideo, VideoGPA, and Wan-SFT. I2V baselines include GeometryForcing, ViewCrafter, and Gen3C. The evaluation includes VBench metrics, 3D reconstruction consistency through PSNR, SSIM, LPIPS, and MSE, and epipolar consistency through epipolar error and inlier rate. The paper explicitly constructs camera-motion-focused T2V prompts and held-out RealEstate10K I2V videos to avoid inflated consistency scores from near-static videos.

The reported T2V table shows VideoWeave-T2V with the best or strongest reported geometry metrics among listed baselines: PSNR 21.4994, SSIM 0.7082, LPIPS 0.2987, MSE 500.8694, epipolar error 7.2780, and inlier rate 0.7068. The reported I2V table shows VideoWeave-I2V improving reconstruction and epipolar metrics over GeometryForcing, ViewCrafter, and Gen3C under the fixed reference image and camera trajectory setting. Ablation tables report that a learnable geometry adapter outperforms PCA projection, that removing joint modeling or joint-prior distillation degrades geometry consistency, and that intermediate-layer geometry prediction offers a favorable tradeoff.

### Conclusion

The paper's core contribution is a training-time shift: geometry becomes a latent companion inside the denoising distribution rather than an explicit decoded artifact used at inference. This makes VideoWeave conceptually relevant to Black-Lake themes around world models, persistent spatial state, embodied-agent reliability, and evaluation beyond surface-level output quality.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Explicit geometry guidance can propagate estimator/reconstruction errors and add overhead. | Author claim | E2 | The introduction and related-work sections make this argument directly; the review treats it as a motivated claim, not a universally proven result. | Medium-high |
| C2 | VideoWeave uses implicit geometry features as training-time latents and discards geometry latents at inference. | Author claim supported by method text | E2, E3 | The inspected method and project page agree on the warm-up, joint-denoising, distillation, and inference-time discard design. | High |
| C3 | GeoVid-80K provides paired appearance and geometry representations for learning 3D-aware video priors. | Author claim | E2 | Dataset construction and filtering are described, but release and licensing details were not independently verified. | Medium |
| C4 | VideoWeave improves reported T2V and I2V geometry metrics while preserving competitive visual quality. | Author empirical claim | E2 | Tables support the reported metrics; no experiments were reproduced, and raw videos were not independently inspected. | Medium-high |
| C5 | Learnable adaptation, joint modeling, and distillation are important components. | Author empirical claim from ablations | E2 | Ablation tables support this within the reported setup; external validity depends on release artifacts and reproduction. | Medium-high |
| C6 | Black-Lake should evaluate generated video/world-model artifacts with spatial consistency evidence, not only visual appeal. | Reviewer interpretation | E2, E5, E6, E7 | Reasonable synthesis across inspected paper and related entries; not stated by the authors as a Black-Lake requirement. | Medium |

## Methodology

- `Research objective`: Review one randomly selected arXiv paper source-first and deposit a schema-complete DEP-E research artifact into Black-Lake.
- `Sources inspected`: Local archive metadata for the selected paper unit, arXiv abstract metadata, arXiv HTML full text, VideoWeave project page, target repository README, related Black-Lake-Data README, and three related DEP entries.
- `Discovery strategy`: Enumerated local arXiv PDFs using `rg --files -g "*.pdf"`, treated each PDF parent directory as a paper unit, selected by PowerShell `Get-Random`, derived arXiv/title/slug markers from file and README metadata, searched Black-Lake, Black-Lake-Data context, and automation memory for duplicates, then inspected public arXiv/project sources and related entries.
- `Inclusion criteria`: Included sources that identified the selected paper, supported method/results claims, documented repository deposition rules, or provided concrete related-entry overlap around world models, geometry, spatial memory, or visual-world reliability.
- `Exclusion criteria`: Did not collect `.source/` files because redistribution was not necessary for this DEP and release/licensing boundaries for non-paper artifacts were not fully established. Did not cite unrelated DEP entries found only by broad keyword search.
- `Analytical approach`: Mixed empirical, conceptual, comparative, implementation, product-research, and replication analysis.
- `Evidence handling`: Author claims are labeled separately from reviewer interpretations. Quantitative metrics are copied from inspected arXiv HTML tables. Related entries are treated as existing repository evidence, not as authority for the selected paper's claims.
- `Uncertainty handling`: Missing code, missing dataset release artifacts, unavailable PDF text extraction, and non-reproduced experiments are recorded as limitations.
- `Extraction process`: Browser-accessible arXiv HTML and project-page text were inspected. The local PDF was identified but not text-extracted due to unavailable extraction tooling in this run.
- `Version control`: The selected paper is pinned as arXiv:2606.14162v1 where visible. Output files are pinned to DEP-E-20260709-VideoWeave Geometry.
- `Reviewer stance`: DEP-ready preservation, paper report, implementation brief, product translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: This artifact reviews VideoWeave and translates its geometry-video modeling ideas into Black-Lake research, evaluation, and MVP implications.
- `Temporal boundary`: Public sources and repository context were accessed on 2026-07-09.
- `Evidence limits`: No experiments were reproduced. No official code or dataset download was found in inspected sources. The local PDF was not text-extracted. Project-page media were not evaluated beyond visible page text.
- `Assumptions`: The arXiv HTML represents the selected paper version adequately for method and results review. Repository-relative related paths are sufficient for future reviewers to locate prior context.
- `Constraints`: Public output excludes local paths, local execution details, source archive layout, and machine-specific metadata. Synthetic media and embodied-agent implications are framed as evaluation and governance concerns, not deployment endorsement.
- `Out of scope`: Model training, dataset download, video generation, metric recomputation, raw video inspection, and any claim that VideoWeave is production-ready.
- `Intended use`: Black-Lake DEP deposition, research backlog planning, evaluation design, and safe MVP ideation.
- `Audience`: Research reviewers, ML systems engineers, embodied-AI evaluators, and agentic media-pipeline designers.
- `Reproducibility boundary`: A reviewer can trace the paper and related context through cited URLs and repository paths, but cannot reproduce VideoWeave results from this artifact alone.
- `Data sensitivity`: Public research pages and repository-relative artifact references only.

## Observations

- `Observed pattern`: Video generation papers are increasingly evaluated as world-model candidates, which forces metrics beyond visual quality.
- `Technical implication`: Geometry should be treated as a latent state and validation target, not merely a rendering byproduct.
- `Open question`: Whether geometry latents learned during post-training remain robust when scenes include dynamic objects, severe occlusion, unusual camera paths, or domains absent from GeoVid-80K.
- `Reviewer hypothesis`: A practical media-generation stack will need a geometry-consistency gate analogous to factuality gates in text generation.
- `Repository implication`: Black-Lake artifacts about generated media should preserve whether the source used explicit geometry guidance, implicit geometry latents, or no geometry-aware evaluation.

## Considerations

VideoWeave has direct relevance for synthetic media provenance, embodied-agent simulation, robotics training data, and generated-world evaluation. The paper's inference-time efficiency claim is attractive because it avoids running a geometry encoder or renderer during generation, but that also means downstream systems need independent validation signals to catch cases where the distilled prior fails.

The dataset is a central dependency. GeoVid-80K's collection from public datasets, licensed commercial footage, and open-access platforms may create useful diversity, but external reviewers need release terms, filtering code, and data documentation to assess bias, licensing, consent, and representativeness. The expert-review step improves curation quality but also needs reproducible criteria.

For product use, generated videos should not be treated as reliable simulations unless geometry, temporal identity, and scene dynamics are validated for the target domain. A generated clip can look coherent while failing as an action-planning substrate. This matters for robotics, autonomous-driving-style simulation, training-data synthesis, and any workflow that turns generated video into downstream decisions.

## Strengths

- The paper attacks a concrete weakness of video diffusion models: geometric drift under viewpoint and camera motion.
- The framework has a clean mechanism: adapt geometry features, jointly model geometry and video latents, and distill the joint prior into an inference-time generator.
- Reported metrics cover visual quality, 3D reconstruction, and epipolar consistency, reducing reliance on appearance-only evaluation.
- The same-budget Wan-SFT baseline helps separate dataset/training-budget effects from geometry-aware component effects.
- Ablations directly test projection strategy, joint modeling, distillation, geometry dimension, prediction layer, and feature-level choices.

## Weaknesses

- Code, model weights, and GeoVid-80K release artifacts were not found in inspected sources, so reproduction remains blocked.
- The artifact does not independently inspect generated videos or recompute metrics.
- Dataset licensing and release checks are unresolved in the inspected text.
- The local PDF could not be text-extracted, so the review relies on arXiv HTML for full-paper detail.
- The strongest claims are empirical but remain source-reported until independent reproduction is possible.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a full dataset card for GeoVid-80K | Dataset transparency | Dataset curation is central to the method | Clearer licensing, bias, filtering, and reuse boundaries | Legal and operational review burden | Check source categories, consent/licensing notes, filters, and splits |
| Release minimal training and evaluation scripts | Reproducibility | Reported gains require nontrivial compute and metric pipelines | Independent validation of tables and ablations | Compute cost and maintenance | Reproduce a small held-out benchmark slice |
| Add failure-case taxonomy | Evaluation | Geometry drift may persist in edge cases | Better deployment boundaries | More annotation effort | Label failures by occlusion, dynamic object, camera path, and texture |
| Add provenance metadata for generated clips | Synthetic media governance | Generated media can be mistaken for physical evidence | Safer downstream use | Extra storage and tooling | Attach model, prompt, metric, and source-card metadata |
| Compare against explicit-geometry pipelines under controlled estimator errors | Mechanism isolation | The core argument concerns avoiding propagated geometry errors | Stronger causal evidence | Need controlled perturbation setup | Vary estimator noise and compare quality/geometry metrics |

## Potential Implementations

1. `Geometry Consistency Gate`
   - `User`: ML engineer reviewing generated video outputs.
   - `Goal`: Reject or flag clips that look plausible but fail geometry checks.
   - `Core mechanism`: Run reconstruction and epipolar metrics on generated clips, then attach pass/fail status and metrics to the artifact record.
   - `Required inputs`: Generated video, camera-motion estimate or prompt class, metric thresholds, source model metadata.
   - `Outputs`: Review decision, metric table, failure notes, and source references.
   - `Risk controls`: Mark metrics as imperfect proxies, use synthetic/public videos, and require human review for high-stakes use.
   - `Evaluation`: Compare accepted clips against human spatial-coherence annotations and reconstruction failures.

2. `World-Model Evidence Card`
   - `User`: Research reviewer or embodied-AI evaluator.
   - `Goal`: Summarize whether a generated video is usable as world-model evidence.
   - `Core mechanism`: Combine visual quality, geometry, temporal identity, occlusion behavior, and provenance fields into a structured card.
   - `Required inputs`: Clip, prompt, generation settings, metric outputs, source URLs, and reviewer notes.
   - `Outputs`: Markdown/JSON evidence card with citation and limitations.
   - `Risk controls`: No claims of physical truth; distinguish simulation, illustration, and evidence roles.
   - `Evaluation`: Reviewer agreement on card fields and downstream misuse reduction.

3. `Geometry-Aware DEP Media Pipeline`
   - `User`: Black-Lake artifact automation.
   - `Goal`: Preserve generated media reviews with spatial reliability evidence.
   - `Core mechanism`: Add geometry-metric summaries and source-page links to media-related DEP entries.
   - `Required inputs`: DEP metadata, source paper/project URLs, generated media files when permitted, metrics, and attribution.
   - `Outputs`: DEP README, manuscript section, metric summary, and artifact provenance.
   - `Risk controls`: Public-safe sanitization, license checks before source-file collection, and explicit source-status labels.
   - `Evaluation`: DEP validation checks and reviewer spot checks.

## Three Ways to Exercise This Research

1. `Metric-table replication plan`: Objective: reconstruct the paper's evaluation table schema without rerunning models. Inputs: arXiv HTML tables and public metric definitions. Method: build a small CSV schema for VBench, reconstruction, and epipolar metrics. Output: reusable evaluation template. Success criterion: every paper-reported metric has a field, directionality, and caveat. Safety boundary: no generated-media deployment claims.
2. `Synthetic drift toy study`: Objective: demonstrate why appearance quality and geometry consistency differ. Inputs: a few synthetic moving-camera toy scenes or public sample videos. Method: perturb frame geometry, then compare visual inspection notes against simple correspondence or reconstruction proxies. Output: short analysis showing when visual plausibility hides drift. Success criterion: at least one failure mode is visible in metrics before narrative judgment. Safety boundary: public or synthetic clips only.
3. `Related-entry concept map`: Objective: connect VideoWeave to existing Black-Lake world-model and spatial-memory entries. Inputs: this DEP, Agent State Review, visual world-model hallucination entry, and HoloAgent-0 entry. Method: map state object, persistence mechanism, evaluation signal, and deployment risk. Output: concept matrix for future Black-Lake reviews. Success criterion: each source has one concrete follow-up question and one validation signal. Safety boundary: no robotics deployment instructions.

## Example MVP Product

- `Product name`: GeoClip Auditor
- `Target user`: ML media engineers and research reviewers.
- `Problem`: Generated videos can appear fluent while violating geometry, temporal identity, or camera-motion consistency.
- `Core workflow`: Import a generated clip and source metadata, compute or attach geometry/epipolar/reconstruction metrics, collect human spatial-coherence notes, generate a provenance-preserving audit card, and export DEP-ready Markdown.
- `Data requirements`: Generated video, prompt or conditioning source, model/version metadata, public source URLs, metric outputs, and reviewer notes. Use synthetic or authorized clips by default.
- `Architecture`: Local CLI, metric adapter layer, source-card parser, threshold policy file, Markdown/JSON exporter, and DEP attribution writer.
- `Success metrics`: Percentage of clips with complete provenance, reviewer agreement on geometry failures, false accept rate on synthetic drift cases, and DEP validation pass rate.
- `Risk controls`: No raw private video ingestion by default, no claims that generated media depicts reality, license checks before source collection, and explicit labels for simulated versus observed content.
- `Limitations`: MVP cannot prove physical validity, cannot reproduce VideoWeave training, and may fail when reconstruction metrics are unreliable.
- `MVP boundary`: Evaluation and documentation only; no autonomous deployment decisions.
- `Deployment model`: Local-only CLI or notebook with Markdown export.
- `Evaluation plan`: Smoke tests on synthetic clips, source-card validation, sanitization tests, and reviewer comparison against manual notes.
- `Failure modes`: Over-trusting metrics, missing semantic identity drift, high compute cost, reconstruction failure on stylized scenes, and incomplete source metadata.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| VideoWeave | Primary paper | Selected paper under review | https://arxiv.org/abs/2606.14162 |
| VideoWeave HTML | Primary full text | Method, dataset, experiments, ablations | https://arxiv.org/html/2606.14162 |
| VideoWeave project page | Official project context | Overview and qualitative framing | https://videoweave.github.io/ |
| GeoVideo | Related baseline | Explicit geometric regularization baseline cited/evaluated by VideoWeave | https://arxiv.org/abs/2512.03453 |
| VideoGPA | Related baseline | Geometry-prior distillation baseline cited/evaluated by VideoWeave | arXiv:2601.23286 |
| Gen3C | Related baseline | I2V/camera-control baseline cited/evaluated by VideoWeave | Cited in VideoWeave references |
| Agent State Review | Related DEP | Persistent state and WorldDirector context | Delphoa/Black-Lake/.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md |
| Visual world-model hallucination entry | Related DEP | Coverage diagnostics for visual world models | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md |
| HoloAgent-0 entry | Related DEP | 3D spatial memory for embodied agents | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260625-Tech Intel 1446/daily_research_findings_2026-06-25_1446.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2606.14162 | Metadata, abstract, DOI, project page link | 2026-07-09 | Primary arXiv page |
| R2 | https://arxiv.org/html/2606.14162 | Method, dataset, evaluation, results, ablations, conclusion | 2026-07-09 | Primary full-text HTML |
| R3 | https://doi.org/10.48550/arXiv.2606.14162 | DOI identifier | 2026-07-09 | arXiv-issued DOI |
| R4 | https://videoweave.github.io/ | Project overview and qualitative framing | 2026-07-09 | Official project page |
| R5 | Delphoa/Black-Lake/.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md | Related processed Black-Lake context | 2026-07-09 | Repository-relative path |
| R6 | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md | Related visual world-model hallucination context | 2026-07-09 | Repository-relative path |
| R7 | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260625-Tech Intel 1446/daily_research_findings_2026-06-25_1446.md | Related HoloAgent-0 3D spatial memory context | 2026-07-09 | Repository-relative path |

## Appendix

### Random Selection and Deduplication

- Candidate enumeration used `rg --files -g "*.pdf"` over the local arXiv archive.
- Each PDF parent directory was treated as one paper unit.
- Candidate count was 66,188.
- Selection used PowerShell `Get-Random` uniform index over the sorted unique paper-unit list.
- Accepted random index was 324.
- Derived markers were `2606.14162`, `VideoWeave`, `Unlocking Geometric Consistency`, `Joint Geometry-Video`, and `videoweave`.
- Black-Lake, Black-Lake-Data context, and automation memory searches found no same-paper `.logs`, `.reports`, `.lake-data/DEP-E-*`, arXiv ID, DOI, normalized title, or slug markers.
- Reselection count was 0.
- Source files collected into this DEP: none.

### Validation Checklist

- YAML `title` and H1 are identical and no more than 40 characters.
- Required manuscript headings are present.
- `## Evidence Ledger` exists and maps sources to claims.
- `## Key Claims and Evidence` separates author claims from reviewer interpretations.
- `## Three Ways to Exercise This Research` contains exactly three entries.
- `## Example MVP Product` contains all required MVP fields.
- Related entries are exactly three and include concrete conceptual overlap.
- DEP README Attribution Block is final.
- Public artifact text uses public URLs and repository-relative paths only.
