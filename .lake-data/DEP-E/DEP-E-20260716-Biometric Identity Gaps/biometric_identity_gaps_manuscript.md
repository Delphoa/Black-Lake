---
title: "Biometric Identity Gaps - DEP-E"
description: "Source-grounded review of gallery-relative virtual biometric identity provisioning."
date: "2026-07-16"
authors:
  - "OpenAI Codex"
artifact_type: "research-manuscript"
dep_class: "DEP-E"
source_arxiv_id: "2605.18238v1"
source_doi: "10.48550/arXiv.2605.18238"
status: "deposited"
tags:
  - arxiv
  - biometrics
  - face-recognition
  - synthetic-identities
  - identity-governance
  - computer-vision
  - safety
---

# Biometric Identity Gaps - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract record | Primary metadata | HTML | arXiv:2605.18238v1; DOI 10.48550/arXiv.2605.18238 | https://arxiv.org/abs/2605.18238v1 | Public metadata; abstract is not full-paper evidence | 2026-07-16 | Inspected |
| S2 | arXiv paper | Primary artifact | PDF | v1; 25 pages; 11 figures reported | https://arxiv.org/pdf/2605.18238 | Complete local copy inspected; file withheld | 2026-07-16 | Inspected in full |
| S3 | arXiv full-paper rendering | Primary artifact | HTML | official v1 rendering | https://arxiv.org/html/2605.18238 | Complete local copy inspected; file withheld | 2026-07-16 | Inspected in full |
| S4 | arXiv source package | Primary artifact | TeX/source archive | v1; main, sections, appendix, and figures | https://arxiv.org/e-print/2605.18238 | Local package inspected; file withheld | 2026-07-16 | Inspected |
| S5 | VILab publication metadata | Official author-lab availability record | JSON in Git repository | commit 271cb74f57f5e26e74f0bd62398742a0b4d46487 | https://github.com/VILab-Drexel/VILab.github.io/blob/271cb74f57f5e26e74f0bd62398742a0b4d46487/info.json | Code and project fields were empty for this paper | 2026-07-16 | Inspected |
| S6 | Document Fraud LLM DEP | Related Black Lake artifact | Markdown | DEP-E-20260715-Document Fraud LLM | `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` | Context only; does not validate S1-S5 claims | 2026-07-16 | Inspected |
| S7 | BA-LoRA Bias DEP | Related Black Lake artifact | Markdown | DEP-E-20260709-BA-LoRA Bias | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` | Context only; does not validate S1-S5 claims | 2026-07-16 | Inspected |
| S8 | Mosaic Safety DEP | Related Black Lake artifact | Markdown | DEP-E-20260709-Mosaic Safety | `.lake-data/DEP-E/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md` | Context only; does not validate S1-S5 claims | 2026-07-16 | Inspected |
| S9 | Black Lake README | Repository authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | DEP naming, contents, attribution, and source-withholding rules | 2026-07-16 | Inspected live |
| S10 | Selection, integrity, cache, and dedup records | Processing evidence | Public-safe summaries | 75,776 units; index 28,438 | This manuscript, Methodology and Appendix | No local path or exact execution timestamp | 2026-07-16 | Generated and validated |

Paper metadata:

- `Full title`: Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning.
- `Authors`: Yuyang Ji, Yixuan Shen, Anil Jain, Xiaoming Liu, and Feng Liu.
- `Affiliations`: Drexel University, Michigan State University, and University of North Carolina at Chapel Hill.
- `Initial arXiv submission`: 2026-05-18.
- `Subject`: Computer Vision and Pattern Recognition (`cs.CV`).
- `Source-declared length`: 25 pages and 11 figures.
- `Public implementation status`: no code, project, dataset, model-weight, or environment link appears in the paper text or inspected author-lab metadata.
- `Source files deposited`: none; no `.source/` directory was created.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S4 | Primary metadata/full text | Title, authors, date, subject, abstract, sections, equations, tables, appendices | Identity and complete paper coverage | High | Metadata alone does not validate claims |
| E2 | S2-S4, Sections 3.1-3.2 | Primary method/theory | Gallery-relative definition, thresholds, centroid model, repulsion/PCA proposal, hard checks | Allocation formulation and mechanism | High for transcription | Exact-check scalability and encoder dependence not independently tested |
| E3 | S2-S4, Appendix C | Primary mathematical analysis | PCA dimensions, spherical-cap volume, GV bound, safety buffer, empirical capacity estimator | Capacity/headroom analysis | Medium-high | Paper itself calls the submanifold mapping an approximation, not a rigorous face-manifold bound |
| E4 | S2-S4, Sections 3.3 and Appendix D | Primary method | GapGen curriculum, round-trip loss, frozen SDXL/encoder, InstantID components | Image realization mechanism | High for source reporting | No code, weights, data manifest, or execution |
| E5 | S2-S4, Tables 1-2 | Primary empirical evidence | 100K-10M embeddings, thresholds/alpha, baseline and 10K-1M image results | Allocation and realization results | High for transcription | Text/caption inconsistency and no independent reproduction |
| E6 | S2-S4, Figure 5 and Appendix C.7 | Primary empirical/model evidence | Held-out WebFace4M test, rare-event model, confidence interval, assumption audit | Open-world assessment | Medium | One held-out source; dependence and demographic density remain material |
| E7 | S2-S4, Table 3 and Appendix E | Primary empirical evidence | v-LFW, IAPCT, deepfake-detector results, unified metric | Recognition/detection evaluation | High for transcription | Generator-specific benchmark and detector training/protocol boundaries |
| E8 | S2-S4, conclusion/ethics | Primary limitations and safety claims | Gallery relativity, revocation, capacity approximation, encoder limitation, misuse discussion | Scope and governance review | High for source wording | Ethics discussion is brief and some safety conclusions exceed the evidence |
| E9 | S5 | Official availability evidence | Empty code/project fields in authors' lab entry | Reproducibility availability | High for inspected record | A release could appear later; absence is time-bounded |
| E10 | S6-S8 | Related DEP artifacts | Forensic calibration, bias/diversity, runtime monitoring/falsification | Cross-DEP synthesis | Medium-high | No joint experiment exists |
| E11 | S9-S10 | Repository/process evidence | Live authority, uniform draw, integrity gate, extraction cache, dedup scans | Compliance and selection provenance | High | Search coverage depends on current repository text and checkout |

## Executive Summary

The paper proposes Biometric Identity Provisioning (BIP): allocate synthetic face identities for digital entities so that a chosen face-recognition encoder does not match them to any enrolled real identity, while also keeping virtual identities mutually separable and renderable as high-quality face images. It frames this as a gallery-relative packing problem on a normalized face-embedding hypersphere.

The allocation method is conceptually clean. Real identity centroids are derived with ArcFace ResNet-100. A candidate starts near a real centroid, moves against the weighted centroid of nearby identities, adds PCA-scaled noise, and is normalized. It is accepted only after hard cosine checks against every enrolled real centroid and every previously accepted virtual identity. The hard checks—not the repulsion heuristic—provide the stated allocation property.

The paper reports an impressive embedding-scale demonstration but uses language that can obscure a second stage. At `tau = 0.391` and `alpha = 4`, Table 1 displays 100.00% non-collision and 99.98% inter-class separation for 10M allocated embeddings. The caption and nearby prose round this to 100%/100%, creating a small but real inconsistency. More importantly, after GapGen renders images and the images are re-encoded, the 1M result is 98.07% non-collision and 78.36% inter-class separation. “Ten million non-colliding identities” therefore describes hard-checked embedding positions, not one million fully successful rendered biometric classes.

The capacity appendix is more cautious than the abstract. PCA finds 95% of variance in 269 of 512 components, and a spherical-cap Gilbert-Varshamov reference gives about `7.41e10` positions at the primary threshold. The paper explicitly says this is an ambient-sphere reference under a submanifold approximation, not a rigorous lower bound for the empirical face manifold. The empirical collision estimator also depends on rare-event, distribution, and weak-dependence assumptions.

The open-world, v-LFW, and detector experiments are useful tests, not universal guarantees. A held-out WebFace4M set of 180K identities shows near-zero collision for 1M virtual embeddings at the default setting as the test gallery grows. v-LFW reports R-V false-accept rate 0.01%, detection AUC 98.13%, and unified accuracy 99.20%. Five deepfake detectors report 87.76%-99.57% accuracy on BIP images. These results do not establish cross-encoder persistence, demographic fairness, site/device robustness, adaptive-attack resistance, or absence of resemblance to people outside a finite gallery.

The governance question is more important than the packing result. A face is not necessary for an AI agent or robot; assigning one can amplify anthropomorphic deception, surveillance, KYC/Sybil, consent, and identity-fraud risks. Any research continuation should start with non-biometric alternatives and a purpose-limitation review. If a face is justified, the identity becomes a revocable, versioned credential bound to one encoder, gallery, threshold, generation model, and monitoring policy—not a permanent identity guarantee.

## Detailed Summary

### Problem Formulation

Let `phi` map a face image to a normalized vector on a `d`-dimensional unit sphere. The deployed face matcher accepts two embeddings as the same identity when cosine similarity is at least threshold `tau`. Each real identity is represented by a normalized mean of its image embeddings, producing gallery `R`.

BIP seeks virtual embeddings `V` satisfying two hard constraints:

- every virtual-to-real similarity is below `tau`; and
- every distinct virtual-to-virtual similarity is below `tau`.

A third requirement is image-level realizability: each virtual embedding should be rendered as a plausible face whose re-encoded embedding still satisfies both constraints. The first two constraints can be checked exactly in embedding space. The third introduces a learned generator and therefore a fidelity gap.

The paper explicitly calls the guarantee gallery-relative. If new real identities are enrolled, any virtual identity that crosses the threshold must be revoked and reassigned. Exact comparison costs scale as the number of virtual identities times new enrollments; approximate nearest-neighbor indexing is suggested. In a safety-sensitive setting, an approximate index must have a measured recall bound or exact verification stage, because a false negative is precisely a missed collision.

### Geometry of the Real Identity Manifold

The study uses a 512-dimensional ArcFace ResNet-100 trained on Glint360K and a gallery of 360,232 real identity centroids. PCA reports effective rank 238.4; 50% of variance appears within 93 components, 90% within 238, 95% within 269, and 99% within 306. The smallest eigenvalue is described as five orders of magnitude below the largest.

The authors infer that realizable virtual faces should remain near the same dominant directions instead of occupying arbitrary low-variance directions. This is plausible as an engineering prior, but PCA energy is not a proof of a smooth 269-dimensional sphere, and an encoder trained on real faces can still map generated images unpredictably outside its training support.

### Repulsion-Based Allocation

For a selected real reference centroid, the method finds `K` nearest real neighbors and forms a temperature-weighted neighborhood centroid. Its negative normalized direction is the repulsion heuristic. Gaussian coefficients along PCA directions, scaled by each direction's standard deviation, add diversity. A perturbation strength `alpha` moves the candidate away from the reference before normalization.

The method then rejects any candidate that violates a virtual-to-real or virtual-to-virtual threshold. Induction makes the accepted set satisfy the checked constraints, assuming exact comparisons, a fixed gallery, a fixed encoder, a fixed threshold, and no numerical error. The proposal only affects acceptance efficiency and realizability; it does not itself guarantee safety.

Increasing `alpha` improves distance from enrolled identities but moves the condition further from the generator's real-face training support. This is the central allocation-realization tradeoff. The default configuration uses `tau = 0.391`, `alpha = 4`, `K = 10`, temperature `0.1`, and PCA-noise weight `1.0`.

### GapGen Image Realization

GapGen builds on InstantID with an SDXL backbone. It receives an allocated ArcFace embedding and produces a 1024-by-1024 portrait. Fine-tuning mixes real FFHQ steps and virtual steps. Real steps use denoising, round-trip identity, and perceptual losses. Virtual steps have no target image; they sample an allocated embedding and optimize the cosine similarity between that target and the frozen encoder's embedding of the generated result.

The SDXL UNet, text encoders, and face encoder remain frozen; IP-Adapter cross-attention projections and IdentityNet are fine-tuned. The appendix reports 30 sampling steps and fixed guidance/control scales. Multiple images for one identity vary prompts, landmarks, and seeds.

Round-trip optimization is circular in an important sense: the same encoder defines the target geometry, trains the identity loss, and measures success. This is internally consistent but may overfit one model's invariances. Cross-encoder agreement is necessary before claiming a persistent identity recognizable across systems.

### Capacity Analysis

The appendix defines a spherical cap with cosine radius `tau` and applies a Gilbert-Varshamov covering argument. On the full 512-dimensional sphere, the reported reference is about `5.75e19`. Substituting the PCA dimension of 269 gives about `7.41e10` at `tau = 0.391`.

The authors correctly qualify the second number: mapping the empirical face manifold to a 268-sphere is a capacity-scale approximation, and a 67-degree cap is not locally small. The value is a headroom reference, not a rigorous face-manifold packing lower bound.

A safety buffer provisions below `tau`, creating a monitoring zone. At `tau_safe = 0.360`, the reported GV reference drops to `1.81e9`, about 1,810 times 1M identities. At `tau_safe = 0.319`, it drops to `2.38e7`, about 24 times 1M. This demonstrates that “vast capacity” depends strongly on threshold and buffer.

The empirical capacity estimator models held-out pair collisions with a Poisson approximation. It distinguishes empirical inverse collision probability from the spherical packing reference and includes exact Poisson intervals. The source also notes that demographic clustering violates uniformity and that collision events are not exactly independent. A flat gallery-size curve is informative but cannot prove absence of demographic-density bias.

### Threshold Selection

The main threshold is calibrated on IJB-B 1:1 verification using ArcFace ResNet-100. The appendix reports 8.01M pairs, AUC 99.49%, and the selected `tau = 0.391` at approximately `2e-5` false-accept rate and 94.30% true-accept rate.

The direction of threshold stringency can be confusing. A larger similarity threshold produces a smaller acceptance cap and a looser BIP exclusion region, even though it represents a stricter face matcher. A smaller threshold accepts more impostor pairs and forces virtual identities farther from real centroids. Operational policy must therefore version the encoder, alignment pipeline, score calibration, threshold, and reference population together.

### Embedding Allocation Results

Table 1 crosses provisioning scale, `alpha`, and six thresholds. At the primary threshold:

- `alpha = 2` yields about 85.6% non-collision, showing the proposal alone is insufficient;
- `alpha = 3` reaches about 99.98% non-collision;
- `alpha = 4` or 5 displays 100.00% non-collision from 100K through 10M;
- at 10M and `alpha = 4`, inter-class separation is 99.98%, not exactly 100%.

At the more permissive recognition threshold `tau = 0.319`, 10M inter-class separation at `alpha = 4` is only 66.99%. Capacity and separability are therefore operating-point claims, not scale-independent facts.

The nearby prose says 100%/100% at 10M while the table shows 100.00%/99.98%. This does not overturn the main result but should be corrected because the work is explicitly about zero collision and exact scale.

### Image Realization Results

Table 2 re-encodes generated images with the same frozen ArcFace model. At 10K, BIP+GapGen reports 98.43% non-collision, 99.57% inter-class separation, FID 56.20, and 87.94% round-trip pass rate. At 100K the values are 98.38%, 97.84%, FID 54.63, and 89.42%. At 500K, inter-class separation falls to 86.30%. At 1M, the reported values are:

- non-collision: 98.07%;
- inter-class separation: 78.36%;
- FID: 56.47;
- round-trip pass rate: 88.75%.

These results are strong relative to the tested synthetic-face baselines, but they invalidate any literal transfer of the embedding hard-check guarantee to every rendered image. At 1M, roughly 1.93% fail the reported non-collision criterion and 21.64% fail the inter-separation metric as defined. The paper acknowledges the realization gap; public summaries should preserve it.

FID against FFHQ measures distributional image statistics, not consent, uniqueness, identity stability, demographic fairness, or absence of resemblance. Qualitative examples likewise cannot establish those properties.

### Open-World Evaluation

The open-world test fixes 1M virtual embeddings and compares them with up to 180K held-out WebFace4M identities, described as disjoint from the enrollment gallery. At the default `alpha = 4`, the plotted collision rate remains near zero as the held-out gallery grows from 10% to 50% of the 360K enrollment size.

This is meaningful evidence beyond the construction gallery. It remains one dataset/encoder pipeline and may share upstream acquisition or training characteristics. The experiment does not cover future demographic shifts, children/aging, accessories, medical changes, sensor changes, adversarial enrollment, identity overlap, capture-quality tails, or a new encoder. “Open-world” should therefore mean held-out-gallery evaluation, not a permanent universal guarantee.

### v-LFW, Detection, and Unified Evaluation

v-LFW mirrors LFW with 5,749 virtual identities and 13,233 generated images. It retains LFW's ten folds and 600-pair structure while adding virtual-virtual, real-virtual, per-image detection, and unified recognition-plus-detection protocols.

The BIP+IAPCT result reports R-R accuracy 99.80%, V-V accuracy 99.18%, R-V false-accept rate 0.01%, detection AUC 98.13%, and unified accuracy 99.20%. The prose rounds R-V FAR to approximately zero. The diagnostic IAPCT head is trained on 100K GapGen virtual images while the ArcFace recognition path stays frozen, so it is an in-family detector evaluation rather than general zero-shot evidence.

Five separate detectors trained on AIFaceFairnessBench are applied without BIP-specific fine-tuning and report 87.76%-99.57% accuracy. This is useful cross-detector evidence. Accuracy without a complete class-balance, subgroup, operating-point, and adaptive-attack report does not show that “no new forensic risks” exist. High detectability today can also erode when a generator is optimized against the detectors.

### Ethics and Identity Governance

The paper states that BIP provisions identities for digital entities rather than clones of real people, that images remain detectable, and that an attacker would need gallery access. It states that training data are used under their licenses and that v-LFW contains no real person's likeness.

These claims need a stricter interpretation. A finite gallery and one embedding model cannot establish absence of resemblance to every person, including unenrolled individuals or visual similarity outside ArcFace. License compliance does not by itself establish consent or acceptable biometric reuse. An attacker may not need a full gallery: partial knowledge, score queries, weak matchers, or a target-specific evasion objective may suffice.

The first governance gate is necessity. Digital agents already have cryptographic, organizational, and device credentials. A synthetic human face can create unwarranted trust and obscure machine status. If a visual identity is needed, non-human marks, explicit machine labels, signed display attestations, and changeable avatars may be safer than a face designed to occupy biometric space.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | BIP formalizes gallery-relative virtual-to-real and virtual-to-virtual exclusion constraints. | Author formulation | E2 | Directly supported and operationally clear for a fixed encoder/gallery/threshold. | High |
| C2 | Repulsion plus PCA-aware noise efficiently proposes candidates while hard checks enforce the constraints. | Author method claim | E2 | The source makes the guarantee/check distinction explicit; efficiency was not reproduced. | Medium-high |
| C3 | The face manifold has vast capacity for virtual identities. | Author theoretical/interpretive claim | E3 | Spherical references show model headroom, but the empirical face-manifold bound is explicitly approximate. | Medium |
| C4 | Ten million virtual embeddings can be allocated with zero observed real-gallery collision at the primary threshold. | Author empirical claim | E5 | Table shows 100.00% non-collision; inter-separation is 99.98%, despite 100%/100% prose. | High for transcription; low for reproduction |
| C5 | GapGen realizes allocated positions as non-colliding high-fidelity faces at million scale. | Author empirical claim | E4, E5 | Partially supported: image-level non-collision is 98.07%, inter-separation 78.36%, and RT pass 88.75% at 1M. | Medium |
| C6 | Open-world non-collision persists as an unseen gallery grows. | Author empirical claim | E6 | Supported for one 180K held-out source and one encoder/threshold, not as a universal guarantee. | Medium |
| C7 | Existing detectors cover BIP faces without modification. | Author safety claim | E7 | Five zero-shot detectors perform well, but class balance, subgroups, attacks, and transfer limit the conclusion. | Medium-low |
| C8 | v-LFW supports joint real/virtual verification and detection. | Author benchmark claim | E7 | The protocol and reported metrics support an initial benchmark; generator-specific artifacts may simplify detection. | Medium-high |
| C9 | BIP does not introduce new forensic risks and v-LFW contains no real person's likeness. | Author ethics/safety claim | E8 | Too strong for a finite gallery, one encoder, one generation family, and non-adaptive detector tests. | Low |
| C10 | A responsible system must treat provisioned faces as revocable, versioned credentials with monitoring and non-biometric alternatives. | Reviewer synthesis | E8, E10 | Grounded in the paper's gallery-update remark and related governance artifacts. | Medium-high |
| C11 | The paper passed first-draw eligibility after local integrity repair. | Process claim | E11 | Source gate, cache, and dedup records support the claim. | High |

## Methodology

- `Research objective`: Select one eligible local arXiv paper uniformly, enforce source integrity before review, reconstruct the paper source-first, select exactly three related DEP entries, and create a schema-complete public-safe DEP-E artifact.
- `Sources inspected`: verified full PDF; official full-paper HTML; metadata HTML; TeX/source including appendices and tables; arXiv metadata; authors' lab publication metadata; live Black Lake authority; dedup locations and automation memory; and exactly three related DEP manuscripts.
- `Discovery strategy`: enumerate PDFs with `rg --files -g "*.pdf"`; collapse unique parent directories into paper units; draw a uniform zero-based PowerShell `Get-Random` index; inspect adjacent metadata; derive and verify the arXiv ID.
- `Inclusion criteria`: primary/official sources establishing identity, formulation, method, results, limitations, ethics, availability, repository rules, duplicate status, or concrete conceptual overlap.
- `Exclusion criteria`: abstract-only text as full-paper evidence, duplicate/recent deposits, secondary summaries where primary text existed, operational biometric instructions, unrelated DEP entries, and unsupported claims of universal safety.
- `Analytical approach`: mathematical reconstruction, table reconciliation, allocation-versus-realization comparison, capacity-bound critique, open-world/protocol analysis, availability audit, ethics/threat review, and defensive product translation.
- `Evidence handling`: author theory, empirical claims, author limitations, reviewer critiques, synthesis, and process evidence are labeled separately. Numerical claims map to source tables or appendices.
- `Uncertainty handling`: no experiment was rerun; “zero observed” is not “zero possible”; approximations, table/text conflict, availability gaps, detector transfer, and governance risks remain explicit.
- `Source integrity`: the unit began `partial` because full-paper HTML was absent. Official HTML, metadata, and source were downloaded with bounded requests, verified, and recorded. Final state `complete`; zero partials.
- `Extraction process`: preflight found `pypdf`; missing-only extraction used `pypdf`, `html-regex`, and `tarfile` on the complete local unit.
- `Cache methodology`: initial miss; 1.4-second backfill; 84,547 bytes of PDF text, 112,658 bytes of HTML text, and 152,886 bytes of source text; final status `cached`.
- `Random selection`: 75,777 PDFs collapsed to 75,776 unique parent-paper units; zero-based selected index 28,438; accepted first draw; exclusions 0; reselections 0.
- `Dedup and reselection validation`: arXiv ID, DOI, normalized title, slug, logs, reports, DEP paths, public pointer, memory, companion repository, and preceding-24-hour markers were searched; no match.
- `Version control`: paper pinned to arXiv v1; author-lab metadata pinned to commit `271cb74f57f5e26e74f0bd62398742a0b4d46487`.
- `Safety handling`: this artifact does not expose source embeddings, galleries, face images, weights, code, or operational evasion instructions. Implementations are limited to synthetic/offline audit, governance, revocation, and evidence tooling.
- `Reviewer stance`: critical preservation, reproducibility/availability review, defensive systems analysis, and rights-aware governance.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2605.18238v1; BIP formulation; allocation; GapGen; capacity model; threshold; embedding/image/open-world/v-LFW/detector results; ethics; availability; and three related DEP bridges.
- `Temporal boundary`: paper pinned to v1 submitted 2026-05-18; source and availability inspection date-only through 2026-07-16.
- `Core technical assumptions`: fixed ArcFace encoder and alignment, meaningful identity centroids, fixed threshold, representative gallery, exact hard checks, stable score distribution, PCA as a useful proposal geometry, and generator/encoder round-trip fidelity.
- `Capacity boundary`: the 269-dimensional spherical model is a headroom approximation, not a proven geometry or capacity of all realizable faces.
- `Open-world boundary`: one held-out gallery is not the open world; new identities, model updates, demographics, sites, sensors, and attacks require fresh validation.
- `Rights boundary`: a matching threshold does not establish consent, likeness rights, data provenance, or lawful biometric processing.
- `Safety boundary`: high detector accuracy is not universal detectability or misuse prevention. No production access-control, KYC, surveillance, or identity system should be built from this artifact.
- `Availability boundary`: no official code/project/data/model release was identified, so results cannot be independently reproduced from the public record inspected.
- `Public-output boundary`: all primary sources and extraction derivatives stay local; the public deposit contains only derived Markdown plus required index/pointer JSON.

## Observations

- The hard-check allocation property is deterministic relative to a frozen gallery, but image realization is probabilistic and materially weaker at scale.
- The paper's own revocation remark converts identity provisioning into continuous lifecycle management rather than one-time generation.
- The 10M headline mixes zero real-gallery collision with 99.98% virtual separation; exact wording matters in a “non-collision” paper.
- The safety buffer consumes capacity rapidly, showing that operational uncertainty cannot be added for free.
- The same encoder defines allocation, trains round-trip fidelity, and evaluates success, increasing model-specificity.
- Near-zero held-out collision can coexist with demographic-density bias if the virtual set occupies underrepresented regions.
- Generator artifacts may make BIP images detectable now while also making the benchmark less representative of future generators.
- Non-human digital identity can be represented without entering human biometric space at all.

## Considerations

- Establish necessity and compare cryptographic/non-biometric identity alternatives before any face-based work.
- Use licensed, consent-aware, identity-disjoint galleries with documented demographic and acquisition coverage.
- Version encoder, alignment, gallery, threshold, approximate-index parameters, generator, and detector as one policy bundle.
- Preserve an exact final collision check even if approximate retrieval accelerates candidate search.
- Evaluate cross-encoder collision and round-trip stability; a single-model pass is insufficient.
- Report absolute failure counts, not only percentages, especially at million scale.
- Treat every generated failure as a revocation/repair event and model operational burden.
- Audit resemblance beyond the chosen encoder with human rights review and independent models without claiming universal absence.
- Red-team Sybil, KYC, enrollment poisoning, score-query, adaptive detector-evasion, and identity-cloning scenarios.
- Publish subgroup performance and threshold sensitivity, including intersections and tail capture conditions.
- Keep real/virtual labeling externally visible and cryptographically bound to the entity's non-human status.
- Make revocation, incident response, appeal, audit access, and deletion first-class requirements.

## Strengths

- The paper defines a previously vague identity-allocation objective with explicit real/virtual and virtual/virtual constraints.
- It correctly separates proposal geometry from hard-check enforcement.
- The appendix exposes threshold, capacity, safety-buffer, and rare-event assumptions in unusual detail.
- Scale experiments cross three provisioning sizes, four perturbation strengths, and six operating thresholds.
- Image-level re-encoding reveals rather than hides the allocation-realization gap.
- The paper includes held-out-gallery, detector, and combined real/virtual protocols.
- The conclusion acknowledges gallery relativity, revocation, approximate capacity, generator fidelity, and encoder specificity.

## Weaknesses

- The abstract/main narrative can conflate allocated embeddings with successfully realized biometric identities.
- A 100%/100% prose/caption claim conflicts with a 100.00%/99.98% 10M table cell.
- One encoder defines target space, training loss, and evaluation, leaving cross-model validity unknown.
- No official code, model, dataset, project, or executable manifest was linked in inspected sources.
- Capacity references rely on an approximate spherical submanifold model and distribution assumptions.
- Open-world evidence is one held-out source and does not cover longitudinal or adversarial conditions.
- FID and selected images do not establish identity rights, consent, demographic parity, or absence of resemblance.
- Detector accuracy and generator-trained IAPCT do not prove universal forensic coverage.
- The ethics section understates Sybil, KYC, anthropomorphic deception, surveillance, and gallery-query risks.

## Potential Improvements

- Rename outputs consistently as allocated embeddings versus realized face instances and publish exact failure counts.
- Correct the 10M table/caption inconsistency and avoid rounding away failed pair constraints.
- Release a licensed implementation, synthetic test fixture, model cards, data manifests, and one-command table reproduction.
- Add cross-encoder and cross-alignment tests with independent commercial/open recognition models.
- Validate exact nearest-neighbor recall after any approximate indexing stage.
- Expand open-world testing across identity-disjoint datasets, sites, devices, ages, demographics, and time.
- Provide dependence-aware confidence intervals and subgroup collision-density estimates.
- Build a repair/revocation cost analysis for failed and newly colliding identities.
- Test adaptive attacks against both the matcher and forensic detectors.
- Compare face identities against explicit non-human visual identities and signed credential displays in user studies.
- Conduct independent biometric-privacy, likeness, consent, discrimination, accessibility, and child-safety review.
- Require visible synthetic-entity disclosure and cryptographic attestation that persists across rendering changes.

## Potential Implementations

1. **Synthetic collision audit harness:** operate only on randomly generated unit vectors and toy galleries to test threshold versioning, exact-versus-approximate recall, failure counts, and revocation policies without real biometric data.
2. **Identity lifecycle ledger:** record the non-human entity, credential, visual asset hash, encoder/gallery/threshold versions, audit outcome, disclosure status, expiry, revocation, and human approval; store no raw face image or embedding in the public ledger.
3. **Biometric necessity and misuse review:** a release gate compares non-biometric alternatives and documents rights, consent, demographic, resemblance, Sybil/KYC, detector, red-team, incident, and deletion evidence before any authorized experiment.

## Three Ways to Exercise This Research

1. **Toy capacity reconciliation:** reproduce cap-volume calculations on low-dimensional synthetic spheres, compare exact packing search with the GV reference, and show where a submanifold approximation stops being a guarantee.
2. **Lifecycle simulation:** use synthetic vectors to simulate gallery growth, threshold changes, approximate-index misses, revocation queues, and repair capacity; measure failures and reviewer workload.
3. **Governance tabletop:** evaluate three alternatives—cryptographic badge, non-human avatar, and synthetic face—against purpose, transparency, accessibility, privacy, deception, attack, revocation, and accountability criteria.

## Example MVP Product

**MVP: Virtual Identity Safety Ledger**

The MVP is an offline governance and test tool. It does not generate faces, store real biometric embeddings, connect to access control, or make identity decisions. It accepts synthetic vector fixtures and a policy record, then:

1. verifies that a non-biometric alternative analysis and authorized purpose exist;
2. checks exact synthetic collision and separation counts for every policy version;
3. compares approximate search with exact ground truth and fails on any missed neighbor;
4. simulates new enrollments, threshold drift, expiry, revocation, and reassignment workload;
5. records disclosure, rights review, subgroup-test placeholders, red-team evidence, and human sign-off;
6. exports a public-safe summary containing no face, embedding, gallery, secret, or local path.

Release criteria are intentionally strict: all checks have fixed denominators; failures remain visible; no “approximately zero” is promoted to zero; policy changes invalidate prior results; and absence of governance evidence blocks progression.

## Related Research and Reading

1. **Document Fraud LLM** - `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md`. Its forensic review shows why omitted outputs, changing denominators, weak calibration, and near-chance image-level aggregation can invalidate a seemingly useful detector. The bridge is fixed-denominator identity/detection reporting and human-supervised hybrid evidence.
2. **BA-LoRA Bias** - `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`. Its bias and representation-collapse analysis shows that aggregate diversity is not minority-group performance and that inherited data imbalance needs explicit monitoring. The bridge is demographic density, synthetic identity diversity, and post-deployment bias governance.
3. **Mosaic Safety** - `.lake-data/DEP-E/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`. Its abstract-state monitor, independent safety query, fallback controller, and falsification workflow offer a lifecycle pattern. The bridge is gallery/update state, collision query, revocation/fallback, and adversarial search—while preserving that a weak fallback can make outcomes worse.

## Source References

1. Ji, Y.; Shen, Y.; Jain, A.; Liu, X.; Liu, F. *Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning*. arXiv:2605.18238v1. https://arxiv.org/abs/2605.18238v1
2. Primary paper PDF. https://arxiv.org/pdf/2605.18238
3. Official full-paper HTML. https://arxiv.org/html/2605.18238
4. Primary TeX/source package. https://arxiv.org/e-print/2605.18238
5. Canonical arXiv DOI. https://doi.org/10.48550/arXiv.2605.18238
6. VILab publication metadata at inspected commit. https://github.com/VILab-Drexel/VILab.github.io/blob/271cb74f57f5e26e74f0bd62398742a0b4d46487/info.json
7. Document Fraud LLM DEP. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Document%20Fraud%20LLM/document_fraud_llm_manuscript.md
8. BA-LoRA Bias DEP. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-BA-LoRA%20Bias/ba-lora-bias-manuscript.md
9. Mosaic Safety DEP. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-Mosaic%20Safety/mosaic_safety_manuscript.md

## Appendix

### Selection and Dedup Record

- Enumeration: 75,777 local PDFs with `rg --files -g "*.pdf"`.
- Unit normalization: 75,776 unique PDF parent directories.
- Uniform draw: PowerShell `Get-Random`, zero-based index 28,438.
- Acceptance: first draw; exclusions 0; reselections 0.
- Dedup keys: arXiv ID, DOI, normalized title, slug, artifact paths, memory, companion repository, and preceding-24-hour markers.
- Result: no prior research artifact matched.

### Integrity and Cache Record

- Initial classification: `partial` because the PDF was valid but full-paper HTML was absent.
- PDF: 8,894,821 bytes; 25 pages; `%PDF-` header; trailing `%%EOF`.
- Repair: official arXiv full-paper HTML, metadata HTML, and source package succeeded with bounded requests.
- HTML verification: 658,614 bytes; 109,692 body characters; document marker; 49 headings; six structure terms.
- Metadata HTML: 44,131 bytes; abstract/metadata only.
- Source package: 8,262,552 bytes; 24 entries.
- Partials after repair: 0; final state `complete`.
- Cache: initial miss; missing-only backfill in 1.4 seconds; final status `cached`.
- Extracted text: PDF 84,547 bytes; HTML 112,658 bytes; source 152,886 bytes.
- Public-source gate: source documents, images, embeddings, models, code, and extraction/cache derivatives were withheld locally and are absent from this DEP.

### Defensive Review Checklist

- [ ] Document why a non-biometric identity is insufficient.
- [ ] Establish lawful purpose, data rights, consent, and retention.
- [ ] Pin encoder, alignment, gallery, threshold, generator, detector, and index versions.
- [ ] Report exact failure counts and fixed denominators at every scale.
- [ ] Validate approximate-search recall against exact checks.
- [ ] Test multiple independent encoders and capture pipelines.
- [ ] Audit demographic, site, device, age, accessibility, and temporal strata.
- [ ] Red-team Sybil, KYC, impersonation, enrollment, query, and detector-evasion risks.
- [ ] Make non-human status visible and cryptographically attestable.
- [ ] Define expiry, revocation, reassignment, appeal, incident response, and deletion.
- [ ] Keep real biometric sources and all embeddings out of public artifacts.
- [ ] Require independent human approval before any authorized real-world study.
