# Black Lake Arxiv DEP Log: CrossNER

- Public run date: 2026-08-01
- Black Lake Arxiv DEP selected and reviewed one arXiv archive paper: *CrossNER: Evaluating Cross-Domain Named Entity Recognition* (arXiv:2012.04373v2).
- Source provenance: public arXiv, ar5iv, and author-repository URLs are cited; the verified local PDF, full-paper HTML, metadata, repair records, and extracted material were withheld.
- Random selection: rg --files -g "*.pdf"; 75,960 PDF candidates; 75,957 unique parent-directory paper units; sorted units; uniform PowerShell Get-Random; accepted zero-based index 42,378. A first metadata helper failed before acceptance and was discarded; no manual substitution was used.
- Eligibility and deduplication: scanned Black Lake .logs, .reports, .lake-data, .staging, automation memory, and live Black Lake / Black-Lake-Data searches for arXiv ID, DOI, normalized title, and slug. Public 24-hour cutoff: 2026-07-31. Duplicate exclusions: 0. Reselections: 0.
- Source-integrity gate: initial unit was partial because full-paper HTML was missing. One bounded repair used official arXiv routes and the approved ar5iv fallback. PDF and full-paper HTML then passed verification; source package remained unavailable.
- Related DEP entries: DoubleTransfer MEDIQA; Dataset Baselines; OMGEval Benchmark.
- Report-Mark: .reports/BL-Arxiv-CrossNER-20260801/Report-Mark.md
- DEP-E deposit: .lake-data/DEP-E/DEP-E-20260801-CrossNER Adapt/README.md
- Manuscript: .lake-data/DEP-E/DEP-E-20260801-CrossNER Adapt/crossner_domain_adaptation_manuscript.md
- Publication index: .lake-data/DEP-E/.index/pubs-index.md
- Validation: public-output allowlist is Markdown-only; no PDF, HTML, source archive, cache, extracted source text, local path, or .source/ directory was staged or uploaded. Manuscript schema, exact-three synthesis counts, and attribution checks passed.

## Questions for the Next Reviewer

1. Does a modern encoder reproduce the reported advantage of task-focused or integrated DAPT under a pinned source/target split?
2. Which specialized-label confusion patterns persist after replacing DBpedia-based pre-annotation with an independently defined ontology?
3. Do the benchmark conclusions hold across additional languages and domains without changing the label semantics?

## Challenges for the Next Review Pass

1. Reconstruct a leakage-audited, version-pinned CrossNER evaluation with seeds, split hashes, and per-label confidence intervals.
2. Compare corpus relevance, corpus size, span masking, and source-domain pre-training through matched ablations.
3. Test an abstaining evaluation gate that reports when domain, ontology, or calibration conditions fall outside the verified envelope.
