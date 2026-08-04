---
title: "CogPortrait - DEP-E"
generated_at: "2026-08-04"
artifact_type: "DEP-E research manuscript"
primary_subject: "CogPortrait fine-grained eye-region control in portrait animation"
source_status: "Verified complete PDF and full-paper HTML; source package unavailable; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-04"
stable_identifier: "arXiv:2605.28056v1; DOI:10.48550/arXiv.2605.28056"
---

# CogPortrait - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Title | CogPortrait: Fine-Grained Eye-Region Control in Portrait Animation via Hierarchical Agent Planning |
| Authors | He Feng; Yongjia Ma; Donglin Di; Lei Fan; Tonghua Su |
| arXiv | 2605.28056v1 |
| Paper date | 2026-05-27, as printed in the paper |
| DOI | https://doi.org/10.48550/arXiv.2605.28056 |
| Abstract record | https://arxiv.org/abs/2605.28056 |
| Full-paper HTML | https://arxiv.org/html/2605.28056 |
| PDF | https://arxiv.org/pdf/2605.28056 |
| Venue context | MM '26 header is printed; acceptance/publication status was not independently verified |
| Source integrity | Initial partial archive unit repaired to verified complete PDF and full-paper HTML before review |
| Source package | Not available from the inspected e-print route |
| Public distribution | Only derived public-safe Markdown and dedup metadata are deposited; source files and caches remain local |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | https://arxiv.org/abs/2605.28056 | Canonical metadata | Title, authors, version, date context, abstract, and public locators | Source identity and scope | High | Metadata alone cannot establish detailed results |
| E2 | https://arxiv.org/html/2605.28056 | Full-paper HTML | Introduction, methodology, benchmark construction, experiments, ablations, user-study statement, conclusion, and references | Method and reported evidence | High for transcription | Results were not reproduced; HTML conversion may omit visual nuance |
| E3 | https://arxiv.org/pdf/2605.28056 | Primary PDF | Tables 1-4, figures, training settings, metric values, paper header, and printed claims | Quantitative reporting and visual/source cross-check | High for paper content | Extracted text contains some encoding noise |
| E4 | https://doi.org/10.48550/arXiv.2605.28056 | DOI locator | Persistent identifier for the arXiv work | Stable identity | High | ArXiv-issued DOI, not a separate publisher record |
| E5 | Private extraction record | Processing evidence | Complete-source verification, cache status, extractor fallback, and source-text absence | Provenance and review boundary | High | Private record is not redistributed or locatable in this artifact |
| E6 | Hallo4 Portrait Motion DEP | Related repository artifact | Preference alignment, temporal motion conditioning, metric tradeoffs, and synthetic-media safety | Related research bridge | Medium | Different paper and implementation state |
| E7 | MoGIC Boosting Motion DEP | Related repository artifact | Intention-to-motion planning, intermediate structure, and evaluation boundaries | Planning and control bridge | Medium | Different motion domain and source evidence |
| E8 | VideoWeave Geometry DEP | Related repository artifact | Latent video conditioning, geometry consistency, multi-metric evaluation, and deployment caution | Representation and evaluation bridge | Medium | Does not validate CogPortrait's claims |

## Executive Summary

CogPortrait proposes a two-stage portrait-animation framework intended to produce fine-grained eye-region and head-motion behavior from high-level labels. The paper frames a control tradeoff: labels and coarse prompts are easy to provide but lack detail, while Action Units or driving videos offer detail at a higher input cost.

Stage 1 uses a planning agent to decompose a label into temporal events, a composition agent to retrieve and stitch behavior prototypes, and a critic to check semantic and physiological constraints. The resulting 17-channel AU, gaze, and head-pose controls are projected into 62 facial keypoints. Stage 2 feeds those keypoints, a reference portrait, audio, and text into a Wan2.2-derived DiT video generator. Dynamic classifier-free guidance emphasizes eye-region conditioning while reducing global color drift, and KTO refinement targets long-tail cases such as asymmetric eyebrow motion and large-angle head turns.

The paper reports strong source-level results. On HDTF, the full system reports FID 16.68, FVD 32.90, LPIPS 0.0633, Sync-C 7.15, ID-Sim 0.9214, and Eye-LMD 0.0107. On the EMH benchmark, it reports BRISQUE 34.20, DSL-FIQA 0.5184, ID-Sim 0.9129, Eye-LMD 0.0145, AU-F1 0.9017, and AU-Temp 0.7397. These values are point estimates from one paper; this review did not run code, generate videos, recompute metrics, or reproduce the user study.

