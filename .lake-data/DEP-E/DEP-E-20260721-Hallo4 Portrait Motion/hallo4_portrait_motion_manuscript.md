---
title: "Hallo4 Portrait Motion - DEP-E"
generated_at: "2026-07-21 (public-safe date; exact timestamp withheld)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-first review of preference-aligned audio- and skeleton-conditioned portrait animation in Hallo4."
source_status: "complete local PDF, HTML, metadata, and TeX sources inspected; public URLs cited; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-21"
temporal_cutoff: "Sources and repository context inspected through 2026-07-21."
primary_url: "https://arxiv.org/abs/2505.23525"
stable_identifier: "arXiv:2505.23525v4; DOI:10.48550/arXiv.2505.23525"
confidence_summary: "High for source identity, method, printed tables, and repository observations; medium for interpretation; low for independent reproducibility because no model, data, or experiment was run."
safety_scope: "consent-aware synthetic-media evaluation, defensive provenance checks, and bounded research prototypes"
distribution_notes: "No PDF, HTML, metadata page, source archive, extracted text, cache, render, model, dataset, voice, face image, or private path is redistributed."
---

# Hallo4 Portrait Motion - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Hallo4 arXiv record | Canonical metadata | HTML | arXiv:2505.23525v4 | https://arxiv.org/abs/2505.23525 | arXiv metadata and non-exclusive distribution-license locator; source redistribution not assumed. | 2026-07-21 | Inspected. |
| S2 | Hallo4 full paper | Primary paper | PDF and HTML | arXiv:2505.23525v4 | https://arxiv.org/html/2505.23525; https://arxiv.org/pdf/2505.23525 | Complete local copies inspected and withheld. | 2026-07-21 | PDF text, tables, and selected visual pages inspected; HTML inspected in full. |
| S3 | Hallo4 source package | Primary source | TeX archive | arXiv:2505.23525v4 | https://arxiv.org/e-print/2505.23525 | Valid local archive inspected and withheld. | 2026-07-21 | Formulas, tables, prose, author block, and limitations inspected. |
| S4 | arXiv-issued DOI | Persistent identity | DOI | 10.48550/arXiv.2505.23525 | https://doi.org/10.48550/arXiv.2505.23525 | Persistent locator; not a publisher DOI. | 2026-07-21 | Inspected. |
| S5 | Official Hallo4 repository | Official implementation | GitHub repository | commit `d8274e5e809ea1cd94279063b2a835b23832e466` | https://github.com/fudan-generative-vision/hallo4 | README says the model derives from Wan2.1 and must comply with the WAN license; no root license file was visible. | 2026-07-21 | README, tree, inference launcher, and requirements inspected; code not run. |
| S6 | OViP Preference DEP | Related research artifact | Markdown | DEP-E-20260714-OViP Preference | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` | Repository-generated review. | 2026-07-21 | Inspected. |
| S7 | VideoWeave Geometry DEP | Related research artifact | Markdown | DEP-E-20260709-VideoWeave Geometry | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Repository-generated review. | 2026-07-21 | Inspected. |
| S8 | AR-Drag Motion DEP | Related research artifact | Markdown | DEP-E-20260720-AR-Drag Motion | `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` | Repository-generated review. | 2026-07-21 | Inspected. |
| S9 | Private integrity and extraction records | Selection and processing provenance | Local records | arXiv:2505.23525 | Local paths withheld | Private processing evidence only; no source material redistributed. | 2026-07-21 | Integrity, cache, random-selection, and dedup summaries inspected. |

The canonical record lists Jiahao Cui, Yan Chen, Mingwang Xu, Hanlin Shang, Yuxuan Chen, Yun Zhan, Zilong Dong, Yao Yao, Jingdong Wang, and Siyu Zhu. Version 1 was submitted on 2025-05-29 and version 4 was revised on 2025-11-30. The official repository labels the work “SIGGRAPH Asia 2025,” but no paper-specific publisher record or publisher DOI was established from the inspected sources. The repository README names “Baoyou Chen” where the paper and canonical arXiv record name “Yan Chen”; this unresolved attribution difference is preserved rather than silently reconciled.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Canonical metadata / DOI | Title, authors, dates, version, subject, public URLs, and DOI. | Source identity and version context. | High | Metadata alone does not validate methods or results. |
| E2 | S2 | Complete primary paper | Method, training data, settings, Tables 1-9, Figures 4-8, user study, limitations, and conclusion. | Mechanism, quantitative claims, visual-review boundary, and author-stated limitations. | High for reporting | No result was reproduced; selected images cannot establish temporal quality from still frames. |
| E3 | S3 | Primary TeX/source | DPO objective, temporal reshaping, exact table values, author block, captions, and prose/table inconsistencies. | Cross-format verification and contradiction checks. | High | Source text reflects the authors' artifact, not independent validation. |
| E4 | S5 | Official implementation | Environment, weights layout, inference command, visible code tree, dependency pinning, social-risk note, and license boundary. | Implementation availability and reproducibility gaps. | High for visible state | Repository was not cloned or executed; model weights were not downloaded. |
| E5 | S6 | Related DEP manuscript | Online preference-data construction, judge dependence, hard-negative auditing, and preservation tradeoffs. | Preference-optimization concept bridge. | Medium | Different task, model family, and evaluation regime. |
| E6 | S7 | Related DEP manuscript | Joint latent conditioning and geometry/temporal consistency evaluation for video diffusion. | Latent-motion and multi-metric evaluation bridge. | Medium | Geometry-video generation does not validate portrait animation. |
| E7 | S8 | Related DEP manuscript | Motion control, inference-aligned rollout, tracker/reward coupling, latency, and synthetic-media safety. | Motion-system and governance bridge. | Medium | Autoregressive drag control differs from audio/skeleton conditioning. |
| E8 | S9 | Private process evidence | Uniform draw, dedup checks, PDF/HTML verification, cache miss/backfill, and extractor outputs. | Eligibility, complete-source gate, and cache methodology. | High | Local records are intentionally not public locators. |

## Executive Summary

Hallo4 combines two ideas for portrait animation: direct preference optimization over human-ranked candidate videos, and temporal motion modulation that converts four-frame motion groups into proportionally wider feature channels instead of simply subsampling them to the video latent rate. The framework is tested as a DPO extension of a UNet portrait model and as a Wan2.1-based DiT system conditioned on reference image, audio, text, and optional skeleton motion.

The strongest reported evidence is metric-specific. On HDTF, the DiT variant reports Sync-C 9.161, Sync-D 6.987, and E-FID 7.645. Its Sync-C exceeds the printed real-video value of 8.976, but its Sync-D is worse than the real-video value of 6.359 because lower is better; the paper's prose overstates this as surpassing real video on both values. On Celeb-V, Hallo4 DiT reports the best displayed Sync-C (5.689) and E-FID (18.998), but not the best FID or FVD. On EMTD, it leads Sync-C, hand-motion variance/confidence, PSNR, and SSIM, while EchoMimic-v2 retains substantially better FID/FVD.

Ablations support the usefulness of full 4x temporal-to-channel redistribution and DPO relative to the tested alternatives. They also expose tradeoffs: adding the portrait-fidelity preference improves Sync-C, Sync-D, and E-FID relative to motion-only preference, while worsening FID and FVD. The printed SFT discussion calls E-FID 21.432 an improvement over 21.065 even though lower is better. These details argue for reporting metric vectors and confidence intervals rather than one “state of the art” label.

Reviewer confidence is high that the paper and tables are reported accurately, medium that preference data plus temporal reshaping is a reusable design, and low for independent reproduction. The paper omits annotator counts, agreement, user-study participant count, ordering/randomization, and uncertainty. The official repository improves inspectability but contains a machine-local wheel URI, inconsistent `.pth` versus `.ckpt` checkpoint names, no visible root license, no obvious training/evaluation pipeline, and an author-name mismatch with the paper.

## Detailed Summary

### Problem Context

Audio-driven portrait animation must coordinate speech, lips, expression, head motion, body gesture, and visual identity. Diffusion video models can produce attractive frames but lose fast motion when audio or skeleton signals are temporally compressed to match a causal VAE latent. Standard reconstruction or likelihood losses also do not directly encode whether people perceive the result as well synchronized and natural.

Hallo4 treats these as separate but complementary failures. Human preference optimization supplies an alignment signal for motion-video synchronization and portrait fidelity. Temporal motion modulation supplies a representation mechanism intended to preserve high-frequency cues through the latent bottleneck.

### Preference Dataset and DPO

For each audio clip, the authors generate candidates with five methods: SadTalker, AniPortrait, EchoMimic-v2, FantasyTalking, and Hallo3. Annotators score each video on a five-point scale along motion-video alignment and portrait fidelity. The two ratings are averaged into a composite reward. The highest- and lowest-scoring candidates form the preferred and dispreferred pair, while low-margin cases are excluded.

The paper adapts diffusion DPO by comparing denoising-trajectory likelihoods for winners and losers relative to a reference policy. The objective uses a KL-constrained reward margin and a reported beta of 2500 during DPO training. This avoids training a separate explicit reward model, but it does not remove dependence on the annotation protocol: the pair distribution, candidate methods, composite averaging, annotator population, and margin filter define what “preference” means.

The training corpus is reported as 220,000 source videos totaling 220 hours, drawn from Celeb-V, HDTF, and YouTube. From it, 20,000 high-confidence preference pairs are curated. The paper does not report annotator count, demographics, qualification, agreement, repeated judgments, score calibration, or licensing/consent provenance for the complete corpus.

### Temporal Motion Modulation

Wan2.1's causal 3D VAE compresses video from `T x H x W` to roughly `T/4 x H/8 x W/8`. Naively downsampling audio or skeleton sequences to `T/4` can discard rapid articulation and gesture changes. Hallo4 instead groups four temporal steps and redistributes them into a 4x wider channel dimension. Audio features from Wav2Vec 2.0 and convolutional skeleton descriptors are reshaped to the latent temporal rate, projected, and fused through cross-attention.

This operation preserves the raw number of grouped feature values, but “preserves high-frequency motion” remains an empirical claim rather than an information-theoretic guarantee. Channel mixing, projection capacity, attention, VAE loss, and training data can still discard or alias motion. Tables 6-7 support the chosen reshape against two smaller alternatives in the tested setup.

### Architectures, Training, and Inference

The UNet variant starts from Hallo/Stable Diffusion-style portrait diffusion and applies DPO. The DiT variant uses Wan2.1 with a causal VAE and flow-matching denoiser. DiT training first updates audio cross-attention in the motion module, then introduces skeleton cross-attention while the VAE and denoiser blocks remain frozen, and finally applies DPO.

The reported implementation uses eight NVIDIA A100 GPUs. Temporal motion modulation trains for 10,000 iterations with AdamW, learning rate `1e-5`, 2,000 warm-up steps, and batch size 8. DPO trains for 12,000 iterations at `1e-8`, 2,500 warm-up steps, beta 2500, and global batch size 8. No wall-clock time, energy, peak memory, seed count, variance, or complete hyperparameter/configuration manifest is printed.

Inference consumes a reference portrait, driving audio, a text prompt, and optional skeleton frames. The official repository further states that reference aspect ratio should lie between 1:1 and 480:832, audio must be WAV, vocals should be clear, and the released model is limited to English audio.

### Main Quantitative Results

| Benchmark | Variant | Key reported gains | Important counterevidence |
|---|---|---|---|
| HDTF | Ours DiT | Sync-C 9.161; Sync-D 6.987; E-FID 7.645, best model values shown. | Real video has lower/better Sync-D 6.359; “surpasses real video” is only true for Sync-C. |
| Celeb-V | Ours DiT | Sync-C 5.689 and E-FID 18.998, best shown. | FID 58.815 and FVD 538.396 trail multiple baselines; Hallo3 FVD is 397.425. |
| Celeb-V | Ours UNet | Sync-C 5.480, E-FID 19.627, FID 49.282, FVD 444.319. | Sync-D 8.389 is worse than Sonic 7.370; DiT has better alignment but worse FID/FVD. |
| EMTD | Ours DiT | Sync-C 6.764, HKV 35.736, HKC 0.886, PSNR 22.221, SSIM 0.808. | FID/FVD 44.422/381.752 trail EchoMimic-v2 at 38.461/301.347. |

The benchmarks cover talking heads, wild high-resolution portraits, and upper-body skeletal motion. Dataset sample counts and evaluation-clip construction are not fully exposed in the inspected paper, and results are point estimates without uncertainty.

### Ablations and User Study

Full 4x temporal-to-channel audio redistribution reports Sync-C 5.689 versus 4.244 for 2x expansion and 2.769 for no expansion. Full skeleton redistribution reports HKV 35.736 and HKC 0.886 versus 33.567/0.873 and 31.096/0.850. DPO reports Sync-C 5.689 and E-FID 18.998 versus SFT 5.387 and 21.432 and baseline 5.326 and 21.065.

The preference ablation is not uniformly monotonic. Motion-only preference reports FID/FVD 55.220/518.380; adding fidelity preference changes them to 58.815/538.396 while improving synchronization and E-FID. The pair-construction ablation favors best-vs-worst on synchronization and E-FID, but another strategy has lower FVD. This suggests the chosen preference objective emphasizes some perceptual dimensions at the expense of distribution metrics.

The user study covers 200 generated EMTD samples and rates lip synchronization, beat alignment, portrait fidelity, and motion diversity on a five-point scale. Hallo4 reports 4.60, 4.48, 4.43, and 4.23, respectively. The paper does not disclose the number of participants, assignments per clip, rater training, randomization, blinding, inter-rater reliability, uncertainty, significance tests, or handling of repeated measures.

### Limitations, Safety, and Repository Boundary

The authors identify three limitations: dependence on precisely aligned audio-visual data, added training overhead from channel expansion, and an upper-body focus that leaves full-body synthesis open. The repository adds social-risk language about deepfakes, privacy, consent, and responsible use.

The official repository provides inference code, a compact launcher, requirements, and weight-download instructions. It does not by itself establish end-to-end reproducibility. The requirements include an absolute machine-local `flash_attn` wheel URI; README weight layout uses `model_weight.pth` while the launcher requests `model_weight.ckpt`; no root license file was visible; and training, preference-data construction, benchmark recreation, and user-study scripts were not evident from the visible root tree. The repository README's “Baoyou Chen” versus the paper's “Yan Chen” remains unresolved.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Human-ranked preference pairs improve lip/body synchronization and expression fidelity. | Author empirical claim | E2-E3, Tables 1-5 and 8-9 | Supported for reported metrics and settings; annotation protocol and uncertainty are underspecified. | Medium-high for reporting |
| C2 | Proportional temporal-to-channel redistribution preserves fast audio and skeleton cues better than direct compression. | Author mechanism and ablation claim | E2-E3, Tables 6-7 | Tested alternatives favor 4x redistribution, but “preservation” is inferred from downstream metrics rather than directly measured information retention. | Medium-high |
| C3 | Hallo4 DiT surpasses real video on HDTF synchronization. | Author prose claim | E2-E3, Table 1 | Partially supported: Sync-C 9.161 exceeds 8.976, but Sync-D 6.987 is worse than 6.359 because lower is better. | High for contradiction |
| C4 | Hallo4 achieves state-of-the-art portrait animation performance. | Author aggregate claim | E2-E3, Tables 1-3 | Too broad. It leads selected synchronization/expression/motion metrics but not all FID/FVD columns. | Medium |
| C5 | DPO outperforms supervised fine-tuning. | Author ablation claim | E2-E3, Table 8 | Supported on Sync-C, Sync-D, E-FID, FID, and FVD for the printed run; no seeds or matched-training audit. | Medium-high |
| C6 | Preference optimization aligns outputs with human judgment. | Author interpretation | E2-E3, dataset construction and user study | Plausible within the chosen raters/axes, but the human evidence lacks protocol and agreement details. | Medium-low |
| C7 | The official repository makes Hallo4 independently reproducible. | Reviewer assessment | E4 | Not established; inference assets exist, but environment, naming, license, training, data, and evaluation gaps remain. | High for boundary |
| C8 | The paper was eligible and complete before synthesis. | Process claim | E8 | First draw was dedup-clear; the partial unit was repaired; PDF and full-paper HTML passed all required checks. | High |

## Methodology

- `Research objective`: Produce a schema-complete, source-first DEP-E review of one uniformly selected, non-duplicate arXiv paper; preserve its mechanism, evidence, contradictions, limitations, implementation implications, and relation to exactly three existing deposits.
- `Sources inspected`: Complete 16-page PDF, official full-paper HTML, metadata HTML, TeX/source archive, three extracted text representations, canonical arXiv record, DOI, official implementation repository, live repository authorities, private integrity/cache records, and exactly three related DEP manuscripts.
- `Discovery strategy`: Used `rg --files -g "*.pdf"` on the archive, grouped unique PDF parents into paper units, selected one zero-based `Get-Random` index, derived the arXiv identity from filename and nearby metadata, searched public and private dedup surfaces, repaired the source unit, extracted local caches, inspected tables/figures/source text, pinned the official repository head, and searched Black Lake for conceptual overlap.
- `Inclusion criteria`: Evidence had to establish identity, directly support method/results/limitations, expose implementation or safety boundaries, document process provenance, or provide concrete overlap in preference learning, latent video consistency, or motion control.
- `Exclusion criteria`: Abstract-only synthesis, secondary summaries, unverified repository behavior, unrelated keyword hits, and source files were excluded from public evidence. Two author-inventory rows were treated as metadata, not research deposits.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Author claims, printed values, reviewer interpretation, and process evidence are separated. HTML and extracted text were cross-checked against TeX tables and selected rendered PDF pages.
- `Uncertainty handling`: Non-reproduction, missing protocol details, metric conflicts, absent uncertainty, code/environment gaps, license ambiguity, and attribution mismatch are explicit.
- `Extraction process`: Required preflight found `pypdf` but not `pdftotext`. Local `missing-only` extraction used `pypdf`, `html-regex`, and `tarfile` after the complete-source gate passed.
- `Cache methodology`: Initial lookup was a miss. The repaired local unit produced a final `cached` record with 53,699 PDF-text bytes, 46,819 HTML-text bytes, and 193,139 source-text bytes. No network was used by the extractor.
- `Random selection methodology`: 75,779 PDFs collapsed to 75,776 unique parent-paper units. PowerShell uniformly selected zero-based index 11,355; the first draw was accepted.
- `Dedup/reselection validation`: The selected ID, DOI, normalized title, slug, artifact patterns, automation memory, relevant Black-Lake-Data content, and active-worktree markers were clear. Exclusions 0; reselections 0.
- `Source-integrity methodology`: Initial state was partial because full-paper HTML was missing. A bounded, single-owner archive repair preserved the valid PDF, obtained official HTML/metadata/source, refreshed local companion records, and verified PDF header/EOF plus HTML size, body, structure, and document markers before review.
- `Reviewer stance`: Paper report, skeptical critique, DEP-ready preservation, implementation translation, safety review, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: Hallo4's preference-data design, DPO adaptation, temporal motion modulation, UNet/DiT integration, printed evidence, implementation boundary, risks, and exactly three Black Lake relationships.
- `Temporal boundary`: Paper v4 and public repository state inspected through 2026-07-21.
- `Evidence limits`: No model, dataset, weight, dependency environment, training run, inference clip, metric implementation, or statistical analysis was executed. Selected PDF still images cannot verify temporal quality.
- `Assumptions`: The base arXiv PDF/HTML endpoints served v4, adjacent archive metadata identifies the reviewed paper, and printed tables reflect the authors' runs.
- `Constraints`: Source files remain local; public text omits private paths and machine data. Portrait animation is safety-sensitive because it can enable impersonation, non-consensual media, and privacy harm.
- `Out of scope`: Production deployment, face or voice cloning, deceptive-media generation, legal clearance, participant re-identification, and claims about languages or bodies outside the evaluated scope.
- `Intended use`: Research review, DEP deposition, reproducibility planning, metric design, consent-aware prototype design, and follow-on audit.
- `Audience`: Video-generation researchers, ML systems engineers, evaluation designers, responsible-AI reviewers, and media-provenance teams.
- `Reproducibility boundary`: Public artifacts permit architectural inspection and limited inference setup, not recreation of training data, preference labels, benchmarks, user study, or reported results.
- `Data sensitivity`: Public research records plus private local source files; downstream portrait/voice inputs may be biometric or personal data and require explicit consent and retention controls.

## Observations

- `Observed pattern`: Preference optimization raises alignment-oriented metrics more consistently than global distribution metrics.
- `Metric tension`: Celeb-V and EMTD show that better synchronization/hand/expression scores can coexist with worse FID/FVD.
- `Contradiction`: The real-video Sync-D and SFT E-FID prose use improvement language inconsistent with the printed lower-is-better values.
- `Technical implication`: Temporal-to-channel reshaping is best viewed as a trainable anti-aliasing hypothesis, not guaranteed lossless preservation.
- `Human-evidence gap`: “Human preference” is central to both training and evaluation, yet rater protocol is one of the least documented components.
- `Repository implication`: An official repo can be useful evidence while still failing a portable-reproduction gate.
- `Open question`: Whether preference improvements transfer across language, culture, age, disability, identity, camera framing, clip length, and full-body motion is unknown.

## Considerations

Portrait animation should be governed as biometric synthetic media, not only as a rendering feature. Product use requires affirmative consent for face and voice, purpose limitation, revocation, encrypted retention, output labeling/watermarking, audit logs, abuse reporting, and controls against impersonation or harassment. Training-data provenance needs source-level rights and consent documentation, not a generic platform list.

Evaluation should report a Pareto surface across synchronization, expression, identity, hand/body kinematics, FID/FVD, temporal artifacts, calibration, and human ratings. Multi-seed intervals and per-subgroup results are necessary before treating small table differences as reliable. Human studies should publish participant counts, assignments, randomization, blinding, agreement, exclusions, compensation, and statistical methods.

The released environment should replace machine-local wheels with reproducible build instructions or hashes, reconcile checkpoint filenames, declare repository/code/model/data licenses separately, pin commits and model revisions, expose metric scripts, and include a minimal expected-output smoke test. English-only audio and precise-alignment dependence must be visible deployment constraints.

## Strengths

- It separates preference alignment from motion-representation loss and supplies targeted mechanisms for both.
- The same preference idea is tested on UNet and DiT backbones, while the temporal module is isolated in DiT ablations.
- Nine tables cover baseline comparison, preference axes, pair construction, temporal reshaping, SFT, and human ratings.
- The paper explicitly acknowledges alignment, compute, and upper-body limitations.
- The official repository provides a real inference surface and model-asset guidance rather than only a paper placeholder.

## Weaknesses

- Annotation and user-study protocols omit essential sample, agreement, randomization, and uncertainty information.
- Results are single point estimates; no repeated seeds, confidence intervals, or significance tests are reported.
- Aggregate “state of the art” language obscures FID/FVD regressions and lower-is-better prose errors.
- Dataset provenance, consent, licensing, demographic composition, and filtering are insufficiently documented for human imagery.
- The repository has portability, naming, license, training/evaluation, and attribution inconsistencies; reproduction was not demonstrated.
- No long-duration, multilingual, full-body, adversarial, identity-safety, watermark, or misuse-resistance evaluation is provided.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a preference/user-study data card | Human evidence | Rater population and agreement define the objective. | Auditable alignment and subgroup analysis. | Privacy and administration burden. | Pre-register protocol; release aggregate demographics, agreement, and bootstrap intervals. |
| Report a multi-objective Pareto analysis | Evaluation | Alignment gains conflict with FID/FVD. | Prevent misleading single-score claims. | Larger evaluation matrix. | Multi-seed paired tests across every metric and benchmark. |
| Add anti-aliasing and information probes | Motion module | Channel reshaping is not automatically lossless. | Mechanistic evidence for fast-motion preservation. | Instrumentation and synthetic-test design. | Frequency sweeps, temporal impulse tests, mutual-information proxies, and ablations. |
| Release a portable reproduction bundle | Engineering | Current dependencies and names are inconsistent. | Lower setup failure and clearer result boundary. | Maintenance and licensing review. | Clean-container build, smoke clip, metric checksum, expected outputs, and CI. |
| Add consent/provenance controls | Safety and governance | Face/voice animation can cause serious harm. | Safer research and deployment decisions. | Dataset reduction and policy overhead. | Provenance coverage, revocation tests, watermark detection, abuse-case red team. |

## Potential Implementations

1. **Preference Protocol Auditor**
   - `User`: Research and responsible-AI reviewers.
   - `Goal`: Detect missing annotation, agreement, uncertainty, and subgroup evidence before accepting a preference-trained media model.
   - `Core mechanism`: Parse a model card and study manifest into a checklist and risk score.
   - `Required inputs`: Public protocol metadata and aggregate results; never raw biometric media.
   - `Outputs`: Missing-evidence report, confidence flags, and release blockers.
   - `Risk controls`: No participant identities; minimum-group thresholds; human review.
   - `Evaluation`: Compare findings with independent protocol audits.

2. **Temporal Motion Probe Suite**
   - `User`: Video-model engineers.
   - `Goal`: Measure whether temporal-to-channel modulation preserves fast, controlled motion.
   - `Core mechanism`: Synthetic audio pulses and skeleton trajectories with known frequencies are propagated through competing conditioning modules.
   - `Required inputs`: Synthetic signals and authorized model endpoints.
   - `Outputs`: Frequency response, phase lag, reconstruction, synchronization, and failure plots.
   - `Risk controls`: Synthetic identities only; offline execution; no public impersonation media.
   - `Evaluation`: Known-signal recovery and blinded comparisons across reshape/downsample variants.

3. **Consent-Aware Portrait Sandbox**
   - `User`: Authorized creators and internal media teams.
   - `Goal`: Explore portrait motion only for verified consenting identities.
   - `Core mechanism`: Local preprocessing, consent token, bounded clip generation, watermarking, and provenance ledger.
   - `Required inputs`: User-controlled portrait/audio and explicit usage scope.
   - `Outputs`: Watermarked preview plus consent/provenance receipt.
   - `Risk controls`: Local-only default, identity matching to consent record, retention expiry, blocked public figures, human approval before export.
   - `Evaluation`: Consent-revocation tests, watermark persistence, access-control tests, and abuse-case review.

## Three Ways to Exercise This Research

1. `Table consistency audit`: Objective - verify every lower/upper-is-better claim; inputs - the nine published tables; method - encode metric directions and compare prose to values; output - contradiction ledger; success - all numeric statements resolve; stop - no inference beyond printed evidence.
2. `Synthetic frequency probe`: Objective - test temporal information retention; inputs - toy audio impulses and skeleton sinusoids; method - compare 4x subsampling, 2x expansion, and 4x expansion in a small local module; output - phase/amplitude error curves; success - results reproduce expected ranking; stop - synthetic data only and no portrait generation.
3. `Reproduction-readiness review`: Objective - make the official inference path auditable without downloading large weights; inputs - pinned repo tree and documentation; method - validate names, URLs, licenses, dependencies, configs, and smoke-test specification; output - executable-readiness checklist; success - every dependency and expected output is versioned; stop - before model download or biometric input.

## Example MVP Product

- `Product name`: Motion Evidence Gate.
- `Target user`: Video-generation research reviewers and model-release owners.
- `Problem`: Headline alignment gains can conceal quality regressions, protocol gaps, and unsafe data practices.
- `Core workflow`: Import a public metrics/protocol manifest, validate metric directions and required evidence, compute Pareto warnings, and emit a signed review report.
- `Data requirements`: Aggregate numeric metrics, study counts, uncertainty, license/provenance coverage, and repository metadata; no raw face or voice data.
- `Architecture`: Local CLI with YAML schema, deterministic validators, Markdown report generator, and optional CI gate.
- `Success metrics`: 100% detection of seeded direction errors; zero raw-media ingestion; stable report hashes; reviewer agreement on release blockers.
- `Risk controls`: Local-only, allowlisted fields, no biometric identifiers, no network by default, and mandatory human override notes.
- `Limitations`: It validates evidence completeness and consistency, not generative quality or legal compliance.

Illustrative dependency-free Python core:

```python
METRIC_DIRECTION = {"sync_c": "max", "sync_d": "min", "e_fid": "min", "fid": "min", "fvd": "min"}

