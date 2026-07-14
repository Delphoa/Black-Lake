# Report-Mark: OViP Preference Learning

## Source Metadata

| Field | Value |
|---|---|
| Canonical title | *OViP: Online Vision-Language Preference Learning for VLM Hallucination* |
| Authors | Shujun Liu; Siyuan Wang; Zejun Li; Jianxiang Wang; Cheng Zeng; Zhongyu Wei |
| Identifier | arXiv:2505.15963v2 |
| DOI | https://doi.org/10.48550/arXiv.2505.15963 |
| Dates | v1 submitted 2025-05-21; v2 revised 2025-09-28 |
| Platform / subjects | arXiv preprint; Computer Vision and Pattern Recognition; Computation and Language |
| License | CC BY 4.0 is linked from the canonical arXiv record |
| Primary records | https://arxiv.org/abs/2505.15963; https://arxiv.org/html/2505.15963; https://arxiv.org/pdf/2505.15963 |
| Official implementation | https://github.com/lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination |
| Review date | 2026-07-14 |
| Source handling | Complete PDF, full-paper HTML, metadata HTML, TeX source, and extracted caches were inspected locally and withheld from the public repository. |

## Review Question

Does OViP provide credible evidence that on-policy, failure-guided image and response preference data reduce LVLM hallucination without merely shortening answers or degrading general multimodal capability, and what should be verified before its design becomes an engineering pattern?

## Concise Research Notes

### Problem

Static multimodal preference datasets often construct negative responses or images with generic edits that do not match the target model's current failure distribution. This can teach an LVLM to recognize easy, off-distribution negatives while leaving its actual hallucinations insufficiently supervised. Evaluation can compound the problem: a model may improve entity precision by omitting relevant content, appearing safer while becoming less informative.

### Method

OViP runs training-time inference with the current LVLM, samples 16 candidate responses per prompt, scores them with an external LLM against a reference answer, and selects pairs whose reward gap is large enough. Positive responses must score at least 6, negative responses at most 4, and the score-gap margin is 3. When all candidates are weak, the offline reference may supply the positive response.

The method asks another LLM to identify semantic differences between positive and negative responses and convert the hallucinated content into an image description. FLUX.1-dev then synthesizes a hard negative image. The current model is optimized with response-side DPO and an image-side contrastive preference loss while an experience buffer smooths variable sample yield. In the paper's usage, “online” means on-policy rather than internet-connected.

### Evidence and Results

The experiments use LLaVA-1.5 7B and 13B models, CLIP ViT-L-336px visual features, Vicuna language backbones, and LoRA rank 256 / alpha 512. The training set has 8,730 samples across 4,013 distinct image-query combinations. Five hallucination-related benchmarks are paired with four general-capability benchmarks.

For LLaVA-1.5-7B after one epoch, Table 1 reports OViP HRI 9.58 and General Accuracy Difference +0.88; after two epochs it reports HRI 10.00 and General Accuracy Difference -1.01. For 13B, one epoch reports HRI 5.25 and +0.85, while two epochs reports HRI 8.02 and +2.02. The online/offline ablation reports one-epoch HRI 9.36 for online OViP versus 4.32 offline, with AMBER-generative Cover 51.1 versus 49.9.

The paper reports approximately 17 hours on seven A800 40GB GPUs: four for VLM training, one for the judge/prompt LLM, and two for diffusion services. The authors estimate 1.97x higher training efficiency than GRPO for comparable performance, despite slower iterations. These are reported results; no training or benchmark was reproduced for this report.

### Evaluation Caveat

OViP improves evaluation by combining AMBER/ObjectHal precision and coverage through F1 and by replacing a text-only MMHal judge with a multimodal judge. Its HRI aggregates normalized improvement across five benchmarks. However, the main reference ranges use OViP's two-epoch results for most metrics, and the appendix defines weights from maximum observed gains. HRI is therefore informative within the paper's comparison but not a universal or independently fixed scale.

### Limitations