The strongest reusable idea is the separation of semantic planning, behavior retrieval, constraint checking, and rendering. The strongest unresolved questions concern benchmark licensing and consent, user-study protocol, official implementation availability, repeated-seed uncertainty, and whether the gains persist when each stage is evaluated under matched compute and controlled ablations.

## Detailed Summary

### Problem Context

Portrait animation increasingly combines a reference face with audio, text, emotion labels, facial keypoints, or motion videos. The paper argues that existing high-level controls usually operate at coarse semantic granularity, while motion-level controls require the user to supply or construct detailed signals. Fine-grained gaze, eyelid, blink, eyebrow, and head coordination is especially difficult for beyond-emotion states such as cognitive effort and drowsiness.

The practical problem is therefore an interface problem as well as a generation problem: how can a user express a temporally structured facial behavior without manually drawing every motion trajectory? CogPortrait answers with an intermediate representation grounded in Action Units, gaze, head pose, retrieved real-behavior prototypes, and explicit checks.

### Method and Architecture

The first-stage prototype library represents each behavior with a category label, 17 control channels, and frame-wise facial keypoints. The controls include 10 AU channels for eyebrow, eyelid, and blink behavior, four gaze channels, and three head-pose channels. Residual motion is separated into non-gaze and gaze components, then organized for retrieval.

The planning agent maps a target label, duration, and optional instruction into staged events with timestamps, frame spans, semantics, and local constraints. The composition agent converts each event into channel requirements, retrieves prototypes using a weighted matching distance, trims or rescales them, and stitches them across the event sequence. The critic checks event order, instruction satisfaction, blink duration, inter-blink intervals, blink asymmetry, AU co-activation, gaze main sequence, and gaze-head coordination. It can approve the sequence or send revisions back to composition or planning.

The mapping layer converts refined AU activations into FLAME-mesh deformation, eyelid and eyebrow keypoints, gaze adjustments for pupils and irises, and yaw/pitch/roll transformations. Mouth motion is not controlled explicitly in Stage 1; it is produced in Stage 2 with audio conditioning.

Stage 2 aligns the keypoint sequence to the reference portrait using thin-plate-spline warping, renders a pose sequence, encodes it with a VAE and 3D convolutional pose adapter, and injects its features into a DiT-based flow-matching generator. Reference tokens, multilingual text embeddings, and multilingual wav2vec audio embeddings condition the denoising process.

### Dynamic Guidance and KTO

The temporal guidance schedule uses a high CFG level early in denoising, transitions linearly, and then settles at a lower level. The motivation is to establish global appearance early and reduce color shift later. A spatial Gaussian weighting map increases guidance around the eye region and keeps the background near a base weight.

KTO refinement uses desirable real boundary-case videos and undesirable current-model outputs. The paper targets asymmetric eyebrows, rapid irregular gaze, rapid blinking, and large-angle head motion. Its desirability signal is based on control accuracy and identity consistency. The source text reports that KTO improves boundary-case Eye-LMD from 0.0377 to 0.0311 and ID-Sim from 0.9089 to 0.9394.

### EMH Benchmark

The EMH benchmark contains six core emotions from MEAD and six beyond-emotion categories. The core categories are sadness, fear, disgust, contempt, anger, and surprise. The beyond-emotion categories are laughter, cognitive effort, low-arousal negative state, social engagement, evasive response, and drowsiness. The paper reports category-level video and actor counts and pairs cases with text prompts and manual eye-region dynamic annotations.

For example, a drowsiness clip is annotated with droopy eyelids, a prolonged blink, and a drowsy head nod across successive frame ranges. The benchmark releases frame indices and prompt annotations, while access to original videos remains subject to source-dataset licenses and usage terms. AU-F1 measures activation correctness; AU-Temp uses dynamic time warping to assess temporal trajectory fidelity.

### Experimental Setup

The paper reports training the DiT backbone from Wan2.2 on eight NVIDIA H200 GPUs. Pose-encoder fine-tuning used AdamW at `1e-5` for seven GPU days. KTO refinement used learning rate `5e-8`, beta `625`, equal KTO and flow-matching loss weights, and two GPU days. Inference used 40 denoising steps with the printed temporal and spatial guidance settings. The CoT agents used Gemini 3.0 in JSON mode.

