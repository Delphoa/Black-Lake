# 2026-07-30 - Arxiv Epsilon Prox-Affine

- Actor/tool: Codex recurring research automation.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260730-Epsilon Prox Affine/`.
- Action: Random paper selection, global deduplication, local source-integrity repair, source-first review, related-DEP synthesis, manuscript/report generation, validation, and submission preparation.
- Paper: *Convex programming with fast proximal and linear operators*.
- Authors: Matt Wytock, Po-Wei Wang, and J. Zico Kolter.
- arXiv ID: `1511.04815v1`.
- DOI: https://doi.org/10.48550/arXiv.1511.04815
- Result: Eligible, source-complete after repair, reviewed, and prepared for DEP-E deposition.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumerated local PDF candidates; PDF paths were collapsed to unique parent-directory paper units; arXiv identifiers were resolved from directory and PDF filenames; globally used IDs and identifier-incomplete units were removed; PowerShell `Get-Random` selected one zero-based index uniformly from the eligible array.
- PDF candidates: `75,959`.
- Unique PDF-parent units: `75,956`.
- Used arXiv base IDs observed: `1,581`.
- Units excluded by used ID: `460`.
- Identifier-incomplete units withheld from the draw: `185`.
- Multiple-identifier units: `0`.
- Eligible units: `75,311`.
- Selected zero-based eligible index: `47,711`.
- Selected paper: arXiv `1511.04815`, *Convex programming with fast proximal and linear operators*.
- Duplicate rejections after the accepted draw: `0`.

## Deduplication and Reselection Validation

- Dedup scan locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; this automation's private memory; and the fetched `Delphoa-Labs/Black-Lake-Data` `.lake-data`, `.logs`, `.reports`, and `.staging` records.
- Match keys: arXiv base/version ID, arXiv DOI, canonical title, normalized title, archive token, and planned slugs.
- Exact acceptance check: no prior deposit or marker matched `1511.04815`, its DOI, canonical title, or planned Epsilon/prox-affine slugs.
- Public-safe 24-hour cutoff date: `2026-07-29`.
- Recent same-paper markers: none.
- Reselection was not required.

## Local Source Integrity

- Initial state: `partial`.
- Initial evidence: a valid full PDF and metadata README were present, but verified full-paper HTML was absent.
- Repair: review paused; the existing valid PDF was preserved; one bounded repair fetched metadata HTML, the approved ar5iv full-paper HTML fallback, and the arXiv source package. The official arXiv HTML endpoint was attempted before the fallback.
- PDF verification: `534,013` bytes, `%PDF-` header present, trailing `%%EOF` present, and the repair copy was SHA-256-identical to the preserved PDF.
- Full-paper HTML verification: `1,077,004` bytes, `88,927` stripped body characters, a LaTeXML document marker, `62` heading markers, and four paper-structure terms.
- Metadata HTML: `40,353` bytes.
- Source package: `231,386` bytes.
- Unexpected partial files: `0`.
- Final source state: `complete`.
- Local companion records updated: README, attribution record, machine-readable summary, and verification report.
- Source locality: PDF, HTML, metadata, TeX/source archive, extraction material, verification records, and renders were withheld locally.

## Review Evidence

- Inspected: complete PDF, full-paper HTML, TeX source, benchmark figures/table, canonical arXiv metadata, arXiv-issued DOI, author publication record, and the paper-linked software locators.
- Visual verification: the compiler/solver diagram, three benchmark-curve pages, and the consolidated result table were rendered and checked against extracted TeX evidence.
- Implementation status: the paper and author page link Epsilon software, but the paper-linked GitHub repository and project site were not currently accessible; code and experiments were not run.
- Main evidence boundary: results are source-reported 2015 comparisons against CVXPY+SCS and CVXPY+ECOS; hardware, seeds, repeated-run uncertainty, modern baselines, and independent reproduction were not established.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Sparse SSN PMM/sparse_ssn_pmm_manuscript.md` - connects prox-friendly structure to a semismooth Newton inner solver and explicit convergence certificates.
2. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - connects ADMM operator splitting, singular-value thresholding, and soft-thresholding to structured decomposition.
3. `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` - connects convex regularizer geometry and generalized Bregman updates to reusable optimization atoms.

## Generated Public Artifacts

- `.logs/20260730-Arxiv-Epsilon-Prox-Affine-LOG.md`
- `.reports/BL-Arxiv-Epsilon-Prox-Affine-20260730/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260730-Epsilon Prox Affine/README.md`
- `.lake-data/DEP-E/DEP-E-20260730-Epsilon Prox Affine/epsilon_prox_affine_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Verification

- Required manuscript headings, matching YAML/H1 title, evidence ledger, exactly three exercise paths, and MVP fields checked.
- Required Report-Mark headings, exactly three related DEP entries, exact-three Synthesis Note lists, and three Python mock-ups checked.
- DEP README inventory, summary, insights, public-safe context, and final Attribution Block checked.
- Public-output leak and source-file allowlist checks required before commit.
- No `.source/` directory was created.
- No source file was copied into the repository.

## Attribution Block

- Source URL: https://arxiv.org/abs/1511.04815
  - Applies to: selection identity, metadata, version, authors, abstract context, and source locators.
  - Notes: Abstract/metadata page only; not used as the full paper.
- Source URL: https://arxiv.org/pdf/1511.04815
  - Applies to: complete-paper review and visual verification.
  - Notes: Source file inspected locally and withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/1511.04815
  - Applies to: verified full-paper HTML review.
  - Notes: Approved full-paper fallback; local copy withheld.
- Source URL: https://arxiv.org/e-print/1511.04815
  - Applies to: TeX source cross-checks.
  - Notes: Source package inspected locally and withheld.
- Source URL: https://doi.org/10.48550/arXiv.1511.04815
  - Applies to: persistent paper identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://zicokolter.com/publications/
  - Applies to: author publication and Epsilon software-link context.
  - Notes: Author-maintained publication record.
- Source URL: https://github.com/mwytock/epsilon
  - Applies to: implementation-availability assessment.
  - Notes: Paper-linked repository locator; inaccessible during this review, so no code claims were derived from it.