The paper does not test PPO or GRPO combined with image-level contrastive objectives. It states that current benchmarks remain incomplete, only a subset of erroneous evaluation cases was manually corrected, and sampling/filter thresholds were not carefully tuned. The external judge does not directly inspect the input image in the shown scoring prompt, which makes reference quality and judge behavior important dependencies. Synthetic negative images can also introduce unrelated artifacts, stereotypes, or shortcut cues unless explicitly audited.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Boundary |
|---|---|---|---|---|
| E1 | Complete arXiv v2 paper body across PDF, HTML, and TeX extraction | Method, formulas, experiments, tables, limitations, appendices | High for reporting | Experiments remain author-reported. |
| E2 | Canonical arXiv metadata and DOI/license link | Title, authors, version dates, subjects, persistent identifier, CC BY 4.0 locator | High | arXiv-issued DOI does not establish journal peer review. |
| E3 | Official OViP repository | Modified LLaMAFactory code, evaluation code, sample archive, dependency/model/data guidance | Medium-high | One visible commit, no release, and no execution in this review. |
| E4 | Local archive verification and extraction summary | Complete-paper gate, repair status, cache outputs | High | Local paths and source files are intentionally withheld. |
| E5 | Black Lake policy README and `.lake-data` README | DEP-E class, nested filing, publication-index, source-withholding rules | High | Process evidence only. |
| E6 | Exactly three related DEP manuscripts | Cross-deposit synthesis | Medium | Related reviews do not validate OViP metrics. |

## Exactly Three Related DEP Entries

1. [VLM Probing manuscript](../../.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md) - VALUE operationalizes fusion, modality importance, relation, leakage, and causal-evidence questions. Applied to OViP, those probes could test whether a better hallucination score corresponds to stronger use of visual evidence rather than answer-style shifts.
2. [VideoWeave Geometry manuscript](../../.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md) - VideoWeave treats generated media quality as a multi-signal consistency problem. Its evidence-gate framing transfers to OViP's diffusion negatives: realism is insufficient unless the requested semantic counterfactual is isolated and other content remains stable.
3. [BA-LoRA Bias manuscript](../../.lake-data/DEP-E/DEP-E-20260709-BA-LoRA%20Bias/ba-lora-bias-manuscript.md) - BA-LoRA frames adaptation as preserving useful base behavior while reducing drift, collapse, and noisy overfit. OViP's LoRA training faces the same preservation problem across multimodal grounding, informativeness, and general capability.

## Synthesis Note

### Concept Bridge

OViP turns a model's current failures into the next training distribution. VLM Probing supplies internal and behavioral diagnostics for whether that feedback changes cross-modal grounding; VideoWeave supplies a consistency discipline for auditing generated visual counterfactuals; BA-LoRA supplies adaptation-drift and behavior-preservation controls. Together they suggest a closed-loop alignment system in which negative-data generation, model updating, and evidence gates are distinct auditable stages rather than one opaque training run.

### Potential Implementations

1. `Counterfactual Quality Gate` - Validate that each generated hard-negative image changes the intended entity, attribute, or relation while preserving unrelated content; reject examples with artifacts, unsafe content, excessive distribution shift, or disagreement among independent semantic checks.
2. `Grounding Regression Harness` - Compare base and adapted LVLMs on precision, coverage, calibration, counterfactual sensitivity, modality-use probes, and general capability; block promotion when hallucination gains come from omission or language-prior shortcuts.
3. `Online Preference Provenance Ledger` - Record aggregate response-pair scores, judge version, prompt version, generator version, filtering yield, rejection reasons, and dataset slices so a training claim can be reconstructed without publishing raw licensed images or model outputs.

### Deeper Relationship Observations

1. OViP's on-policy loop and BA-LoRA's drift controls address opposite sides of adaptation: one keeps supervision aligned with emerging failures, while the other asks whether the update preserves useful inherited behavior.
2. OViP's generated negative image is both training data and an empirical claim about causality; VideoWeave shows why visual plausibility alone cannot establish that the intended semantic factor changed cleanly.
3. VLM Probing reveals a possible hidden failure: an adapted model can improve output metrics without increasing causal dependence on vision, so internal probes must be paired with interventions and behavioral counterfactuals.

### Conceptual Similarities

1. All four works separate aggregate task performance from a more specific reliability signal: hallucination balance, cross-modal representation behavior, geometry consistency, or adaptation robustness.
2. All rely on structured intermediate artifacts—preference pairs, probe activations, geometry latents, or output distributions—that can be inspected independently of the final score.
3. All expose a preservation trade-off: removing one failure mode can damage informativeness, general capability, geometry, diversity, or base knowledge unless evaluation is explicitly multi-objective.

### MVP Implementations with Code Mock-ups

1. `Negative-pair semantic validator` - a local, deterministic contract for rejecting examples whose declared change is not isolated.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class NegativeAudit:
    target_changed: bool
    unrelated_similarity: float
    unsafe: bool

