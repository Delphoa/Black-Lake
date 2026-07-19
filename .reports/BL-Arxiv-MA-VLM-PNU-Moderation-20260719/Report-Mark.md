# Report-Mark: MA-VLM PNU Moderation

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P01`
- Review date: 2026-07-19
- Review type: source-first Arxiv DEP research review and implementation synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Multi-Agent VLMs Guided Self-Training with PNU Loss for Low-Resource Offensive Content Detection* |
| Authors | Han Wang; Deyi Ji; Junyu Lu; Lanyun Zhu; Hailong Zhang; Haiyang Wu; Liqun Liu; Peng Shu; Roy Ka-Wei Lee |
| Stable identifier | arXiv:2511.13759v1 |
| Submission date | 2025-11-14 |
| Venue context | The arXiv comments identify AAAI-26; this review does not independently establish proceedings publication. |
| DOI | https://doi.org/10.48550/arXiv.2511.13759 |
| Primary record | https://arxiv.org/abs/2511.13759 |
| Full-paper HTML | https://arxiv.org/html/2511.13759 |
| PDF | https://arxiv.org/pdf/2511.13759 |
| Source package | https://arxiv.org/e-print/2511.13759 |
| Official code | https://github.com/Social-AI-Studio/MA-VLM |
| License visibility | CC BY 4.0 link visible on the arXiv record; third-party datasets and code retain their own terms. |
| Source state | Verified complete after bounded local repair; all original and extracted source files withheld locally. |
| Deployment job ID | `BLAD-2200-20260719-7D93E819` |
| Deployment item ID | `BLAD-2200-20260719-7D93E819-P01` |

## Concise Research Notes

### Problem

Offensive-content detection needs culturally and contextually sensitive labels, but high-quality annotations are expensive and rare. Traditional self-training can amplify the errors of a weak classifier trained on only tens or hundreds of labels. Calling a large VLM for every production item is also costly. The paper asks whether a large multimodal model can guide training while a smaller CLIP-based classifier remains the deployed inference model.

### Method

The pipeline first trains a lightweight classifier on `n` labeled examples. It ranks unlabeled examples by confidence and sends the top `k` candidates to two Qwen-2.5-VL-72B personas: a strict moderator and a lenient user. Each persona issues an initial decision and rationale, reviews the other's judgment, and revises its decision. A sample becomes Positive or Negative `Agreed-Unknown` only when the classifier and both agents agree; every conflict becomes `Disagreed-Unknown`.

Both groups are retained. Agreed samples receive soft targets (`0.67` positive and `0.33` negative in the reported setup). Disagreed samples remain unlabeled and enter a customized positive-negative-unlabeled loss. The dataset-dependent parameter `gamma` interpolates PN training with PU or NU risk. Development performance determines whether a round is retained or reverted; the process continues through the unlabeled pool.

### Data and Evaluation

The paper evaluates four binary tasks: Facebook Hateful Memes (FHM), MAMI misogyny, HSOL hate/offensive language, and Sentiment140. It uses 80/10/10 train/development/test splits. FHM contributes 9,000 usable examples because its official test labels are unavailable; MAMI is about 10,000 examples; HSOL and Sentiment140 are balanced and subsampled to 10,000 examples. The core table uses only 100 labeled training examples, with Accuracy and Macro-F1 and Macro-F1 as the primary metric.

The classifier is CLIP-Large plus a one-layer MLP. The large pseudo-labeling model is frozen Qwen-2.5-VL-72B. Training uses 10 epochs per round, `k=500`, class prior `0.5`, and dataset-specific `gamma` (`0.0` for FHM and `0.1` for the other reported tasks). Qwen-2.5-VL-7B is a supervised-only large-model comparator; RGCL and supervised-only CLIP are additional baselines.

### Reported Results

With `n=100`, combined CLIP-plus-Qwen pseudo-labeling reports Macro-F1 of 72.68 on FHM, 73.49 on MAMI, 86.69 on HSOL, and 77.11 on Sentiment140. Supervised-only CLIP reports 59.24, 62.18, 85.30, and 64.22 respectively. Supervised-only Qwen-7B reports 70.41, 76.06, 84.89, and 78.19. The guided lightweight model is therefore strongest in the table on FHM and HSOL, while trailing Qwen-7B on MAMI and Sentiment140.

At `n=50`, the guided method reports Macro-F1 71.27 on FHM and 71.40 on MAMI, compared with supervised-only CLIP at 48.76 and 56.03. On MAMI, supervised-only Qwen-7B remains slightly higher at 73.00; on FHM it is much lower at 39.11. The result supports low-label utility in the tested splits but is not evidence of universal dominance.

The prompt-format ablation reports MAMI Macro-F1 81.64 for the dual-persona format versus 79.17 zero-shot, 75.08 few-shot, and 78.28 chain-of-thought when Qwen-72B is used without classifier training. On FHM, the margin is small: 74.62 versus 74.46 zero-shot and 74.43 chain-of-thought. The `gamma` ablation makes the dataset dependency visible: FHM's best Macro-F1 is at `gamma=0.0`, while MAMI's is at `0.1`.

### Reviewer Interpretation

The durable pattern is disagreement routing, not automated consensus as truth. Agreement is used as softer supervision; disagreement is preserved rather than discarded. That is a stronger design than hard pseudo-labeling, but the three voters are not independent: the agents share a model family and prompt frame, while the classifier and teacher may inherit correlated pretraining biases. The paper does not demonstrate demographic fairness, cross-cultural reliability, or production moderation safety despite motivating the method in those terms.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | Canonical arXiv record and DOI | Identity, authors, date, subjects, venue comment, license link | High | Metadata does not validate results. |
| E2 | Verified full-paper HTML, PDF, and source package | Method, equations, datasets, tables, ablations, conclusion | High for transcription | Experiments were not rerun. |
| E3 | Table 1 and Table 3 | Main `n=100` and label-count results | High for reported values | No confidence intervals or multi-seed uncertainty were identified. |
| E4 | Table 4 and Table 5 | Prompt-format and `gamma` sensitivity | High for reported values | Only selected datasets appear in the main ablations. |
| E5 | Official MA-VLM repository | Data layout, inference script, training command, demo data, 25-commit public history | Medium-high | Repository was inspected but not cloned, installed, or executed; no release was published. |
| E6 | Local integrity and extraction records | Random draw, dedup, repair, complete-source gate, cache status | High | Private source locations are withheld. |
| E7 | OViP Preference DEP | On-policy VLM feedback and judge-dependence bridge | Medium | Different hallucination-alignment task. |
| E8 | Adversarial Label Noise DEP | Soft-target and distribution-mismatch bridge | Medium | Different robustness setting and threat model. |
| E9 | RLMF Uncertainty DEP | Conditional self-evaluation and proxy-governance bridge | Medium | Language-model uncertainty rather than moderation labels. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
   - Relevance: OViP generates model-specific VLM feedback as the target model changes. MA-VLM similarly uses a large VLM system to shape a smaller model's training distribution. Both pipelines can amplify a judge's blind spots and therefore need judge provenance, held-out auditing, and explicit failure strata.
   - Source basis: inspected OViP manuscript sections on online negative generation, external scoring, ablations, and judge dependence.
2. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md`
   - Relevance: both works reject hard one-hot labels as complete truth under ambiguity. KD-AT-Auto rectifies uncertain adversarial labels; MA-VLM assigns soft targets to consensus pseudo-labels and treats contested cases as unlabeled. Both require calibration checks because a teacher can be confidently wrong.
   - Source basis: inspected manuscript sections on implicit label-distribution mismatch, soft rectification, total-variation reasoning, and teacher limitations.
