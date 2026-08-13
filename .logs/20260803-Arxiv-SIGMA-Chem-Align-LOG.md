# Black Lake Arxiv DEP: SIGMA

## Selection

- Selected paper: *SIGMA: Structure-Invariant Generative Molecular Alignment for Chemical Language Models via Autoregressive Contrastive Learning*.
- Stable identifier: arXiv:2603.25062v1; arXiv DOI: https://doi.org/10.48550/arXiv.2603.25062.
- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent units, sorted frozen pool, and uniform PowerShell `Get-Random`.
- Candidate counts: 75,960 PDFs; 75,957 unique parent units; 75,640 prior-identifier exclusions; 185 identifier-incomplete units; 132 eligible units.
- Draw: zero-based eligible-pool index 23; first valid frozen-pool draw; duplicate exclusions 0; reselections 0.
- Dedup keys: base/versioned arXiv ID, arXiv DOI, normalized title, slug, Black Lake artifacts, automation memory, metadata-only Black-Lake-Data inventory, and exact remote ID/title searches. No owning record was found.

## Source Integrity Gate

- Classification before review: complete.
- PDF validation: 2,358,330 bytes, `%PDF-` header, and trailing `%%EOF`.
- Full-paper HTML validation: 361,481 bytes, 66,317 visible body characters after script/style removal, article/LaTeXML markers, 91 heading/section markers, and seven paper-structure terms.
- Repair: none required; the valid PDF and full-paper HTML were already present.
- Source policy: PDF, full-paper HTML, metadata, extracted text, caches, and other original source material stayed in the private local archive and were not uploaded.

## Generated Outputs

- `.logs/20260803-Arxiv-SIGMA-Chem-Align-LOG.md`
- `.reports/BL-Arxiv-SIGMA-Chem-Align-20260803/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260803-SIGMA Chem Align/README.md`
- `.lake-data/DEP-E/DEP-E-20260803-SIGMA Chem Align/sigma_chem_align_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Can an independent implementation reproduce the reported TIS, FCD, validity, and scaffold-diversity results from a pinned code and data release?
2. How do stereochemistry, tautomer normalization, scaffold splits, and out-of-distribution molecular families change the invariance and diversity claims?
3. What is the measured wall-clock and memory cost of IsoBeam when RDKit validation is applied throughout large-beam decoding?

## Challenges

1. The paper reports no public implementation at review time and says code and pretrained models will be released upon acceptance.
2. The method text specifies a 128-dimensional projection output while the appendix and hyperparameter table specify a 256-dimensional projection head.
3. The strongest exploration results use a single ZINC-250k setting and three-run PMO summaries without visible significance tests or external chemical validation.

## Public Source Policy

Only generated Markdown artifacts and public source locators are in scope for submission. No PDF, HTML, source archive, extracted text, cache, local path, machine identifier, or `.source/` directory is included.
