# Arxiv DEP Job Log: DMNN Conditional Paths

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:1902.10949v3, *Dynamic Multi-path Neural Network*
- Selection: first uniform draw; zero exclusions and reselections
- Source integrity: initial `partial`, repaired to verified `complete`
- Cache: initial miss; final `cached`
- Source policy: paper files, metadata, cache, and extracted text remain local; none are deposited

## Random Selection

- Enumeration: `rg --files -g "*.pdf"`
- PDFs / parent units: 75,777 / 75,776
- Sampling: PowerShell `Get-Random` over sorted unique paper units
- Zero-based index: 61,074
- Exclusions / reselections: 0 / 0

## Dedup Validation

No prior matching arXiv ID, DOI, normalized title, slug, job log, report, DEP-E manuscript, dedup pointer, automation-memory entry, companion-repository entry, or 24-hour same-paper marker was found. The first draw was eligible.

## Source Integrity and Cache

- PDF: 2,535,345 bytes; `%PDF-` header and trailing `%%EOF` valid
- Repair: official arXiv HTML was unavailable; approved ar5iv full-paper HTML and arXiv metadata HTML were fetched with bounded retries
- Full HTML: 404,027 bytes; 47,624 body characters; two document markers; 27 heading/section markers; five paper-structure terms
- Metadata: 42,940 bytes; metadata only; partial files: 0; source package: not collected
- Cache: miss to `cached` in 0.864 seconds using `pypdf` / `html-regex`
- PDF / HTML / source text: 40,803 / 47,308 / 0 bytes

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - separates parameter/FLOP claims from latency, memory, energy, and target-device evidence in efficient vision models.
2. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` - supplies compact-vision latency, memory, model-size, and deployment-failure evidence absent from DMNN.
3. `.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity/smes_expert_sparsity_manuscript.md` - connects conditional routing and active-compute sparsity to load balance, grouped execution, temporary memory, and observed latency.

## Output Paths

- `.logs/20260716-Arxiv-DMNN-Conditional-Paths-LOG.md`
- `.logs/20260716-Arxiv-DMNN-Conditional-Paths-PHASE-LOG.md`
- `.reports/BL-Arxiv-DMNN-Conditional-Paths-20260716/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/README.md`
- `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Do the reported FLOP savings survive compilation as lower p50/p95 latency, peak memory, energy, and cost on GPU, mobile NPU, and CPU targets?
2. How stable are the learned path decisions across random seeds, corruptions, distribution shift, batch sizes, and classes outside the training hierarchy?
3. Which controller features, hierarchy labels, execution-rate targets, and sub-block granularities produce the best accuracy-resource frontier under matched training budgets?

## Challenges

1. FLOPs are a proxy: dynamic branching can reduce arithmetic while worsening kernel occupancy, batching, memory traffic, and tail latency.
2. Category-supervised routing uses class hierarchy during training, so transfer to unseen taxonomies or unlabeled domains is unresolved.
3. Comparisons rely partly on the authors' stronger ResNet reimplementations and report no repeated-seed uncertainty or independently runnable code.

## Known Shortfalls

- No model was reproduced, compiled, or benchmarked; no official implementation was identified in the inspected paper, arXiv record, or focused GitHub search.
- Device latency, energy, memory, calibration, routing stability, and failure traces remain unmeasured.
- The public deposit contains review text and derived status JSON only; source documents and cache outputs are withheld.

## Submission Record

- Primary artifact commit: pending
- Slack notification: pending
- Source-upload gate: passed with exactly seven Markdown/JSON artifacts and zero paper, HTML, source archive, cache, or extracted-text artifacts
- Submission status: prepared for direct default-branch submission
