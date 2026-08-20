# Black Lake Arxiv DEP Log: ClapperText

- Run date: 2026-08-06 (public-safe date; exact execution time withheld).
- Selected paper: *ClapperText: A Benchmark for Text Recognition in Low-Resource Archival Documents*.
- Stable identifier: arXiv:2510.15557v1; DOI: https://doi.org/10.48550/arXiv.2510.15557.
- Authors: Tingyu Lin, Marco Peer, Florian Kleber, and Robert Sablatnig.

## Random Selection and Deduplication

- Method: `rg --files -g "*.pdf"` enumerated the local arXiv archive; each PDF parent directory was treated as one paper unit. A PowerShell `Get-Random` zero-based index was drawn uniformly from the frozen eligible parent-unit array.
- Inventory: 75,960 PDFs; 75,957 unique parent units; 75,772 units with normalized modern arXiv IDs; 185 identifier-incomplete units withheld.
- Deduplication: 1,534 normalized arXiv IDs were collected from Black Lake logs/reports/DEP artifacts and automation memory; 587 matching parent units were excluded, leaving 75,185 eligible units.
- Draw: eligible index 67,887 selected arXiv:2510.15557; duplicate exclusions after the draw: 0; reselections: 0; same-paper markers within the preceding 24 hours: 0.
- Exact-ID/title/slug validation found no existing ClapperText ownership in Black Lake, the related Black-Lake-Data repository, or automation memory. Remote repository searches for `2510.15557` and `ClapperText` returned no matches.

## Local Source Integrity Gate

- Initial classification: partial. The PDF was present and the full-paper HTML was missing; the `/abs/` page was treated as metadata only.
- Repair: one bounded request to the official arXiv full-paper HTML endpoint completed; the approved ar5iv fallback was not needed. The metadata page was also retained locally for provenance.
- Verification: PDF 4,076,658 bytes, valid `%PDF-` header and trailing `%%EOF`; full-paper HTML 175,381 bytes, 42,377 visible body characters, document marker present, 39 heading markers, and six paper-structure terms. No partial files remained.
- Local archive README, attribution/provenance record, machine-readable summary, and verification report were updated. The PDF, full-paper HTML, metadata HTML, and other source records remain local and were not uploaded.

## Evidence Review

- Primary evidence: verified local source pair plus public arXiv metadata and full-paper HTML.
- Supporting evidence: official `linty5/ClapperText` repository README and license; live Black Lake and Black-Lake-Data README rules; three existing related DEP manuscripts.
- Main findings: ClapperText contains 127 archival video segments, 9,813 annotated frames, 94,573 word instances, 67.4% handwritten instances, 1,566 partial occlusions, strict 18/8/101 video-level splits, polygon and semantic annotations, six recognition models, and seven detection models. Fine-tuning improves recognition and detection, but the source reports persistent handwriting, occlusion, noise, and domain-shift limits.
- No dataset/video files, model weights, source package, or executable artifacts were collected into the public DEP, and no experiment was rerun.

## Related DEP Entries

1. [`SSP Detection - DEP-E`](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md) — oriented polygons, spatial partitioning, and detection evaluation overlap with ClapperText’s rotated-box annotation and frame-level detection task.
2. [`VideoWeave - DEP-E`](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md) — temporal video variation and geometry-consistency evaluation provide a neighboring video-level reliability lens.
3. [`OMGEval Benchmark - DEP-E`](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md) — benchmark construction, culturally situated data, slice reporting, and judge/evaluation governance provide a complementary dataset-design lens.

## Generated Public Artifacts

- `.logs/20260806-Arxiv-ClapperText-LOG.md`
- `.reports/BL-Arxiv-ClapperText-20260806/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260806-ClapperText/README.md`
- `.lake-data/DEP-E/DEP-E-20260806-ClapperText/clappertext_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` (required publication-index row).

## Next-Review Questions

1. Does the public dataset release expose immutable video-level manifests, annotation provenance, and exact train/validation/test membership matching the paper?
2. How much of the reported gain survives repeated seeds, held-out archives, temporal subsampling, and cross-collection handwriting shifts?
3. Can temporal context improve partial-occlusion recovery without leaking near-duplicate frames across evaluation boundaries?

## Challenges

1. Reproduction requires licensed archival video, the exact MMOCR environment, pretrained weights, and paper-aligned configurations that were not collected or run here.
2. Benchmark scores can be inflated by temporal correlation, uneven word categories, or data leakage unless video-level splits and per-video aggregation remain enforced.
3. Public reuse must reconcile the dataset’s stated CC BY 4.0 terms, code MIT terms, and upstream HISTORIAN/source-video rights before redistribution or deployment.

## Submission Gate

- Public-output allowlist: generated Markdown log, Report-Mark, DEP README, and schema-complete manuscript only.
- No PDF, HTML, metadata page, source archive, cache, extracted text, local provenance record, or `.source/` directory was staged or uploaded.
- Final attribution uses public arXiv/DOI/repository URLs and explicitly states that source files were withheld locally.
