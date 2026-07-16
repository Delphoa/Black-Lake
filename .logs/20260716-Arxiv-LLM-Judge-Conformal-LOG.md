# Arxiv DEP Job Log: LLM Judge Conformal

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2509.18658v1, *Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction*
- Selection result: accepted on the first uniform draw
- Source-integrity result: initial `partial`, repaired to verified `complete`
- Source-file policy: all PDF, HTML, metadata, TeX/source, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"`
- PDF count: 75,777
- Unique parent-paper units: 75,776
- Sampling method: PowerShell `Get-Random` over the complete sorted unique parent-unit list
- Zero-based selected index: 29,719
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, normalized title, slug, DOI, prior Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, automation-memory entry, or recent active-worktree marker was found. One author-inventory row was metadata only and did not count as a research deposit. Black-Lake-Data search returned no matching DEP artifact.

## Source Integrity and Cache

- Existing PDF: 3,119,581 bytes, `%PDF-` header present, trailing `%%EOF` present
- Initial full-paper HTML: missing
- Repair: official arXiv HTML, metadata HTML, and TeX/source archive succeeded on their first bounded requests
- Verified HTML: 890,619 bytes, 193,341 body characters, 115 heading markers, eight structure terms, and a document marker
- Source archive: 2,383,959 bytes, 25 listed entries
- Remaining partial files: 0
- Extractors: `pypdf`, `html-regex`, `tarfile`
- Cache outputs: PDF text 136,698 bytes; HTML text 160,453 bytes; source text 342,736 bytes

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` - separates faithful uncertainty expression from factual correctness and exposes proxy/judge dependence.
2. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` - provides finite-sample interval and distribution-shift boundaries for confidence-based decisions.
3. `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` - connects model confidence to reasoning-resource control and highlights evaluator dependence.

## Output Paths

- Job log: `.logs/20260716-Arxiv-LLM-Judge-Conformal-LOG.md`
- Phase log: `.logs/20260716-Arxiv-LLM-Judge-Conformal-PHASE-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-LLM-Judge-Conformal-20260716/Report-Mark.md`
- DEP README: `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/README.md`
- DEP manuscript: `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md`
- Publication index: `.lake-data/DEP-E/.index/pubs-index.md`
- Dedup pointer: `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. How stable are the reported intervals under judge-model updates, prompt changes, and natural distribution shift?
2. Can calibration data be selected without leaking evaluation labels or reinforcing annotator bias?
3. Which interval policy best combines coverage, width, abstention load, and downstream decision cost?

## Challenges

1. The selected unit lacked full-paper HTML, so synthesis paused for a bounded archive repair and independent integrity verification.
2. The empirical grid spans many datasets, judges, frameworks, and conformal methods, requiring careful separation of coverage from interval efficiency.
3. The statistical guarantee depends on exchangeability, while real deployments may change prompts, models, populations, and annotation practices.

## Known Shortfalls

- The authors' experiments, notebooks, API calls, and GPU evaluations were not rerun.
- The proof of non-decreasing coverage was inspected but not independently formalized.
- The official repository has no visible license and its data lineage was not exhaustively audited.
- Long-term coverage under production drift remains unestablished.

## Submission Record

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/72f56304bb93f4906fe75e5fa59ddc73ec34c09e
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784199878245929
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source files
- Submission status: direct default-branch push succeeded; Slack notice delivered
