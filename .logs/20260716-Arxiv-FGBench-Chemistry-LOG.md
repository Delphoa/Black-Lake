# Arxiv DEP Job Log: FGBench Chemistry

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2508.01055v4, *FGBench: A Dataset and Benchmark for Molecular Property Reasoning at Functional Group-Level in Large Language Models*
- Venue: NeurIPS 2025 Datasets and Benchmarks Track
- Selection: first uniform draw; zero exclusions and reselections
- Source integrity: initial `partial`, repaired to verified `complete`
- Cache: initial miss; final `cached`
- Source policy: paper files, molecular data, repository contents, cache, and extracted text remain local/remote at their source; none are deposited

## Random Selection

- Enumeration: `rg --files -g "*.pdf"`
- PDFs / parent units: 75,777 / 75,776
- Sampling: PowerShell `Get-Random` over sorted unique units
- Zero-based index: 29,946
- Exclusions / reselections: 0 / 0

## Dedup Validation

No prior matching ID, DOI, normalized title, slug, logs, report, DEP-E manuscript, dedup pointer, memory entry, companion deposit, or 24-hour marker was found.

## Source Integrity and Cache

- PDF: 5,996,608 bytes; `%PDF-` and trailing `%%EOF` valid
- Repair: official arXiv v4 full-paper and metadata HTML fetched once
- Full HTML: 351,922 bytes; 65,713 body characters; two document markers; 65 heading/section markers; six structure terms
- Metadata: 46,404 bytes; metadata only; partials: 0; source package: not collected
- Cache: miss to `cached` in 0.579 seconds using `pypdf` / `html-regex`
- PDF / HTML / source text: 66,093 / 65,496 / 0 bytes

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-Structure Aware Systems/structure-aware-systems.md` - task-relevant structure, verifiable boundaries, and distribution-shift testing.
2. `.lake-data/DEP-E/DEP-E-20260715-Control Surfaces/control-surfaces.md` - peptide-generation safety and the boundary between in-silico predictors and biological evidence.
3. `.lake-data/DEP-E/DEP-E-20260709-Tech Intel 2338/tech-intel-2338-research.md` - life-science benchmark governance, artifact availability, and workflow-realistic evaluation.

## Output Paths

- `.logs/20260716-Arxiv-FGBench-Chemistry-LOG.md`
- `.logs/20260716-Arxiv-FGBench-Chemistry-PHASE-LOG.md`
- `.reports/BL-Arxiv-FGBench-Chemistry-20260716/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260716-FGBench Chemistry/README.md`
- `.lake-data/DEP-E/DEP-E-20260716-FGBench Chemistry/fgbench_chemistry_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. How do scaffold-, molecule-, functional-group-, and source-dataset-disjoint splits change performance and reveal memorization from MoleculeNet-derived training corpora?
2. Do chemists agree that generated comparisons, functional-group localization, property directions, and numerical targets are chemically valid across rare groups and stereochemical cases?
3. Which graph/3D-aware representations and calibrated tools improve interaction reasoning without turning benchmark scores into unsupported drug-design claims?

## Challenges

1. The 625,936 QA pairs are template expansions from 42,967 molecular comparisons, so nominal scale exceeds the number of independent molecular transformations.
2. Benchmark properties have different numerical units/scales, making pooled RMSE difficult to interpret; validity and per-dataset values are necessary.
3. MoleculeNet derivation creates contamination and dependence risks for models previously trained on the underlying molecules or tasks.

## Known Shortfalls

- No dataset/model run or chemical expert audit was performed; official code/data were inventoried only.
- Position, chain, and stereoisomerism are explicitly incomplete; 3D/conformer/context effects remain absent.
- Repository hygiene includes committed caches/OS metadata, and exact environment/version locks are incomplete.

## Submission Record

- Primary artifact commit: pending
- Slack notification: pending
- Source-upload gate: passed with exactly seven Markdown/JSON files and zero paper, code, molecular-data, cache, or image artifacts
- Submission status: pending
