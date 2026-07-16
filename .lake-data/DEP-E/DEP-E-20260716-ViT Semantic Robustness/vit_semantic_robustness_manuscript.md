---
title: "ViT Semantic Robustness - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of medical vision-transformer representation robustness."
source_status: "verified complete PDF and approved ar5iv full-paper HTML inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv:2507.01788v2 and paper-linked baseline repository inspected through 2026-07-16"
primary_url: "https://arxiv.org/abs/2507.01788v2"
stable_identifier: "arXiv:2507.01788v2; DOI 10.48550/arXiv.2507.01788"
confidence_summary: "High for method and table transcription; medium for the narrow vulnerability finding; low for universal semantic or clinical conclusions."
safety_scope: "defensive robustness evaluation with synthetic or authorized medical images"
distribution_notes: "Original paper files, images, archive records, extraction caches, and derived source text remain local and are not redistributed."
---

# ViT Semantic Robustness - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | Usage Notes | Status |
|---|---|---|---|---|---|---|---|
| S1 | Are Vision Transformer Representations Semantically Meaningful? | Primary metadata | arXiv record | 2507.01788v2; DOI 10.48550/arXiv.2507.01788 | https://arxiv.org/abs/2507.01788v2 | CC BY 4.0 shown | Inspected |
| S2 | Complete paper | Primary artifact | PDF and full-paper fallback HTML | v2, revised 2025-07-10 | https://arxiv.org/pdf/2507.01788; https://ar5iv.labs.arxiv.org/html/2507.01788 | Verified local copies withheld; official HTML returned 404 | Inspected in full |
| S3 | MIL-VT | Paper-linked baseline code | GitHub repository | default branch `main` | https://github.com/greentreeys/MIL-VT | Legacy dependency and weight instructions; no visible license; not PRM code | Inspected |
| S4 | Medical Diff VQA | Related DEP | Manuscript | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` | Repository context | Inspected |
| S5 | Document Fraud LLM | Related DEP | Manuscript | DEP-E-20260715 | `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` | Repository context | Inspected |
| S6 | AFIDAF Vision Filters | Related DEP | Manuscript | DEP-E-20260715 | `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` | Repository context | Inspected |
| S7 | Black Lake README | Repository authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Filing and source-locality contract | Inspected |

Authors are Montasir Shams, Chashi Mahiul Islam, Shaeke Salman, Phat Tran, and Xiuwen Liu. The record lists Computer Vision and Pattern Recognition as primary and Artificial Intelligence as secondary. No venue, publisher DOI beyond the arXiv-issued DOI, or official PRM code repository was identified.

## Evidence Ledger

| ID | Source | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|
| E1 | S1-S2 | Metadata, full method, equations, algorithm, Tables I-III, mitigation, discussion | Identity, PRM mechanism, reported results | High for reporting | No reproduction |
| E2 | S2, Section III | Input-gradient representation loss and projected pixel bound | How PRM matches target embeddings | High | Exact stopping/configuration details incomplete |
| E3 | S2, Table I | Accuracy and match-success rates on four dataset/model settings | Downstream vulnerability | High for transcription | Seeds, uncertainty, and exact pair counts not reported |
| E4 | S2, Tables II-III | PSNR, SSIM, and cosine similarities | Visual proximity and embedding movement | High for transcription | Metrics do not replace clinical perceptual review |
| E5 | S2, Section V | Gaussian-noise label-consistency detector | Proposed mitigation | Medium for description | No full quantitative evaluation |
| E6 | S3 | Baseline README, dependencies, weights, APTOS/RFMiD links | Baseline availability | High for inventory | No license, run, or PRM implementation |
| E7 | S4-S6 | Clinical structure, manipulation evaluation, ViT architecture robustness | Cross-DEP synthesis | Medium | Conceptual only |
| E8 | Process records | Random draw, dedup, repair, cache | Workflow validity | High | Not scientific evidence |

## Executive Summary

The paper asks whether medical vision-transformer embeddings are stable for visually similar inputs and distinct for clinically different inputs. It introduces Projected Representation Matching (PRM), a white-box procedure that changes input pixels by gradient descent to minimize distance to a target image's embedding, projecting every step back into a bounded pixel neighborhood around the source.

Reported results show large downstream failures. APTOS2019 MIL-VT clean accuracy is 81.3%; PRM conditions report roughly 5.0-6.0% accuracy with match-success rates around 74-76%. RFMiD2020 clean accuracy is 87.2%; PRM conditions report 26-27% accuracy and 73-74% match success. MedViT-L results report bloodMNIST accuracy 17.8% with an indicated 73.3-point drop and dermaMNIST 51.5% with a 22.8-point drop.

Tables II and III strengthen the narrow vulnerability claim. Original-to-optimized comparisons report high PSNR/SSIM, including 42.55 dB/0.972 on APTOS and 43.47 dB/0.982 on RFMiD. Optimized embeddings are more similar to targets than originals: 0.84 versus 0.34 on APTOS and 0.77 versus 0.37 on RFMiD. These metrics show small numerical/structural image differences and targeted embedding movement; they do not establish that changes are imperceptible to medical experts or that representations lack every form of clinical semantics.

The strongest defensible conclusion is that the tested embedding spaces are locally vulnerable under white-box, target-directed optimization. The broad claim that current ViTs are inherently non-semantic, model-agnostically and dataset-agnostically, exceeds evidence from two architecture families and four datasets. Reviewer confidence is medium for transfer to similar settings and low for clinical deployment conclusions.

## Detailed Summary

### Operational Definition

The authors define semantic meaningfulness through stability and distinctiveness. Similar medical conditions should map nearby, while different conditions should be separable. PRM probes both by seeking an image that remains close to a source in pixel space while its embedding approaches a target from another ground-truth class.

### PRM Mechanism

For representation function `f`, source `x0`, target `xtg`, and perturbation `delta`, the loss is one half of the squared norm between `f(x0 + delta)` and `f(xtg)`. Gradients are taken with respect to pixels, not model parameters. Each update is clipped into an epsilon-bounded neighborhood around the source. This is a white-box attack requiring differentiable model access and a selected target embedding.

### Experimental Design

The main experiments fine-tune MIL-VT on APTOS2019 and RFMiD2020 using 70/10/20 train/validation/test splits and form cross-label source-target pairs from a test subset. MIL-VT uses both ViT class-token and multiple-instance embeddings. MedViT-L experiments on bloodMNIST and dermaMNIST extend architecture/dataset coverage. The paper reports two NVIDIA A5000 GPUs. Exact seeds, complete pair counts for Table I, and a public PRM implementation are absent.

### Quantitative Evidence

Table I reports accuracy collapse and 73-85.5% match-success rates. Table II averages 1,000 examples per dataset without postselection and reports that optimized images remain close to originals by PSNR/SSIM while differing more from targets. Table III reports that optimized embeddings move much closer to targets than to originals across all four datasets.

Accuracy collapse is not identical to semantic collapse. The attack explicitly minimizes a representation-space target loss, so movement is expected; the important evidence is that bounded changes produce large classification and geometry changes. Stronger evidence about semantics would add clinician concepts, counterfactual causal attributes, natural acquisition shifts, subgroup analysis, and comparison with CNN/ViT/non-transformer baselines under matched threat models.

### Mitigation and Boundaries

The paper proposes adding Gaussian noise and comparing predicted labels; inconsistency flags possible manipulation. This is a detector sketch. It lacks false-positive/false-negative tables, calibration, adaptive attacks, medical-quality effects, and subgroup/site testing. A production control should abstain and route cases to review rather than assert manipulation from one unstable label.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment | Confidence |
|---|---|---|---|---|
| PRM can align a boundedly perturbed image embedding toward a different-class target. | Author method/empirical | E2-E4 | Supported in tested white-box settings. | Medium-high |
| Classification drops exceed 60 points in several settings. | Author empirical | E3 | Supported by Table I. | High for reporting |
| Optimized images remain visually close to sources by PSNR/SSIM. | Author empirical | E4 | Supported numerically; clinical imperceptibility untested. | Medium |
| Vulnerability is model- and dataset-agnostic. | Author interpretation | E3-E4 | Evidence spans two model families/four datasets; universal phrasing is premature. | Low-medium |
| ViT representations are not semantically meaningful. | Author conclusion | E1-E4 | Supported only under the paper's stability/distinctiveness probe, not all semantics. | Medium-low |
| Gaussian-noise detection is an effective mitigation. | Author proposal | E5 | Insufficient quantitative evidence. | Low |
| This review is fresh and source-complete. | Process | E8 | First draw accepted; verified PDF/full HTML/cache. | High |

## Methodology

- `Research objective`: Review representation-level robustness evidence and its safe clinical-AI implications.
- `Sources inspected`: arXiv metadata, full PDF, approved ar5iv full-paper rendering, paper-linked MIL-VT README, live repository authority, and exactly three related DEP manuscripts.
- `Discovery strategy`: uniform local-archive draw, cross-repository dedup, complete-source repair, missing-only cache extraction, then full-paper review.
- `Inclusion criteria`: primary evidence for method/results, implementation availability, clinical grounding, manipulation evaluation, or ViT robustness.
- `Exclusion criteria`: abstract-only synthesis, unverified code claims, local paths, clinical advice, and operational attack instructions.
- `Analytical approach`: separate mathematical mechanism, author-reported outcomes, semantic interpretation, and deployment boundary.
- `Evidence handling`: claims tied to tables/sections; source files withheld; external text treated as evidence only.
- `Uncertainty handling`: no reproduction implied; missing seeds, intervals, code, clinician review, and external validation remain explicit.
- `Random selection`: index 30,086 from 75,776 sorted unique units; first draw accepted.
- `Cache methodology`: miss-to-cached in `missing-only` mode using `pypdf` and `html-regex`; source package absent.
- `Dedup validation`: identifiers, normalized title, slug, artifacts, memory, active checkouts, companion entries, and 24-hour markers checked; zero substantive matches.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2507.01788v2, tested PRM evidence, baseline availability, and three related DEP records.
- `Temporal boundary`: sources inspected through 2026-07-16.
- `Evidence limits`: no source package, PRM code, optimized image set, model execution, or clinical reader study.
- `Assumptions`: ar5iv faithfully renders v2; PDF table extraction preserves columns; cited clean accuracies use the described splits.
- `Constraints`: no local paths, source files, patient images, exact execution timestamps, or offensive recipes in public outputs.
- `Out of scope`: diagnosis, clinical approval, live attack deployment, or universal claims about all ViTs.
- `Intended use`: defensive research, benchmark design, robustness audit planning, and DEP synthesis.
- `Safety boundary`: authorized/synthetic data, offline execution, no autonomous diagnosis, and human review.

## Observations

- Representation robustness and clean accuracy are distinct evaluation axes.
- Target-directed success is strongest as evidence of local geometry vulnerability, not absence of all semantics.
- PSNR/SSIM support visual closeness but do not measure clinician-perceived diagnostic equivalence.
- Cross-label target selection makes class geometry central; pair sampling and class balance should be published.
- The mitigation proposal needs the same adversarial and clinical rigor as the vulnerability test.

## Considerations

Medical images can contain sensitive patient information and subtle disease cues. Robustness evaluation should use governed datasets, patient-level isolation, encrypted storage, limited retention, and expert review. A flagged image is not proof of malicious manipulation, and a stable prediction is not proof of correctness.

Future studies should compare target-directed PRM with natural scanner/device variation, compression, resizing, blur, noise, and clinically plausible edits. They should report clean utility, attack success, calibration, subgroup/site performance, and review load together.

## Strengths

- Representation-level analysis goes beyond output-only adversarial accuracy.
- Projection makes the perturbation constraint explicit.
- Multiple embeddings, models, and datasets provide an initial transfer check.
- Tables combine downstream accuracy, match success, image quality, and embedding similarity.
- The paper states white-box scope and proposes a mitigation direction.

## Weaknesses

- “Semantic” is narrower than clinician concepts, causality, or diagnostic faithfulness.
- Two model families and four datasets do not justify universal generality.
- No PRM code, fixed manifest, seeds, uncertainty intervals, or optimized-image release.
- No clinician imperceptibility/semantic-equivalence study.
- No matched CNN baseline, black-box transfer, external site, device shift, or subgroup audit.
- Mitigation evidence is qualitative and not adaptively evaluated.

## Potential Improvements

| Improvement | Rationale | Validation |
|---|---|---|
| Release PRM manifests and code | Enables exact reproduction | Recreate Tables I-III from hashes/configs |
| Clinician-blinded perceptual review | PSNR/SSIM are insufficient | Agreement and diagnostic-equivalence intervals |
| Broaden models/modalities/sites | Tests claimed generality | Locked cross-site/architecture matrix |
| Add natural-corruption controls | Distinguishes adversarial from ordinary fragility | Equal-budget corruption comparison |
| Held-out black-box transfer | Tests practical threat transfer | Surrogate-to-target success with budgets |
| Quantify detector performance | Mitigation lacks evidence | ROC, calibration, adaptive evasion, review load |

## Potential Implementations

1. `Representation robustness card`: versioned report combining clean utility, PRM success, PSNR/SSIM, embedding movement, uncertainty, and missing evidence.
2. `Clinical equivalence review queue`: blinded source/optimized pairs routed to credentialed reviewers with disagreement and harm labels.
3. `Selective stability monitor`: repeated benign perturbations trigger abstention and secondary review when representation/prediction instability exceeds calibrated bounds.

## Three Ways to Exercise This Research

1. Reproduce one synthetic PRM slice with a small open model, fixed pairs, seeds, epsilon, and hashes; success requires deterministic geometry/accuracy outputs and no sensitive images.
2. Compare PRM with blur, compression, resizing, and scanner-like noise at matched perceptual budgets; success requires separate adversarial and natural-fragility curves.
3. Evaluate a noise-stability abstention rule on held-out benign and manipulated samples; success requires calibrated risk-coverage and documented false-review load.

## Example MVP Product

- `Product name`: Clinical Representation Audit
- `Target user`: Medical-imaging ML safety and validation teams.
- `Problem`: Clean accuracy hides unstable or non-distinct internal representations.
- `Core workflow`: Import authorized model/data manifest, run bounded offline probes, compute utility/geometry/image-quality metrics, route ambiguous pairs to expert review, and export a public-safe evidence card.
- `Data requirements`: Synthetic or governed images, patient-isolated splits, model/config hashes, clinical labels, and reviewer annotations.
- `Architecture`: Isolated probe runner, metric engine, encrypted evidence store, review UI, calibration module, and Markdown/JSON exporter.
- `Success metrics`: Reproducibility, risk-coverage, cross-site stability, reviewer agreement, subgroup parity, and zero unauthorized data export.
- `Risk controls`: Offline only, least privilege, encryption, no diagnosis, perturbation budgets, human review, retention limits, and no image publication.
- `Limitations`: Cannot certify clinical safety or discover all representation failures.
- `MVP boundary`: Synthetic/public smoke tests before governed clinical data; no production decisions.

## Related Research and Reading

1. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` - anatomy/disease graphs make “semantic” structure explicit and expose clinical grounding, leakage, and external-validation needs.
2. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` - subtle visual manipulations show why image-level detection, fixed denominators, calibration, and causal evidence matter.
3. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - ViT alternatives and robustness audit requirements connect architecture claims to corruption/device evidence.

## Source References

- https://arxiv.org/abs/2507.01788v2
- https://arxiv.org/pdf/2507.01788
- https://ar5iv.labs.arxiv.org/html/2507.01788
- https://doi.org/10.48550/arXiv.2507.01788
- https://github.com/greentreeys/MIL-VT
- https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA/medical_diff_vqa_manuscript.md
- https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Document%20Fraud%20LLM/document_fraud_llm_manuscript.md
- https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md
- https://github.com/Delphoa/Black-Lake/blob/main/README.md

## Appendix

- Selection: 75,777 PDFs / 75,776 units; index 30,086; first draw; zero exclusions/reselections.
- Repair: official HTML 404; approved ar5iv full text passed; metadata official; zero partials.
- Cache: initial miss, `missing-only`, `pypdf` and `html-regex`, final cached.
- Representative Table I rows: APTOS MIL epsilon 0.02, 5.03% accuracy and 73.9% MSR; RFMiD ViT epsilon 0.10, 26.0% and 74.0%; bloodMNIST MedViT-L epsilon 0.10, 17.8% and 85.5%.
- Source policy: all original and derived source files withheld; no `.source/`.
