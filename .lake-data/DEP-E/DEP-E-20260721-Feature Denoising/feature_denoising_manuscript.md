---
title: "Feature Denoising - DEP-E"
generated_at: "2026-07-21 (date-only public marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of trainable feature-denoising blocks for adversarially robust ImageNet classifiers."
source_status: "Verified local PDF, full-paper HTML, metadata HTML, and source archive; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-21"
temporal_cutoff: "arXiv:1812.03411v2, CVPR 2019 record, and archived official code repository inspected through 2026-07-21"
primary_url: "https://arxiv.org/abs/1812.03411"
stable_identifier: "arXiv:1812.03411v2; DOI:10.48550/arXiv.1812.03411"
confidence_summary: "High for source identity, method reconstruction, and reported values; medium for generalization; low for current production readiness without modern reproduction."
safety_scope: "Defensive robustness research using synthetic, public, or authorized data only"
distribution_notes: "Derived Markdown and public URLs only; original sources, caches, renders, repair records, and private execution context are withheld."
---

# Feature Denoising - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:1812.03411v2 | https://arxiv.org/abs/1812.03411 | Metadata and source links; abstract alone was not used for synthesis | 2026-07-21 | Inspected |
| S2 | Complete paper | Primary artifact | PDF | arXiv:1812.03411v2 | https://arxiv.org/pdf/1812.03411 | Nine-page local copy verified and visually inspected; withheld | 2026-07-21 | Fully inspected |
| S3 | Full-paper rendering | Primary artifact | HTML | ar5iv rendering of arXiv:1812.03411v2 | https://ar5iv.labs.arxiv.org/html/1812.03411 | Passed full-document integrity gate; withheld | 2026-07-21 | Fully inspected |
| S4 | arXiv source package | Primary manuscript source | TeX/source archive | arXiv:1812.03411v2 | https://arxiv.org/e-print/1812.03411 | Main TeX, figures, equations, captions, and tables inspected; withheld | 2026-07-21 | Inspected |
| S5 | CVPR open-access record | Publisher/venue record | HTML | CVPR 2019, pages 501-509 | https://openaccess.thecvf.com/content_CVPR_2019/html/Xie_Feature_Denoising_for_Improving_Adversarial_Robustness_CVPR_2019_paper.html | Venue and accepted-version attribution | 2026-07-21 | Inspected |
| S6 | Official implementation | Code and models | GitHub repository | Archived `master` branch | https://github.com/facebookresearch/ImageNet-Adversarial-Training | CC BY-NC 4.0; public models, evaluation, and distributed-training code | 2026-07-21 | README, instructions, and focused model code inspected |
| S7 | Adversarial Label Noise - DEP-E | Related processed research | Markdown | DEP-E-20260716 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md | Adversarial-training dynamics and calibration context | 2026-07-21 | Inspected |
| S8 | ViT Semantic Robustness - DEP-E | Related processed research | Markdown | DEP-E-20260716 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-ViT%20Semantic%20Robustness/vit_semantic_robustness_manuscript.md | Representation-level perturbation context | 2026-07-21 | Inspected |
| S9 | AFIDAF Vision Filters - DEP-E | Related processed research | Markdown | DEP-E-20260715 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md | Feature filtering and architecture-control context | 2026-07-21 | Inspected |
| S10 | Black Lake authorities | Repository rules | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Filing, attribution, index, and source-locality contract | 2026-07-21 | Fetched and read |

Paper/work metadata:

