# Black Lake Arxiv DEP: OMGEval

- Public run date: 2026-07-17
- Action: `Black Lake Arxiv DEP` selected and reviewed one paper from the local arXiv archive.
- Selected paper: *OMGEval: An Open Multilingual Generative Evaluation Benchmark for Large Language Models* (`arXiv:2402.13524v2`; arXiv-issued DOI `10.48550/arXiv.2402.13524`).
- Sanitized provenance: a verified local paper unit plus public arXiv and official GitHub records; source files remain local and were not uploaded.
- Random method: `rg --files -g "*.pdf"` found 75,777 PDF candidates, collapsed to 75,776 unique parent-directory paper units, followed by uniform PowerShell `Get-Random`; selected zero-based index 39,883.
- Eligibility: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data were scanned for the arXiv ID, DOI, exact title, and slug. Exclusions: 0; reselections: 0. The public-safe 24-hour cutoff date marker was 2026-07-16.
- Source integrity: initially partial because full-paper HTML was absent. The valid PDF was preserved; official full-paper HTML, metadata HTML, and the arXiv source package were repaired locally. PDF, full-paper HTML, extraction-cache, companion-record, and no-partial-file gates passed.
- Related DEP entries: `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`.
- Report-Mark: `.reports/BL-Arxiv-OMGEval-20260717/Report-Mark.md`.
- DEP-E: `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark`.
- Manuscript: `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md`.
- Validation: source claims and reviewer inferences are separated; exact-three synthesis counts and manuscript schema are checked; staged files must pass the public-output allowlist and leak scan before submission.

## Questions for the Next Reviewer

1. Does judge-human agreement remain stable for every OMGEval language, capability slice, model family, and localized subset rather than only the reported Chinese and Spanish comparison?
2. Can culturally localized questions be paired with measurement-invariance tests that distinguish language competence from cultural familiarity and annotation preference?
3. How do model rankings change under multiple independently calibrated judges, randomized answer order, and a baseline other than GPT-3.5-Turbo?

## Challenges for the Next Review Pass

1. Reproduce the full and localized win-rate tables with fixed model snapshots, blinded answer-order randomization, repeated judge samples, and confidence intervals.
2. Build per-language and per-capability support cards that expose sample counts, human agreement, judge disagreement, and localization provenance.
3. Stress-test benchmark leakage and feedback-loop contamination by separating immutable test items from an audited development set used for on-policy improvement.
