# Black Lake Arxiv DEP: AV Emotion Fusion

- Run date: 2026-07-13
- Actor/tool: Codex running the recurring `Black Lake Arxiv DEP` workflow.
- Action: Selected and reviewed one paper from a private arXiv archive, then prepared a log, Report-Mark, and DEP-E research deposit.
- Selected paper: **Emotion Recognition in Audio and Video Using Deep Neural Networks** by Mandeep Singh and Yuan Fang (arXiv:2006.08129v1).
- Public provenance: https://arxiv.org/abs/2006.08129, https://arxiv.org/html/2006.08129, and https://github.com/julieeF/CS231N-Project. A private archive PDF was inspected but is not redistributed.
- Random method: `rg --files -g "*.pdf"`, parent-directory paper units, then a uniform `Get-Random` index. PDF candidates: 75,761; unique paper units: 75,761; zero-based selected index: 19,382.
- Eligibility: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data were searched for the arXiv ID, exact title, and normalized topic. Exclusions: 0; reselections: 0; same-paper 24-hour marker: none; cutoff date: 2026-07-12.
- Related DEP entries: `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`; `.lake-data/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`; `.lake-data/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`.
- Report-Mark: `.reports/BL-Arxiv-AV-Emotion-Fusion-20260713/Report-Mark.md`.
- DEP: `.lake-data/DEP-E-20260713-AV Emotion Fusion`.
- Validation: the complete nine-page paper text, public arXiv full text, result table, limitations, and paper-declared code repository were inspected. Private extraction used `pypdf`; local HTML and source-package inputs were unavailable. Manuscript-schema, exact-count, code-syntax, inventory, staged-scope, and public-safety gates passed before submission. SciPy is declared but was not installed, so one mock-up's external import was not resolved.

## Questions for the Next Reviewer

1. Does the 1.50-point three-class gain from audio-video fusion persist across speaker-independent folds and repeated seeds?
2. How much of the happiness failure comes from label ambiguity, limited unique examples, side-view faces, or the oversampling procedure?
3. Which representation probes and calibration intervals best reveal when one modality is uninformative or contradictory?

## Challenges for the Next Review Pass

1. Reproduce all four-class and three-class comparisons with speaker-disjoint splits, confidence intervals, and per-class metrics.
2. Replace static face cropping with tracked regions while testing missing, delayed, and conflicting modalities.
3. Add an abstention policy whose release threshold is supported by held-out calibration data and shift monitoring.