- `Full title`: Feature Denoising for Improving Adversarial Robustness.
- `Authors`: Cihang Xie, Yuxin Wu, Laurens van der Maaten, Alan L. Yuille, and Kaiming He.
- `Affiliations in the paper`: Johns Hopkins University and Facebook AI Research.
- `arXiv dates`: submitted 2018-12-09; v2 revised 2019-03-25.
- `Publication`: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, June 2019, pages 501-509.
- `Stable identifiers`: arXiv:1812.03411v2; arXiv DOI 10.48550/arXiv.1812.03411.
- `Research domain`: adversarial robustness, ImageNet, adversarial training, feature denoising, non-local neural networks, white-box attacks, and black-box attacks.
- `Local source paths`: Withheld by public-output policy. Verified sources remain outside the repository.
- `Code and data`: The official archived repository supplies code, released models, and evaluation instructions. ImageNet and the secret CAAD 2018 test set are not redistributed here.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, subjects, dates, version, abstract, DOI, source links | Source identity and chronology | High | Abstract does not establish method or results |
| E2 | S2-S4 | Complete primary paper | Sections 1-7, Equations 1-3, Figures 1-8, Tables 1-3, references, source captions | Method, experimental settings, reported results, and source-disclosed limits | High for transcription | No independent run |
| E3 | S2/S4, Figure 6 | Primary empirical evidence | 10-2,000-step targeted PGD curves for matched baselines and denoising model | White-box robustness contribution | High for reported values | Curves lack intervals and repeated seeds |
| E4 | S2/S4, Figure 7 and Table 1 | Primary ablation evidence | Null, capacity, filter-family, `1 x 1`, and residual-path controls | Denoising-specific and block-design claims | High for reported values | No independent reproduction |
| E5 | S2/S4, Table 2 and Figure 8 | Primary black-box/competition evidence | Five-attacker all-or-nothing ablation and CAAD 2018 ranking | Black-box and competition claims | Medium-high | Secret CAAD data/attackers limit auditability |
| E6 | S2/S4, Table 3 | Primary clean-utility evidence | Clean-only controls and adversarial-training clean-accuracy trade-off | Utility boundary | High for reported values | Significance statement not backed by intervals |
| E7 | S6 | Official code/model release | Dependencies, model zoo, attack flags, insertion points, runtime notes, license, archived state | Implementation availability and reproducibility assessment | High for inventory | Code and checkpoints not executed |
| E8 | S7-S9 | Related processed research | Label correction, representation matching, and feature-filter architecture analyses | Cross-DEP synthesis | Medium | Related deposits do not validate the paper |
| E9 | Private integrity records summarized publicly | Local process evidence | PDF and HTML validation, repair, provenance update, zero partials | Mandatory complete-source gate | High | Private files and exact paths intentionally withheld |
| E10 | Live repository scans and automation memory | Process evidence | Identifier/title/slug and 24-hour dedup checks | Selection eligibility | High | Process evidence only |

## Executive Summary

The paper proposes a trainable residual block that filters intermediate convolutional features and is jointly optimized with large-scale PGD adversarial training. The authors motivate it with visual examples in which small pixel perturbations produce diffuse, semantically irrelevant feature activations. A denoising operation - non-local means, bilateral, mean, or median filtering - is followed by a learned `1 x 1` convolution and added back to the original features through a residual connection. Gaussian non-local means is the strongest reported variant.

The matched evidence supports a real but narrower effect than the headline comparison suggests. Under 10-step targeted PGD at `epsilon=16/256`, the authors' ResNet-152 baseline reaches 52.5% and the denoising version reaches 55.7%, a 3.2-point gain. At 2,000 steps, the values are 39.2% and 42.6%, a 3.4-point gain. The widely cited 27.9%-to-55.7% comparison is against ALP on a different backbone and implementation; the paper itself calls this system-level.

Controlled ablations strengthen the architecture claim. Parameter-matched null blocks, added bottleneck capacity, and local/non-local alternatives separate denoising from parameter count. Removing the `1 x 1` projection sharply reduces robustness; removing the residual path destabilizes training. In the five-attacker black-box test, non-local denoising reaches 46.2-46.4% versus 43.1% for the baseline and 44.1% for the null control, while local filters do not clearly beat the null block. Adding non-local denoising after every residual block reaches 49.5%.

The 50.6% CAAD 2018 win against 48 unknown attackers is important competition evidence but cannot be independently reconstructed from the secret test set. The official repository improves reuse by publishing models, evaluation, and distributed-training code, yet it is archived, non-commercially licensed, tied to legacy frameworks, and computationally demanding. Reviewer confidence is high for source fidelity, medium for transfer to similar ImageNet/PGD settings, and low for production certification without a modern, repeated-seed, multi-attack reproduction.

## Detailed Summary

### Problem Context

Adversarial examples can remain visually close to clean inputs while sending a classifier toward a wrong label. The paper focuses on how this perturbation expands inside the network: feature maps from adversarial inputs appear spatially diffuse and activate regions unrelated to the object. The authors call this feature noise and ask whether explicitly filtering intermediate representations can make a differentiable classifier more robust without relying on non-differentiable input preprocessing.

The distinction matters because earlier pixel denoisers could create gradient obfuscation. Here, the filter is part of the network, and the white-box attacker differentiates through it. The defense therefore aims to change learned representation transport rather than block gradient access.

