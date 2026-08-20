---
title: "Invisible Backdoor - DEP-E"
generated_at: "2026-08-18"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded defensive review of invisible input-conditioned backdoors in diffusion image editing."
source_status: "URLs only; verified local source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-18"
temporal_cutoff: "Public and repository evidence inspected through 2026-08-18"
primary_url: "https://arxiv.org/abs/2506.04879"
stable_identifier: "arXiv:2506.04879v1; DOI:10.48550/arXiv.2506.04879"
confidence_summary: "High for source transcription; medium for cross-DEP synthesis; low for independent reproducibility and deployment transfer."
safety_scope: "defensive evaluation, provenance, detection, robustness, and authorized testing only"
distribution_notes: "Original PDF, full-paper HTML, metadata, source package, extracted text, and caches remain local and are not redistributed."
---

# Invisible Backdoor - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | 2506.04879v1 | https://arxiv.org/abs/2506.04879 | Canonical identity, authors, date, subject, abstract, and DOI locator. | 2026-08-18 | Inspected |
| S2 | Complete paper | Primary artifact | PDF and full-paper HTML | 2506.04879v1 | https://arxiv.org/pdf/2506.04879; https://arxiv.org/html/2506.04879 | Verified locally; source files withheld. | 2026-08-18 | Inspected in full |
| S3 | arXiv-issued DOI | Persistent identity | DOI | 10.48550/arXiv.2506.04879 | https://doi.org/10.48550/arXiv.2506.04879 | Persistent public locator. | 2026-08-18 | Referenced |
| S4 | Authors' implementation repository | Official implementation context | GitHub | default branch observed on access date | https://github.com/aiiu-lab/BackdoorImageEditing | Apache-2.0 label and environment notes visible; not executed. | 2026-08-18 | Inspected |
| S5 | Context Backdoor Defense | Related DEP | Markdown | DEP-E-20260720 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-Context%20Backdoor/context_backdoor_defense_manuscript.md | Provenance, runtime interlocks, and defensive context-integrity bridge. | 2026-08-18 | Inspected |
| S6 | TRACE Poison Detection | Related DEP | Markdown | DEP-A-20260729 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260729-TRACE%20Poison%20Detection/2606.25721-whitepaper-review.md | Influence attribution and poisoned-corpus detection bridge. | 2026-08-18 | Inspected |
| S7 | Document Fraud LLM | Related DEP | Markdown | DEP-E-20260715 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260715-Document%20Fraud%20LLM/document_fraud_llm_manuscript.md | Visual forensics, calibration, fixed-denominator, and human-triage bridge. | 2026-08-18 | Inspected |
| S8 | Black Lake repository authority | Process source | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Filing, source locality, attribution, index, and commit rules. | 2026-08-18 | Inspected |
| S9 | Black-Lake-Data repository authority | Related-repository process source | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related layout and provenance context. | 2026-08-18 | Inspected |
| S10 | Local integrity records | Process evidence | Private JSON/CSV/Markdown | selected paper unit | Public path withheld | Repair, verification, and source-locality evidence only. | 2026-08-18 | Verified; not distributed |

**Paper title:** *Invisible Backdoor Triggers in Image Editing Model via Deep Watermarking*
**Authors:** Yu-Feng Chen; Tzuhsuan Huang; Pin-Yen Chiu; Jun-Cheng Chen
**Submitted:** 2025-06-05; v1
**Subject:** Computer Vision and Pattern Recognition
**Source policy:** The complete local PDF and full-paper HTML were inspected. No source files, extracted text, caches, or `.source/` directory are included in this DEP.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 and S3 | Primary metadata | Identity, authors, date, version, subject, abstract, DOI, and code locator. | Source Metadata and public provenance. | High | Metadata does not establish experimental validity. |
| E2 | S2 Sections 3-5 | Primary full text | InstructPix2Pix base, clean/poisoned branches, watermark-conditioned target behavior, metrics, and conclusion. | Method and central thesis. | High for transcription | No independent reproduction. |
| E3 | S2 Table 1 | Primary empirical evidence | Utility and specificity for VINE, StegaStamp, and RoSteALS at poison rate 0.1. | Reported ASR, EAR, MSE, and CLIP comparisons. | High for reporting | One model family and one principal poison rate. |
| E4 | S2 Tables 2-3 | Primary empirical evidence | Distortion robustness and watermark image-quality metrics. | Robustness and perceptual tradeoff claims. | High for reporting | No confidence intervals or independent statistical tests. |
| E5 | S2 Table 4 and Appendix C | Primary ablation evidence | Loss-component ablation and multiple trigger-target-pair discussion. | Training-objective and extensibility observations. | Medium | The multiple-pair result is author-reported and lightly specified. |
| E6 | S4 | Official implementation context | Public repository existence, Apache-2.0 label, environment, and training/demo references. | Implementation relevance and availability boundary. | Medium | Repository presence is not proof of reproducibility. |
| E7 | S5-S7 | Related processed research | Context provenance, influence attribution, visual manipulation triage, calibration, and fixed-denominator lessons. | Cross-DEP synthesis. | Medium | Conceptual neighbors use different domains and benchmarks. |
| E8 | S8-S10 | Process evidence | Repository authority, random selection, deduplication, repair, integrity, and no-source-upload gate. | Workflow validity. | High | Process evidence is not scientific evidence. |