Training used TalkVid and DH-FaceVid-1K. KTO preference data included 400 large-irregular-head-motion clips and three self-collected categories, each with 400 clips and a 350/50 train/test split, from 15 volunteers. The paper states that training and test identities were non-overlapping. Preprocessing converted video to 25 FPS, audio to 16 kHz, and face regions to 512 by 512.

The HDTF comparison included eight representative baselines across audio-driven, label-driven, and video-driven inputs. The EMH comparison included BRISQUE, DSL-FIQA, ID-Sim, Eye-LMD, AU-F1, and AU-Temp. The paper states that baselines used official implementations and pretrained checkpoints, but this review did not independently inspect or run those implementations.

### Reported Results

On HDTF, CogPortrait's printed row is FID 16.68, FVD 32.90, LPIPS 0.0633, Sync-C 7.15, ID-Sim 0.9214, and Eye-LMD 0.0107. The paper highlights a 38% relative Eye-LMD reduction against the second-best Follow-Your-Emoji row at 0.0173. Sonic has a higher Sync-C of 7.43, so CogPortrait is not best on every HDTF metric.

On EMH, the full pipeline reports BRISQUE 34.20, DSL-FIQA 0.5184, ID-Sim 0.9129, Eye-LMD 0.0145, AU-F1 0.9017, and AU-Temp 0.7397. With ground-truth keypoints, the paper reports AU-F1 0.9303 and AU-Temp 0.7830; with its inverted prototype construction, it reports 0.9192 and 0.7791. HunyuanPortrait reports 0.9145 and 0.7475 for the two AU metrics.

The Stage 1 ablation moves from direct label-to-keypoints AU-Temp 0.5676 to rule-based retrieval 0.5899, Agent 1 only 0.7112, Agent 1 plus Agent 2 without the critic 0.7135, and the full pipeline 0.7397. The CFG ablation reports AU-F1 0.8823 with fixed CFG, 0.8835 with temporal reweighting only, 0.8903 with spatial reweighting only, and 0.9017 for the full pipeline. The boundary-case table reports a KTO improvement over the no-KTO variant on Eye-LMD, AU-F1, AU-Temp, and ID-Sim.

### User Study and Limitations

The paper states that a user study compares CogPortrait with FLOAT, Hallo3, and ACTalker on motion realism, motion diversity, identity consistency, and overall preference, with details in the supplement. The inspected main text does not expose participant counts, assignment design, randomization, blinding, annotator training, agreement, uncertainty, or statistical testing.

The source also leaves important implementation and governance questions open. No official code repository or checkpoint was identified in the inspected paper sources. The EMH source videos remain governed by their original licenses and terms. Portrait and voice synthesis can create impersonation, privacy, and consent risks, so a safe implementation must use synthetic or explicitly authorized inputs, preserve provenance, and abstain when rights or evidence are incomplete.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Hierarchical planning, prototype retrieval, and a critic can compile high-level labels into fine-grained facial controls. | Author method claim | E2, E3 | The mechanism is described in detail and is internally coherent; independent implementation evidence is absent. | Medium-high |
| C2 | The full pipeline improves reported eye-region and temporal control over the paper's baselines and ablations. | Author empirical claim | E2, E3 | Supported by printed tables within the reported setting; no reproduction, seeds, or uncertainty. | Medium-high for reporting |
| C3 | Dynamic CFG and eye-region weighting improve control while reducing global color drift. | Author ablation claim | E2, E3 | Supported by the paper's ablation table and qualitative discussion; causal attribution remains limited to the tested variants. | Medium |
| C4 | KTO improves long-tail control and identity consistency. | Author empirical claim | E2, E3 | Supported on the boundary-case subset in Table 4; sample construction and independent audit are not available. | Medium |
| C5 | CogPortrait achieves broadly superior portrait-animation performance. | Author aggregate interpretation | E2, E3 | Too broad without qualification: it leads several metrics but not every quality or synchronization column. | Medium |
| C6 | The EMH benchmark is reusable for independent research. | Reviewer interpretation | E2 | Potentially valuable, but reuse depends on release status, licensing, annotations, splits, and evaluation code. | Low-medium |
| C7 | The method is ready for production portrait animation. | Unsupported implication | No inspected evidence | Rejected; deployment would require consent controls, robust evaluation, artifact release, and safety review. | High rejection confidence |

## Methodology

