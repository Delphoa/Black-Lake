# 2026-07-19 - Arxiv CAP Rank Sparsity

- Actor/tool: Codex scheduled `Black Lake Arxiv DEP 1100` workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/`.
- Action: randomly select one unused local arXiv paper unit, enforce the complete-source gate, review it source-first, connect it to exactly three verified DEP entries, and prepare public-safe research artifacts.
- Paper: *Large Language Model Compression with Global Rank and Sparsity Optimization*.
- arXiv ID: `2505.03801v3`.
- Canonical URLs: https://arxiv.org/abs/2505.03801 and https://doi.org/10.48550/arXiv.2505.03801.
- Run date: 2026-07-19.
- Result: complete research deposit prepared for direct submission.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumerated PDFs; unique PDF-parent directories were paper units; PowerShell `Get-Random` selected one uniform zero-based raw-unit index; identity and dedup gates then applied rejection sampling.
- PDF candidates: 75,778.
- Unique PDF-parent units: 75,776.
- Used arXiv IDs observed across Black Lake artifacts, automation memory, and relevant Black-Lake-Data records: 969.
- Units excluded by used arXiv ID: 213.
- Identifier-incomplete units withheld from eligibility counts: 185.
- Eligible units after corpus-level ID exclusion: 75,378.
- Selected zero-based raw-unit index: 18,321.
- Duplicate rejections/reselections: 0.
- Selected paper: `2505.03801v3`, *Large Language Model Compression with Global Rank and Sparsity Optimization*.

## Deduplication and Recency Validation

- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; this automation's memory; and current Black-Lake-Data `.lake-data` and `.reports` records.
- Matching keys: base/versioned arXiv ID, arXiv DOI, exact and normalized title, and `CAP-Rank-Sparsity`-style slug variants.
- Exact ID/title/slug matches representing prior research deposits: 0.
- Public-safe 24-hour cutoff date: 2026-07-18.
- Same-paper or same-unit markers on or after the cutoff: 0.
- Acceptance decision: eligible on the first random draw.

## Source Integrity

- Initial state: `partial`; the existing PDF passed validation, but full-paper HTML was absent.
- Repair: review remained paused while a one-paper, bounded official-arXiv companion-bundle repair fetched metadata HTML, full-paper HTML, and the TeX/source package. The valid archive-unit PDF was preserved unchanged. The repair used a 100 MB target ceiling, a 20 MB partial ceiling, one attempt per artifact, and no credentials or shared download cache.
- PDF verification: 1,957,758 bytes, `%PDF-` header present, trailing `%%EOF` present.
- Full-paper HTML verification: 507,233 bytes, 112,922 body characters, a full-document marker, 219 heading/section markers, and eight paper-structure terms.
- Metadata HTML: 44,536 bytes; metadata only.
- Source package: 1,397,382 bytes with 26 readable entries.
- Partial files after repair: 0.
- Final source state: `complete`.
- Local records updated: paper README, attribution/provenance note, machine-readable CSV summary, and JSON verification report.
- Source locality: PDF, HTML, metadata, TeX/source, rendered pages, caches, and verification records remain in the private local archive. No source file is included in this repository deposit.

## Evidence Review

- Inspected: complete PDF, official full-paper HTML, metadata HTML, TeX/source package, method equations, experiment tables, appendix ablations, limitations, ICLR 2026 poster record, OpenReview forum locator, author-maintained publication page, and exact code-release searches.
- Visual PDF review: Tables 1, 2, 4-6, Figure 2, Appendix Table 11, Figure 5, and the limitations page were rendered and checked.
- Principal reported results: at 50% sparsity, CAP reports 56.8% GSM8K versus Wanda's 45.6% on LLaMA-3.1-8B-Instruct; the dense model reports 84.5%. On one A100-80G throughput setup, CAP reports 176.5 tok/s versus 163.4 tok/s for Wanda.
- Reproduction boundary: no model compression run, benchmark, kernel profile, or statistical replication was performed. No official implementation repository was established from the inspected primary-source and exact release searches.

## Exactly Three Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - places low-rank decomposition and pruning in the broader resource-efficient foundation-model taxonomy.
2. `.lake-data/DEP-A/DEP-A-20260715-STAR-KV Ranks/2606.08382-whitepaper-review.md` - learns fine-grained rank profiles and connects nominal low-rank compression to custom-kernel runtime realization.
3. `.lake-data/DEP-A/DEP-A-20260717-QUOTA Joint Compression/2604.17320-whitepaper-review.md` - jointly allocates two compression mechanisms under sensitivity and budget constraints instead of composing fixed stages.

## Public Outputs

- `.logs/20260719-Arxiv-CAP-Rank-Sparsity-LOG.md`
- `.reports/BL-Arxiv-CAP-Rank-Sparsity-20260719/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/README.md`
- `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Does cost-weighted global selection of rank directions and sparse entries reproduce the paper's top-budget masks when the two candidate types have different storage costs?
2. How stable are learned allocation profiles across calibration corpora, model revisions, task mixtures, and random seeds?
3. Which sparse/low-rank kernel combinations preserve CAP's throughput advantage outside the reported A100-80G, batch-one, 1,024-token setting?

## Challenges

1. The initial archive unit was incomplete and required a source-gated repair before any research synthesis could begin.
2. The paper's cross-type final selection is not specified deeply enough to audit its claimed utility-to-cost comparability from prose alone.
3. The reproducibility statement names implementation files, but no official public repository was established for independent execution.

## Validation and Submission Controls

- Public-output policy: repository-relative paths and public URLs only; all source documents and derived source caches are withheld locally.
- Required validation: manuscript schema/headings/front matter/title, exact-three synthesis counts, Python mock-up syntax, publication-index ownership, final attribution blocks, URL coverage, public-safety leak scan, staged allowlist, and zero source files.
- Submission policy: stage only the five generated or updated Markdown files listed above; reject PDFs, HTML, archives, caches, extracted source text, rendered images, or other local source material.
- Blockers: none at drafting time.
