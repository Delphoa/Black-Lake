# 2026-07-20 - Arxiv CFE2 Search Explanation

- Actor/tool: Codex scheduled `Black Lake Arxiv DEP 0900` workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260720-CFE2 Search Explain/`.
- Action: randomly select one unused local arXiv paper unit, enforce the complete-source gate, review it source-first, connect it to exactly three verified DEP entries, and prepare public-safe research artifacts.
- Paper: *Counterfactual Editing for Search Result Explanation*.
- arXiv ID: `2301.10389v3`.
- Published DOI: https://doi.org/10.1145/3664190.3672508.
- Canonical arXiv URLs: https://arxiv.org/abs/2301.10389 and https://doi.org/10.48550/arXiv.2301.10389.
- Run date: 2026-07-20; exact execution timestamp withheld.
- Result: complete research deposit prepared for direct submission.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, used-ID exclusion, then a uniform PowerShell `Get-Random` draw over eligible units.
- PDF candidates: 75,778.
- Unique PDF-parent units: 75,776.
- Used arXiv base IDs observed across the dedup corpus: 999.
- Units excluded by used arXiv ID: 222.
- Identifier-incomplete units withheld from the draw: 185.
- Eligible units: 75,369.
- Selected zero-based eligible index: 64,032.
- Duplicate rejections/reselections: 0.
- Selected paper: `2301.10389v3`, *Counterfactual Editing for Search Result Explanation*.
- Indexing note: the initial parent-directory-only identifier pass yielded no draw because IDs are primarily carried by PDF filenames; the corrected candidate-unit pass used filenames plus parent directories before randomness was invoked.

## Deduplication and Recency Validation

- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and Black-Lake-Data `.logs`, `.reports`, `.lake-data`, and `.staging` from fetched default-branch state.
- Matching keys: arXiv ID, arXiv DOI, published DOI, exact title, normalized title, `CFE2`, and `CFE2-Search-Explanation`-style slug variants.
- Exact ID/DOI/title/slug matches: 0.
- Public-safe 24-hour cutoff date: 2026-07-19.
- Same-paper or same-unit markers on or after the cutoff: 0.
- Acceptance decision: eligible; no duplicate or recency marker required reselection.

## Source Integrity

- Initial state: `partial`; the existing PDF was valid, but full-paper HTML was absent.
- Repair: preserved the valid PDF and used a fresh one-paper repair staging target with one bounded request per companion artifact, a 250 MiB total ceiling, a 50 MiB partial ceiling, and a 180-second request timeout. Official arXiv full-paper HTML passed, so no fallback was needed.
- PDF verification: 1,014,492 bytes, `%PDF-` header present, trailing `%%EOF` present. The repair PDF hash matched the existing PDF hash, so the existing file was retained.
- Full-paper HTML verification: 551,159 bytes, 98,103 body characters, a full-document marker, 47 heading/section markers, and seven paper-structure terms.
- Metadata HTML: 42,975 bytes; retained as metadata only.
- Source package: downloaded, 1,434,369 bytes, 30 archive entries.
- Partial files after repair: 0.
- Final source state: `complete`.
- Local records updated: paper README, attribution/provenance note, machine-readable CSV summary, and JSON verification report.
- Source locality: PDF, HTML, metadata, source package, extracted visual material, repair staging, and verification records remain in the private local archive. No source file is included in this repository deposit.

## Evidence Review

- Inspected: complete PDF, official full-paper HTML, arXiv metadata HTML, TeX/source package, canonical arXiv record, ICTIR 2024 accepted-paper record, ACM publication DOI as exposed by the paper and author-maintained publication record, OpenReview venue record, and Utah NLP publication record.
- Visual review: the CFE2 overview, detailed editing loop, and beam-size ablation were inspected from the verified source package while remaining inside the private archive.
- Technical scope: formal pairwise rank-flip objective; CL-DRD search model; ColBERT-inspired masker; DistilBERT masked-language editor; beam search; five datasets; four baseline families; automatic metrics; MTurk evaluation; rank, beam, and editor ablations; qualitative successes and failures.
- Reproduction boundary: code and experiments were not run. No official CFE2 implementation repository was established from the bounded primary-source search.

## Exactly Three Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Beyond XAI/beyond_xai_manuscript.md` - tests the boundary between useful bounded explanations and claims of global faithfulness or causal understanding.
2. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - constructs targeted counterfactual evidence and highlights semantic-isolation, shortcut, and independent-verification risks.
3. `.lake-data/DEP-A/DEP-A-20260717-REAL Temporal Graph/2606.10694-whitepaper-review.md` - uses beam-searched retrieval plus counterfactual expansion and makes provenance separation for generated counterfactual state explicit.

## Public Outputs

- `.logs/20260720-Arxiv-CFE2-Search-Explanation-LOG.md`
- `.reports/BL-Arxiv-CFE2-Search-Explanation-20260720/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260720-CFE2 Search Explain/README.md`
- `.lake-data/DEP-E/DEP-E-20260720-CFE2 Search Explain/cfe2_search_explanation_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Validation and Submission Controls

- Public-output policy: repository-relative paths and public URLs only; source documents withheld locally.
- Required validation: manuscript schema/headings, exactly three exercise paths, exact-three Report-Mark synthesis counts, title length/equality, DEP inventory, final attribution blocks, publication-index ownership, URL coverage, public-safe leak scan, staged allowlist, and zero source files.
- Submission policy: stage only the five generated/updated Markdown files listed above; reject PDFs, HTML, archives, caches, extracted source text, repair artifacts, or other local source material.
- Blockers: none at drafting time.