- `Research objective`: Produce a schema-complete, source-grounded DEP-E manuscript from one eligible random paper and preserve method, evidence, uncertainty, implementation implications, and safe follow-up paths.
- `Sources inspected`: Local verified PDF and full-paper HTML, local metadata/provenance records, central extraction cache summaries and text outputs, the public arXiv abstract/HTML/PDF locators, the arXiv-issued DOI locator, live Black-Lake and Black-Lake-Data READMEs, and exactly three live related DEP manuscripts.
- `Discovery strategy`: Used `rg --files -g "*.pdf"` against the local archive root, treated each PDF parent directory as one paper unit, collapsed 75,960 PDFs to 75,957 unique units, and used a uniform PowerShell `Get-Random` zero-based index. The selected index was 43,688.
- `Inclusion criteria`: Kept sources that established paper identity, supported method or reported results, documented source integrity or processing provenance, or provided concrete related-entry overlap in portrait animation, intention-to-motion planning, latent video conditioning, or evaluation.
- `Exclusion criteria`: Excluded source-incomplete paper units from review until repaired, prior duplicate markers, abstract-only pages as paper evidence, unsupported repository claims, source-file redistribution, and production-readiness inferences.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication analysis.
- `Evidence handling`: Author claims, reported metrics, reviewer interpretations, source metadata, and processing evidence are labeled separately. Tables and method details were cross-checked between PDF-derived text and full-paper HTML text.
- `Uncertainty handling`: Missing source package, absent official implementation, unreproduced experiments, missing user-study details, point estimates without uncertainty, dataset licensing questions, and encoding noise are stated rather than smoothed over.
- `Random selection methodology`: The first uniform draw at index 43,688 was accepted. Dedup and reselection checks found no matching arXiv ID, DOI, normalized title, slug, prior artifact, automation-memory marker, or relevant Black-Lake-Data hit. Duplicate exclusions 0; source-gate exclusions 0; reselections 0.
- `Source-integrity methodology`: The initial unit was partial because full-paper HTML was absent while the PDF was valid. A bounded single-paper archive repair obtained official full-paper HTML and refreshed the local README, provenance record, machine-readable summary, receipt, and verification report. Review began only after PDF header/EOF and full-paper HTML structural checks passed.
- `Cache methodology`: Required extractor preflight found `pypdf` and no `pdftotext`. Missing-only extraction against the selected paper created a central `cached` record using `pypdf` for PDF text and `html-regex` for HTML text. The source extractor reported missing because no TeX/source package was available. The extractor itself used no network backfill.
- `Reviewer stance`: Source-first paper review, skeptical critique, DEP-ready preservation, implementation translation, consent-aware synthetic-media analysis, and bounded replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: Paper identity, method, EMH benchmark, experiments, ablations, reported limitations, related DEP synthesis, safe implementation concepts, and replication needs.
- `Temporal boundary`: Public repository and paper context inspected on 2026-08-04; the paper is pinned to arXiv v1 as identified in the local source.
- `Evidence limits`: No model, checkpoint, code, dataset, video, metric implementation, user study, or training run was executed. Printed results remain author-reported.
- `Assumptions`: The verified arXiv PDF and full-paper HTML represent the same v1 paper; printed tables and captions are the authors' reported evidence.
- `Constraints`: All source files, extracted text, cache records, and private integrity details remain local. Public artifacts use public URLs and repository-relative related-entry paths only.
- `Safety and legal constraints`: Real portraits, voices, and source videos require consent, licensing, and purpose limitation. Examples are synthetic, local-only, evaluation-oriented, or explicitly authorized.
- `Out of scope`: Production deployment, identity impersonation, non-consensual media, dataset redistribution, training a model, generating portraits, and claims of independent validation.
- `Intended use`: Research review, evaluation design, source-grounded knowledge deposition, and safe MVP scoping.
- `Reproducibility boundary`: A future reviewer can locate the paper and related public artifacts, but cannot reproduce the reported results from this manuscript alone.

## Observations

- `Observed pattern`: The strongest methodological boundary is the explicit intermediate control representation between natural-language intent and video generation.
- `Observed pattern`: Prototype retrieval and physiological checks are practical ways to constrain a language model, but they move bias and coverage questions into the prototype library and rule set.
- `Technical implication`: AU-F1 and AU-Temp can test whether a planned behavior survives rendering, while ID-Sim and visual-quality measures monitor collateral damage.
- `Contradiction or tension`: The full system is strong on several reported control metrics, yet the HDTF table shows Sonic with higher Sync-C; aggregate superiority needs metric-by-metric reporting.
- `Open question`: Whether the agent-generated controls remain stable under unseen duration, accent, pose, lighting, and identity conditions.
- `Reviewer hypothesis`: A staged plan-and-render architecture may make failure diagnosis easier than an end-to-end label-to-video model, but only if intermediate controls and revisions are logged.