## Executive Summary

The paper presents a source-grounded study of hidden input-conditioned behavior in instruction-based diffusion image editing. It uses invisible deep-watermark signals as triggers in poisoned training examples and evaluates whether the resulting model can preserve clean editing while producing a predefined target for watermarked inputs. The primary experimental base is InstructPix2Pix, with StegaStamp, VINE, and RoSteALS used as watermarking components.

The strongest reported results occur for StegaStamp and RoSteALS at poison rate 0.1: Table 1 reports ASR 0.956/EAR 0.000 for StegaStamp and ASR 0.894/EAR 0.003 for RoSteALS, while VINE reports ASR 0.552/EAR 0.114. The robustness tables show that erasing and JPEG can preserve high trigger response for the stronger methods, but rotation, resized crop, and blur remain difficult. StegaStamp is weaker under contrast and RoSteALS under Gaussian noise. These are paper-reported values, not reproduced results.

The reviewer's defensible interpretation is narrower than the paper's attack framing: image-editing systems need explicit tests for hidden input-conditioned behavior, clean-input utility, false activation, provenance, and ordinary transformation response. The latent-residual explanation is a useful hypothesis for test design, not a causal law. The official code repository was inspected but not executed, and no deployment readiness or universal watermark claim follows from this evidence.

## Detailed Summary

### Problem

Diffusion image-editing systems can be influenced by patterns in their inputs. The paper argues that visible triggers are impractical where image fidelity or ownership matters, and it studies whether off-the-shelf invisible watermarking can act as an input-conditioned trigger during training. This is a dual-use topic; the public artifact therefore preserves mechanism and evidence at a defensive level and omits operational trigger construction.

### Method

The method separates training into a clean branch and a poisoned branch. The poisoned branch pairs watermarked conditioning images with a predefined target, while the clean branch retains ordinary image-editing pairs and prompts. The total objective combines denoising and image-space MSE terms for both branches. The paper frames the watermark as a hidden condition that changes model behavior while leaving the clean path useful.

### Evaluation

The authors fine-tune an InstructPix2Pix model on 10,000 training pairs and 1,000 test pairs at 256-by-256 resolution, using a 0.1 poison rate for the main comparison. The reported metrics separate model utility—CLIP direction, image, and output similarity—from model specificity—MSE, ASR, and EAR. ASR and EAR use an MSE threshold of 0.1. The robustness suite covers rotation, resized crop, erasing, brightness, contrast, JPEG, blur, and Gaussian noise.

### Results

StegaStamp reports the strongest main-table specificity, while RoSteALS is close and VINE is weaker. Watermark image-quality results expose a tradeoff: VINE reports the highest PSNR/SSIM, while StegaStamp reports the strongest specificity. The ablation indicates that denoising alone is insufficient, MSE alone can damage clean editing, and the combined loss offers the reported balance. The paper also reports a stable ASR trend as the number of trigger-target pairs increases, but does not provide an independently reproducible benchmark package in the inspected sources.

### Limitations

