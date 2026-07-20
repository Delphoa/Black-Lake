# Report-Mark: APB2Face Safety

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P03`
- Review date: 2026-07-20
- Review type: source-first defensive synthetic-media review

## Source Metadata

| Field | Value |
|---|---|
| Paper | *APB2Face: Audio-guided face reenactment with auxiliary pose and blink signals* |
| Authors | Jiangning Zhang; Liang Liu; Zhucun Xue; Yong Liu |
| Stable identifier | arXiv:2004.14569v1 |
| Submitted / venue | 2020-04-30; ICASSP 2020 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2004.14569 |
| Primary record | https://arxiv.org/abs/2004.14569 |
| Verified full-paper HTML | https://ar5iv.labs.arxiv.org/html/2004.14569 |
| PDF | https://arxiv.org/pdf/2004.14569 |
| Source state | Verified complete after bounded ar5iv fallback; all source files withheld locally. |
| Deployment job ID | `BLAD-2200-20260720-8636EDC7` |
| Deployment item ID | `BLAD-2200-20260720-8636EDC7-P03` |

## Concise Research Notes

### Problem and Method

APB2Face decomposes identity-specific, audio-guided face reenactment into two stages. GeometryPredictor fuses MFCC audio features with explicit yaw/pitch/roll and eye-blink controls to predict facial landmarks. FaceReenactor draws those landmarks into a 256x256 geometry image and uses an identity-specific modified Pix2Pix model to synthesize a face. Adversarial landmark and image losses supplement L1 losses; a face-region mask increases reconstruction weight around the face.

The AnnVI dataset contains six announcers and 23,790 frames collected from YouTube, with synchronized audio, landmarks, pose, and blink measurements. The paper states that landmark detections were manually checked. It does not provide an inspected consent, licensing, demographic, retention, or subject-notification protocol.

### Evidence and Results

Adding the landmark discriminator reduces the reported average landmark L1 error from 1.500 plus/minus 0.064 pixels to 0.666 plus/minus 0.034. Across six identities, Table 1 reports average SSIM 0.799, FID 11.862, face-detection rate 98.8%, landmark error 1.429, pose error 0.0195, and blink error 0.0413. The identity-specific reenactor is reported at 75 FPS on a GPU.

The Wav2Pix comparison uses the same identity but not the original data, because the authors say those data were unavailable. Qualitative figures and the source's custom metrics therefore do not constitute a fully matched, independent state-of-the-art evaluation. Dataset scale is six identities, and no cross-dataset or demographic analysis is reported.

### Reviewer Interpretation and Safety

The two-stage geometry interface is useful for audit because pose/blink controls and identity appearance are separated. The same controllability creates impersonation and non-consensual synthetic-media risks. A safe derivative system would require explicit subject consent, identity authorization, dataset rights, output disclosure, provenance binding, misuse monitoring, revocation, and independent detection. This review intentionally omits operational generation code, media, weights, and reproduction steps.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | Canonical arXiv record and DOI | Identity, authors, date, venue, abstract | High | Metadata only. |
| E2 | Verified full paper and PDF | Dataset, architecture, losses, training, metrics, conclusion | High for transcription | No independent rerun. |
| E3 | AnnVI section | Six identities, 23,790 frames, 256x256 processing, annotations | High for source report | Consent/license/demographic protocol not established. |
| E4 | Table 1 and experiments | SSIM/FID/detection/geometry metrics and 75 FPS claim | High for transcription | Custom metrics, narrow identities, hardware unspecified. |
| E5 | Wav2Pix comparison | Claimed visual/metric improvement | Medium | Original comparison data unavailable; matching is limited. |
| E6 | Private process records | Randomness, dedup, repair, integrity, locality | High | Private paths withheld. |
| E7 | Three related DEP manuscripts | Forensics, identity governance, motion-generation safety | Medium | Later systems and different evaluation settings. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md`
   - Relevance: APB2Face creates controllable synthetic media; Document Fraud LLM shows that general-purpose multimodal detectors may remain near chance and argues for layered specialized forensics, calibration, and human review.
   - Source basis: inspected benchmark denominator, AUC results, specialized baselines, omitted-output handling, and review-first architecture.
2. `.lake-data/DEP-E/DEP-E-20260716-Biometric Identity Gaps/biometric_identity_gaps_manuscript.md`
   - Relevance: identity-specific reenactors and synthetic face provisioning share resemblance, consent, biometric-threshold, lifecycle, and revocation risks. Both require a non-biometric alternative and purpose limitation.
   - Source basis: inspected embedding/image gap, exact hard checks, synthetic identity realization, detector evaluation, and governance limitations.
