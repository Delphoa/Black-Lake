# Arxiv DEP Job Log: CorrKD Missing Modality

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2404.16456v2, *Correlation-Decoupled Knowledge Distillation for Multimodal Sentiment Analysis with Incomplete Modalities*
- Selection result: accepted on the first uniform draw
- Source-integrity result: initial `partial`, repaired to verified `complete`
- Source-file policy: PDF, HTML, metadata, TeX/source, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"`
- PDF count: 75,777
- Unique parent-paper units: 75,776
- Sampling method: PowerShell `Get-Random` over the complete sorted unique parent-unit list
- Zero-based selected index: 52,075
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, DOI, normalized title, slug, Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, memory entry, companion-repository DEP, or recent active-worktree marker was found. Generic uses of the word “correlation” were unrelated.

## Source Integrity and Cache

- Existing PDF: 1,273,346 bytes, `%PDF-` header and trailing `%%EOF` present
- Initial full-paper HTML: missing
- Repair: official arXiv full-paper HTML, metadata HTML, and source archive succeeded on first bounded requests
- Verified HTML: 511,017 bytes, 79,155 body characters, 23 headings, five structure terms, and a document marker
- Source archive: 806,246 bytes, 13 entries
- Remaining partial files: 0
- Cache: 1.013-second missing-only backfill via `pypdf`, `html-regex`, and `tarfile`
- Cache outputs: PDF text 52,926 bytes; HTML text 75,382 bytes; source text 115,172 bytes

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md` - directly overlaps audiovisual emotion classification, IEMOCAP, fusion, missing/corrupt pathways, and consent boundaries.
2. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` - provides modality-fusion, dominance, representation, leakage, and intervention diagnostics.
3. `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` - supplies teacher/student distillation-system, versioning, parity, and reproducibility patterns.

## Output Paths

- Job log: `.logs/20260716-Arxiv-CorrKD-Missing-Modality-LOG.md`
- Phase log: `.logs/20260716-Arxiv-CorrKD-Missing-Modality-PHASE-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-CorrKD-Missing-Modality-20260716/Report-Mark.md`
- DEP README: `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/README.md`
- DEP manuscript: `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md`
- Publication index: `.lake-data/DEP-E/.index/pubs-index.md`
- Dedup pointer: `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Does CorrKD retain its advantage under naturally occurring, temporally structured, and not-missing-at-random failures rather than zero-masked simulation?
2. How much of the gain comes from teacher information versus additional objectives, batch/category structure, or hyperparameter budget?
3. Do improvements persist on speaker-, session-, language-, demographic-, and device-shifted evaluation with calibrated uncertainty?

## Challenges

1. The selected unit lacked full-paper HTML, requiring repair and integrity verification before review.
2. Three coupled distillation mechanisms make causal attribution and fair baseline matching difficult.
3. Source-reported F1 gains are small in several conditions and lack published uncertainty despite five-seed averaging.

## Known Shortfalls

- No experiment, dataset pipeline, teacher/student checkpoint, or baseline reimplementation was run.
- No official CorrKD code repository or raw seed-level results were identified.
- Missingness is synthetically imposed by zero replacement and whole-modality dropping; natural failure mechanisms were not evaluated.
- Privacy, demographic fairness, calibration, consent, and downstream decision risks are outside the paper's empirical scope.

## Submission Record

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/a829f8c9ed2b2c89d046b7b57794ec164555216a
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784202721825399
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source files
- Submission status: direct default-branch push succeeded; Slack notice delivered