## Considerations

Portrait animation is dual-use synthetic media. A local evaluation tool should default to synthetic faces, synthetic audio, or explicit authorization; store provenance for prompts, model versions, input rights, and output status; and avoid presenting generated clips as evidence of a person's real behavior. A public benchmark needs source-dataset licensing, consent, demographic coverage, identity-split, and retention documentation.

Operationally, the method has a large dependency surface: MLLM agents, a behavior library, face/keypoint tooling, FLAME mapping, a DiT video backbone, audio and text encoders, KTO data, and metric implementations. This surface creates cost, latency, version-drift, and observability concerns. The review therefore recommends a plan-only validation mode that can test event timing and physiological rules without rendering a face.

## Strengths

- Separates semantic planning, retrieval/composition, constraint checking, and rendering into inspectable stages.
- Gives the control representation explicit semantics across AU, gaze, blink, eyelid, eyebrow, and head-pose channels.
- Introduces AU-level activation and temporal metrics aligned with the stated fine-grained control problem.
- Reports ablations for Stage 1 components, dynamic CFG, and KTO rather than presenting only a full-pipeline comparison.
- Preserves a source-first, public-safe path for follow-on review even though the original media and source package remain unavailable.

## Weaknesses

- No official implementation, checkpoint, full configuration, or reproducible environment was found in the inspected paper sources.
- No result was independently generated or recomputed; printed point estimates have no visible seeds, confidence intervals, or significance tests.
- The user-study protocol is deferred to the supplement and key human-evidence details are absent from the inspected main text.
- EMH depends on multiple source datasets and self-collected volunteer data, but licensing, consent, annotation agreement, and release mechanics are not fully documented in the inspected text.
- The agent prompts, prototype library, rule thresholds, and critic revision traces are not available as a public reproducibility bundle.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release an EMH data card and evaluation package | Dataset and benchmark | The benchmark is central to the paper's claim | Clearer licensing, consent, splits, annotation, and replication | Legal review and annotation maintenance | Independent evaluator recreates metric inputs and split counts |
| Publish prompt, prototype, and rule manifests | Interpretability | Stage 1 behavior depends on hidden structured assets | Auditable plan-to-control behavior and safer debugging | May expose sensitive or licensed examples | Compare plan traces and control trajectories across seeds |
| Add repeated-seed and component-isolation studies | Statistical validity | The full pipeline combines several interventions | Better attribution and uncertainty | Significant compute and evaluation cost | Matched compute, fixed data, multiple seeds, confidence intervals |
| Add consent and provenance gates to inference | Safety | Portrait and voice synthesis can cause harm | Safer authorized use and traceability | Product friction and metadata overhead | Red-team synthetic misuse cases and audit-log review |

## Potential Implementations

1. `Plan-to-controls review tool`: User: researcher or animator. Goal: inspect event timing, retrieved prototypes, AU/gaze/head-pose ranges, and critic revisions before rendering. Inputs: synthetic label, duration, optional instruction, approved prototype catalog, and rules. Outputs: structured plan, validation status, and reviewer notes. Risk controls: synthetic or authorized data, no face rendering required, and abstention for missing provenance. Evaluation: agreement between expert reviewers and rule outcomes.
2. `Consent-aware portrait-control pipeline`: User: authorized media research team. Goal: produce a portrait animation with explicit input-rights and output-provenance records. Inputs: authorized portrait, audio, text prompt, control plan, model version, and benchmark annotations. Outputs: generated clip plus provenance card and metric report. Risk controls: consent proof, access control, watermarking/metadata, non-deceptive labeling, and human review. Evaluation: benchmark metrics, failure taxonomy, and safety audit.
3. `Fine-grained motion benchmark adapter`: User: ML evaluator. Goal: compare control methods on eye-region activation, temporal trajectory, identity, synchronization, and visual quality. Inputs: public or synthetic clips, expected AU annotations, model outputs, and evaluator versions. Outputs: metric table, uncertainty summary, and abstention status. Risk controls: licensed inputs only, no person-level claims, and clear metric limitations. Evaluation: repeated seeds, split audits, reviewer agreement, and cross-method calibration.

