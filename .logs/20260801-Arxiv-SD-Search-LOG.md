# Arxiv DEP Job Log

## Selection and Eligibility

- Selected paper: *SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning*.
- Identifier: arXiv:2605.18299v1; DOI: https://doi.org/10.48550/arXiv.2605.18299
- Selection method: uniform random draw over unique PDF-parent paper units enumerated with `rg --files -g "*.pdf"`; PowerShell `Get-Random` selected zero-based index 43,732.
- Candidate counts: 75,960 PDF files; 75,957 unique parent-paper units.
- Exclusions before acceptance: 0; reselections: 0; same-paper markers within 24 hours: 0.
- Dedup checks covered the public pointer index, logs, reports, DEP-E artifacts, automation memory, arXiv ID, DOI, normalized title, and slug. No prior Arxiv DEP marker was found.

## Source Integrity and Locality

- Initial source state: partial — valid full PDF present, full-paper HTML missing.
- Repair: bounded archive repair fetched public arXiv metadata/full-paper HTML/source into the local archive staging area; the valid PDF was preserved.
- Final verification: complete. The PDF passed the size, header, and trailing EOF checks; full-paper HTML passed the size, body-text, document-marker, heading, and structure-term checks; no partial files remained.
- Source policy: PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, cache, and verification records were retained locally and were not uploaded, staged, attached, or posted.

## Outputs

- `.logs/20260801-Arxiv-SD-Search-LOG.md`
- `.logs/20260801-Arxiv-SD-Search-PHASE-LOG.md`
- `.reports/BL-Arxiv-SD-Search-20260801/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260801-SD Search Reasoning/README.md`
- `.lake-data/DEP-E/DEP-E-20260801-SD Search Reasoning/sd_search_reasoning_manuscript.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-review Questions

1. Does SD-Search retain its advantage when outcome labels are noisy, learned, or unavailable for open-ended tasks?
2. How does group size and label homogeneity affect query diversity, search frequency, and answer faithfulness under matched compute?
3. Can an independent implementation reproduce the reported gains with the same retriever, corpus snapshot, seeds, and training schedule?

## Challenges

1. The source unit required repair before review because the local full-paper HTML was missing.
2. `pdftotext` was unavailable, so PDF extraction used the successful `pypdf` fallback; typography noise remains in some extracted symbols.
3. No official implementation was identified in the inspected source bundle or focused public search, and no training or benchmark reproduction was run.

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.18299
  - Applies to: selection, metadata, abstract, authors, date, and source identity.
- Source URL: https://arxiv.org/html/2605.18299
  - Applies to: full-paper method, experiments, limitations, and conclusion review.
- Source URL: https://arxiv.org/pdf/2605.18299
  - Applies to: PDF integrity gate and extracted paper text.
- Source URL: https://arxiv.org/e-print/2605.18299
  - Applies to: source-package structure, equations, tables, and appendix cross-checks.
- Source URL: https://doi.org/10.48550/arXiv.2605.18299
  - Applies to: persistent paper identity.
- Source files: local verified source bundle and processing cache.
  - Applies to: source-first review only; all source files were withheld from public submission.
