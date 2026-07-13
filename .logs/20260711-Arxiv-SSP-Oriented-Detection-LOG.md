# 2026-07-11 - Arxiv SSP Oriented Detection Job Log

## Public-Safe Run Summary

- `Selected paper`: Semantic-decoupled Spatial Partition Guided Point-supervised Oriented Object Detection.
- `Stable identifier`: arXiv:2506.10601v2; publisher DOI 10.1016/j.patcog.2026.114079.
- `Selection method`: Enumerated PDFs with `rg --files -g "*.pdf"`, treated each PDF parent directory as one paper unit, and used PowerShell `Get-Random` for one uniform zero-based index.
- `Candidate count`: 75,438 PDFs and 75,438 paper units.
- `Selected index`: 29,914.
- `Duplicate exclusions`: 0.
- `Same-paper 24-hour exclusions`: 0.
- `Reselections`: 0.
- `Source-file deposition`: No source files collected; no `.source/` directory created.

## Dedup and Eligibility

The selected arXiv ID, DOI, normalized title, and slug were checked against `.staging/arxiv-dep-dedup-index.json`, Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and Black-Lake-Data code search. No earlier Arxiv DEP artifact or same-paper marker was found. The paper was accepted on the first draw.

## Cache and Source Review

Extractor preflight found neither `pdftotext` nor a supported Python PDF extraction backend. Initial cache lookup was a miss. Local missing-only extraction produced a metadata-only record in 0.11 seconds. After approved public arXiv access, missing-only backfill added HTML and TeX-source text in 3.92 seconds. Final cache status was `cached`; HTML and source extractors succeeded, while PDF text extraction remained unavailable.

Evidence inspected included the local archive README/PDF presence, arXiv metadata, extracted HTML and source text, the publisher DOI page, the official Apache-2.0 code repository at a pinned commit, the live Black Lake and Black-Lake-Data README files, and exactly three related DEP manuscripts. Author results were not reproduced.

## Output Paths

- `.logs/20260711-Arxiv-SSP-Oriented-Detection-LOG.md`
- `.logs/20260711-Arxiv-SSP-Oriented-Detection-PHASE-LOG.md`
- `.reports/BL-Arxiv-SSP-Oriented-Detection-20260711/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/README.md`
- `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` - explicit structural priors for reconstruction from sparse visual evidence.
2. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - geometry-aware representations for consistency beyond appearance alone.
3. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - explicit boundaries that constrain spatial exploration and invalid expansion.

## Next-Review Questions

1. Can SSP learn category compatibility and partition uncertainty without losing its low-resource simple-model advantage?
2. Which result values are authoritative for DOTA-v1.5, DOTA-v2.0, and 30% point offset, and can a table-to-config manifest resolve the prose discrepancies?
3. Do repeated-seed tests on bridge-like, low-contrast, overlapping, noisy, and low-resolution strata preserve the reported aggregate gains?

## Challenges

1. The environment had no working PDF text extractor, requiring public HTML/source backfill before full review.
2. Several paper prose values conflict with nearby tables, so exact claims required a discrepancy register rather than silent reconciliation.
3. Reproducibility remains unverified because code, datasets, pseudo-label archives, checkpoints, and experiments were inspected only at repository-documentation level.

## Outcome

The source-first review, schema-complete DEP manuscript, Report-Mark synthesis, public-safe logs, and dedup pointer were prepared as one atomic Black Lake artifact set. Repository submission and Slack notification are recorded in the completion report after validation.