### Denoising Block

For an input feature tensor, the block first applies one of four operations:

1. Gaussian non-local means computes feature-dependent, softmax-normalized weights across spatial locations, using learned embeddings.
2. Dot-product non-local means uses unnormalized feature inner products and can avoid extra embedding parameters.
3. Bilateral filtering restricts interaction to a local neighborhood while preserving feature-dependent weights.
4. Mean and median filters provide simpler local smoothing and outlier removal.

The filtered output passes through a `1 x 1` convolution and is added to the original tensor. The convolution learns how much filtered signal to retain and how to combine channels; the residual connection preserves an identity path. By default, four blocks are inserted after the final residual blocks of `res2`, `res3`, `res4`, and `res5`. The CAAD winner instead places non-local denoising after every residual block in a ResNeXt-101-32x8 backbone.

### Adversarial Training

Training uses targeted PGD generated from the current model. The `L_inf` budget is 16 on a 0-255/256-style pixel scale, step size is 1, and the inner loop runs for 30 steps. Twenty percent of batches initialize PGD from the clean input; 80% initialize randomly inside the perturbation cube. Each synchronized SGD batch contains 4,096 adversarial images across 128 GPUs and no clean images.

The models train for 110 epochs with learning-rate drops at epochs 35, 70, and 95 and label smoothing of 0.1. The paper reports roughly 38 hours on 128 V100s for the ResNet-101 baseline and 52 hours for the ResNet-152 baseline. The official instructions report about 90 hours for ResNet-152 denoising and note that the Gaussian softmax non-local operation lacks an efficient implementation; the dot-product version is faster. An XLA/FP16 option reportedly halves training time at a robustness cost of about three points.

### White-Box Evaluation

Evaluation uses ImageNet's 50,000 validation images, a uniformly sampled incorrect target class, random attack initialization, and top-1 classification accuracy regardless of attack target. Attack step size is 1 except at 10 steps, where it is 1.6. The study spans 10 to 2,000 PGD iterations and states that PGD was the strongest among additional FGSM, iterative FGSM, and momentum variants considered.

At 10 steps, ALP on Inception-v3 reports 27.9%, the authors' ResNet-101 baseline reports 49.7%, ResNet-152 baseline reports 52.5%, and ResNet-152 denoising reports 55.7%. At 2,000 steps, the latter two report 39.2% and 42.6%. The denoising improvement remains near 3 points, while much of the headline improvement over ALP comes from the training system, backbone, and implementation.

Figure 7 compares the baseline, added bottleneck capacity, a null `1 x 1` block, and multiple filters. Every denoising variant exceeds those controls in the shown white-box range. Table 1 shows 100-step accuracy falling from 45.5% to 36.8% when the `1 x 1` projection is removed. Removing the residual path produces unstable training with non-decreasing loss. These controls support the interpretation that filtering plus learned signal reintegration matters.

### Black-Box and Competition Evaluation

For five top CAAD 2017 attackers, the paper applies the CAAD 2018 all-or-nothing rule: a sample counts correct only if the model classifies every attacked version correctly. The attack budget is 32 even though training used 16. Under this test, the baseline reaches 43.1%, the null control 44.1%, non-local dot product 46.2%, and Gaussian non-local 46.4%. Local filters range from 43.6% to 44.4%, so they are not clearly stronger than the null control. Adding Gaussian non-local denoising after all residual blocks reaches 49.5%.

The CAAD 2018 winning submission uses the all-block ResNeXt design and reports 50.6% against 48 unknown attackers on a secret ImageNet-like dataset. Second place reports 40.8%; all but the top two teams report below 10%. The winning model's public ImageNet white-box results are 56.0% at 10 steps and 40.4% at 100 steps, but its training settings differ from the ResNet-152 experiments.

### Clean Accuracy and Boundary Conditions

With clean-only training, the tested ResNet-152 controls and denoising variants remain within about 0.2 points of the 78.91% reference across repeated baseline runs, and the authors describe no significant advantage. With adversarial training, baseline and denoising clean accuracies fall to 62.32% and 65.30%, compared with 78.91% and 79.08% under clean training. Feature denoising improves the robustly trained model's clean result, but does not remove the clean-robust trade-off.

The study openly states that feature noise is difficult to quantify across architectures or training methods because end-to-end changes alter feature scales and distributions. The evidence therefore combines qualitative feature maps with downstream robustness rather than directly measuring the proposed noise variable.