3. `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md`
   - Relevance: both systems turn explicit motion controls into synthetic video. AR-Drag adds modern long-horizon evaluator, cache, physical-plausibility, disclosure, and provenance concerns that APB2Face's narrow image metrics do not cover.
   - Source basis: inspected motion conditioning, autoregressive rollout, evaluator-based rewards, benchmark, limitations, ethics, and provenance boundary.

## Synthesis Note

### Concept Bridge

Synthetic-media quality, controllability, identity rights, and detectability are separate axes. APB2Face measures reconstruction and control on six identity-specific models; the related deposits show why deployment also needs source consent, identity authorization, provenance, manipulation detection, uncertainty, revocation, and human appeal. High SSIM or face-detection rate does not establish safe identity use.

### Potential Implementations

1. **Consent-bound avatar evaluator:** evaluate only authorized identities and require signed scope, expiry, revocation, and output disclosure.
2. **Synthetic-media provenance receipt:** bind source authorization, model/version, control inputs, output hash, watermark status, and distribution policy.
3. **Defensive detector benchmark:** test specialized spatial/temporal/audio-visual detectors with fixed denominators, calibration, and abstention.

### Deeper Relationship Observations

1. Separating landmarks from appearance improves controllability but also makes identity substitution easier to reason about and misuse.
2. An identity-specific reenactor embeds personal appearance in model parameters, creating retention and revocation obligations beyond dataset deletion.
3. Real-time throughput increases distribution risk; provenance and authorization checks must remain in the critical path rather than post-processing.

### Conceptual Similarities

1. APB2Face and AR-Drag expose explicit motion controls whose evaluation requires more than frame realism.
2. APB2Face and Biometric Identity Gaps bind generated faces to identity representations and therefore inherit resemblance and lifecycle risk.
3. APB2Face and Document Fraud LLM require layered forensics because generator and detector evidence are both distribution-sensitive.

### MVP Implementations with Code Mock-Ups

1. **Authorization gate**

```python
def authorized(identity_id, consent):
    return consent["identity"] == identity_id and consent["active"] and consent["scope"] == "avatar"
```

2. **Provenance receipt**

```python
def receipt(output_hash, model_version, disclosure):
    return {"output_hash": output_hash, "model_version": model_version,
            "synthetic_disclosure": bool(disclosure)}
```

3. **Defensive review gate**

```python
def publishable(auth_ok, provenance_ok, forensic_score, threshold):
    return auth_ok and provenance_ok and forensic_score <= threshold
```

### Developer Challenges

1. Enforcing identity authorization and revocation across model checkpoints, caches, previews, and downstream copies.
2. Evaluating audio-visual synchrony, geometry, identity leakage, temporal artifacts, and detector evasion without storing unnecessary biometrics.
3. Binding robust disclosure/provenance to outputs while preserving an immutable consent and model-version receipt.

### Author Challenges

1. Establishing dataset consent, YouTube licensing, subject rights, demographic composition, and permitted redistribution.
2. Expanding beyond six identities with cross-dataset, cross-speaker, demographic, temporal, and independent evaluation.
3. Reporting matched baselines, uncertainty, human studies, provenance, detector performance, and misuse mitigations.

## Validation Notes

- Deployment job `BLAD-2200-20260720-8636EDC7`; item `BLAD-2200-20260720-8636EDC7-P03`.
- Uniform index 65,096 of 75,776 units; first draw; duplicate exclusions 0; reselections 0.
- No duplicate by ID, DOI, normalized title, slug, artifact markers, memory, companion repository, current job, or 24-hour markers.
- Partial archive repaired to complete with approved ar5iv fallback; PDF and HTML gates passed.
- Full paper, table, figures, metadata, and exactly three related manuscripts inspected; no data, model, code, or experiment rerun.
- Exactly three entries appear in every required Synthesis Note list; code mock-ups are defensive and non-generative.
- Public sanitization passed subject to final scan; no `.source/` and no source file eligible for staging.

## Attribution Block

- https://arxiv.org/abs/2004.14569 - identity, authors, date, abstract, venue, DOI, source locators.
- https://ar5iv.labs.arxiv.org/html/2004.14569 - verified full-paper dataset, method, experiments, table, conclusion; local copy withheld.
- https://arxiv.org/pdf/2004.14569 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2004.14569 - persistent identity.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260715-Document%20Fraud%20LLM - defensive forensics synthesis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Biometric%20Identity%20Gaps - biometric identity-governance synthesis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260720-AR-Drag%20Motion - controllable-video safety synthesis.
- Source files: verified PDF, fallback HTML, metadata HTML, and private verification records; all withheld locally. Zero source uploads. Job `BLAD-2200-20260720-8636EDC7`, item `BLAD-2200-20260720-8636EDC7-P03`.
