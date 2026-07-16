# DEP-E-20260716-Adversarial Label Noise

**Title:** Label noise in adversarial training review
**Tags:** adversarial-training, robust-overfitting, label-noise, calibration, source-first-review

Public-safe context: on 2026-07-16, one local arXiv paper unit was selected uniformly from 75,776 unique PDF-parent units and accepted on the first draw after ID, DOI, both known titles, slug, repository, memory, companion-repository, and 24-hour checks. Its valid PDF lacked full-paper HTML, so the official arXiv full-paper page was fetched and passed the mandatory integrity gate. No local path, exact execution timestamp, private cache, or source file appears here.

## Contents

- `adversarial_label_noise_manuscript.md` - schema-complete, source-grounded research manuscript.
- `README.md` - deposit context, inventory, synthesis, and attribution.

## Summary of Items

The manuscript reconstructs the paper's implicit-label-noise account of robust overfitting, its epoch-wise double-descent observation, KD-AT-Auto label rectification, total-variation existence results, and experiments across datasets, architectures, training methods, and attacks. It records selection, deduplication, source repair, cache behavior, and the no-source-upload gate.

## Insights and Relevance

The paper reframes adversarial training labels as distributions that may change after perturbation, while standard training retains the clean one-hot label. A robust self-teacher, temperature scaling, and interpolation substantially reduce the reported best-to-last robust-accuracy gaps. On CIFAR-10 the gap falls from 5.93 to 0.25 points, and on CIFAR-100 from 5.04 to 0.12.

The three related deposits expose the main validation boundary. ViT Semantic Robustness asks whether bounded perturbations preserve human semantics; PAC Confidence distinguishes calibrated finite-sample uncertainty from unsupported transfer under adversarial shift; AFIDAF Vision Filters calls for architecture- and hardware-aware robustness audits. Together they motivate per-example semantic review, held-out calibration, repeated seeds, and attack-transfer tests before treating rectified soft labels as ground truth.

## Attribution Block

- Primary paper: *Label Noise in Adversarial Training: A Novel Perspective to Study Robust Overfitting*, Chengyu Dong, Liyuan Liu, and Jingbo Shang.
- arXiv: https://arxiv.org/abs/2110.03135v4
- Full paper: https://arxiv.org/pdf/2110.03135 and https://arxiv.org/html/2110.03135
- arXiv DOI: https://doi.org/10.48550/arXiv.2110.03135
- Proceedings: https://proceedings.neurips.cc/paper_files/paper/2022/hash/6fe6a2ba2594521d15af3b1f2162d79c-Abstract-Conference.html
- This deposit is an independent review. Source files, metadata HTML, cache outputs, and extracted text were withheld locally and were not uploaded.
