# DEP-E-20260714-OViP Preference

#vision-language #multimodal-ai #hallucination #preference-learning #online-learning #synthetic-data #evaluation #responsible-ai #arxiv-review

Public-safe DEP-E context: this entry preserves a source-grounded review of arXiv:2505.15963v2, *OViP: Online Vision-Language Preference Learning for VLM Hallucination*. The review covers failure-guided on-policy preference data, diffusion-generated negative images, response- and image-side objectives, balanced hallucination evaluation, reported results, compute, limitations, related Black Lake research, and bounded implementation ideas. No source document or local processing path is redistributed.

## Contents

- `README.md` - DEP inventory, item summaries, relevance notes, and source attribution.
- `ovip_preference_manuscript.md` - Schema-complete research manuscript with metadata, evidence ledger, detailed method/results review, limitations, safe implementation paths, replication checklist, and public source references.

No `.source/` directory exists. PDF, full-paper HTML, metadata HTML, TeX source, extracted text, and caches were retained locally and withheld from this public deposit.

## Summary of Items

`ovip_preference_manuscript.md` distinguishes the authors' claims from reviewer interpretation and preserves the paper's most decision-relevant evidence. OViP samples the current LVLM during training, selects high-contrast response pairs with an external judge, synthesizes hard-negative images from response discrepancies, and applies response- and image-side preference losses. The manuscript records the paper's one-epoch 7B HRI 9.58 and General Accuracy Difference +0.88, the online/offline ablation, the reported 1.97x efficiency claim, and the seven-A800 training topology without implying independent reproduction.

The artifact also preserves critical boundaries: HRI is normalized with observed reference gains that include OViP endpoints; benchmark corrections were incomplete; filter thresholds were not carefully tuned; the shown response judge does not directly inspect the image; and synthetic negative images were not independently audited for semantic isolation, bias, or shortcuts. Official code and sample data were inspected at repository-documentation level but not executed.

## Insights and Relevance

OViP is relevant to Black Lake because it treats alignment data as a moving target: the model's current failures determine which counterexamples should be created next. The exactly three related deposits sharpen that idea from complementary directions. VLM Probing supplies internal and behavioral grounding diagnostics; VideoWeave Geometry supplies consistency checks for generated visual evidence; and BA-LoRA Bias supplies behavior-preservation and drift controls for low-rank adaptation. Together they motivate an auditable feedback loop in which negative generation, model updating, and balanced release evidence remain separate reviewable stages.

The practical near-term opportunity is not an unreviewed reproduction of the full seven-GPU stack. It is a local evidence gate for preference-pair provenance, synthetic-negative quality, precision/coverage balance, calibration, modality dependence, general-capability retention, and public-safe reporting. Such a gate should use fixed metric ranges, aggregate outputs, independent audits, and human review before any model promotion.

## Attribution Block

- Source URL: https://arxiv.org/abs/2505.15963
  - Applies to: `ovip_preference_manuscript.md` and `README.md`.
  - Notes: Canonical metadata, title, authors, version dates, abstract, subjects, DOI, license, and source locators.
- Source URL: https://arxiv.org/html/2505.15963
  - Applies to: `ovip_preference_manuscript.md`.
  - Notes: Primary full-paper evidence for method, experiments, evaluation, results, ethics, limitations, and appendices.
- Source URL: https://arxiv.org/pdf/2505.15963
  - Applies to: `ovip_preference_manuscript.md`.
  - Notes: Public PDF locator; the verified local copy was withheld.
- Source URL: https://arxiv.org/e-print/2505.15963
  - Applies to: `ovip_preference_manuscript.md`.
  - Notes: Public TeX-source locator used to resolve formulas and table formatting; the local archive was withheld.
- Source URL: https://doi.org/10.48550/arXiv.2505.15963
  - Applies to: source identity in both files.
  - Notes: arXiv-issued persistent identifier.
- Source URL: https://github.com/lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination
  - Applies to: implementation and reproducibility notes in `ovip_preference_manuscript.md`.
  - Notes: Official repository inspected without code execution or redistribution.
- Source URL: https://creativecommons.org/licenses/by/4.0/
  - Applies to: license notes in both files.
  - Notes: License target linked by the canonical arXiv record; unrelated code/data dependencies require separate review.
- Source file: Withheld locally by policy.
  - Applies to: PDF, full-paper HTML, metadata HTML, TeX source, extracted text, caches, and private verification records used for the review.
  - Notes: No source files were uploaded, committed, staged, copied into the DEP, or sent to Slack.
