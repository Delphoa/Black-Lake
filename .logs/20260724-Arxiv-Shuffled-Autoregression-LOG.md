# Arxiv DEP Log: Shuffled Autoregression

- Date: 2026-07-24
- Actor: Codex
- Action: Randomly select one eligible locally archived arXiv paper, verify and repair its complete source state, create a source-grounded review, and deposit a DEP-E research package.
- Selected paper: *Shuffled Autoregression For Motion Interpolation*
- Canonical record: [arXiv:2306.06367v1](https://arxiv.org/abs/2306.06367v1)
- Result: Complete; the public repository submission contains generated Markdown only.
- Affected DEP: `.lake-data/DEP-E/DEP-E-20260724-Shuffled Autoregress/`
- Blockers: None.

## Random Selection and Deduplication

- Candidate discovery used `rg --files -g "*.pdf"` over the private archive, with each PDF parent directory treated as one paper unit.
- The enumeration produced 75,780 PDFs in 75,777 candidate units.
- A used-paper index was assembled from Delphoa/Black-Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and the corresponding surfaces in Delphoa-Labs/Black-Lake-Data. Matching arXiv IDs, DOI values, normalized titles, and slugs were treated as duplicates.
- The index contained 1,204 used arXiv base identifiers. It excluded 297 candidate units as already used; another 185 units were withheld because a canonical identifier could not be established reliably.
- The remaining eligible pool contained 75,295 units. PowerShell `Get-Random` selected uniform zero-based eligible index 30,096.
- The accepted identifier was arXiv:2306.06367, *Shuffled Autoregression For Motion Interpolation*.
- Duplicate rejections and reselections: 0.
- The 24-hour marker cutoff was 2026-07-23. The accepted paper had no matching recent marker.
- A final exact-match check covered arXiv ID `2306.06367`, arXiv DOI `10.48550/arXiv.2306.06367`, IEEE DOI `10.1109/ICASSP49357.2023.10095312`, canonical title, normalized title, archive-unit token, and public slug. No prior Black Lake Arxiv DEP artifact was found.

## Source Integrity Gate

- Initial state: partial. A valid full PDF was present, but verified full-paper HTML was absent.
- Repair: the valid PDF was preserved. A bounded one-paper acquisition collected the canonical metadata page, full-paper HTML through the approved ar5iv fallback, and the arXiv TeX/source package. One strategy owned the repair, retries were bounded, and no partial bytes were counted as progress.
- Final PDF verification: 2,310,025 bytes; `%PDF-` header present; trailing `%%EOF` present; five pages; unencrypted.
- Final full-paper HTML verification: 189,178 bytes; 30,036 script/style-stripped body characters; a full-document marker; 43 heading markers; and six paper-structure terms.
- Supporting verification: metadata HTML 41,910 bytes; source package 2,641,656 bytes; seven author-profile links; zero partial files.
- Final classification: complete and verified.
- Source-file policy: all PDF, HTML, source-package, metadata, render, cache, provenance, and verification materials were withheld in the private archive. No source file was copied into, staged for, or uploaded to the public repository.

## Public Artifacts

- `.logs/20260724-Arxiv-Shuffled-Autoregression-LOG.md`
- `.reports/BL-Arxiv-Shuffled-Autoregression-20260724/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260724-Shuffled Autoregress/README.md`
- `.lake-data/DEP-E/DEP-E-20260724-Shuffled Autoregress/shuffled_autoregression_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` publication-index update

## Related DEP Basis

1. `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` — autoregressive motion generation, exposure-bias control, and long-horizon error propagation.
2. `.lake-data/DEP-A/DEP-A-20260715-Structured Thoughts/2607.10386-whitepaper-review.md` — custom attention masks that encode a nonstandard visibility graph and must match inference-time state transitions.
3. `.lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md` — human-motion generation, temporal coherence, interaction constraints, and domain-specific evaluation.

## Public Sources

- [Canonical arXiv record](https://arxiv.org/abs/2306.06367v1)
- [Full-paper ar5iv HTML fallback](https://ar5iv.labs.arxiv.org/html/2306.06367)
- [arXiv PDF](https://arxiv.org/pdf/2306.06367)
- [arXiv DOI](https://doi.org/10.48550/arXiv.2306.06367)
- [IEEE DOI](https://doi.org/10.1109/ICASSP49357.2023.10095312)
- [ICASSP 2023 program](https://icassp23-static-program.pages.dev/)
- [Author-group publication page](https://hcsi.cs.tsinghua.edu.cn/)