## Three Ways to Exercise This Research

1. `Synthetic plan validation`: Objective: test event decomposition and physiological constraints without rendering real faces. Inputs: synthetic labels such as drowsiness, duration, three toy prototypes, and the paper's stated checks. Method: create staged events, run ordering and duration checks, inspect revised controls, and record failures. Output: auditable plan ledger. Success criterion: every event has a bounded time span and every revision has a stated reason. Stop condition: any missing provenance or ambiguous rule causes abstention.
2. `Metric-contract study`: Objective: show how different metrics expose different failure modes. Inputs: synthetic eye-region trajectories and controlled perturbations for gaze, blink, eyebrow asymmetry, and identity drift. Method: compute toy AU-F1, AU-Temp, Eye-LMD, and identity-proxy scores, then compare them with human review notes. Output: metric tradeoff table. Success criterion: at least one perturbation is caught by a metric that visual-quality scoring misses. Stop condition: do not make person-level or production claims.
3. `Authorized pipeline review`: Objective: evaluate the feasibility of a consent-aware portrait-control prototype. Inputs: explicitly authorized synthetic or volunteer data, a plan-only implementation, public metric definitions, and provenance fields. Method: run the plan validator, attach source/license records, test abstention, and review output labels. Output: local-only evaluation report. Success criterion: every output has a complete provenance status and a documented failure boundary. Stop condition: halt if consent, licensing, or retention status is unclear.

## Example MVP Product

- `Product name`: CogPortrait Control Ledger
- `Target user`: Research engineers and reviewers building authorized portrait-animation prototypes.
- `Problem`: High-level labels are easy to provide but do not expose whether the resulting fine-grained eye motion is plausible, interpretable, or safe to reuse.
- `Core workflow`: Accept a synthetic or authorized label and duration, generate a structured event plan, retrieve approved behavior prototypes, run physiological and instruction checks, optionally attach rendered-video metrics, and export an evidence card.
- `Data requirements`: Synthetic or authorized portrait/audio inputs, label and optional instruction, approved prototype trajectories, rule manifest, model/version metadata, public source URLs, and evaluation annotations.
- `Architecture`: Local-only planner adapter, prototype catalog, rule engine, keypoint-schema exporter, metric adapters, provenance ledger, Markdown/JSON artifact writer, and human-review surface.
- `Success metrics`: Plan validation pass rate, reviewer agreement, AU-F1/AU-Temp on synthetic fixtures, identity-proxy preservation, provenance completeness, abstention correctness, and time to diagnose a failed control.
- `Risk controls`: Local processing by default, explicit data-permission field, no private-media upload, synthetic fixtures, output labeling, provenance retention, human review, and no claims that a generated behavior is real.
- `Limitations`: The MVP does not train or run CogPortrait, cannot prove realism, cannot replace consent or legal review, and cannot establish the paper's reported performance.
- `MVP boundary`: Plan validation and evidence logging first; video generation is optional and restricted to authorized test inputs.
- `Deployment model`: Local CLI or notebook with Markdown/JSON export.
- `Evaluation plan`: Unit tests for event ordering, rule boundaries, provenance fields, metric directionality, and public-safe sanitization; synthetic perturbation tests; reviewer spot checks.
- `Failure modes`: Over-trusting a metric, incomplete prototype coverage, prompt ambiguity, rule conflicts, identity drift, dependency drift, missing consent, and misleading output labels.
- `Maintenance plan`: Version prototype catalogs and rules, re-audit source permissions, pin metric implementations, review new benchmark versions, and run periodic misuse and privacy checks.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| Hallo4 Portrait Motion | Related DEP | Preference alignment, temporal motion conditioning, portrait animation, and synthetic-media safety | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Hallo4%20Portrait%20Motion/hallo4_portrait_motion_manuscript.md |
| MoGIC Boosting Motion | Related DEP | Intention understanding, structured motion generation, and safe evaluation boundaries | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260726-MoGIC%20Boosting%20Motion/mogic_boosting_motion_manuscript.md |
| VideoWeave Geometry | Related DEP | Latent video conditioning, temporal/spatial consistency, and evaluation beyond appearance | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md |
| KTO: Model Alignment as Prospect Theory | Primary related reading cited by paper | Preference optimization with binary desirability feedback | https://arxiv.org/abs/2402.01306 |
| Wan: Open and Advanced Large-Scale Video Generative Models | Primary related reading cited by paper | Video-generation backbone context | https://arxiv.org/abs/2503.20314 |
| MEAD | Dataset paper cited by paper | Core emotion source and benchmark context | https://arxiv.org/abs/2010.16180 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2605.28056 | Metadata, title, authors, abstract, version, and public source locators | 2026-08-04 | Canonical public record |
| R2 | https://arxiv.org/html/2605.28056 | Full-paper method, EMH benchmark, experiments, ablations, user-study statement, and conclusion | 2026-08-04 | Full-paper HTML inspected; source file withheld |
| R3 | https://arxiv.org/pdf/2605.28056 | Tables, figures, training settings, paper header, and printed metrics | 2026-08-04 | Complete PDF inspected locally; not deposited |
| R4 | https://doi.org/10.48550/arXiv.2605.28056 | Persistent identifier | 2026-08-04 | ArXiv-issued DOI |
| R5 | https://arxiv.org/abs/2402.01306 | KTO concept cited by the paper | 2026-08-04 | Related reading and locator |
| R6 | https://arxiv.org/abs/2503.20314 | Wan2.2/video-generation context cited by the paper | 2026-08-04 | Related reading and locator |
| R7 | https://arxiv.org/abs/2010.16180 | MEAD dataset context cited by the paper | 2026-08-04 | Related reading and locator |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Hallo4%20Portrait%20Motion/hallo4_portrait_motion_manuscript.md | Related DEP evidence for preference-aligned portrait motion | 2026-08-04 | Live repository manuscript inspected |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260726-MoGIC%20Boosting%20Motion/mogic_boosting_motion_manuscript.md | Related DEP evidence for intention-to-motion planning | 2026-08-04 | Live repository manuscript inspected |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md | Related DEP evidence for latent video consistency and multi-metric evaluation | 2026-08-04 | Live repository manuscript inspected |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, DEP class, attribution, and public-source policy | 2026-08-04 | Live README read before writing |
| R12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository layout and source-file policy | 2026-08-04 | Live README read before writing |

