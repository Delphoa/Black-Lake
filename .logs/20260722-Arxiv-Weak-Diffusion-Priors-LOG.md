# 2026-07-22 - Arxiv Weak Diffusion Priors

- Actor/tool: Codex scheduled `Black Lake Arxiv DEP 0900` workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260722-Weak Diffusion Priors/`.
- Action: randomly select one unused local arXiv paper unit, enforce the complete-source gate, review it source-first, connect it to exactly three verified DEP entries, and prepare public-safe research artifacts.
- Paper: *Weak Diffusion Priors Can Still Achieve Strong Inverse-Problem Performance*.
- Authors: Jing Jia, Wei Yuan, Sifan Liu, Liyue Shen, and Guanyang Wang.
- arXiv ID: `2601.22443v2`.
- arXiv DOI: https://doi.org/10.48550/arXiv.2601.22443.
- Canonical source: https://arxiv.org/abs/2601.22443.
- Run date: 2026-07-22; exact execution timestamp withheld.
- Result: complete research deposit prepared for direct submission.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, identifier resolution, used-ID exclusion, then a uniform PowerShell `Get-Random` draw over eligible units.
- PDF candidates: 75,780.
- Unique PDF-parent units: 75,777.
- Used arXiv base IDs observed across the dedup corpus: 1,100.
- Units excluded by used arXiv ID: 265.
- Identifier-incomplete units withheld from the draw: 185.
- Eligible units: 75,327.
- Selected zero-based eligible index: 13,239.
- Duplicate rejections/reselections: 0.
- Selected paper: `2601.22443v2`, *Weak Diffusion Priors Can Still Achieve Strong Inverse-Problem Performance*.

## Deduplication and Recency Validation

- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and Black-Lake-Data `.lake-data`, `.reports`, and `.staging` from fetched default-branch state.
- Matching keys: arXiv base/version ID, arXiv DOI, canonical title, normalized title, and `Weak-Diffusion-Priors` slug variants.
- Exact ID/DOI/title/slug matches: 0.
- Public-safe 24-hour cutoff date: 2026-07-21.
- Same-paper or same-unit markers on or after the cutoff: 0.
- Acceptance decision: eligible; no duplicate or recency marker required reselection.

## Source Integrity

- Initial state: `partial`; the existing PDF was valid, but full-paper HTML was absent.
- Repair: preserved the valid PDF and used a fresh one-paper direct-HTTPS repair target with bounded requests, a 250 MiB total ceiling, a 100 MiB partial ceiling, and a 60-second request timeout. Official arXiv full-paper HTML passed, so no fallback was needed.
- PDF verification: 19,154,514 bytes, `%PDF-` header present, trailing `%%EOF` present. The repair PDF hash matched the existing PDF hash, so the existing file was retained.
- Full-paper HTML verification: 671,986 bytes, 115,796 body characters, a full-document marker, 125 heading/section markers, and seven paper-structure terms.
- Metadata HTML: 44,102 bytes; retained as metadata only.
- Source package: downloaded, 14,500,237 bytes, 31 archive entries.
- Partial files after repair: 0.
- Final source state: `complete`.
- Local records updated: paper README, attribution/provenance note, machine-readable CSV summary, and JSON verification report.
- Source locality: PDF, HTML, metadata, source package, rendered pages, repair records, and verification files remain in the private local archive. No source file is included in this repository deposit.

## Evidence Review

- Inspected: complete 37-page PDF, official full-paper HTML, arXiv metadata HTML, TeX/source package, canonical arXiv record, official project page, official code repository at commit `0f787b44274f07b9f7657cff9305a7608f69472a`, and three related DEP manuscripts.
- Visual review: pages containing the headline reconstruction trajectory, cross-domain tables, failure-mode plot and examples, noise and compute comparisons, and latent-diffusion examples were rendered and inspected.
- Technical scope: three-step DDIM initial-noise optimization, `ADAMSPHERE`, `HOLDOUTTOPK`, posterior concentration under a Gaussian-mixture surrogate, spatial-autocorrelation diagnostics, four restoration tasks, three natural-image domains, scientific inverse problems, noise sensitivity, and compute-matched comparisons.
- Reproduction boundary: code and experiments were not run. The repository was inspected for implementation evidence only, and no root license or tagged release was visible.
- Key limitation: the paper supports weak priors in measurement-informative regimes, not as a universal substitute for strong matched priors. Large box inpainting, 16x super-resolution, high measurement noise, scientific-domain mismatch, and higher INO cost remain explicit boundaries.

## Exactly Three Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md` - reuses a frozen diffusion prior for a downstream geometric task and exposes the same need to validate domain transfer, geometry preservation, and failure gates.
2. `.lake-data/DEP-E/DEP-E-20260720-WKGM MRI Reconstruction/wkgm_mri_reconstruction_manuscript.md` - combines a learned score prior with acquired-measurement consistency in a medical inverse problem, directly paralleling the paper's data-versus-prior balance.
3. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - makes measurement informativeness, identifiability, and conditioning explicit through controlled reference measurements, providing an analytic complement to prior-robust reconstruction.

## Public Outputs

- `.logs/20260722-Arxiv-Weak-Diffusion-Priors-LOG.md`
- `.reports/BL-Arxiv-Weak-Diffusion-Priors-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-Weak Diffusion Priors/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-Weak Diffusion Priors/weak_diffusion_priors_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Validation and Submission Controls

- Public-output policy: repository-relative paths and public URLs only; source documents withheld locally.
- Required validation: manuscript schema/headings, exactly three exercise paths, exact-three Report-Mark synthesis counts, title length/equality, DEP inventory, final attribution blocks, publication-index ownership, URL coverage, public-safe leak scan, staged allowlist, and zero source files.
- Submission policy: stage only the five generated or updated Markdown files listed above; reject PDFs, HTML, archives, caches, extracted source text, repair artifacts, or other local source material.
- Blockers: none at drafting time.
