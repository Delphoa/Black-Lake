# 2026-07-18 - Arxiv DEP: Stable Diffusion Depth

- Actor/tool: Codex scheduled research workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/`.
- Action: Randomly selected, source-repaired, verified, reviewed, synthesized, and prepared a DEP-E research deposit for *Stealing Stable Diffusion Prior for Robust Monocular Depth Estimation*.
- Inputs: Verified complete arXiv PDF, official full-paper HTML, TeX/source, metadata, official project and repository records, and related DEP manuscripts. Original source documents were withheld locally.
- Outputs: `.reports/BL-Arxiv-Stable-Diffusion-Depth-20260718/Report-Mark.md`, `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/README.md`, `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md`, publication-index update, and public dedup-pointer update.
- Outcome: Ready for repository validation and submission.
- Blockers: None.

## Random Selection and Deduplication

- Candidate enumeration: `rg --files -g "*.pdf"` over the local archive.
- Candidate unit: Unique PDF parent directory.
- PDF candidates: 75,777.
- Candidate paper units: 75,776.
- Random method: PowerShell `Get-Random` selected one uniform zero-based index over all candidate units, followed by identity and dedup validation.
- Selected zero-based index: 45,232.
- Selected paper: *Stealing Stable Diffusion Prior for Robust Monocular Depth Estimation*.
- Selected arXiv ID: `2403.05056v1` (base ID `2403.05056`).
- Exclusions: 0.
- Duplicate rejections and reselections: 0.
- Dedup scan locations: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`; automation memory; Black-Lake-Data `.lake-data`, `.logs`, `.reports`, and `.staging`; and active worktree artifacts.
- Matching keys: arXiv ID, arXiv DOI `10.48550/arXiv.2403.05056`, normalized title, and `Stable-Diffusion-Depth` slug.
- Result: No substantive same-paper artifact or marker was found, including within the public-safe 24-hour cutoff date of 2026-07-17. Metadata-only author-inventory rows did not exclude the paper.

## Source Integrity Gate

- Initial state: Partial. A valid complete PDF was present, but full-paper HTML was missing.
- Repair: Preserved the existing PDF; made one bounded official arXiv pull for full-paper HTML, abstract metadata, PDF comparison, and TeX/source; verified the existing and downloaded PDF hashes were identical.
- PDF verification: 1,385,815 bytes; `%PDF-` header present; trailing `%%EOF` present.
- Full-paper HTML verification: 326,876 bytes; 61,973 body characters after script/style/tag removal; article and LaTeXML document markers; 45 heading/section markers; six paper-structure terms.
- Metadata HTML: 41,897 bytes and used only as metadata/provenance.
- Source package: 4,220,563 bytes with 30 valid archive entries.
- Partial files remaining: 0.
- Final state: Verified complete.
- Source locality: PDF, HTML, metadata, TeX/source, extracted text, caches, hashes, and archive records remained local. Review pages were rendered locally, inspected, and removed as reproducible intermediates. No `.source/` directory was created and no source file was uploaded, staged, committed, attached, or posted.

## Extraction Cache

- Initial cache status: Miss.
- Mode: `missing-only`.
- Final status: `cached`.
- PDF extractor: `pypdf`, 48,076 text bytes; `pdftotext` was unavailable.
- HTML extractor: `html-regex`, 63,736 text bytes.
- Source extractor: `tarfile`, 95,602 text bytes.
- Extraction elapsed: 0.826 seconds.

## Evidence and Related DEP Validation

- Full methods, equations, Tables 1-3, Figures 3-6, references, arXiv metadata/DOI, official project page, and official repository at commit `a5b11b77e33d3faf7d6f35d501f6fd27d0f65137` were inspected.
- The official repository contains a README, license, and four image assets, but no implementation, training configuration, dataset manifest, or weights; its announced December 2024 release is not present at the pinned revision.
- No publisher version or publisher DOI was identified in the inspected primary records.
- Exactly three related DEP entries were inspected and accepted:
  1. `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/uav_visual_localization_manuscript.md` - DINOv2-based robust cross-source visual matching and safety-aware localization evaluation.
  2. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - diffusion priors constrained by geometry and the need for independent spatial-consistency gates.
  3. `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md` - driving-scene depth/disparity, adverse-condition gaps, calibration, temporal failure, and deployment evidence.

## Submission Gate

- Allowed public scope: Generated Markdown under `.logs`, `.reports`, and `.lake-data`, the publication-index Markdown update, and the required public-safe dedup JSON.
- Forbidden source extensions and archive/cache content: None permitted.
- Required checks: manuscript headings/front matter/title, exact-three contracts, code syntax, publication-index and dedup uniqueness, final attribution blocks, URL coverage, public-safety scan, staged allowlist, and source-extension scan.

## Next-Review Questions

1. Does the released-or-future implementation resolve the teacher-mask inequality and multiplication-direction contradiction between Equation 5, Equation 6, and the surrounding prose?
2. How much of the reported robustness comes from DINOv2/DPT, from diffusion-translated training images, and from the two losses under a factorial repeated-seed ablation?
3. Do improvements persist under geographically independent day, night, rain, snow, glare, sensor, and calibration shifts when median scaling and fixed-depth truncation are removed?

## Challenges

1. Reproducing GDT requires a multi-model stack whose versions, prompts, seeds, filtering rules, and generated-image inventory are not released.
2. The public repository promises code and weights but currently exposes no executable implementation or environment, blocking direct verification.
3. The paper's teacher-mask equation appears directionally inconsistent with its stated intent, and no code is available to disambiguate it.
