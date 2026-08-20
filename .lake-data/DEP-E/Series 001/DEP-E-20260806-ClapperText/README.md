# DEP-E-20260806-ClapperText

#clappertext #ocr #archival-video #document-analysis #benchmark

Public-safe research deposit for arXiv:2510.15557v1, *ClapperText: A Benchmark for Text Recognition in Low-Resource Archival Documents*. The source unit passed the mandatory complete PDF plus full-paper HTML gate after a bounded local repair. Original PDF, HTML, metadata, source package, cache, extracted text, and local provenance records remain local and are withheld from this public DEP; no `.source/` directory is present.

## Contents

- `README.md` — DEP inventory, public-safe context, summary, relevance, and attribution.
- `clappertext_manuscript.md` — schema-complete manuscript research artifact with source metadata, evidence ledger, methodology, claims, limitations, implementation paths, and replication boundaries.

## Summary of Items

The manuscript preserves the paper’s dataset design and reported benchmark evidence: 127 archival video segments, 9,813 annotated frames, 94,573 word-level instances, polygon and semantic labels, strict video-level splits, six recognition models, seven detection models, fine-tuning results, augmentation ablations, and detection throughput. It distinguishes author-reported metrics from reviewer interpretation and does not claim independent reproduction.

## Insights and Relevance

ClapperText is useful as a bridge between archival-data stewardship and robust OCR evaluation. Its video-level split discipline, geometry-aware labels, occlusion slices, per-video aggregation, and provenance requirements connect directly to Black Lake work on oriented detection, video geometry, and benchmark governance. The public-safe artifact therefore emphasizes measurement contracts, license review, temporal leakage controls, and bounded implementation paths rather than redistributing historical media or asserting deployment readiness.

## Attribution Block

- Source URL: https://arxiv.org/abs/2510.15557
  - Applies to: `README.md` and `clappertext_manuscript.md`.
  - Notes: Public paper identity, authors, date, abstract, and locator.
- Source URL: https://arxiv.org/html/2510.15557
  - Applies to: `clappertext_manuscript.md`.
  - Notes: Public full-paper evidence for method, dataset, evaluation, results, ablations, and conclusion.
- Source URL: https://arxiv.org/pdf/2510.15557
  - Applies to: `clappertext_manuscript.md`.
  - Notes: Public primary PDF; local copy was integrity-checked and withheld.
- Source URL: https://doi.org/10.48550/arXiv.2510.15557
  - Applies to: Stable paper identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://github.com/linty5/ClapperText
  - Applies to: Availability and license context.
  - Notes: Official repository README states CC BY 4.0 for dataset annotations/derived images and MIT for code; no repository contents were executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md
  - Applies to: Related research context in `clappertext_manuscript.md`.
  - Notes: Existing Black Lake processed artifact on oriented detection and spatial geometry.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: Related research context in `clappertext_manuscript.md`.
  - Notes: Existing Black Lake processed artifact on video and geometry consistency.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md
  - Applies to: Related research context in `clappertext_manuscript.md`.
  - Notes: Existing Black Lake processed artifact on benchmark construction and culturally situated evaluation.
- Source file: none.
  - Applies to: Public DEP.
  - Notes: Original source files were withheld locally; no PDF, HTML, metadata, source archive, cache, extracted text, or `.source/` file was uploaded.
