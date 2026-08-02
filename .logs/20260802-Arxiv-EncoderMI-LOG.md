# Arxiv DEP Log: EncoderMI

## Selection and Source Gate

- Selected paper: *EncoderMI: Membership Inference against Pre-trained Encoders in Contrastive Learning*.
- Stable identity: arXiv:2108.11023; DOI:10.1145/3460120.3484749.
- Selection method: enumerate `rg --files -g "*.pdf"` under the local arXiv archive, reduce to sorted unique PDF-parent paper units, and draw one uniform zero-based index with PowerShell `Get-Random`.
- Candidate counts: 75,960 PDFs; 75,957 unique parent units.
- Draw: zero-based index 15,397; first draw accepted.
- Initial source state: partial. The PDF passed the size, `%PDF-`, and trailing `%%EOF` checks, but metadata HTML and full-paper HTML were absent.
- Repair: one bounded single-paper repair through the pinned v4 broker preserved the valid PDF and added metadata HTML plus a verified full-paper HTML fallback.
- Final source state: complete. PDF 858,195 bytes; full-paper HTML 653,784 bytes; metadata HTML 44,475 bytes; 56 heading markers; 118,365 extracted body characters; eight paper-structure term classes; zero partial files.
- Source package: unavailable through the broker redirect policy; not required for the PDF-plus-full-paper-HTML gate.
- Source boundary: PDF, HTML, metadata, provenance, verification records, and any extracted source material remain in the private local archive.

## Deduplication and Reselection

- Scanned prior `.logs`, `.reports`, `.lake-data`, this automation memory, and relevant Black-Lake-Data inventory results for arXiv ID, DOI, normalized title, and slug.
- Exclusion count: zero prior Arxiv DEP artifacts, zero same-paper-within-24-hours markers, zero matching DOI/title/slug artifacts, and zero other exclusions.
- The repository search returned only a metadata-only `.lists` author inventory row; it is not a processed DEP and did not exclude the paper.
- Reselections: zero.

## Generated Public Outputs

- `.logs/20260802-Arxiv-EncoderMI-LOG.md`
- `.reports/BL-Arxiv-EncoderMI-20260802/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260802-EncoderMI Privacy/README.md`
- `.lake-data/DEP-E/DEP-E-20260802-EncoderMI Privacy/encodermi_privacy_manuscript.md`

No public `.source/` directory is created.

## Next-Review Questions

1. Can a consented, ground-truth membership benchmark separate true membership inference from near-duplicate, source-distribution, or image-search artifacts?
2. What privacy-utility frontier results when early stopping, DP-SGD, augmentation changes, and feature-release controls are compared under matched downstream utility?
3. How do query budgets, adaptive probing, calibration, and model-version drift change the false-positive operating point of EncoderMI?

## Challenges

1. Reproduce the shadow-encoder and eight-background-knowledge grid without silently changing datasets, augmentations, model architecture, or split semantics.
2. Build a defensible CLIP-style audit set with verified members, verified non-members, consent provenance, and duplicate control.
3. Turn a research signal into a safe audit workflow that cannot be mistaken for formal proof of training-data membership.

## Submission Boundary

Only generated public-safe Markdown artifacts under `.logs`, `.reports`, and `.lake-data` are eligible for submission. No PDF, HTML, metadata page, source archive, cache, extracted source text, local archive path, or other source file is staged, committed, uploaded, or attached.

## Attribution Block

- Primary arXiv record: https://arxiv.org/abs/2108.11023
  - Applies to: selection, source identity, and all generated artifacts.
- Primary PDF locator: https://arxiv.org/pdf/2108.11023
  - Applies to: source-integrity and paper review claims; the verified source file was withheld locally.
- Full-paper HTML locator: https://arxiv.org/html/2108.11023
  - Applies to: full-text review claims; the verified fallback rendering was withheld locally.
- Published paper DOI: https://doi.org/10.1145/3460120.3484749
  - Applies to: publication metadata and venue attribution.
- Source files were withheld locally and no source files were uploaded.