### Implementation Availability

The official repository includes three released model configurations, an evaluation script, distributed training code, and prediction generation for black-box evaluation. It documents TensorFlow 1.x-era dependencies, Tensorpack, OpenCV, Horovod/NCCL, ImageNet directory structure, and distributed launch commands. Focused model code matches the paper's four default insertion points and the all-block ResNeXt winner. The repository was archived read-only in 2021 and uses CC BY-NC 4.0, limiting commercial reuse and increasing environment-reconstruction work.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Adversarial inputs create noisy feature activations that motivate feature filtering. | Author observation/hypothesis | E2, Figures 1-3 | Visually demonstrated, but not quantitatively normalized across models. | Medium |
| C2 | Four Gaussian non-local denoising blocks improve matched ResNet-152 targeted-PGD robustness. | Author empirical claim | E3 | +3.2 points at 10 steps and +3.4 at 2,000 steps in the reported setup. | High for reporting |
| C3 | Feature denoising, not only added parameters, explains the improvement. | Author ablation claim | E4 | Null and capacity controls underperform every shown denoising variant; supports but does not exhaust all confounders. | Medium-high |
| C4 | The `1 x 1` projection and residual path are essential to the block. | Author ablation claim | E4 | Projection removal loses 8.7 points at 100 steps; residual removal destabilizes training. | High for reporting |
| C5 | Non-local denoising is more useful than local filtering under the black-box test. | Author interpretation | E5 | Non-local 46.2-46.4 versus local 43.6-44.4 and null 44.1; supported within this test. | Medium-high |
| C6 | The method won CAAD 2018 with 50.6% against 48 unknown attackers. | Competition result | E5 | Supported by the paper and official release; secret data and attacks prevent full reproduction. | Medium-high |
| C7 | Denoising has a special advantage for adversarial rather than clean-only training. | Author interpretation | E4, E6 | Robust ablations are stronger than clean-only differences; scope remains ImageNet/these architectures. | Medium |
| C8 | The released system is directly production-reproducible today. | Reviewer test | E7 | Not established: archived legacy stack, non-commercial license, high compute, and no modern attack suite. | Low |
| C9 | The random selection was fresh and source-complete before synthesis. | Process claim | E9-E10 | First draw accepted after repair and final verification. | High |

## Methodology

