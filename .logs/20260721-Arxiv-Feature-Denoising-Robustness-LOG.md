# Arxiv DEP Job Log: Feature Denoising

- Public run marker: 2026-07-21 (date only)
- Outcome: Complete after bounded local source repair
- Selected paper: *Feature Denoising for Improving Adversarial Robustness*
- Stable identifier: arXiv:1812.03411v2
- Public record: https://arxiv.org/abs/1812.03411
- arXiv DOI: https://doi.org/10.48550/arXiv.1812.03411

## Selection and Deduplication

- Candidate enumeration used `rg --files -g "*.pdf"` against the private source archive.
- The enumeration produced 75,779 PDF files and 75,776 unique PDF-parent paper units.
- Unique paper units were sorted, then PowerShell `Get-Random` selected zero-based index 61,119 uniformly from `[0, 75,776)`.
- The first draw was accepted: 0 duplicate exclusions, 0 other exclusions, and 0 reselections.
- Dedup checked arXiv ID, DOI, normalized title, slug family, and same-paper markers across live `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and relevant Black-Lake-Data records.
- Black-Lake-Data contains one metadata-only author-inventory row for this paper; it is not a processed DEP artifact and did not trigger exclusion.
- No matching Arxiv DEP artifact or same-paper marker within the prior 24 hours was found.

## Local Source Integrity

- Initial classification: Partial. The existing 8,228,548-byte PDF passed the minimum-size, `%PDF-`, trailing `%%EOF`, and SHA-256 checks, but full-paper HTML was absent.
- Repair: One bounded companion-bundle acquisition preserved the valid PDF and collected official metadata HTML, approved ar5iv full-paper HTML, and the arXiv source archive. The transfer used a 100 MB target ceiling, a 20 MB partial ceiling, no credentials, and one attempt per artifact.
- Final classification: Complete. The full-paper HTML is 218,260 bytes with 47,873 body characters, a full-document marker, 57 heading/section markers, six paper-structure term classes, no abstract/error marker, and zero partial files.
- Local README, attribution/provenance, machine-readable summaries, and verification report were updated before review.
- Source locality: PDF, full-paper HTML, metadata HTML, source archive, extraction material, repair records, and renderings remained private. No source files were uploaded and no public `.source/` directory was created.

## Review Outcome

The paper adds trainable residual feature-denoising blocks to intermediate convolutional features and combines them with large-scale PGD adversarial training. The default ResNet-152 comparison improves 10-step targeted PGD accuracy from 52.5% to 55.7% and 2,000-step accuracy from 39.2% to 42.6% at an `L_inf` budget of 16/256. Controlled null, capacity, filter, and block-design ablations support a denoising-specific contribution, while the 27.9%-to-55.7% headline comparison is system-level and should not be attributed to denoising alone. The archived official repository supplies models and evaluation/training code but depends on a legacy TensorFlow/Tensorpack/Horovod stack.

## Generated Outputs

- `.logs/20260721-Arxiv-Feature-Denoising-Robustness-LOG.md`
- `.reports/BL-Arxiv-Feature-Denoising-Robustness-20260721/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260721-Feature Denoising/README.md`
- `.lake-data/DEP-E/DEP-E-20260721-Feature Denoising/feature_denoising_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` - adversarial-training dynamics, threat-model calibration, and robust-overfitting controls.
2. `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md` - bounded perturbations, representation movement, and feature-space robustness claims.
3. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - feature filtering, non-local/global mixing, and architecture-level ablation discipline.

## Next-Review Questions

1. Do feature-denoising gains persist under modern multi-attack suites, untargeted attacks, and matched compute across current convolutional and transformer backbones?
2. Can feature-noise reduction be measured quantitatively without confounding it with end-to-end changes in feature scale and distribution?
3. Which residual gate, filter family, and insertion depth gives the best robust-accuracy, clean-accuracy, latency, and memory frontier on contemporary hardware?

## Challenges

1. The strongest headline comparison mixes denoising with a substantially stronger adversarial-training system, so causal attribution requires the within-system ablations.
2. The CAAD 2018 evaluation uses a secret ImageNet-like test set and unknown attackers, limiting independent reproduction despite its strong competition result.
3. Reproducing the release requires legacy frameworks and large distributed compute, while the paper reports no repeated-seed uncertainty or modern attack-suite evaluation.

## Attribution Block

- Source URL: https://arxiv.org/abs/1812.03411
  - Applies to: selection identity, metadata, revision history, DOI, and public paper links.
- Source URL: https://openaccess.thecvf.com/content_CVPR_2019/html/Xie_Feature_Denoising_for_Improving_Adversarial_Robustness_CVPR_2019_paper.html
  - Applies to: CVPR 2019 venue and pages 501-509.
- Source URL: https://github.com/facebookresearch/ImageNet-Adversarial-Training
  - Applies to: code, model, license, dependency, and archive-status notes.
- Source files: Withheld locally; none were uploaded.
