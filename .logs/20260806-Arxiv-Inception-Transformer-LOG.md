# Arxiv DEP Job Log

- Run date: 2026-08-06
- Selected paper: arXiv:2205.12956v2, *Inception Transformer*.
- Selection method: enumerate PDF files with `rg --files -g "*.pdf"` under the local arXiv archive, collapse PDF parents into paper units, then draw a uniform zero-based index with PowerShell `Get-Random`.
- Candidate census: 75,960 PDFs collapsed to 75,957 unique parent-paper units.
- Draw: index 74,770; first draw accepted after dedup validation; duplicate exclusions 0; reselections 0.
- Dedup validation: public dedup index, Black Lake logs/reports/DEP artifacts, automation memory, and relevant Black-Lake-Data entries were checked for the arXiv ID, DOI, normalized title, and slug. No prior research marker or same-paper marker within 24 hours was found.
- Source integrity: the selected unit initially had a valid PDF but no full-paper HTML. The bounded brokered archive repair preserved the PDF, obtained full-paper HTML through the approved ar5iv fallback after official arXiv HTML returned 404, refreshed the local README/provenance/summary/verification records, and passed the complete-paper gate. The TeX/source package was unavailable.
- Cache status: initial cache miss; `missing-only` extraction completed as `cached` with `pypdf` PDF text and `html-regex` HTML text. `pdftotext` was unavailable; no source text was created because no source package was available. Cache and extracted text remain local.
- Evidence reviewed: arXiv metadata, full-paper HTML/PDF-derived text, methods, tables, figures/captions, ablation, limitation, conclusion, official code README/model source/license, and three related DEP manuscripts. Experiments and code were not executed.

## Generated Outputs

- `.logs/20260806-Arxiv-Inception-Transformer-LOG.md`
- `.logs/20260806-Arxiv-Inception-Transformer-PHASE-LOG.md`
- `.reports/BL-Arxiv-Inception-Transformer-20260806/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260806-Inception Transformer/README.md`
- `.lake-data/DEP-E/DEP-E-20260806-Inception Transformer/inception_transformer_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

No PDF, HTML, metadata page, source package, cache, extracted text, repair receipt, or `.source/` directory is included in the public outputs. Public artifacts cite canonical URLs and state that source files were withheld locally.

## Exactly Three Next-Review Questions

1. Does the reported frequency complementarity persist under matched training recipes, repeated seeds, corruption tests, and resolution shifts?
2. How do iFormer’s warm/cold latency, peak memory, energy, and operator support compare with attention and Fourier alternatives on target devices?
3. Can the frequency-ramp ratios be learned or transferred across tasks without losing the compact accuracy/compute trade-off?

## Exactly Three Challenges

1. Reproduction requires ImageNet/COCO/ADE20K access, multi-GPU training, pinned legacy dependencies, and the authors’ checkpoint/configuration pairing.
2. The paper’s frequency interpretation is plausible and visualized, but the causal contribution of each branch is not fully isolated beyond the reported ablation.
3. Public deployment claims would need privacy, domain-shift, failure-case, and model-license review, especially for downstream recognition or surveillance use.

## Attribution Block

- Source URL: https://arxiv.org/abs/2205.12956
  - Applies to: this job log and all generated artifacts.
  - Notes: Public metadata and canonical paper locator; source files were withheld locally.
- Source URL: https://ar5iv.labs.arxiv.org/html/2205.12956
  - Applies to: source-first method, results, and limitation review.
  - Notes: Approved full-paper HTML fallback used because the official arXiv HTML endpoint returned 404.
- Source URL: https://github.com/sail-sg/iFormer
  - Applies to: implementation availability and reproduction notes.
  - Notes: Official repository inspected; no code or checkpoints were copied into Black Lake.