The evidence is narrow: one main editing architecture, one primary dataset family, a fixed secret-message setup, a principal poison rate, a thresholded metric, and author-run experiments. The paper does not establish uncertainty intervals, repeated-seed stability, causal identification of latent residuals, independent reproduction, or transfer to other editing models. The official repository is evidence of implementation availability, not evidence that the results can be reproduced without additional checkpoints, data, configuration, and environment work.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Invisible watermark signals can be used as hidden input conditions in the studied image-editing training setup. | Author method claim | E2 | Supported as a paper-defined mechanism. | High for transcription |
| C2 | StegaStamp and RoSteALS achieve high reported ASR with low EAR at poison rate 0.1. | Author empirical claim | E3 | Supported by Table 1; no independent reproduction. | High for reporting |
| C3 | Robustness is transformation-dependent, with strong response under some erasing/JPEG settings and weak response under rotation/crop/blur. | Author empirical claim | E4 | Supported by Table 2; generalization beyond tested strengths is unknown. | High for reporting |
| C4 | Larger latent residuals help explain stronger trigger response. | Author interpretation | E2-E4 | Plausible correlation, not causal proof. | Medium-low |
| C5 | The combined denoising and MSE objective better balances clean utility and specificity than either loss alone. | Author ablation claim | E5 | Supported for the reported settings. | Medium-high |
| C6 | A public implementation exists. | Source metadata/implementation fact | E6 | Repository is public and linked by the paper; it was not executed here. | High for availability |
| C7 | A defensive guard should join provenance, influence/representation signals, visual forensics, and human review. | Reviewer synthesis | E7-E8 | Useful design inference, not a source-proven deployment result. | Medium |

## Methodology

