# 2026-07-19 - Arxiv CLOVER Test Benchmark

- Actor/tool: Codex scheduled `Black Lake Arxiv DEP 0900` workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260719-CLOVER Test Benchmark/`.
- Action: randomly select one unused local arXiv paper unit, enforce the complete-source gate, review it source-first, connect it to exactly three verified DEP entries, and prepare public-safe research artifacts.
- Paper: *CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verification*.
- arXiv ID: `2502.08806v1`.
- Canonical URLs: https://arxiv.org/abs/2502.08806 and https://doi.org/10.48550/arXiv.2502.08806.
- Run date: 2026-07-19.
- Result: complete research deposit prepared for direct submission.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, used-ID exclusion, then a uniform PowerShell `Get-Random` draw over eligible units.
- PDF candidates: 75,778.
- Unique PDF-parent units: 75,776.
- Used arXiv IDs observed across the dedup corpus: 810.
- Units excluded by used arXiv ID: 192.
- Identifier-incomplete units withheld from the draw: 185.
- Eligible units: 75,399.
- Selected zero-based eligible index: 33,124.
- Duplicate rejections/reselections: 0.
- Selected paper: `2502.08806v1`, *CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verification*.

## Deduplication and Recency Validation

- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and Black-Lake-Data `.lake-data` and `.reports` from fetched default-branch state.
- Matching keys: arXiv ID, arXiv DOI, exact title, normalized title, and `CLOVER-Test-Benchmark`-style slug variants.
- Exact ID/title/slug matches: 0.
- Public-safe 24-hour cutoff date: 2026-07-18.
- Same-paper or same-unit markers on or after the cutoff: 0.
- Acceptance decision: eligible; no duplicate or recency marker required reselection.

## Source Integrity

- Initial state: `partial`; the existing PDF was valid, but full-paper HTML was absent.
- Repair: preserved the valid PDF and made one bounded request per companion artifact for official full-paper HTML, arXiv metadata HTML, and the arXiv source package. Official arXiv full-paper HTML passed, so no fallback was needed.
- PDF verification: 827,506 bytes, `%PDF-` header present, trailing `%%EOF` present.
- Full-paper HTML verification: 526,611 bytes, 88,981 body characters, a full-document marker, 55 heading/section markers, and seven paper-structure terms.
- Metadata HTML: 42,490 bytes.
- Source package: downloaded, 330,636 bytes.
- Partial files after repair: 0.
- Final source state: `complete`.
- Local records updated: paper README, attribution/provenance note, machine-readable CSV summary, and JSON verification report.
- Source locality: PDF, HTML, metadata, source package, extracted content, and verification records remain in the private local archive. No source file is included in this repository deposit.

## Evidence Review

- Inspected: full PDF, official full-paper HTML, arXiv metadata HTML, TeX/source package, arXiv record, OpenReview DL4C @ ICLR 2025 record, author publication page, and exact GitHub/Hugging Face release searches.
- Visual PDF review: title/abstract, benchmark construction tables, model-result tables, limitations, safety, and legal-compliance pages were rendered and checked.
- Reproduction boundary: benchmark code and experiments were not run. No official CLOVER code or dataset repository was established from the inspected sources.

## Exactly Three Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md` - coverage signals as explicit optimization and evaluation objectives for generated tests.
2. `.lake-data/DEP-A/DEP-A-20260715-TACO Terminal Context/2604.19572-whitepaper-review.md` - context-budget management and verified terminal/software-engineering evaluation.
3. `.lake-data/DEP-A/DEP-A-20260716-ContextWeaver Selective a/2604.23069-whitepaper-review.md` - selective, dependency-aware preservation of long-horizon coding evidence.

## Public Outputs

- `.logs/20260719-Arxiv-CLOVER-Test-Benchmark-LOG.md`
- `.reports/BL-Arxiv-CLOVER-Test-Benchmark-20260719/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260719-CLOVER Test Benchmark/README.md`
- `.lake-data/DEP-E/DEP-E-20260719-CLOVER Test Benchmark/clover_test_benchmark_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Validation and Submission Controls

- Public-output policy: repository-relative paths and public URLs only; source documents withheld locally.
- Required validation: manuscript schema/headings, exact-three synthesis counts, title length/equality, DEP inventory, final attribution blocks, publication-index ownership, URL coverage, public-safe leak scan, staged allowlist, and zero source files.
- Submission policy: stage only the five generated/updated Markdown files listed above; reject PDFs, HTML, archives, caches, extracted source text, or other local source material.
- Blockers: none at drafting time.