- `Research objective`: Preserve and critique the paper's architecture, threat model, empirical evidence, limitations, implementation relevance, and connections to existing Black Lake research.
- `Sources inspected`: Verified complete PDF, full-paper HTML, metadata HTML, TeX/source archive, CVPR record, official repository README/instructions/focused model code, live repository authorities, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated all private archive PDFs with `rg --files -g "*.pdf"`, grouped by parent directory, selected one sorted unit uniformly with `Get-Random`, ran cross-repository dedup, repaired missing source companions, then inspected primary sources before interpretation.
- `Inclusion criteria`: Primary evidence for identity, architecture, training, threat model, quantitative results, ablations, limitations, or implementation; related DEP items required concrete overlap in robustness, representations, or feature filtering.
- `Exclusion criteria`: Abstract-only synthesis, unverifiable secondary metrics, private paths, source-file redistribution, exact private execution timestamps, and claims that robust accuracy alone certifies safety.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Extraction process`: Nine PDF pages were rendered and visually inspected; TeX/source lines were used to cross-check equations, captions, settings, and table values; official web records supplied current repository/venue status.
- `Version control`: Paper pinned to arXiv v2; code assessed on the archived public `master` branch as exposed by the official repository.
- `Claim selection`: Prioritized matched-baseline deltas, ablations, threat-model details, clean-robust trade-offs, competition evidence, and reproducibility boundaries over headline prose.
- `Cross-checking`: Quantitative statements were checked across PDF visuals, full-paper HTML/source, and code instructions where corresponding implementation details existed.
- `Evidence handling`: Author claims, reported measurements, reviewer interpretations, and process evidence are labeled separately and mapped to ledger IDs.
- `Uncertainty handling`: No experiment is represented as reproduced; secret data, missing uncertainty, outdated dependencies, and untested generalization remain explicit.
- `Random selection`: 75,779 PDFs and 75,776 unique paper units; uniform zero-based index 61,119; first draw accepted; zero exclusions and reselections.
- `Dedup validation`: arXiv ID, DOI, normalized title, slug, live artifacts, related repository entries, automation memory, and 24-hour markers were scanned. A metadata-only inventory row was not treated as prior processing.
- `Source repair`: Initial partial state became verified complete after one bounded repair; the valid PDF was preserved and no partial bytes remained.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:1812.03411v2, its CVPR record, official code/model release, and exactly three related Black Lake deposits.
- `Temporal boundary`: Public sources inspected through 2026-07-21; scientific claims remain those of the 2019 work unless explicitly labeled reviewer context.
- `Evidence limits`: No training, checkpoint evaluation, attack reproduction, ImageNet inspection, CAAD replay, or independent statistics were performed.
- `Assumptions`: The approved full-paper rendering faithfully represents v2; the official repository corresponds to the paper; graph values visually read from the paper are accurate to the printed labels.
- `Constraints`: Source documents remain local; repository output is public-safe Markdown; code/model license is non-commercial; ImageNet and CAAD data have separate access/usage constraints.
- `Out of scope`: Production certification, adversarial attack deployment, safety guarantees, commercial license advice, and claims about all modern architectures or threat models.
- `Intended use`: Research preservation, replication planning, robustness benchmark design, engineering ideation, and follow-on DEP synthesis.
- `Audience`: Robust-ML researchers, vision engineers, evaluation teams, and technical product reviewers.
- `Reproducibility boundary`: Released models and code improve auditability, but the legacy stack, distributed compute, dataset access, random targets/initialization, and secret CAAD evaluation block complete reproduction here.
- `Operational boundary`: Implementations must remain defensive, offline, authorized, and evaluation-focused.
- `Data sensitivity`: Public paper/code metadata and authorized benchmark data only; no private images or credentials.

## Observations

- `Observed pattern`: The denoising increment is remarkably stable at roughly three points from 10 to 2,000 PGD steps, while the strong baseline accounts for most of the gap to ALP.
- `Observed pattern`: Local filters help in the shown white-box study but not convincingly beyond the null block in black-box evaluation; long-range feature interaction appears to matter more there.
- `Technical implication`: A corrective filter needs a learned reintegration path. Pure smoothing can erase signal, and the projection/residual ablation quantifies this failure.
- `Contradiction or tension`: The work presents denoising as a mechanism, yet explicitly cannot quantify feature noise across models; output robustness is therefore an indirect proxy for the proposed internal cause.
- `Contradiction or tension`: The release enables evaluation, but the most celebrated CAAD result remains tied to secret data and unknown attackers.
- `Reviewer hypothesis`: Modern normalization and attention architectures may already implement some non-local denoising behavior; parameter-matched contemporary controls could shrink or redistribute the gain.
- `Open question`: Does feature-noise suppression predict calibration, corruption stability, and semantic representation preservation, or only targeted-PGD accuracy?

## Considerations

Robustness evaluation should pin model/checkpoint hashes, preprocessing, attack code, target-selection policy, initialization, step size, iterations, restarts, epsilon, and success metric. Attack convergence needs diagnostics rather than an iteration count alone. Targeted and untargeted attacks, gradient-free checks, transfer attacks, adaptive attacks, corruptions, and distribution shift should be reported separately.

Architecture comparison should hold insertion points, parameters, FLOPs, optimizer, training compute, seeds, and data constant. The 2019 system's 128-GPU recipe is an important operational cost, and modern evaluation should add latency, memory, energy, and carbon/accounting notes. Legacy code should run in a sandboxed, pinned environment because outdated frameworks and untrusted serialized checkpoints create supply-chain and compatibility risk.

High robust accuracy is not a deployment guarantee. Applications involving safety-critical vision need domain-specific data, abstention, monitoring, human review, incident response, and evaluation under physically plausible shifts. The defensive examples in this artifact do not generate attacks or authorize use against third-party systems.

## Strengths

- Uses a fully differentiable defense and evaluates white-box attacks through the denoising blocks rather than relying on gradient obstruction.
- Establishes a strong in-house adversarial-training baseline before adding the proposed architecture.
- Includes parameter-matched null, added-capacity, filter-family, projection, and residual-path ablations.
- Tests long PGD runs to 2,000 iterations and reports matched baseline/candidate curves.
- Includes both white-box and black-box settings plus a competition result against many unknown attackers.
- Reports clean-only controls and the clean-robust accuracy trade-off.
- Releases code, models, and evaluation/training instructions aligned with the architecture.
- Provides an interpretable residual correction pattern reusable beyond the exact filter family.

## Weaknesses

- Feature noise is qualitatively visualized but not quantitatively defined or independently linked to robustness.
- The headline ALP comparison is system-level and confounds backbone, training system, and architecture.
- No repeated-seed intervals, statistical tests, or prominent uncertainty analysis accompany the robustness values.
- The white-box scope is targeted PGD with random targets; the release explicitly excludes untargeted and attacker-controlled-target evaluation.
- Modern multi-attack suites, calibration, corruption robustness, physical attacks, and distribution shift are not covered.
- CAAD 2018 uses secret data and unknown attackers, preventing full independent replay.
- The official stack is archived, legacy, computationally expensive, and CC BY-NC licensed.
- Clean-robust trade-offs remain substantial despite the denoising improvement.
- Local filters' black-box gains are weak, narrowing the generality of the broad denoising label.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Define normalized layerwise noise metrics | Mechanism | Separates feature-scale changes from perturbation amplification | Directly tests the motivating hypothesis | Metric may not track semantics | Correlate across layers, seeds, models, and attacks |
| Run modern attack suites | Evaluation | Targeted PGD alone is an incomplete certificate | Stronger robustness boundary | High compute and tuning leakage risk | AutoAttack-style, adaptive, transfer, and gradient-free matrix |
| Add repeated seeds and intervals | Statistics | Current deltas are a few points | Quantifies reliability | Expensive adversarial training | Pre-register seeds; report mean, interval, and paired effect |
| Match modern architectures and compute | Causal attribution | Attention/normalization may change the baseline | Establishes contemporary value | Large search space | CNN/ViT controls with fixed budgets and insertion points |
| Measure systems cost | Deployment | Non-local operations can be hardware-sensitive | Real deployment frontier | Device-specific results | Latency, memory, throughput, energy, and compiler profiles |
| Release a public CAAD replay surrogate | Reproducibility | Secret evaluation cannot be reconstructed | Auditable black-box diversity | Risk of benchmark overfitting | Hidden public server plus versioned replay set |
| Quantify clean/robust calibration | Reliability | Accuracy omits confidence behavior | Better selective prediction | Extra evaluation complexity | ECE/NLL, risk-coverage, and shift calibration |

## Potential Implementations

1. `Modern denoising-block benchmark`
   - `User`: Robust-ML research and model-evaluation teams.
   - `Goal`: Determine whether local/non-local feature correction still improves current backbones.
   - `Core mechanism`: Plug parameter-matched blocks into fixed insertion points and run one versioned training/evaluation manifest.
   - `Required inputs`: Authorized datasets, backbone definitions, block implementations, attacks, seeds, and hardware manifest.
   - `Outputs`: Clean/robust accuracy, intervals, attack convergence, latency, memory, energy, and failure cases.
   - `Risk controls`: Sandboxed checkpoints, fixed threat models, no third-party targeting, data governance, and independent holdout evaluation.
   - `Evaluation`: Paired deltas against baseline, capacity, null, local, and non-local controls.
2. `Representation-noise observatory`
   - `User`: Architecture researchers and interpretability engineers.
   - `Goal`: Test whether normalized feature perturbation and suppression predict robust behavior.
   - `Core mechanism`: Collect layerwise clean/perturbed/repaired activations, normalize by clean feature statistics, and link changes to output and concept metrics.
   - `Required inputs`: Authorized images, model hooks, layer manifest, perturbation/corruption suite, and concept annotations where available.
   - `Outputs`: Layerwise noise curves, suppression/signal-loss ratios, semantic stability, and correlations with accuracy/calibration.
   - `Risk controls`: Private activation storage, retention limits, synthetic/public first, and no claim that one norm equals semantics.
   - `Evaluation`: Cross-seed/model stability and predictive value on held-out attacks/shifts.
3. `Robustness evidence-card generator`
   - `User`: Model reviewers, governance teams, and deployment owners.
   - `Goal`: Prevent unmatched or incomplete robustness claims.
   - `Core mechanism`: Validate manifests and controls before exporting a public-safe Markdown/JSON card.
   - `Required inputs`: Model/config hashes, training recipe, attack results, uncertainty, clean utility, hardware costs, and provenance.
   - `Outputs`: Evidence ledger, claim table, gaps, risks, and explicit non-certification statement.
   - `Risk controls`: No raw data export, schema checks, signed manifests, human approval, and clear distinction between reported and reproduced results.
   - `Evaluation`: Re-run determinism, missing-field rejection, and reviewer agreement.

## Three Ways to Exercise This Research

1. `Reproduce one released checkpoint`: Objective - verify the published evaluation path without retraining. Inputs - official checkpoint, pinned legacy container, authorized ImageNet validation data, and exact targeted-PGD manifest. Method - hash all inputs, reproduce clean and 10/100-step values, then test 2,000-step convergence. Output - a versioned replication card. Success criterion - documented agreement within the release's stated random fluctuation. Stop condition - dependency, license, data, or checkpoint-integrity failure.
2. `Run a small matched architecture study`: Objective - isolate filtering from capacity on a modern public toy benchmark. Inputs - synthetic/public images, one small backbone, and baseline/capacity/null/local/non-local blocks. Method - fix parameters, compute, seeds, insertion points, and a defensive perturbation/corruption suite. Output - paired accuracy, calibration, and cost table. Success criterion - reproducible effect across at least three seeds. Stop condition - unmatched controls or non-convergent evaluation.
3. `Test the feature-noise hypothesis`: Objective - connect internal suppression to external robustness. Inputs - clean, corrupted, and authorized adversarial examples; layer hooks; normalized feature metrics; and concept labels where possible. Method - measure before/after block deltas and signal loss, then predict held-out robustness. Output - correlation and failure-case report. Success criterion - stable held-out relationship beyond feature scale. Stop condition - metric collapse, privacy risk, or evidence that suppression erases task signal.

## Example MVP Product

- `Product name`: Feature Defense Audit
- `Target user`: Vision robustness researchers and model-assurance teams.
- `Problem`: Architecture defenses are often compared with unmatched training, threats, or capacity, making gains difficult to attribute.
- `Core workflow`: Import signed model and evaluation manifests; validate matched controls; run offline authorized checks; compute clean/robust/calibration/system metrics; inspect feature suppression; export an evidence card with gaps and non-certification limits.
- `Data requirements`: Synthetic, public, or governed images; fixed splits; model/config hashes; attack/corruption manifests; optional concept annotations; no private data in public output.
- `Architecture`: Sandboxed runner, checkpoint verifier, control-matrix validator, metric engine, activation-statistics store, report generator, and reviewer approval queue.
- `Success metrics`: Reproduction agreement, paired effect stability, attack convergence, calibration, risk-coverage, runtime/memory/energy, zero unauthorized data export, and complete provenance.
- `Risk controls`: Offline execution, least privilege, signed artifacts, dependency scanning, dataset access controls, bounded evaluation, human review, and no autonomous deployment decision.
- `Limitations`: Cannot prove absence of attacks, guarantee real-world safety, or transfer one benchmark result across domains.
- `MVP boundary`: Evaluate released or toy-scale models first; no full distributed retraining, secret benchmark substitution, or production serving.
- `Deployment model`: Local CLI plus static Markdown/JSON report.
- `Evaluation plan`: Golden-manifest smoke tests, deliberately mismatched-control rejection, repeated-seed toy study, checkpoint tamper test, and independent review of one evidence card.
- `Failure modes`: Stale dependencies, hidden preprocessing differences, insufficient attack convergence, tuning on test evidence, feature-scale confounds, and misleading aggregation.
- `Maintenance plan`: Version attack suites and schemas, pin environments, refresh compatibility notes, and retain immutable report manifests.

## Related Research and Reading

1. [Adversarial Label Noise - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md) - Adds a supervision-side account of adversarial-training failure, robust overfitting, teacher calibration, and cross-attack validation. It complements feature denoising's architecture-side correction.
2. [ViT Semantic Robustness - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-ViT%20Semantic%20Robustness/vit_semantic_robustness_manuscript.md) - Tests how bounded pixel changes redirect representations, providing a direct stress test for the internal geometry that feature denoising aims to stabilize.
3. [AFIDAF Vision Filters - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md) - Compares local image-domain and global Fourier-domain filters, offering matched architecture and systems-cost lessons for modern denoising-block studies.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1812.03411 | Identity, dates, DOI, abstract, paper/source links | 2026-07-21 | Metadata only; not the full-paper evidence |
| R2 | https://arxiv.org/pdf/1812.03411 | Complete paper method, figures, tables, and conclusions | 2026-07-21 | Verified local copy withheld |
| R3 | https://ar5iv.labs.arxiv.org/html/1812.03411 | Full-paper text cross-check | 2026-07-21 | Approved fallback rendering; verified local copy withheld |
| R4 | https://arxiv.org/e-print/1812.03411 | TeX equations, captions, tables, and source inventory | 2026-07-21 | Verified local source package withheld |
| R5 | https://doi.org/10.48550/arXiv.1812.03411 | Persistent arXiv identifier | 2026-07-21 | DOI locator |
| R6 | https://openaccess.thecvf.com/content_CVPR_2019/html/Xie_Feature_Denoising_for_Improving_Adversarial_Robustness_CVPR_2019_paper.html | CVPR venue, pages, authors, accepted-version context | 2026-07-21 | Official CVF record |
| R7 | https://github.com/facebookresearch/ImageNet-Adversarial-Training | Code/models, license, dependencies, evaluation/training instructions, archived status | 2026-07-21 | Official archived release; not executed |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md | Related adversarial-training synthesis | 2026-07-21 | Processed research; not primary evidence for this paper |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-ViT%20Semantic%20Robustness/vit_semantic_robustness_manuscript.md | Related representation-robustness synthesis | 2026-07-21 | Processed research; not primary evidence for this paper |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md | Related feature-filter architecture synthesis | 2026-07-21 | Processed research; not primary evidence for this paper |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | DEP location, attribution, source-locality, and public-safety rules | 2026-07-21 | Live default-branch authority |
| R12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository layout and dedup context | 2026-07-21 | Live default-branch authority |

## Appendix

### Selection and Integrity Record

- Candidate enumeration: 75,779 PDFs and 75,776 unique PDF-parent paper units.
- Uniform draw: sorted-unit zero-based index 61,119 using `Get-Random`.
- Outcome: first draw accepted; zero duplicate exclusions, zero other exclusions, zero reselections.
- Dedup: no matching processed Arxiv DEP artifact or prior-24-hour marker; one metadata-only author-inventory row did not constitute prior processing.
- Initial source state: partial because full-paper HTML was missing; valid PDF preserved.
- Repair policy: one bounded acquisition; 100 MB target ceiling; 20 MB partial ceiling; no credentials; one attempt per artifact.
- Final source state: complete; PDF and full-paper HTML gates passed; zero partials.
- Distribution: no source documents, archives, caches, extractions, renders, verification records, or private paths uploaded; no `.source/` directory.

### Representative Quantitative Record

| Setting | Baseline / control | Feature-denoising result | Difference / interpretation |
|---|---:|---:|---|
| Targeted PGD, 10 steps, `epsilon=16` | ResNet-152: 52.5% | Gaussian non-local: 55.7% | +3.2 points |
| Targeted PGD, 2,000 steps, `epsilon=16` | ResNet-152: 39.2% | Gaussian non-local: 42.6% | +3.4 points |
| Five black-box attackers, all-or-nothing, `epsilon=32` | ResNet-152: 43.1% | Gaussian non-local: 46.4% | +3.3 points |
| Same black-box setting | Null `1 x 1`: 44.1% | Non-local dot product: 46.2% | +2.1 points over parameter-matched null |
| Same black-box setting | ResNet-152: 43.1% | Denoising after every residual block: 49.5% | +6.4 points |
| CAAD 2018 secret evaluation | Runner-up: 40.8% | Winning denoising entry: 50.6% | +9.8 points; paper describes approximately 10 |
| Clean-only ResNet-152 | Baseline: 78.91% | Gaussian non-local: 79.08% | +0.17; within reported natural variation |
| Adversarially trained clean accuracy | Baseline: 62.32% | Gaussian non-local: 65.30% | +2.98, but large clean-training trade-off remains |

## Attribution Block

- Primary paper: Cihang Xie, Yuxin Wu, Laurens van der Maaten, Alan L. Yuille, and Kaiming He. *Feature Denoising for Improving Adversarial Robustness*. CVPR 2019. https://arxiv.org/abs/1812.03411
- Persistent identifier: https://doi.org/10.48550/arXiv.1812.03411
- Official venue record: https://openaccess.thecvf.com/content_CVPR_2019/html/Xie_Feature_Denoising_for_Improving_Adversarial_Robustness_CVPR_2019_paper.html
- Official code and models: https://github.com/facebookresearch/ImageNet-Adversarial-Training
- Source files: Withheld locally; none were uploaded.