- `Research objective`: Preserve a complete, source-grounded, public-safe review of arXiv:2506.04879v1 and connect it to three concrete Black Lake defensive research records.
- `Sources inspected`: Verified local PDF and full-paper HTML, public arXiv metadata/full text, DOI, official code repository README, live Black Lake READMEs, live Black-Lake-Data README, three related DEP manuscripts, and repository publication/index context.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`; treated each PDF parent directory as one paper unit; derived the arXiv ID from the filename and local README; used a uniform PowerShell `Get-Random` draw over unique parent units.
- `Inclusion criteria`: Complete primary-paper evidence, stable identifiers, method/results/limitations, official implementation context, and related DEP entries with concrete overlap in backdoor risk, poisoning detection, visual forensics, robustness, or governance.
- `Exclusion criteria`: Abstract-only evidence, unverified summaries, local source paths, operational attack recipes, source-file redistribution, and related entries without a clear conceptual bridge.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, replication, and provenance review.
- `Evidence handling`: Author claims are labeled as claims; reviewer interpretations and implementation proposals are separated; numerical values are tied to tables or cited sections; related DEP material is treated as contextual evidence rather than independent validation.
- `Uncertainty handling`: Missing seeds, intervals, threshold sweeps, external architectures, causal tests, and independent reproduction remain explicit rather than being inferred.
- `Extraction process`: The verified full-paper HTML supplied readable sections, tables, figures, and appendices; the PDF was retained for integrity cross-checking; no source document was copied into the public repository.
- `Version control`: The selected work is pinned to arXiv v1; related DEP paths and repository authorities were read from the live default branches on 2026-08-18.
- `Claim selection`: Priority was given to the two-branch mechanism, Table 1 specificity/utility, Tables 2-4 robustness and ablations, Appendix limits, code availability, and defensive transfer.
- `Cross-checking`: Identity and authors were checked against the canonical arXiv record; method and values were checked across the full-paper HTML and PDF; the official code repository was inspected but not run.
- `Safety handling`: This artifact is defensive and evaluation-only. It does not publish trigger construction, poisoning procedures, operational payloads, or attack code. Any testing must use synthetic/public data, isolated environments, and explicit authorization.
- `Reviewer stance`: Critical paper review, DEP-ready preservation, defensive implementation planning, and replication backlog.
- `Random selection`: 75,967 PDF candidates; 75,964 unique parent-directory units; uniform zero-based index 3,623; first draw accepted after source repair.
- `Deduplication and reselection validation`: Scanned Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data identifier/title search surfaces. Exact arXiv ID and title matches were absent from prior public artifacts; a broad token hit in a metadata-only inventory was unrelated to this paper. Duplicate exclusions: 0. Reselections: 0. Public 24-hour cutoff: 2026-08-17.
- `Source-integrity validation`: Initial state was partial because full-paper HTML was missing. One bounded broker-mediated repair produced a PDF/full-paper HTML pair meeting the size, header, EOF, body, marker, heading, and structure gates. Source package acquisition was unavailable; no source file was uploaded.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2506.04879v1, its reported invisible-watermark/backdoor mechanism, tables and appendices, official implementation context, defensive implications, and exactly three related DEP bridges.
- `Temporal boundary`: Public and repository evidence inspected through 2026-08-18; deduplication used a public 24-hour cutoff of 2026-08-17.
- `Evidence limits`: No model training, attack execution, dataset download, checkpoint download, code execution, independent benchmark, or deployment test was performed.
- `Assumptions`: The canonical arXiv record and v1 full-paper HTML represent the reviewed version; the public repository README accurately describes its current visible setup; related DEP manuscripts accurately preserve their own source reviews.
- `Constraints`: No local paths, usernames, drive names, machine identifiers, local timezone labels, exact execution times, raw source files, extracted source text, or caches may enter public output.
- `Out of scope`: Attack construction, trigger generation, poisoned-data recipes, unauthorized image editing, watermark circumvention, production deployment, and claims about all diffusion models or all watermark systems.
- `Intended use`: Defensive research review, benchmark design, provenance planning, safe MVP ideation, and future authorized replication.
- `Audience`: Vision-security researchers, model-governance teams, image-editing engineers, evaluators, and Black Lake reviewers.
- `Depth target`: Schema-complete manuscript report with evidence ledger and cross-DEP synthesis.
- `Reproducibility boundary`: Readers can trace the public paper and code locator, but cannot assume exact reproduction without the dataset, checkpoints, configurations, seeds, and environment.
- `Operational boundary`: Discussed concepts are for detection, evaluation, simulation, and authorized testing only; the manuscript does not operationalize a backdoor.
- `Data sensitivity`: Public scholarly sources; any real user images, ownership marks, or training data require governance, minimization, consent, and retention controls.

## Observations

- `Observed pattern`: Clean utility and hidden-trigger specificity are separate objectives; a model can preserve ordinary editing while still containing an input-conditioned failure path.
- `Observed pattern`: Watermark image quality and latent separability trade off in the reported tables; pixel-space similarity alone cannot certify behavioral safety.
- `Technical implication`: Robustness must include false activation on clean inputs, not only response to marked inputs.
- `Technical implication`: Provenance records should join input identity, training-data lineage, model version, transformation, output, and reviewer action.
- `Contradiction or tension`: The reported method aims for imperceptible changes while relying on latent differences large enough to steer behavior; that tension is a testable design boundary.
- `Open question`: Whether the latent-residual relationship persists across watermark families and editing backbones is not established.
- `Reviewer hypothesis`: Independent provenance and policy gates will be more durable than a detector that relies on the same representation channel as the edited model.

## Considerations

This is a dual-use security topic. Public artifacts should describe failure modes, evidence boundaries, detection, evaluation, and governance while withholding trigger recipes, poisoned examples, payloads, and unauthorized deployment steps. Research should use synthetic or licensed public images, isolated models, no real-user image collections, and explicit authorization.

An image-editing service should treat clean-input behavior, watermark presence, output similarity, and provenance as separate evidence channels. A failed or missing provenance check should route to review, not silently rewrite the image. The monitoring layer should be independent from the model under test and should record false activations, abstentions, latency, and reviewer outcomes.

The official repository may reduce implementation friction, but its presence does not prove that the paper's tables reproduce. Reproduction requires pinned checkpoints, dataset manifests, transform strengths, seeds, threshold policy, hardware/environment, and a public-safe evaluation harness.

## Strengths

- The paper makes the clean-versus-poisoned behavior split explicit.
- Utility and specificity are evaluated separately instead of collapsing to one score.
- Robustness and loss ablations expose meaningful failure boundaries.
- The method is tied to a concrete image-editing framework and named watermark families.
- The official code locator improves provenance and makes a future authorized replication more feasible.

## Weaknesses

- Results are author-reported and lack independent reproduction, uncertainty intervals, repeated seeds, or broad architecture transfer.
- The main comparison centers on one editing backbone, one data source, one principal poison rate, and a fixed threshold.
- The latent-residual explanation is correlational; a causal intervention or controlled latent-separation study is absent.
- Distortion robustness is incomplete, with rotation, crop, and blur remaining difficult and no adaptive or real-world distribution study.
- Clean false activation, dataset provenance, checkpoint lineage, and operational monitoring are not developed into a deployment contract.
- The topic is dual-use, so public operational detail must remain bounded even though the paper and repository are public.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish fixed manifests and seeds | Reproducibility | Exact data/checkpoint identity is needed to compare runs. | Deterministic reruns and auditability. | Dataset/checkpoint rights and maintenance. | Recreate tables from hashes and version pins. |
| Add threshold and uncertainty sweeps | Evaluation | ASR/EAR depend on an MSE threshold. | Honest operating curves and calibration. | More compute and analysis. | Report intervals, ROC/PR, and clean false activation. |
| Test multiple editing backbones | Generalization | One backbone cannot establish transfer. | Architecture-boundary evidence. | Model and compute cost. | Locked cross-backbone matrix with the same data protocol. |
| Add independent provenance controls | Safety | Hidden behavior is easier to investigate when lineage is explicit. | Faster triage and recovery. | Key management and retention design. | Signed input/output receipts and fault-injection tests. |
| Release a defensive benchmark | Governance | Reproduction should not require operational attack material. | Safer independent evaluation. | Careful curation and disclosure review. | Synthetic marked/clean pairs, fixed denominators, and red-team review. |

## Potential Implementations

1. **Input provenance guard** — `User`: image-editing service operator. `Goal`: prevent unverified inputs from entering consequential editing workflows. `Core mechanism`: verify image identity and signed provenance, run non-invasive watermark/representation checks, and abstain on disagreement. `Required inputs`: public or authorized images, manifests, model/version IDs, and policy. `Outputs`: allow/review record and evidence receipt. `Risk controls`: no automatic attribution, least privilege, retention limits, and human review. `Evaluation`: clean utility, false activation, abstention rate, latency, and audit completeness.
2. **Training-data integrity audit** — `User`: model training and governance team. `Goal`: detect suspicious input-conditioned behavior before release. `Core mechanism`: combine data lineage, influence/representation residual monitoring, clean controls, and fixed-denominator regression tests. `Required inputs`: versioned dataset manifest, model snapshots, safe synthetic controls, and calibration policy. `Outputs`: release gate, anomaly report, and rollback evidence. `Risk controls`: isolated execution, no raw sensitive images in public logs, and independent review. `Evaluation`: seeded benign controls, held-out distributions, false-positive burden, and reproducible evidence.
3. **Visual evidence triage queue** — `User`: safety reviewer or image-forensics analyst. `Goal`: prioritize ambiguous cases without delegating a high-impact decision to one model. `Core mechanism`: retain low-level, semantic, provenance, and uncertainty channels separately, then route disagreements to a human. `Required inputs`: redacted image, channel scores, support counts, and policy context. `Outputs`: review priority, channel-level evidence, and disposition. `Risk controls`: no automatic accusation or denial, appeals, redaction, and retention limits. `Evaluation`: channel ablations, calibration, reviewer agreement, time-to-decision, and subgroup slices.

## Three Ways to Exercise This Research

1. **Synthetic robustness audit** — Use public images and a non-malicious watermarking or transformation library to measure clean-edit utility, image-quality metrics, and representation residuals. Success requires a fixed manifest and complete denominator; stop if the experiment would create a backdoored model or process private images.
2. **Benign distortion matrix** — Apply JPEG, erasing, brightness, contrast, resizing, blur, and noise to authorized inputs and evaluate a defensive integrity/abstention monitor. Success requires transformation-specific utility, false-activation, and abstention curves; stop before any trigger construction or unauthorized model modification.
3. **Provenance tabletop** — Walk a signed image-manifest, model-version, output-receipt, and reviewer-escalation workflow using inert examples. Success requires every decision to be traceable and reversible; stop if the exercise requests real-user images, operational payloads, or autonomous consequential action.

## Example MVP Product

- `Product name`: Watermark-Conditioned Editing Guard
- `Target user`: Vision-model safety and platform-integrity teams.
- `Problem`: Image-editing models may behave differently on subtly transformed inputs while clean-case metrics remain acceptable.
- `Core workflow`: Accept an authorized image and manifest, verify identity and provenance, run independent defensive checks, perform a bounded edit only when policy permits, compare output/utility metrics, and route disagreement to human review.
- `Data requirements`: Public or governed images, signed manifests, model/version hashes, safe calibration sets, transformation definitions, and reviewer labels.
- `Architecture`: Local verifier, isolated evaluation runner, independent policy engine, evidence ledger, review queue, and public-safe Markdown/JSON exporter.
- `Success metrics`: Clean-edit utility, false activation, abstention calibration, provenance coverage, reviewer agreement, latency, and zero unauthorized data export.
- `Risk controls`: Offline-first evaluation, least privilege, no trigger generation, no automatic high-impact decision, source minimization, retention limits, and incident rollback.
- `Limitations`: Cannot certify absence of hidden behavior, watermark legitimacy, or general safety across unseen models and distributions.
- `MVP boundary`: Synthetic/public smoke tests only; no model poisoning, no real-user images, no production release gate without independent review.

## Related Research and Reading

| Item | Type | Relevance | Public locator |
|---|---|---|---|
| Context Backdoor Defense | Related DEP | Provenance, layered controls, runtime interlocks, and safe incident response for hidden context-driven behavior. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-Context%20Backdoor/context_backdoor_defense_manuscript.md |
| TRACE Poison Detection | Related DEP | Influence attribution and recurrence-based detection for poisoned inputs, with explicit evidence limits. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260729-TRACE%20Poison%20Detection/2606.25721-whitepaper-review.md |
| Document Fraud LLM | Related DEP | Visual manipulation triage, calibration, missingness accounting, and human review. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260715-Document%20Fraud%20LLM/document_fraud_llm_manuscript.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2506.04879 | Identity, authors, date, version, abstract, and source locator. | 2026-08-18 | Primary metadata record. |
| R2 | https://arxiv.org/html/2506.04879 | Full method, experiments, tables, robustness, ablation, and appendices. | 2026-08-18 | Primary full-paper HTML. |
| R3 | https://arxiv.org/pdf/2506.04879 | PDF integrity cross-check. | 2026-08-18 | Verified locally; not redistributed. |
| R4 | https://doi.org/10.48550/arXiv.2506.04879 | Persistent identity. | 2026-08-18 | arXiv-issued DOI. |
| R5 | https://github.com/aiiu-lab/BackdoorImageEditing | Official implementation context and license label. | 2026-08-18 | Inspected but not executed. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-Context%20Backdoor/context_backdoor_defense_manuscript.md | Related provenance and runtime-control evidence. | 2026-08-18 | Derived repository artifact. |
| R7 | https://arxiv.org/abs/2408.02882 | Primary source basis for Related DEP 1. | 2026-08-18 | Preserved by the related DEP. |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260729-TRACE%20Poison%20Detection/2606.25721-whitepaper-review.md | Related influence-attribution and poisoning-detection evidence. | 2026-08-18 | Derived repository artifact. |
| R9 | https://arxiv.org/abs/2606.25721v1 | Primary source basis for Related DEP 2. | 2026-08-18 | Preserved by the related DEP. |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260715-Document%20Fraud%20LLM/document_fraud_llm_manuscript.md | Related visual-forensics and calibrated-triage evidence. | 2026-08-18 | Derived repository artifact. |
| R11 | https://arxiv.org/abs/2508.11021 | Primary source basis for Related DEP 3. | 2026-08-18 | Preserved by the related DEP. |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, source locality, attribution, and commit rules. | 2026-08-18 | Live authority read before writing. |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing, publication index, and no-source-upload rules. | 2026-08-18 | Live authority read before writing. |
| R14 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository layout and provenance context. | 2026-08-18 | Live README read before relying on its layout. |
| R15 | Verified local source bundle for arXiv:2506.04879v1 | Full-paper review and integrity evidence. | 2026-08-18 | Local path withheld; no source file uploaded. |

## Appendix

### Selection and Integrity Record

- Candidate enumeration: 75,967 PDFs; 75,964 unique parent-directory paper units.
- Selection: uniform zero-based index 3,623; no manual substitution; first accepted draw.
- Deduplication: exact ID/title/slug checks across Black Lake public artifact surfaces, staging, memory, and Black-Lake-Data search surfaces found no substantive prior artifact; duplicate exclusions 0; reselections 0.
- Source repair: initial `partial` state due to missing full-paper HTML; one bounded repair; final PDF and full-paper HTML passed required integrity gates; source package unavailable.
- Public allowlist: only the log, Report-Mark, DEP README, manuscript, and required DEP-E publication-index Markdown row are intended for staging. No PDF, HTML, source archive, extracted text, cache, local path, or `.source/` directory is part of the DEP.
- Independent reproduction: not performed. The paper's numerical results remain author-reported.
