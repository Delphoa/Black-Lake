# Black Lake Arxiv DEP Log: HSRNet Aliasing

- `Run`: Black Lake Arxiv DEP 1500
- `Selected paper`: *Hierarchical Similarity Learning for Aliasing Suppression Image Super-Resolution*
- `Identity`: arXiv:2206.03361v1
- `Selection method`: `rg --files -g "*.pdf"` enumeration, parent-directory paper units, immutable private candidate index, and uniform cryptographic selection from the locked eligible set.
- `Candidate accounting`: 75,967 PDF paths; 67,990 unique canonical paper identities; 66,372 eligible; 1,618 excluded with overlapping permanent-dedup and marker reasons.
- `Reservation`: One paper reserved under the shared `black-lake-arxiv-dep-v1` family; no reselection was required after reservation.
- `Source integrity`: Initial unit was partial because full-paper HTML was absent. A bounded local archive repair fetched the official full-paper route, refreshed provenance and verification records, and produced a complete paper unit. PDF and full-paper HTML passed the required validation gate; TeX/source package was unavailable.
- `Review basis`: Verified local PDF and full-paper HTML, official arXiv metadata, IEEE publication metadata, and exactly three related DEP manuscripts. No source file was uploaded or copied to the public repository.
- `Cache result`: Paper-specific cache was treated as a miss/backfill. `missing-only` extraction completed with `pypdf` for PDF text and HTML-regex for full-paper HTML; final status was `cached`. No network was used during extraction.

## Output Paths

- `.logs/20260822-Arxiv-HSRNet-Aliasing-LOG.md`
- `.logs/20260822-Arxiv-HSRNet-Aliasing-PHASE-LOG.md`
- `.reports/BL-Arxiv-HSRNet-Aliasing-20260822/Report-Mark.md`
- `.lake-data/DEP-E/Series 002/DEP-E-20260822-HSRNet Aliasing/README.md`
- `.lake-data/DEP-E/Series 002/DEP-E-20260822-HSRNet Aliasing/hsrnet_aliasing_manuscript.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/Series 002/DEP-E-20260819-LFMamba Light Field Image/lfmamba_light_field_image_manuscript.md` - direct super-resolution and multi-scale restoration overlap.
2. `.lake-data/DEP-E/Series 001/DEP-E-20260720-WKGM MRI Reconstruction/wkgm_mri_reconstruction_manuscript.md` - iterative inverse reconstruction and learned data-consistency overlap.
3. `.lake-data/DEP-E/Series 001/DEP-E-20260819-EnsIR An Ensemble/ensir_an_ensemble_manuscript.md` - image-restoration ensemble and uncertainty overlap.

## Next-Review Questions

1. Does HEB or MSA provide the dominant gain when parameter count, training schedule, and degradation are held constant?
2. How does the solver/denoiser structure behave under real sensor noise, blur, compression, and motion rather than bicubic degradation?
3. Can the reported quality-efficiency tradeoff be reproduced with public code, fixed seeds, hardware traces, and a resolved source-table discrepancy?

## Challenges

1. Reproducing the paper's exact pipeline without an identified official implementation or source package.
2. Separating genuine aliasing suppression from dataset, degradation, or baseline effects.
3. Measuring real deployment latency, memory, and failure behavior without overstating benchmark evidence.

## Attribution Block

- Primary source: https://arxiv.org/abs/2206.03361
- Full-paper source: https://arxiv.org/html/2206.03361
- PDF source: https://arxiv.org/pdf/2206.03361
- Publication DOI: https://doi.org/10.1109/TNNLS.2022.3191674
- Source files were withheld locally and were not uploaded to Black Lake or Slack.