3. `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md`
   - Relevance: RLMF permits metacognitive feedback to amplify only completions that already pass an independent faithfulness predicate. MA-VLM can adopt the same governance pattern: agent consensus should weight or route evidence, never independently authorize a consequential moderation action.
   - Source basis: inspected manuscript sections on metacognitive targets, conditional advantage scaling, selection, and evaluator-proxy limitations.

## Synthesis Note

### Concept Bridge

The three related deposits expose a shared design problem: learning from model-generated supervision without mistaking the supervisor for ground truth. OViP adapts feedback to the model's current failures; Adversarial Label Noise replaces brittle hard labels with distributional targets; RLMF gates self-evaluation behind an independently measured objective. MA-VLM combines all three motifs imperfectly—dynamic pseudo-labeling, soft labels, and disagreement—but lacks an explicit governance layer that measures agent correlation, calibration, and subgroup error before pseudo-labels become training data.

### Potential Implementations

1. **Offline disagreement router:** run the classifier and two role prompts on a consented or synthetic moderation set, storing only decisions, confidence, rationale hashes, and disagreement strata. Human reviewers label a balanced sample from every stratum before any retraining.
2. **Teacher-calibration harness:** measure whether consensus probability predicts human agreement across topics, languages, and protected groups; use calibration error and subgroup false-positive gaps to cap pseudo-label weights.
3. **PNU training sandbox:** reproduce only the training loss on public benchmark subsets, compare hard labels, soft consensus, abstention, and PNU routing over multiple seeds, and forbid direct integration with enforcement systems.

### Deeper Relationship Observations

1. Consensus among role prompts is weaker than consensus among independent annotators because both agents share the same weights and training data; diversity of prose does not establish statistical independence.
2. Treating disagreement as unlabeled preserves information, but a global `gamma` can still hide heterogeneous uncertainty; per-stratum or learned weights need held-out calibration and conservative clipping.
3. The validation-revert step is a useful circuit breaker, yet repeated use of the same development set can overfit the entire self-training trajectory even when each round appears to improve.

