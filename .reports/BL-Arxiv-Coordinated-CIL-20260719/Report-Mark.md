# Report-Mark: Coordinated CIL

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P09`
- Review date: 2026-07-19
- Review type: source-first continual-learning and imbalance synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Joint Input and Output Coordination for Class-Incremental Learning* |
| Authors | Shuai Wang; Yibing Zhan; Yong Luo; Han Hu; Wei Yu; Yonggang Wen; Dacheng Tao |
| Stable identifier | arXiv:2409.05620v1 |
| Submission history | Submitted 2024-09-09 |
| DOI | https://doi.org/10.48550/arXiv.2409.05620 |
| Primary record | https://arxiv.org/abs/2409.05620 |
| Full-paper HTML | https://arxiv.org/html/2409.05620 |
| PDF | https://arxiv.org/pdf/2409.05620 |
| Source state | Verified complete after one bounded repair; source files withheld locally. |
| Deployment job ID | `BLAD-2200-20260719-7D93E819` |
| Deployment item ID | `BLAD-2200-20260719-7D93E819-P09` |

## Concise Research Notes

### Problem

Rehearsal-based class-incremental learning keeps few old examples beside abundant new data. This creates old/new task imbalance, within-task class imbalance, and interference between old and new classifier outputs.

### Method

JIOC adds two losses to existing memory-based learners. Input coordination weights each training example using the absolute gradient magnitude associated with its true-class output, aiming to reduce dominance by overrepresented categories. Output coordination uses task-split heads and distillation to preserve each old task's output distribution on new data, while suppressing old examples on new-task heads. The mechanism is added to ICARL, DER, and FOSTER.

### Evidence

Experiments cover balanced CIFAR100, MiniImageNet, TinyImageNet, CUB-200-2011, and long-tail CIFAR10/100 across memory budgets and task counts. On CIFAR100-LT with ICARL, 10 tasks, and 1K old examples, Table 2 reports 55.24 versus 50.17 average accuracy; the gain is larger on some ICARL configurations and smaller for DER. Table 3 reports gains across the four balanced datasets, including ICARL gains up to 9.42 points on CUB-200-2011. Ablations separate input and output coordination and generally show their combination strongest.

### Limits

Evaluation is limited to image classification with stored exemplars, average accuracy is the primary metric, and the work does not deeply report calibration, fairness, memory/computation overhead, hyperparameter sensitivity, task-order variance, or privacy of retained samples. Gradient-derived weights may reflect hard/noisy examples as well as minority classes. The human-memory analogy is motivational rather than biological evidence.

## Evidence and Attribution

| Claim | Source basis | Reviewer qualification |
|---|---|---|
| JIOC addresses input imbalance and output interference jointly. | Sections 3.2-3.4. | Direct method transcription. |
| The mechanism improves ICARL, DER, and FOSTER across reported datasets. | Tables 2-3. | Source-reported; gains vary materially by base method and setting. |
| Input and output terms are complementary. | Tables 4-6 and section 4.3. | Strongest in the authors' ICARL ablations. |
| Gradient magnitude balances categories. | Section 3.3. | Mechanism is plausible but can also upweight label noise or outliers. |
| Task-split distillation preserves old outputs. | Section 3.4. | Stability may trade off plasticity and depends on stored-data quality. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` - difficult examples and noisy labels can distort adaptive weighting.
2. `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` - distillation quality depends on workload, teacher behavior, and evaluation budget.
3. `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` - multi-task interference needs explicit measurement rather than architectural assertion.

## Synthesis Note

### Concept Bridge

JIOC coordinates which examples receive learning pressure and which output distributions must remain stable. Adversarial Label Noise warns that high-gradient examples may be mislabeled or adversarial rather than merely underrepresented. KDFlow shows that distillation is not a generic preservation guarantee; it depends on teacher quality, workload, and capacity. Device Tuning MTL supplies a broader task-interference boundary: shared or sequential models need explicit per-task evidence. Together these deposits motivate a continual-learning audit that decomposes class balance, gradient weight, label quality, old/new accuracy, calibration, memory budget, and task order.

### Potential Implementations

1. Build an offline rehearsal evaluator with frozen task orders, exemplar budgets, and per-class old/new accuracy.
2. Add a robust weight cap and noise diagnostic before gradient-derived sample weights affect training.
3. Create a distillation audit that records teacher version, per-task logits, temperature, divergence, and stability-plasticity trade-offs.

### Deeper Relationship Observations

1. Adaptive input weighting and replay selection jointly determine which historical evidence survives, even if designed separately.
2. Output preservation can protect old classes while freezing earlier bias or calibration error.
3. Average accuracy can improve while rare-class, old-task, or new-task behavior worsens, so decomposition is essential.

### Conceptual Similarities

1. JIOC input weights and label-noise defenses both interpret per-example difficulty signals and risk confusing minority evidence with corruption.
2. JIOC output coordination and KDFlow both preserve behavior through teacher-student output constraints.
3. JIOC task heads and device multi-task designs both confront interference between shared representation and task-specific outputs.

### MVP Implementations with Code Mock-Ups

1. Capped gradient weighting:

```python
def sample_weight(prob_true, cap=2.0, floor=0.1):
    raw = abs(prob_true - 1.0)
    return min(cap, max(floor, raw))
```

2. Per-task retention record:

```python
def retention(before, after):
    return {task: {"before": before[task], "after": after[task],
                   "delta": after[task] - before[task]}
            for task in before}
```

3. Distillation divergence gate:

```python
def distill_gate(divergence, threshold, noisy_fraction):
    return {"accept": divergence <= threshold and noisy_fraction < 0.1,
            "divergence": divergence, "noisy_fraction": noisy_fraction}
```

### Developer Challenges

1. Replay buffers, task boundaries, label maps, and teacher checkpoints must remain reproducible across steps.
2. Per-example gradients add overhead and can be unstable under mixed precision or noisy labels.
3. Task-split heads complicate deployment when task identity is unavailable or class spaces evolve irregularly.

### Author Challenges

1. Evaluate task-order variance, repeated seeds, compute/memory overhead, and broader continual-learning protocols.
2. Distinguish imbalance from label noise, hard examples, and domain shift in the weighting mechanism.
3. Report calibration, per-class forgetting, stability-plasticity frontiers, and privacy implications of stored exemplars.

## Validation Notes

- Random selection: index 51,598 of 75,777 units from 75,790 PDFs; first draw; duplicate exclusions 0; reselections 0.
- Integrity: one bounded partial-to-complete repair; PDF and official HTML passed; cache `cached`; no partials.
- Structure: required Report-Mark sections; exactly three items per mandated synthesis category; three syntax-checked Python blocks.
- Safety: implementation ideas are offline evaluation and diagnostics; no privacy-sensitive dataset or model artifact is distributed.
- Public-safety: no local path, exact timestamp, timezone label, user/machine context, or source document is published.

## Attribution Block

- https://arxiv.org/abs/2409.05620 - canonical metadata, authorship, abstract, and identifier.
- https://arxiv.org/html/2409.05620 - primary full-paper method, results, tables, and appendix evidence.
- https://arxiv.org/pdf/2409.05620 - validated complete PDF; withheld locally.
- https://doi.org/10.48550/arXiv.2409.05620 - persistent identifier.
- `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` - related noise/imbalance evidence.
- `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` - related distillation evidence.
- `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` - related task-interference evidence.
- PDF, HTML, metadata, extracted text, and cache files were withheld locally; zero source uploads.
