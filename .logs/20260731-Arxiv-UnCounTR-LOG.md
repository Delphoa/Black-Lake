# Black Lake Arxiv DEP — UnCounTR

- Public-safe run date: 2026-07-31.
- Selected and reviewed: arXiv:2307.08727, *Learning to Count without Annotations*.
- Source provenance: official arXiv metadata, PDF, and full-paper HTML; official implementation repository. Source files remain withheld locally.
- Random selection: rg --files -g "*.pdf" produced 75,960 PDF candidates and 75,957 unique paper units; uniform PowerShell Get-Random selected zero-based unit index 14,240.
- Eligibility: scanned Black Lake .logs, .reports, .lake-data, and .staging; automation memory; and Black-Lake-Data context for identifier and title. Duplicate exclusions: 0; reselections: 0; 24-hour cutoff date: 2026-07-30.
- Source integrity: initial state partial because full-paper HTML was absent. One brokered local repair preserved the valid PDF and produced verified metadata HTML plus full-paper HTML. PDF and HTML gates passed; source package was unavailable; no source file was uploaded.
- Related DEP entries selected:
  1. .lake-data/DEP-E/DEP-E-20260725-Improved Counting and/improved_counting_and_manuscript.md
  2. .lake-data/DEP-E/DEP-E-20260730-Self-supervised TransUNet/self_supervised_transunet_manuscript.md
  3. .lake-data/DEP-E/DEP-E-20260724-Visible-Thermal Tiny/visible_thermal_tiny_manuscript.md
- Outputs: .reports/BL-Arxiv-UnCounTR-20260731/Report-Mark.md; .lake-data/DEP-E/DEP-E-20260731-UnCounTR Counting/README.md; .lake-data/DEP-E/DEP-E-20260731-UnCounTR Counting/uncountr_counting_manuscript.md.
- Validation: manuscript schema, exact-three synthesis blocks, DEP inventory, publication index, public-safety scan, and no-source-upload allowlist are pending final pre-commit verification.

## Questions for the Next Reviewer

1. How much of UnCounTR's high-count error is attributable to the Self-Collage count range versus the frozen representation?
2. Does masked composition reduce real-world occlusion error compared with whole-image pasting under a controlled benchmark?
3. Which uncertainty signal is most useful for routing difficult count estimates to human review?

## Challenges for the Next Review Pass

1. Reproduce the reported FSC-147, MSO, and CARPK comparisons with frozen versions of data and dependencies.
2. Measure sensitivity to background assumptions, cluster quality, and object-scale distribution using controlled ablations.
3. Test calibration and abstention under occlusion, tiny objects, multimodal shift, and unseen count ranges.
