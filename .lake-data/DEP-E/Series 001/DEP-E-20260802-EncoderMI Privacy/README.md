# DEP-E-20260802-EncoderMI Privacy

#membership-inference #contrastive-learning #encoder-privacy #security-evaluation #privacy

Public-safe context: this DEP records a source-grounded review of arXiv:2108.11023 after uniform local selection, deduplication, complete-source validation, and one bounded local archive repair. The source PDF, full-paper HTML, metadata HTML, source-package status, provenance records, and verification records remain private and are not deposited here. Exact local paths and execution times are intentionally omitted.

## Contents

- `README.md` - public-safe classification, inventory, source boundary, and attribution.
- `encodermi_privacy_manuscript.md` - schema-complete manuscript review of EncoderMI, its evidence, limitations, safe implementation paths, and related DEP context.

No `.source/` directory exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable research artifact is deposited.

## Summary of Items

### `README.md`

Defines the public deposition boundary and points future reviewers to the canonical arXiv and DOI records.

### `encodermi_privacy_manuscript.md`

Reconstructs the threat model, shadow-encoder pipeline, augmentation-similarity membership features, vector/set/threshold inference classifiers, CIFAR10/STL10/Tiny-ImageNet evaluation, CLIP audit caveat, early-stopping trade-off, limitations, and safe follow-on implementation ideas. It separates author-reported results from reviewer interpretation and records the random-selection and source-integrity gates.

## Insights and Relevance

EncoderMI makes a useful privacy boundary visible: a black-box encoder can expose membership-related signal through the stability of representations across augmented views, even when a single feature vector is not itself an overfitting indicator. The strongest downstream lesson is to treat membership auditing as a calibrated, consented, false-positive-controlled evaluation—not as proof that any individual image was used for training. The related DEP records connect this mechanism to memory membership attacks and to contrastive representation methods, giving future reviewers a bridge across privacy threat models, representation design, and evidence quality.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2108.11023
  - Applies to: this README and `encodermi_privacy_manuscript.md`.
  - Notes: public metadata and canonical paper identity.
- Canonical PDF: https://arxiv.org/pdf/2108.11023
  - Applies to: `encodermi_privacy_manuscript.md`.
  - Notes: the complete source PDF was verified locally and withheld from this repository.
- Full-paper HTML locator: https://arxiv.org/html/2108.11023
  - Applies to: `encodermi_privacy_manuscript.md`.
  - Notes: the complete paper rendering was verified locally through an approved fallback and withheld.
- Published paper DOI: https://doi.org/10.1145/3460120.3484749
  - Applies to: source metadata and publication attribution.
- Related DEP: `.lake-data/DEP-A/DEP-A-20260726-MRMMIA Memory Attack/2605.27825-whitepaper-review.md`
  - Notes: direct membership-inference and privacy-evaluation overlap.
- Related DEP: `.lake-data/DEP-E/DEP-E-20260722-4DContrast Contrastive/4dcontrast_contrastive_manuscript.md`
  - Notes: contrastive representation and augmentation/evaluation overlap.
- Related DEP: `.lake-data/DEP-E/DEP-E-20260721-Equivariant Contrastive/equivariant_contrastive_manuscript.md`
  - Notes: contrastive augmentation and representation-invariance overlap.
- Source boundary: all source files and local integrity records were withheld locally; zero source files were uploaded.
