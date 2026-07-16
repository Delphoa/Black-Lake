# Arxiv DEP Job Log: PIArena Evaluation

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2604.08499v1, *PIArena: A Platform for Prompt Injection Evaluation*
- Selection result: accepted on the first uniform draw
- Source-integrity result: initial `partial`, repaired to verified `complete`
- Source-file policy: PDF, full-paper HTML, metadata HTML, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"`
- PDF count: 75,777
- Unique parent-paper units: 75,776
- Sampling method: PowerShell `Get-Random` over the complete sorted unique parent-unit list
- Zero-based selected index: 1,108
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, DOI, normalized title, slug, Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, automation-memory entry, or same-paper marker from the preceding 24 hours was found. A companion-repository search returned one metadata inventory row, not a substantive review or DEP artifact, so the first draw remained eligible.

## Source Integrity and Cache

- Existing PDF: 1,081,223 bytes; `%PDF-` header and trailing `%%EOF` present
- Initial full-paper HTML: missing
- Repair: official arXiv full-paper HTML and metadata HTML fetched once through bounded requests
- Verified HTML: 675,320 bytes, 86,861 body characters, 84 heading/section markers, six structure terms, and a document marker
- Metadata HTML: 42,741 bytes; abstract/metadata only
- Source archive: not collected
- Remaining partial files: 0
- Cache: 0.762-second missing-only backfill via `pypdf` and `html-regex`
- Cache outputs: PDF text 98,133 bytes; HTML text 101,304 bytes; source text absent

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md` - connects distributed tool-description injection, source-ingestion attack surfaces, and process-grounded agent evaluation.
2. `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` - connects prompt-inline and memory-channel compromise paths with trace observability and channel-specific detection limits.
3. `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` - connects PIArena's judge-based utility/ASR labels with interval uncertainty, calibration drift, and audit-oriented routing.

## Output Paths

- Job log: `.logs/20260716-Arxiv-PIArena-Evaluation-LOG.md`
- Phase log: `.logs/20260716-Arxiv-PIArena-Evaluation-PHASE-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-PIArena-Evaluation-20260716/Report-Mark.md`
- DEP README: `.lake-data/DEP-E/DEP-E-20260716-PIArena Evaluation/README.md`
- DEP manuscript: `.lake-data/DEP-E/DEP-E-20260716-PIArena Evaluation/piarena_evaluation_manuscript.md`
- Publication index: `.lake-data/DEP-E/.index/pubs-index.md`
- Dedup pointer: `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. How stable are PIArena's rankings when evaluator models, prompts, decision thresholds, and repeated-sampling procedures are changed or calibrated against human labels?
2. Which defenses retain both utility and low attack success under held-out adaptive strategies, unseen application domains, multilingual contexts, and end-to-end tool execution?
3. Can content-level provenance and corroboration controls address task-aligned disinformation without creating unacceptable latency, privacy leakage, or false rejection?

## Challenges

1. The benchmark mixes task-specific utility metrics with LLM-as-a-judge labels, so cross-dataset averages compress heterogeneous measurement error into one score.
2. Detection defenses suppress responses on flagged inputs, making utility under attack unavailable and complicating direct trade-off comparisons with prevention defenses.
3. The strategy attack is strong but depends on attacker-model, search-budget, and success-judge choices; the reported results do not establish universal worst-case robustness.

## Known Shortfalls

- Experiments, model APIs, datasets, and the official code were inspected but not executed or independently reproduced.
- Human validation is limited to a reported 100-sample judge audit with 98% accuracy; no full inter-rater or evaluator-uncertainty study is presented.
- The official repository is available under MIT, but dependency/runtime reproducibility and exact table regeneration were not tested.
- Venue status is reported by the arXiv comments and official repository as ACL 2026; this review did not inspect conference proceedings.

## Submission Record

- Primary artifact commit: pending
- Slack notification: pending
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source artifacts
- Submission status: validated and prepared for primary commit