## Appendix

### Random Selection and Deduplication

- Candidate enumeration used `rg --files -g "*.pdf"` against the local arXiv archive root.
- Each PDF parent directory was treated as one paper unit; nearby README and metadata files were used for identity context.
- The inventory contained 75,960 PDFs and 75,957 unique parent-paper units.
- PowerShell `Get-Random` selected uniform zero-based index 43,688 from the sorted unit list.
- The first draw was accepted with zero duplicate exclusions, zero source-gate exclusions, zero reselections, and zero same-paper recent-marker exclusions.
- Dedup checks covered arXiv ID `2605.28056`, arXiv-issued DOI, normalized title, `CogPortrait-Eye-Control` slug, public log/report/DEP surfaces, the live dedup index, automation memory, and relevant Black-Lake-Data search results.

### Source Integrity and Cache Validation

- Initial state was partial because a valid PDF existed without full-paper HTML.
- The bounded archive-repair route obtained official full-paper HTML and refreshed local provenance, summary, README, receipt, and verification records.
- PDF verification passed the minimum byte threshold, `%PDF-` header, and trailing `%%EOF` marker.
- Full-paper HTML verification passed the minimum byte threshold, more than 2,000 body characters after script/style removal, an article/main/LaTeXML marker, at least two headings/section markers, and at least two paper-structure terms.
- Extractor preflight found `pypdf` and no `pdftotext`. Missing-only extraction produced a `cached` record with PDF and HTML text; source text remained absent because the TeX/source package was unavailable.
- No source files, extracted text, cache, or private verification record is included in this DEP. No `.source/` directory was created.

### Replication Checklist

- Obtain the authors' implementation, model checkpoints, prompt manifests, prototype library, FLAME/keypoint mapping, and KTO data under reviewed licenses.
- Reconstruct the 12-category EMH split with documented permissions, actor counts, identity separation, annotations, and evaluator versions.
- Run repeated seeds under matched compute for direct label mapping, retrieval, agent stages, critic, dynamic CFG, and KTO.
- Report AU-F1, AU-Temp, Eye-LMD, ID-Sim, Sync-C, FID/FVD/LPIPS, human-study agreement, uncertainty, and failure categories together.
- Run an authorized-use safety review for synthetic-media provenance, consent, privacy, and misuse controls before any public-facing demonstration.