### Conceptual Similarities

1. MA-VLM and OViP both use frozen large multimodal systems to create training signals for a more efficient target model.
2. MA-VLM's soft `Agreed-Unknown` labels and KD-AT-Auto's rectified targets both acknowledge that model-produced labels are distributions, not facts.
3. MA-VLM disagreement routing and RLMF conditional gain control both separate an auxiliary confidence signal from the primary task objective.

### MVP Implementations with Code Mock-Ups

1. **Consensus triage record**

```python
def triage(classifier, moderator, user):
    votes = [classifier.label, moderator.label, user.label]
    agreed = len(set(votes)) == 1
    return {
        "route": "soft_pseudo_label" if agreed else "human_review",
        "label": votes[0] if agreed else None,
        "confidence": min(v.confidence for v in [classifier, moderator, user]),
    }
```

2. **Bounded pseudo-label weight**

```python
def pseudo_weight(consensus_confidence, calibration_error):
    raw = consensus_confidence * (1.0 - calibration_error)
    return max(0.0, min(raw, 0.5))  # never equal human-label weight in the MVP
```

3. **Stratified audit sampler**

```python
def audit_sample(records, per_stratum=25):
    buckets = {}
    for record in records:
        key = (record["route"], record["language"], record["topic"])
        buckets.setdefault(key, []).append(record)
    return {key: rows[:per_stratum] for key, rows in buckets.items()}
```

### Developer Challenges

1. Reproducing the iterative state machine without leakage between train, development, test, and pseudo-label audit records.
2. Making VLM inference, rationale exchange, and dataset preprocessing deterministic enough for traceable comparison while preserving sensitive content controls.
3. Implementing PNU risk estimates and calibration caps without numerical instability, class-prior drift, or silent subgroup underperformance.

### Author Challenges

1. Demonstrating that dual personas add information beyond repeated samples or prompt ensembling from the same model.
2. Establishing fairness and cultural validity with multilingual, subgroup-aware, human-reviewed evaluation rather than relying on aggregate Macro-F1.
3. Reporting multi-seed uncertainty, annotation-quality audits, compute/token cost, and independent test sets sufficient to support scalability claims.

## Validation Notes

- Deployment job ID: `BLAD-2200-20260719-7D93E819`.
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P01`.
- Random selection: uniform one-based index 25,453 of 75,776 candidate units; first draw accepted.
- Dedup validation: no arXiv ID, DOI, normalized-title, slug, artifact, memory, companion-repository, current-job, or preceding-24-hour same-paper marker; duplicate exclusions 0; reselections 0.
- Source validation: initial partial state repaired to verified complete. PDF and official full-paper HTML passed all byte, marker, structure, and truncation checks before synthesis.
- Cache validation: PDF, HTML, and source-package extraction all succeeded; cache status `cached`.
- Research depth: complete paper text, tables, appendices/source, canonical metadata, official repository README, and three related DEP manuscripts were inspected. No experiment was rerun.
- Related DEP count: exactly three.
- Synthesis cardinality: exactly three potential implementations, three deeper observations, three conceptual similarities, three code-mock MVPs, three developer challenges, and three author challenges.
- Public sanitization: passed subject to final pre-commit scan; no local path, home name, workspace root, machine name, local timezone label, or exact execution timestamp is intended for publication.
- Source locality: PDF, full-paper HTML, metadata HTML, source package, extracted text, and cache remain local. No `.source/` directory was created and no source file is eligible for staging.

## Attribution Block

- Source URL: https://arxiv.org/abs/2511.13759
  - Applies to: source identity, authors, dates, abstract, subjects, venue comment, and license locator.
- Source URL: https://arxiv.org/html/2511.13759
  - Applies to: full-paper method, experiments, results, limitations, tables, and appendices.
- Source URL: https://arxiv.org/pdf/2511.13759
  - Applies to: cross-format full-paper verification; source file withheld locally.
- Source URL: https://arxiv.org/e-print/2511.13759
  - Applies to: equations, tables, configuration details, and source cross-checks; source file withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2511.13759
  - Applies to: persistent paper identity.
- Source URL: https://github.com/Social-AI-Studio/MA-VLM
  - Applies to: official implementation availability, public README, commands, demo layout, and release boundary.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference
  - Applies to: related VLM feedback-loop synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise
  - Applies to: related soft-label and distribution-mismatch synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-RLMF%20Uncertainty
  - Applies to: related conditional self-evaluation synthesis.
- Source files: locally verified PDF, full-paper HTML, metadata HTML, source package, extracted text, and cache records.
  - Applies to: complete-source integrity, extraction, and claim cross-checking.
  - Notes: Withheld locally; none were copied, staged, uploaded, attached, or placed under `.source/`.