def dominates(candidate: dict[str, float], baseline: dict[str, float]) -> bool:
    checks = []
    for name, direction in METRIC_DIRECTION.items():
        checks.append(candidate[name] >= baseline[name] if direction == "max" else candidate[name] <= baseline[name])
    return all(checks)

def evidence_gate(report: dict) -> list[str]:
    findings = []
    if not report.get("seed_count") or report["seed_count"] < 2:
        findings.append("missing repeated-seed evidence")
    if not report.get("annotator_count"):
        findings.append("missing annotator count")
    if not report.get("confidence_intervals"):
        findings.append("missing uncertainty")
    return findings
```

Dependencies: Python 3.10+ only. Failure modes: incorrect metric schema, incomparable evaluation sets, and missing baselines can produce false confidence; production use needs schema versioning, tests, signatures, and reviewer approval.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| OViP Preference | Black Lake DEP-E | Shows how preference optimization depends on evolving negatives, judges, synthetic generation, and behavior-preservation evidence. | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` |
| VideoWeave Geometry | Black Lake DEP-E | Provides a shared-latent video-conditioning comparison and argues for structural/temporal evaluation beyond appearance. | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` |
| AR-Drag Motion | Black Lake DEP-E | Provides an inference-aligned motion-control comparison, tracker/reward caveat, and synthetic-media governance context. | `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` |
| Diffusion-DPO | Primary methodological neighbor | Establishes direct preference optimization for diffusion models, which Hallo4 adapts to portrait video. | https://arxiv.org/abs/2311.12908 |
| Wan 2.1 | Primary backbone context | DiT/causal-VAE foundation named by the paper and official repository. | https://arxiv.org/abs/2503.20314 |
| Wav2Vec 2.0 | Primary audio representation context | Supplies frame-aligned speech features used by the motion module. | https://arxiv.org/abs/2006.11477 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2505.23525 | Identity, authors, dates, abstract, version history, public links. | 2026-07-21 | Canonical metadata. |
| R2 | https://arxiv.org/html/2505.23525 | Full method, experiments, results, limitations, and references. | 2026-07-21 | Official full-paper HTML. |
| R3 | https://arxiv.org/pdf/2505.23525 | Visual table/figure and layout review. | 2026-07-21 | Local copy inspected and withheld. |
| R4 | https://arxiv.org/e-print/2505.23525 | Formulas, tables, captions, author block, and cross-format checks. | 2026-07-21 | Local archive inspected and withheld. |
| R5 | https://doi.org/10.48550/arXiv.2505.23525 | Persistent arXiv identity. | 2026-07-21 | Not a publisher DOI. |
| R6 | https://github.com/fudan-generative-vision/hallo4 | Implementation tree, environment, model assets, launcher, risks, and license boundary. | 2026-07-21 | Inspected at commit `d8274e5e809ea1cd94279063b2a835b23832e466`; not run. |
| R7 | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` | Preference-loop bridge. | 2026-07-21 | Related Black Lake artifact. |
| R8 | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Latent-video consistency bridge. | 2026-07-21 | Related Black Lake artifact. |
| R9 | `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` | Motion-control and safety bridge. | 2026-07-21 | Related Black Lake artifact. |
| R10 | `.logs/20260721-Arxiv-Hallo4-Portrait-Motion-PHASE-LOG.md` | Public-safe selection, integrity, extraction, and cache summary. | 2026-07-21 | Private paths and source content withheld. |

## Appendix

### Replication Checklist

- Pin paper v4, repository commit, weight revision, and every dependency.
- Replace the machine-local wheel URI and reconcile `.pth` versus `.ckpt` naming.
- Publish code/model/data/license boundaries separately.
- Document source-video provenance, consent, removals, demographic coverage, and split leakage.
- Publish preference annotator count, assignments, training, agreement, exclusions, and margin distribution.
- Release training and evaluation configurations, seeds, metric versions, raw per-sample results, and expected smoke outputs.
- Repeat HDTF, Celeb-V, and EMTD evaluation with confidence intervals and independent human raters.
- Add multilingual, long-duration, full-body, subgroup, consent, watermark, and misuse-resistance tests.

### Source and Distribution Note

The local source unit was repaired from partial to verified complete before synthesis. PDF, official full-paper HTML, metadata HTML, a valid 19-entry source archive, extracted texts, cache manifests, hashes, integrity reports, and temporary page renderings were retained or inspected locally. Temporary visual-review renderings were removed after inspection. No source file, cache, extracted source text, or `.source/` directory was uploaded.