def accept(a: NegativeAudit) -> bool:
    return a.target_changed and a.unrelated_similarity >= 0.90 and not a.unsafe
```

Dependencies: Python 3.11 standard library. Failure mode: upstream similarity and safety signals can be wrong; retain human review for sampled and disputed cases.

2. `Balanced hallucination gate` - reject apparent gains that are purchased by coverage or general-capability loss.

```python
def release_gate(base, candidate):
    return {
        "precision_ok": candidate["precision"] >= base["precision"],
        "coverage_ok": candidate["coverage"] >= base["coverage"] - 0.5,
        "general_ok": candidate["general"] >= base["general"] - 1.0,
        "calibration_ok": candidate["ece"] <= base["ece"],
    }
```

Dependencies: Python 3.11 standard library. Failure mode: thresholds are illustrative and must be fixed before evaluation on licensed, versioned slices.

3. `Aggregate provenance record` - emit a public-safe summary without raw prompts, images, or local paths.

```python
def public_record(run):
    allowed = ("model_id", "judge_id", "generator_id", "prompt_version",
               "sample_count", "accepted_count", "rejection_counts")
    return {key: run[key] for key in allowed if key in run}

assert "raw_images" not in public_record({"raw_images": [b"private"]})
```

Dependencies: Python 3.11 standard library. Failure mode: allowlists must be versioned and tested against identifiers, free text, secrets, and licensed content before publication.

### Developer Challenges

1. Build asynchronous sampling, scoring, prompt generation, diffusion, buffering, and training without deadlocks, silent retries, stale model versions, or unbounded storage growth.
2. Pin the judge, generator, training framework, datasets, templates, and metric implementations so reruns can distinguish method effects from infrastructure drift.
3. Create privacy- and license-aware telemetry that supports audit, bias analysis, and rollback while preventing raw prompts, images, user data, secrets, or local paths from entering public artifacts.

### Author Challenges

1. Validate HRI with independently fixed reference ranges, confidence intervals, judge variation, and corrected benchmark labels so aggregation is not coupled to the best OViP result.
2. Quantify semantic isolation and bias in generated negative images, including whether unrelated objects, styles, demographics, or backgrounds become shortcut signals.
3. Test additional model families, data domains, reinforcement-learning objectives, and carefully tuned filters while reporting the full Pareto surface across hallucination, coverage, general capability, calibration, and compute.

## Validation Notes

- The first uniform draw was accepted after ID, DOI, normalized-title, slug, memory, repository, related-repository, and 24-hour worktree checks; exclusions and reselections were zero.
- Review did not begin until the repaired archive unit passed both PDF and full-paper HTML integrity rules.
- The cache was initially absent and became fully cached through local `missing-only` extraction after repair.
- Table signs and HRI values were checked against TeX source because HTML rendering dropped some sign formatting.
- Source files, caches, extracted text, local paths, exact execution timestamps, usernames, machine identifiers, and timezone labels are absent from this report.
- Official code and sample data were inspected at repository-documentation level but not executed; reproducibility is not claimed.
- Exactly three related DEP entries and the exact-count Synthesis Note elements were checked during validation.

## Attribution Block

- Source URL: https://arxiv.org/abs/2505.15963
  - Applies to: this Report-Mark.
  - Notes: Canonical title, authors, identifier, version dates, abstract, subjects, DOI, license, and source locators.
- Source URL: https://arxiv.org/html/2505.15963
  - Applies to: this Report-Mark.
  - Notes: Full-paper method, experiments, metrics, results, ethics, limitations, and appendices.
- Source URL: https://arxiv.org/pdf/2505.15963
  - Applies to: this Report-Mark.
  - Notes: Public PDF locator; the locally verified source copy was withheld.
- Source URL: https://doi.org/10.48550/arXiv.2505.15963
  - Applies to: source identity and persistent attribution.
  - Notes: arXiv-issued persistent identifier.
- Source URL: https://github.com/lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination
  - Applies to: implementation and reproducibility notes.
  - Notes: Official code repository inspected without execution or redistribution.
- Source URL: https://creativecommons.org/licenses/by/4.0/
  - Applies to: license note.
  - Notes: License target linked by the canonical arXiv record.
- Source file: Withheld locally by policy.
  - Applies to: PDF, full-paper HTML, metadata HTML, TeX source, and extraction caches used for review.
  - Notes: No source files were uploaded, committed, staged, copied into the DEP, or sent to Slack.
