---
title: "APB2Face Safety Review - DEP-E"
generated_at: "2026-07-20 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A defensive source-grounded review of audio-guided identity-specific face reenactment."
source_status: "verified complete local PDF, fallback full-paper HTML, and metadata HTML inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-20"
temporal_cutoff: "Sources and repository context inspected through the batch invocation."
primary_url: "https://arxiv.org/abs/2004.14569"
stable_identifier: "arXiv:2004.14569v1; DOI:10.48550/arXiv.2004.14569"
deployment_job_id: "BLAD-2200-20260720-8636EDC7"
deployment_item_id: "BLAD-2200-20260720-8636EDC7-P03"
confidence_summary: "High for source transcription; medium for the narrow six-identity evaluation; low for consent, demographic transfer, and safe deployment."
safety_scope: "defensive evaluation, consent, provenance, disclosure, detection, revocation, and human review; no operational generation guidance"
distribution_notes: "No media, biometric data, model, code, PDF, HTML, extracted text, cache, verification record, or local path is redistributed."
---

# APB2Face Safety Review - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Metadata | HTML | arXiv:2004.14569v1 | https://arxiv.org/abs/2004.14569 | Metadata only; paper license/data rights not inferred. | 2026-07-20 | Inspected. |
| S2 | Full-paper rendering | Primary paper | HTML | arXiv:2004.14569v1 | https://ar5iv.labs.arxiv.org/html/2004.14569 | Verified fallback local copy withheld. | 2026-07-20 | Inspected in full. |
| S3 | Paper PDF | Primary paper | PDF | arXiv:2004.14569v1 | https://arxiv.org/pdf/2004.14569 | Verified local copy withheld. | 2026-07-20 | Integrity checked and cross-read. |
| S4 | arXiv DOI | Identity | DOI | 10.48550/arXiv.2004.14569 | https://doi.org/10.48550/arXiv.2004.14569 | Persistent locator. | 2026-07-20 | Resolved. |
| S5 | Document Fraud LLM DEP | Related | Markdown | DEP-E-20260715 | `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` | Defensive synthesis only. | 2026-07-20 | Inspected. |
| S6 | Biometric Identity Gaps DEP | Related | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Biometric Identity Gaps/biometric_identity_gaps_manuscript.md` | Safety synthesis only. | 2026-07-20 | Inspected. |
| S7 | AR-Drag Motion DEP | Related | Markdown | DEP-E-20260720 | `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` | Safety/evaluation synthesis only. | 2026-07-20 | Inspected. |
| S8 | Selection, repair, integrity | Process evidence | Private records | `BLAD-2200-20260720-8636EDC7-P03` | Local path withheld | Randomness, dedup, integrity, locality. | 2026-07-20 | Verified. |

Authors: Jiangning Zhang, Liang Liu, Zhucun Xue, and Yong Liu. Submitted 2020-04-30; ICASSP 2020. Deployment job `BLAD-2200-20260720-8636EDC7`; item `BLAD-2200-20260720-8636EDC7-P03`.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Metadata | Identity, date, venue, subjects, DOI. | Canonical record. | High | No result evidence. |
| E2 | S2, S3 | Complete paper | Dataset, architecture, losses, training, metrics, figures, conclusion. | Method and results. | High for transcription | No rerun. |
| E3 | S2 AnnVI section | Primary paper | Six announcers, 23,790 frames, YouTube sourcing, annotations. | Dataset scope. | High for source report | Consent/license/demographics not established. |
| E4 | S2 experiments/Table 1 | Primary paper | SSIM, FID, detection and control errors, 75 FPS. | Performance claims. | High for transcription | Narrow/custom evaluation; hardware incomplete. |
| E5 | S2 Wav2Pix comparison | Primary paper | Same-identity visual and metric comparison. | Baseline claim. | Medium | Original baseline data unavailable. |
| E6 | S5-S7 | Related DEP evidence | Detection, identity governance, motion safety. | Defensive synthesis. | Medium | Different systems and dates. |
| E7 | S8 | Private process evidence | Uniform draw, dedup, repair, integrity, source locality. | Deployment validity. | High | Private context withheld. |

## Executive Summary

APB2Face predicts facial landmarks from audio plus explicit head-pose and blink controls, then renders an identity-specific 256x256 face from the landmark image. The AnnVI dataset contains six YouTube announcers and 23,790 frames. Source-reported metrics indicate controllability and real-time generation, but the evaluation is narrow and partly custom.

The paper predates current synthetic-media governance expectations and does not establish a consent, licensing, demographic, disclosure, watermarking, detector, or revocation framework. This artifact therefore treats the work as evidence for defensive evaluation and consent-bound avatar research, not as an implementation recipe.

## Detailed Summary

### Dataset

AnnVI includes three men and three women, with 1,230 to 6,400 frames per identity and 23,790 total. Frames were extracted from 1080p YouTube videos, faces cropped and resized to 256x256, MFCC audio extracted at 44.1 kHz, and pose/landmarks detected then manually checked. Blink is a normalized eye aspect ratio. The inspected paper does not document subject consent, source-video licenses, data-release terms, demographic diversity beyond the six identities, or deletion/revocation.

### GeometryPredictor

Separate audio, pose, and blink branches produce features that are concatenated to regress landmarks. L1 and an adversarial landmark discriminator supervise geometry. The paper reports the discriminator reducing average landmark L1 error from 1.500 plus/minus 0.064 pixels to 0.666 plus/minus 0.034.

### FaceReenactor

Predicted landmarks are rendered as a binary image and passed to an identity-specific modified Pix2Pix model. The generator is trained with L1, face-region mask, and adversarial losses. Identity appearance resides in the model while landmarks carry geometry.

### Experiments

Across six identities, average SSIM is 0.799, FID 11.862, detection rate 98.8%, average landmark error 1.429, pose error 0.0195, and blink error 0.0413. A GPU throughput of 75 FPS is reported without a complete hardware/latency profile. The Wav2Pix comparison does not use the original authors' data, weakening matched-baseline inference.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Explicit pose/blink controls improve controllability over audio alone. | Author claim | E2, E4 | Qualitative decoupling and custom control metrics support the displayed identities. | Medium-high |
| C2 | The two-stage model produces photorealistic real-time faces. | Author claim | E4 | SSIM/FID and 75 FPS are reported; realism, hardware, and independent testing are limited. | Medium |
| C3 | AnnVI supports the method. | Author claim | E3 | It supports narrow training/evaluation but not broad identity or demographic transfer. | Medium |
| C4 | Identity-specific models require lifecycle revocation and consent controls. | Reviewer interpretation | E3, E6 | Appearance can persist in weights and outputs after source removal. | High |
| C5 | Safe use requires provenance and defensive detection beyond image-quality metrics. | Reviewer interpretation | E4, E6 | Current related evidence shows quality scores do not measure misuse or detectability. | High |

## Methodology

- `Research objective`: preserve the paper's mechanism and evidence while translating it into defensive synthetic-media governance.
- `Sources inspected`: arXiv metadata, verified fallback HTML, verified PDF, and three related Black Lake manuscripts.
- `Discovery strategy`: uniform local archive draw, identity/title/DOI/slug dedup, bounded repair, full-paper extraction, related safety search.
- `Inclusion criteria`: dataset provenance, architecture, losses, metrics, baselines, limitations, and defensive implications.
- `Exclusion criteria`: operational generation instructions, media/assets, weights, code, evasion, and unsupported consent claims.
- `Analytical approach`: empirical, comparative, safety/ethics, implementation, product governance, and replication.
- `Evidence handling`: source claims, reported numbers, reviewer interpretation, and private process evidence are separated.
- `Uncertainty handling`: consent, licensing, demographics, reproducibility, and cross-dataset gaps remain explicit.
- `Safety handling`: all examples are authorization, disclosure, provenance, and detection oriented.

## Scope, Constraints, and Assumptions

- `Scope`: dataset, two-stage architecture, reported evaluation, identity/synthetic-media risks, and defensive controls.
- `Temporal boundary`: paper v1 and repository context available on 2026-07-20.
- `Evidence limits`: no dataset/media/code, no independent user study, no rerun, no current detector test.
- `Assumptions`: table values accurately reflect the stated six-identity experiments.
- `Constraints`: identity authorization, biometric privacy, copyright, consent, provenance, temporal quality, and detector arms races.
- `Out of scope`: instructions for generating impersonations, identity cloning, evasion, or unrestricted deployment.
- `Intended use`: defensive review, governance design, consent-bound research, and detector benchmarking.
- `Data sensitivity`: biometric face imagery and voices; none redistributed.
- `Operational boundary`: synthetic/offline evaluation only with authorized identities.

## Observations

- `Observed pattern`: explicit non-audio controls improve separation of pose and blink from mouth motion on the displayed examples.
- `Technical implication`: identity appearance embedded in a per-person model complicates deletion and revocation.
- `Contradiction or tension`: high face-detection rate indicates recognizable face structure, not authenticity or safe use.
- `Open question`: how do outputs fare under modern temporal, audio-visual, watermark, and deepfake detectors?
- `Reviewer hypothesis`: a landmark-control interface can support safe avatars only when identity authorization and provenance are mandatory inputs.

## Considerations

Use requires explicit and revocable consent for both face and voice, source licensing, purpose limitation, data minimization, retention policy, model deletion, output disclosure, watermark/provenance, abuse monitoring, and human appeal. Evaluations should include temporal consistency, lip-sync, identity leakage, demographic performance, impersonation risk, detector performance, and repeated-run uncertainty. Public release of identity-specific weights or source media would materially expand risk and is not recommended by this artifact.

## Strengths

- Clear two-stage separation between geometry and appearance.
- Explicit head-pose and blink controls address an audio-only limitation.
- Dataset counts, preprocessing, and several control metrics are reported.
- Landmark adversarial ablation includes a concrete error change.
- Identity-crossed audio examples test some driver/target separation.

## Weaknesses

- Only six identities and no broad demographic or cross-dataset evaluation.
- YouTube sourcing lacks an inspected consent/licensing protocol.
- Identity-specific reenactors reduce scalability and increase retention risk.
- Baseline comparison is not fully matched because original data were unavailable.
- Metrics omit temporal realism, user deception, watermarking, detectors, and misuse.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Consent/data-rights card | Governance | Source subjects and permissions are unclear. | Lawful, reviewable scope. | May restrict dataset. | Consent/license audit and revocation test. |
| Cross-dataset demographic study | External validity | Six identities cannot support general claims. | Fairness and transfer evidence. | Sensitive data governance. | Predeclared groups and uncertainty. |
| Temporal/detector evaluation | Safety | Frame metrics miss synthetic-media risk. | More realistic release gate. | Detector drift. | Multi-detector and human review benchmark. |
| Provenance by design | Distribution | Real-time outputs can spread quickly. | Traceability and disclosure. | Metadata stripping. | Robustness to common transformations. |

## Potential Implementations

1. **Authorized-avatar audit**
   - `User`: media safety reviewer.
   - `Goal`: evaluate a consented avatar without distributing generation assets.
   - `Core mechanism`: authorization, disclosure, temporal and forensic test suite.
   - `Required inputs`: signed scope, approved outputs, detector results.
   - `Outputs`: pass/abstain/reject receipt.
   - `Risk controls`: identity revocation and no public weights.
   - `Evaluation`: consent and provenance drills.
2. **Provenance verifier**
   - `User`: publisher/platform.
   - `Goal`: confirm synthetic disclosure and model authorization.
   - `Core mechanism`: output hash, signed manifest, watermark check.
   - `Required inputs`: media and public verification keys.
   - `Outputs`: provenance status and uncertainty.
   - `Risk controls`: no biometric gallery.
   - `Evaluation`: transformation robustness.
3. **Defensive reenactment benchmark**
   - `User`: forensic researcher.
   - `Goal`: measure detector/generalization gaps using authorized synthetic media.
   - `Core mechanism`: fixed denominator, multiple detectors, calibration, abstention.
   - `Required inputs`: consented benchmark and disclosure metadata.
   - `Outputs`: AUC, calibration, failure slices, audit log.
   - `Risk controls`: controlled access and no evasion optimization.
   - `Evaluation`: held-out generator and transformation tests.

## Three Ways to Exercise This Research

1. `Consent-model audit`: map every identity, source clip, permission, weight, cache, and output to a revocation action; output the lifecycle matrix and stop if any artifact lacks an owner.
2. `Metric-gap exercise`: evaluate authorized outputs with SSIM/FID plus temporal, lip-sync, forensic, disclosure, and human-review measures; output disagreements and stop before public distribution.
3. `Provenance stress test`: apply benign resizing/transcoding to disclosed synthetic outputs, verify provenance retention, and stop if disclosure cannot survive the approved distribution path.

## Example MVP Product

- `Product name`: Consent-Bound Avatar Auditor.
- `Target user`: media organization using authorized digital presenters.
- `Problem`: visual quality metrics do not prove authorization, provenance, or safety.
- `Core workflow`: verify consent; ingest approved output only; run temporal/forensic/provenance tests; issue human-reviewed release receipt.
- `Data requirements`: signed consent record, output media, model/version manifest; no reusable biometric gallery.
- `Architecture`: local verifier, consent registry, detector ensemble, provenance checker, immutable audit log.
- `Success metrics`: 100% authorization coverage, revocation drill success, provenance survival, calibrated detector abstention.
- `Risk controls`: no generation endpoint, no weights, no unconsented media, access control, expiry, appeal.
- `Limitations`: detectors and watermarks can fail; authorization remains organizational/legal.
- `Deployment model`: local-only review station.
- `Evaluation plan`: red-team distribution, metadata stripping, revocation, false-positive, and human-review tests.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| APB2Face | Primary paper | Audio/pose/blink-controlled face reenactment. | https://arxiv.org/abs/2004.14569 |
| Document Fraud LLM DEP | Related review | Layered manipulation detection and calibration. | `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/` |
| Biometric Identity Gaps DEP | Related review | Synthetic identity, resemblance, revocation, and governance. | `.lake-data/DEP-E/DEP-E-20260716-Biometric Identity Gaps/` |
| AR-Drag Motion DEP | Related review | Motion control, evaluator limits, provenance, and synthetic-media risk. | `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/` |
| C2PA specification | Standard | Content provenance and disclosure context. | https://c2pa.org/specifications/specifications/2.2/index.html |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2004.14569 | Identity, authors, date, venue, abstract, DOI. | 2026-07-20 | Metadata only. |
| R2 | https://ar5iv.labs.arxiv.org/html/2004.14569 | Dataset, method, experiments, metrics, figures, conclusion. | 2026-07-20 | Verified local copy withheld. |
| R3 | https://arxiv.org/pdf/2004.14569 | Primary PDF/cross-format evidence. | 2026-07-20 | Verified local copy withheld. |
| R4 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260715-Document%20Fraud%20LLM | Defensive detection context. | 2026-07-20 | Related DEP. |
| R5 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Biometric%20Identity%20Gaps | Identity-governance context. | 2026-07-20 | Related DEP. |
| R6 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260720-AR-Drag%20Motion | Motion-generation context. | 2026-07-20 | Related DEP. |

## Appendix

### Selection, Deduplication, and Integrity

- Uniform draw: one-based index 65,096 of 75,776 units from 75,779 PDFs.
- Duplicate exclusions: 0; reselections: 0; current-job duplicates: 0.
- Dedup surfaces: Black Lake artifacts/index, automation memory, relevant Black-Lake-Data records, current-job set, and 24-hour markers.
- Source gate: PDF 4,277,655 bytes with valid header/EOF; fallback HTML 206,725 bytes with 25,459 body characters, 17 document markers, 17 headings, and 37 structure terms.
- Locality: media, PDF, HTML, metadata, verification records, and caches withheld; no `.source/`; zero source uploads.

### Defensive Replication Checklist

- Obtain documented consent and source licenses before any media access.
- Use authorized identities and controlled storage only.
- Reproduce dataset counts and reported metrics without redistributing subjects.
- Add temporal, lip-sync, calibration, detector, provenance, and demographic evaluation.
- Exercise revocation across data, model, cache, output, and downstream copies.
