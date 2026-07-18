# 2026-07-18 - Arxiv DEP: SpOctA

- Actor/tool: Codex scheduled research workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260718-SpOctA Accelerator/`.
- Action: Randomly selected, source-verified, reviewed, synthesized, and prepared a DEP-E research deposit for *SpOctA: A 3D Sparse Convolution Accelerator with Octree-Encoding-Based Map Search and Inherent Sparsity-Aware Processing*.
- Inputs: Public arXiv, ar5iv, DOI, IEEE, author-publication, repository-authority, and related-DEP records. Original source documents were inspected from a local archive and withheld from publication.
- Outputs: `.reports/BL-Arxiv-SpOctA-20260718/Report-Mark.md`, `.lake-data/DEP-E/DEP-E-20260718-SpOctA Accelerator/README.md`, `.lake-data/DEP-E/DEP-E-20260718-SpOctA Accelerator/spocta_accelerator_manuscript.md`, publication-index update, and public dedup-pointer update.
- Outcome: Ready for repository validation and submission.
- Blockers: None. The official arXiv full-paper HTML endpoint was unavailable, so the approved ar5iv full-paper fallback was fetched and verified.

## Random Selection and Deduplication

- Candidate enumeration: `rg --files -g "*.pdf"` over the local archive.
- Candidate unit: Unique PDF parent directory.
- PDF candidates: 75,777.
- Candidate paper units: 75,776.
- Used arXiv IDs observed across the dedup sources: 757.
- Candidate units excluded by used arXiv ID: 185.
- Candidate units without a derivable arXiv ID: 185; withheld from the draw rather than guessed.
- Eligible units: 75,406.
- Random method: PowerShell `Get-Random` uniform zero-based index over eligible units after used-ID exclusion.
- Selected zero-based eligible index: 6,812.
- Selected paper: *SpOctA: A 3D Sparse Convolution Accelerator with Octree-Encoding-Based Map Search and Inherent Sparsity-Aware Processing*.
- Selected arXiv ID: `2308.09249v1` (base ID `2308.09249`).
- Duplicate rejections and reselections: 0.
- Selection note: An initial enumeration implementation reached its execution bound before producing a random index. The optimized rerun completed the same prescribed enumeration and made the single recorded draw above.
- Dedup scan locations: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`; automation memory; and Black-Lake-Data `.lake-data` and `.reports`.
- Matching keys checked after title resolution: arXiv ID, published DOI `10.1109/ICCAD57390.2023.10323728`, normalized title, and `SpOctA` slug.
- Exact same-paper matches in artifact or memory locations: 0.
- Public-safe 24-hour cutoff date: 2026-07-17. No same-paper artifact or marker was found inside the cutoff window.

## Source Integrity Gate

- Initial state: Partial. A full PDF was present, but full-paper HTML was absent.
- Repair: Preserved the valid PDF; fetched arXiv metadata HTML and TeX source; attempted official arXiv full-paper HTML once; then used the approved ar5iv fallback after the official endpoint was unavailable.
- PDF verification: 6,442,343 bytes; `%PDF-` header present; trailing `%%EOF` present.
- Full-paper HTML verification: 312,845 bytes; 53,023 body characters after script/style/tag removal; document marker present; 90 heading/section markers; six paper-structure terms.
- Metadata HTML: 42,555 bytes and used only as metadata/provenance.
- Source package: 2,792,455 bytes with 21 valid tar entries.
- Extraction cache: PDF, HTML, and source-text extraction all succeeded; cache status `cached`.
- Final state: Verified complete.
- Source locality: PDF, HTML, metadata, TeX/source, extracted text, caches, and verification records remained local. No source file was copied, staged, committed, attached, or posted.

## Evidence and Related DEP Validation

- Full paper sections, evaluation figures, comparison table, arXiv metadata, ICCAD publication record, published DOI locator, and author publication page were inspected.
- The work is a Verilog/40 nm synthesis and cycle-simulation evaluation, not evidence of fabricated silicon or independent reproduction.
- No official SpOctA code repository was established through the arXiv record, author page, or exact-title GitHub search.
- Exactly three related DEP entries were inspected and accepted:
  1. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - resource accounting, sparse execution, and operational-envelope discipline.
  2. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` - representation-substrate efficiency and the separation of digital results from hardware claims.
  3. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` - 3D point-cloud/autonomous-driving workload context and spatial-representation constraints.

## Submission Gate

- Allowed public scope: Generated Markdown under `.logs`, `.reports`, and `.lake-data`, plus the required public-safe dedup JSON.
- Forbidden source extensions and archive/cache content: None included.
- Public artifacts use only date-level run markers, public URLs, repository-relative paths, counts, and withheld-local-context notes.
- Required pre-commit checks: schema headings, title equality/length, exact-three section counts, code syntax, publication-index uniqueness, attribution finality, URL coverage, leak scan, staged allowlist, and source-extension scan.
